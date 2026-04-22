#!/usr/bin/env python3
import json
import math
import re
import statistics
import subprocess
import wave
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
DATASET_ROOT = ROOT / "dataset"
OUTPUT_JSON = ROOT / "files" / "dataset" / "chinese-speaking-dataset-summary.json"
OUTPUT_IMAGE = ROOT / "images" / "projects" / "chinese-speaking-dataset-speakers.png"
TEMP_DIR = ROOT / "images" / "projects" / ".dataset-speaker-cache"
TRAIN_FILENAME = "train.txt"


DATASETS = {
    "TalkVid": {
        "speaker_from_stem": lambda stem: re.match(r"^(clip\d+)_", stem).group(1),
        "source_from_stem": lambda stem: talkvid_video_id(stem),
        "source_group_from_stem": lambda stem: talkvid_source_group(stem),
        "speaker_count_method": "Grouped by filename prefix clipxxx. The current metadata does not expose an explicit speaker_id, so this is a naming-based estimate for overview use.",
    },
    "JoyGen": {
        "speaker_from_stem": lambda stem: stem.split("_shot_")[0],
        "source_from_stem": lambda stem: stem.split("_shot_")[0],
        "source_group_from_stem": lambda stem: stem.split("_shot_")[0],
        "speaker_count_method": "Grouped by the source identifier before _shot_.",
    },
}


def talkvid_parts(stem: str) -> tuple[str, str, str, str]:
    stem = re.sub(r"^clip\d+_", "", stem)
    video_id, source_idx, clip_start, clip_end = stem.rsplit("_", 3)
    return video_id, source_idx, clip_start, clip_end


def talkvid_video_id(stem: str) -> str:
    return talkvid_parts(stem)[0]


def talkvid_source_group(stem: str) -> str:
    video_id, source_idx, _, _ = talkvid_parts(stem)
    return f"{video_id}_{source_idx}"


def ffprobe_json(path: Path, select_streams: str, show_entries: str) -> dict:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        select_streams,
        "-show_entries",
        show_entries,
        "-of",
        "json",
        str(path),
    ]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(out.stdout)


def probe_video(path: Path) -> dict:
    data = ffprobe_json(
        path,
        "v:0",
        "stream=width,height,avg_frame_rate,duration:format=duration,size",
    )
    stream = data["streams"][0]
    num, den = stream["avg_frame_rate"].split("/")
    fps = float(num) / float(den) if float(den) else 0.0
    duration = float(stream.get("duration") or data["format"]["duration"])
    return {
        "duration": duration,
        "fps": fps,
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "size_bytes": int(data["format"]["size"]),
    }


def probe_wav(path: Path) -> dict:
    with wave.open(str(path), "rb") as wav:
        return {
            "sample_rate": wav.getframerate(),
            "channels": wav.getnchannels(),
            "sample_width": wav.getsampwidth() * 8,
            "frames": wav.getnframes(),
            "duration": wav.getnframes() / wav.getframerate(),
        }


def median_bbox(face_list):
    xs1 = [box[0] for box in face_list]
    ys1 = [box[1] for box in face_list]
    xs2 = [box[2] for box in face_list]
    ys2 = [box[3] for box in face_list]
    return [
        int(statistics.median(xs1)),
        int(statistics.median(ys1)),
        int(statistics.median(xs2)),
        int(statistics.median(ys2)),
    ]


def crop_speaker_tile(mp4_path: Path, meta: dict, out_path: Path) -> None:
    face_list = meta.get("face_list") or []
    if not face_list:
        raise ValueError(f"No face list for {mp4_path}")

    frame_count = len(face_list)
    frame_idx = min(frame_count // 2, frame_count - 1)
    bbox = face_list[frame_idx] if face_list[frame_idx] else median_bbox(face_list)

    width = int(meta["video_size"][1])
    height = int(meta["video_size"][0])
    fps = 25.0
    timestamp = max(frame_idx / fps, 0.0)

    frame_path = out_path.with_suffix(".frame.jpg")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(mp4_path),
            "-frames:v",
            "1",
            str(frame_path),
        ],
        check=True,
    )

    with Image.open(frame_path) as frame:
        frame = frame.convert("RGB")
        x1, y1, x2, y2 = [int(v) for v in bbox]
        face_w = max(x2 - x1, 1)
        face_h = max(y2 - y1, 1)
        pad_x = int(face_w * 0.25)
        pad_top = int(face_h * 0.35)
        pad_bottom = int(face_h * 0.18)

        crop = (
            max(0, x1 - pad_x),
            max(0, y1 - pad_top),
            min(width, x2 + pad_x),
            min(height, y2 + pad_bottom),
        )
        tile = frame.crop(crop)
        tile = ImageOps.fit(tile, (132, 132), method=Image.Resampling.LANCZOS, centering=(0.5, 0.38))
        tile.save(out_path, quality=92)

    frame_path.unlink(missing_ok=True)


def human_duration(seconds: float) -> str:
    hours = seconds / 3600
    if hours >= 1:
        return f"{hours:.2f} h"
    minutes = seconds / 60
    return f"{minutes:.1f} min"


def percent(numerator: float, denominator: float) -> float:
    return (numerator / denominator * 100.0) if denominator else 0.0


def summarize_dataset(name: str, config: dict) -> tuple[dict, dict]:
    dataset_dir = DATASET_ROOT / name
    meta_dir = dataset_dir / "meta"
    media_dir = dataset_dir / "video_audio_clip_root"
    train_path = dataset_dir / TRAIN_FILENAME

    meta_paths = {p.stem: p for p in meta_dir.glob("*.json")}
    mp4_paths = {p.stem: p for p in media_dir.glob("*.mp4")}
    wav_paths = {p.stem: p for p in media_dir.glob("*.wav")}
    inventory_stems = sorted(mp4_paths.keys() & meta_paths.keys())

    train_lines = [line.strip() for line in train_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    train_stems = [Path(line).stem for line in train_lines]
    usable_stems = sorted(stem for stem in train_stems if stem in mp4_paths and stem in meta_paths)
    usable_count = len(usable_stems)
    train_missing_mp4 = sorted(stem for stem in train_stems if stem in meta_paths and stem not in mp4_paths)
    train_missing_meta = sorted(stem for stem in train_stems if stem not in meta_paths)

    video_results = {}
    with ThreadPoolExecutor(max_workers=12) as executor:
        future_map = {executor.submit(probe_video, mp4_paths[stem]): stem for stem in usable_stems}
        for future in as_completed(future_map):
            video_results[future_map[future]] = future.result()

    metas = {}
    for stem in usable_stems:
        metas[stem] = json.loads(meta_paths[stem].read_text(encoding="utf-8"))

    wav_original = []
    wav_16k = []
    for stem, wav_path in wav_paths.items():
        if stem.endswith("_16k"):
            wav_16k.append(wav_path)
        else:
            wav_original.append(wav_path)
    train_original_wav_count = sum(1 for stem in usable_stems if stem in wav_paths)
    train_wav16k_count = sum(1 for stem in usable_stems if f"{stem}_16k" in wav_paths)

    original_wav_samples = [probe_wav(path) for path in wav_original[: min(80, len(wav_original))]]
    wav16k_samples = [probe_wav(path) for path in wav_16k[: min(80, len(wav_16k))]]

    durations = [video_results[stem]["duration"] for stem in usable_stems]
    frame_counts = [int(metas[stem]["frames"]) for stem in usable_stems]
    face_ratios = []
    face_widths = []
    face_heights = []
    for stem in usable_stems:
        meta = metas[stem]
        face_w = int(meta["face_size"][1])
        face_h = int(meta["face_size"][0])
        video_h = int(meta["video_size"][0])
        video_w = int(meta["video_size"][1])
        face_widths.append(face_w)
        face_heights.append(face_h)
        face_ratios.append((face_w * face_h) / (video_w * video_h))

    speaker_to_stems = defaultdict(list)
    source_counter = Counter()
    for stem in usable_stems:
        speaker = config["speaker_from_stem"](stem)
        speaker_to_stems[speaker].append(stem)
        source_counter[config["source_from_stem"](stem)] += 1

    resolution_set = sorted({f'{video_results[stem]["width"]}x{video_results[stem]["height"]}' for stem in usable_stems})
    fps_set = sorted({round(video_results[stem]["fps"], 3) for stem in usable_stems})
    schema_keys = sorted({key for meta in metas.values() for key in meta.keys()})

    dataset_summary = {
        "name": name,
        "split_basis": TRAIN_FILENAME,
        "train_list_count": len(train_lines),
        "meta_json_count": len(meta_paths),
        "inventory_clip_count": len(inventory_stems),
        "inventory_meta_without_mp4_count": len(meta_paths) - len(inventory_stems),
        "usable_clip_count": usable_count,
        "train_missing_mp4_count": len(train_missing_mp4),
        "train_missing_meta_count": len(train_missing_meta),
        "total_duration_seconds": round(sum(durations), 3),
        "total_duration_human": human_duration(sum(durations)),
        "duration_stats_seconds": {
            "mean": round(statistics.mean(durations), 3),
            "median": round(statistics.median(durations), 3),
            "min": round(min(durations), 3),
            "max": round(max(durations), 3),
        },
        "unique_speakers": len(speaker_to_stems),
        "clips_per_speaker": {
            "mean": round(statistics.mean([len(v) for v in speaker_to_stems.values()]), 2),
            "median": round(statistics.median([len(v) for v in speaker_to_stems.values()]), 2),
            "max": max(len(v) for v in speaker_to_stems.values()),
        },
        "speaker_count_method": config["speaker_count_method"],
        "resolution": resolution_set,
        "fps": fps_set,
        "frame_count_stats": {
            "mean": round(statistics.mean(frame_counts), 2),
            "median": round(statistics.median(frame_counts), 2),
            "min": min(frame_counts),
            "max": max(frame_counts),
        },
        "face_box_stats": {
            "mean_width": round(statistics.mean(face_widths), 2),
            "mean_height": round(statistics.mean(face_heights), 2),
            "median_width": round(statistics.median(face_widths), 2),
            "median_height": round(statistics.median(face_heights), 2),
            "mean_area_ratio_percent": round(statistics.mean(face_ratios) * 100.0, 2),
            "median_area_ratio_percent": round(statistics.median(face_ratios) * 100.0, 2),
        },
        "modalities": {
            "train_mp4_clips": usable_count,
            "train_wav_clips": train_original_wav_count,
            "train_wav_16k_clips": train_wav16k_count,
            "inventory_wav_clips": len(wav_original),
            "inventory_wav_16k_clips": len(wav_16k),
            "original_wav_sample_rates": sorted({sample["sample_rate"] for sample in original_wav_samples}),
            "original_wav_channels": sorted({sample["channels"] for sample in original_wav_samples}),
            "original_wav_bits": sorted({sample["sample_width"] for sample in original_wav_samples}),
            "wav_16k_sample_rates": sorted({sample["sample_rate"] for sample in wav16k_samples}),
        },
        "metadata_schema": schema_keys,
        "format_description": {
            "root": str(dataset_dir.relative_to(ROOT)).replace("\\", "/"),
            "meta_dir": str(meta_dir.relative_to(ROOT)).replace("\\", "/"),
            "media_dir": str(media_dir.relative_to(ROOT)).replace("\\", "/"),
            "split_file": str(train_path.relative_to(ROOT)).replace("\\", "/"),
            "pairing_rule": "One JSON metadata file and one MP4 clip share the same stem; each clip also has paired WAV audio.",
            "json_fields": schema_keys,
            "json_video_size_order": "[height, width]",
            "json_face_size_order": "[height, width]",
            "annotations": [
                "per-frame face bounding boxes",
                "per-frame facial landmarks",
                "frame count",
                "paired audio/video paths",
                "face crop size",
                "validity flag",
            ],
        },
        "speaker_examples": {},
        "top_sources_by_clips": source_counter.most_common(10),
    }

    used_source_groups = set()
    for speaker, stems in sorted(speaker_to_stems.items()):
        ordered_stems = sorted(stems)
        chosen = None
        for stem in ordered_stems:
            source_group = config["source_group_from_stem"](stem)
            if source_group not in used_source_groups:
                chosen = stem
                used_source_groups.add(source_group)
                break
        dataset_summary["speaker_examples"][speaker] = chosen or ordered_stems[0]
    return dataset_summary, metas


def build_collage(all_speakers: list[dict]) -> None:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)

    tile_size = 132
    cols = 16
    rows = math.ceil(len(all_speakers) / cols)
    gutter = 8
    top_bar = 94
    canvas_width = cols * tile_size + (cols + 1) * gutter
    canvas_height = rows * tile_size + (rows + 1) * gutter + top_bar

    canvas = Image.new("RGB", (canvas_width, canvas_height), "#f5efe4")
    draw = ImageDraw.Draw(canvas)

    try:
        title_font = ImageFont.truetype("arial.ttf", 34)
        meta_font = ImageFont.truetype("arial.ttf", 16)
    except OSError:
        title_font = ImageFont.load_default()
        meta_font = ImageFont.load_default()

    draw.rectangle((0, 0, canvas_width, top_bar), fill="#1f2a37")
    draw.text((24, 20), "Chinese Speaking Dataset", fill="#ffffff", font=title_font)
    draw.text(
        (24, 58),
        f"{len(all_speakers)} speakers | TalkVid + JoyGen processed",
        fill="#d9e2ec",
        font=meta_font,
    )

    border_colors = {
        "TalkVid": "#e76f51",
        "JoyGen": "#2a9d8f",
    }

    for idx, speaker in enumerate(all_speakers):
        cache_path = TEMP_DIR / f'{speaker["dataset"]}_{speaker["speaker"]}.jpg'
        if not cache_path.exists():
            crop_speaker_tile(speaker["mp4_path"], speaker["meta"], cache_path)

        with Image.open(cache_path) as tile:
            tile = tile.convert("RGB")
            framed = Image.new("RGB", (tile_size, tile_size), border_colors[speaker["dataset"]])
            framed.paste(tile.resize((tile_size - 6, tile_size - 6), Image.Resampling.LANCZOS), (3, 3))
            x = gutter + (idx % cols) * (tile_size + gutter)
            y = top_bar + gutter + (idx // cols) * (tile_size + gutter)
            canvas.paste(framed, (x, y))

    canvas.save(OUTPUT_IMAGE, quality=92)


def main() -> None:
    summary = {
        "generated_from": str(DATASET_ROOT.relative_to(ROOT)).replace("\\", "/"),
        "selection_rule": "Only samples listed in dataset/*/train.txt and backed by both JSON metadata and MP4 media are counted.",
        "datasets": {},
    }

    all_speakers = []
    metas_by_dataset = {}
    for name, config in DATASETS.items():
        dataset_summary, metas = summarize_dataset(name, config)
        metas_by_dataset[name] = metas
        summary["datasets"][name] = dataset_summary

        for speaker, stem in dataset_summary["speaker_examples"].items():
            all_speakers.append(
                {
                    "dataset": name,
                    "speaker": speaker,
                    "stem": stem,
                    "mp4_path": DATASET_ROOT / name / "video_audio_clip_root" / f"{stem}.mp4",
                    "meta": metas[stem],
                }
            )

    combined_duration = sum(v["total_duration_seconds"] for v in summary["datasets"].values())
    combined_clips = sum(v["usable_clip_count"] for v in summary["datasets"].values())
    combined_speakers = sum(v["unique_speakers"] for v in summary["datasets"].values())

    summary["combined"] = {
        "usable_clip_count": combined_clips,
        "unique_speakers": combined_speakers,
        "total_duration_seconds": round(combined_duration, 3),
        "total_duration_human": human_duration(combined_duration),
        "datasets": list(summary["datasets"].keys()),
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    all_speakers.sort(key=lambda item: (item["dataset"], item["speaker"]))
    build_collage(all_speakers)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Saved summary to {OUTPUT_JSON}")
    print(f"Saved collage to {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()
