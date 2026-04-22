---
permalink: /
title: "YH"
layout: splash
author_profile: false
redirect_from:
  - /about/
  - /about.html
---
<div id="top" class="portfolio-home portfolio-home--resume">
  <section class="resume-hero">
    <div class="resume-hero__copy">
      <div class="resume-hero__identity-card">
        <div class="resume-hero__avatar-frame">
          <div class="resume-hero__avatar">
            <img src="/images/profile/yh-portrait.png" alt="YH 头像">
          </div>
        </div>
        <div class="resume-hero__identity">
          <h1 class="resume-hero__name">YH</h1>
          <div class="resume-hero__links" aria-label="联系方式">
            <a class="resume-hero__icon-link" href="https://github.com/svitass" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 .5C5.65.5.5 5.66.5 12.02c0 5.09 3.29 9.4 7.86 10.93.58.11.79-.25.79-.56v-2.17c-3.2.69-3.88-1.36-3.88-1.36-.52-1.34-1.28-1.69-1.28-1.69-1.05-.72.08-.71.08-.71 1.16.08 1.78 1.2 1.78 1.2 1.03 1.77 2.71 1.26 3.37.96.1-.75.4-1.26.73-1.55-2.56-.29-5.26-1.29-5.26-5.75 0-1.27.45-2.3 1.19-3.11-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.19 1.19a11.07 11.07 0 0 1 5.8 0c2.22-1.5 3.18-1.19 3.18-1.19.64 1.59.24 2.76.12 3.05.74.81 1.18 1.84 1.18 3.11 0 4.47-2.7 5.45-5.28 5.74.42.36.79 1.06.79 2.14v3.18c0 .31.21.68.8.56A11.53 11.53 0 0 0 23.5 12C23.5 5.66 18.35.5 12 .5Z"/>
              </svg>
            </a>
            <a class="resume-hero__icon-link" href="mailto:2410383183@qq.com" aria-label="邮箱">
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M3 5.5h18a1.5 1.5 0 0 1 1.5 1.5v10A1.5 1.5 0 0 1 21 18.5H3A1.5 1.5 0 0 1 1.5 17V7A1.5 1.5 0 0 1 3 5.5Zm0 1.5v.26l9 6.18 9-6.18V7H3Zm18 10V9.08l-8.57 5.89a.75.75 0 0 1-.86 0L3 9.08V17h18Z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>

    <aside class="resume-hero__visual">
      <div class="resume-hero__map-card">
        <div class="resume-hero__map-head">
          <span>Overview Reference</span>
          <strong>数字人经历总览</strong>
        </div>
        <img src="/images/projects/overview.png" alt="数字人方向经历总览图">
      </div>
      <div class="resume-hero__signal">
        <div class="resume-hero__signal-item">
          <span>中文口型优化</span>
          <strong>1.95 帧 → 0.62 帧</strong>
        </div>
        <div class="resume-hero__signal-item">
          <span>动作生成成果</span>
          <strong>ACM MM 2024 Oral</strong>
        </div>
        <div class="resume-hero__signal-item">
          <span>项目产出</span>
          <strong>论文 / 专利 / Demo</strong>
        </div>
      </div>
    </aside>
  </section>

  <section id="chinese-dataset" class="portfolio-section">
    <div class="section-heading section-heading--wide">
      <p class="section-heading__eyebrow">CHINESE DATASET</p>
      <h2>中文说话人视频数据集</h2>
      <p>基于 TalkVid 与 JoyGen 做了中文场景下的二次处理，当前仓库内保留了可直接用于中文口型同步、数字人口部驱动与说话人视频建模的裁剪片段、配套音频和逐帧人脸标注。</p>
    </div>

    <div class="dataset-showcase">
      <div class="dataset-showcase__intro">
        <article class="dataset-panel dataset-panel--highlight">
          <p class="portfolio-eyebrow">TRAIN SPLIT</p>
          <h3>实际训练使用的中文说话视频</h3>
          <p>按 <code>dataset/TalkVid/train.txt</code> 与 <code>dataset/JoyGen/train.txt</code> 重算，且只统计同时具备 <code>json + mp4 + wav</code> 的训练样本，共有 <strong>2262</strong> 个视频片段，累计 <strong>8.98 小时</strong>，覆盖 <strong>112 个命名归并说话人</strong>。</p>
          <div class="dataset-kpis">
            <div class="dataset-kpi">
              <span>总时长</span>
              <strong>8.98h</strong>
            </div>
            <div class="dataset-kpi">
              <span>视频片段</span>
              <strong>2262</strong>
            </div>
            <div class="dataset-kpi">
              <span>说话人归并</span>
              <strong>112</strong>
            </div>
            <div class="dataset-kpi">
              <span>视频帧率</span>
              <strong>25 FPS</strong>
            </div>
          </div>
          <div class="dataset-tags">
            <span>MP4 + WAV 配对</span>
            <span>16 kHz 单声道音频</span>
            <span>逐帧人脸框</span>
            <span>逐帧关键点</span>
            <span>JSON 元数据</span>
          </div>
        </article>

        <article class="dataset-panel">
          <p class="portfolio-eyebrow">FORMAT</p>
          <h3>数据组织与字段</h3>
          <div class="dataset-format">
            <div>
              <strong>目录结构</strong>
              <p><code>dataset/{TalkVid, JoyGen}/meta/*.json</code><br><code>dataset/{TalkVid, JoyGen}/video_audio_clip_root/*.{mp4,wav}</code></p>
            </div>
            <div>
              <strong>标注字段</strong>
              <p><code>mp4_path</code> / <code>wav_path</code> / <code>video_size</code> / <code>face_size</code> / <code>frames</code> / <code>face_list</code> / <code>landmark_list</code> / <code>isvalid</code></p>
            </div>
            <div>
              <strong>训练相关信息</strong>
              <p>支持逐帧口型建模、音视频对齐、裁剪脸框重建与说话人视频检索；<code>video_size</code> 与 <code>face_size</code> 采用 <code>[height, width]</code> 顺序。</p>
            </div>
          </div>
        </article>
      </div>

      <article class="dataset-speakers">
        <div class="dataset-speakers__head">
          <div>
            <p class="portfolio-eyebrow">SPEAKER OVERVIEW</p>
            <h3>说话人总览图</h3>
          </div>
          <a class="dataset-speakers__link" href="/files/dataset/chinese-speaking-dataset-summary.json">下载统计 JSON</a>
        </div>
        <img src="/images/projects/chinese-speaking-dataset-speakers.png" alt="中文说话人视频数据集说话人总览图">
        <p class="dataset-speakers__caption">总览图仅基于训练集样本生成。JoyGen 按源视频前缀归并；TalkVid 当前元数据未显式提供 <code>speaker_id</code>，此处按文件命名进行概览级归并，适合主页展示，不作为严格身份标注声明。</p>
      </article>
    </div>

    <div class="dataset-breakdown">
      <article class="dataset-card">
        <p class="portfolio-eyebrow">TALKVID PROCESSED</p>
        <h3>TalkVid 子集</h3>
        <ul class="dataset-card__list">
          <li><strong>5.57 小时 / 1017 段训练视频</strong>，全部来自 <code>dataset/TalkVid/train.txt</code>，训练清单与本地文件完全对齐。</li>
          <li><strong>平均片段长度 19.71 秒</strong>，中位数 19.12 秒，适合中文口型和长句驱动训练。</li>
          <li><strong>训练音频配对完整</strong>，1017 段视频均有 16 kHz、16-bit、单声道 WAV，同时库存中还保留 2287 条 <code>_16k.wav</code>。</li>
          <li><strong>库存与训练口径差异明显</strong>：仓库库存有 2347 段 mp4、4091 条元数据，其中 1744 条元数据未附对应 mp4，不应计入训练统计。</li>
        </ul>
      </article>

      <article class="dataset-card">
        <p class="portfolio-eyebrow">JOYGEN PROCESSED</p>
        <h3>JoyGen 子集</h3>
        <ul class="dataset-card__list">
          <li><strong>3.41 小时 / 1245 段训练视频</strong>，全部来自 <code>dataset/JoyGen/train.txt</code>，训练清单与本地文件完全对齐。</li>
          <li><strong>91 个源说话人归并</strong>，平均每位说话人 13.68 段视频，中位数 8 段。</li>
          <li><strong>平均片段长度 9.87 秒</strong>，更适合高密度口型同步和短句生成训练。</li>
          <li><strong>库存与训练差异较小</strong>：库存为 1506 段，训练实际使用 1245 段，说明主要是清单过滤而不是文件缺失。</li>
        </ul>
      </article>

      <article class="dataset-card">
        <p class="portfolio-eyebrow">WHY IT MATTERS</p>
        <h3>说话人视频数据集常看的信息</h3>
        <ul class="dataset-card__list">
          <li><strong>时长、片段数、说话人数</strong> 决定覆盖度与训练上限。</li>
          <li><strong>帧率、分辨率、脸框占比</strong> 直接影响口型、表情和裁剪质量。</li>
          <li><strong>音频规格与音视频配对</strong> 决定后续对齐、重采样与训练稳定性。</li>
          <li><strong>逐帧边框和关键点</strong> 能显著降低二次清洗与预处理成本。</li>
        </ul>
      </article>
    </div>
  </section>

  <section id="experience-map" class="portfolio-section">
    <div class="section-heading section-heading--wide">
      <p class="section-heading__eyebrow">EXPERIENCE MAP</p>
      <h2>数字人经历鱼骨主线</h2>
      <p>主线不是简单分类，而是我在数字人方向上逐步搭起来的一条能力链。点击鱼骨上的节点，下方会切换到该方向下的代表项目，一行一个项目，展示项目内容和我的参与度。</p>
    </div>

    <div class="fishbone-stage" data-fishbone>
      <div class="fishbone-stage__badge">数字人经历链路</div>
      <div class="fishbone-track">
        <div class="fishbone-track__notes fishbone-track__notes--top" aria-hidden="true">
          <span>清洗 / 对齐 / 多源整合</span>
          <span>口型同步 / 实时对话</span>
          <span>图片到角色 / 可编辑接入</span>
        </div>

        <div class="fishbone-track__main" role="tablist" aria-label="数字人经历主线">
          <button class="fishbone-step" type="button" data-track-key="data" data-track-index="0">
            <span class="fishbone-step__index">1</span>
            <span class="fishbone-step__label">数据</span>
          </button>
          <button class="fishbone-step" type="button" data-track-key="drive" data-track-index="1">
            <span class="fishbone-step__index">2</span>
            <span class="fishbone-step__label">骨骼动画</span>
          </button>
          <button class="fishbone-step" type="button" data-track-key="face" data-track-index="2">
            <span class="fishbone-step__index">3</span>
            <span class="fishbone-step__label">面部</span>
          </button>
          <button class="fishbone-step is-active" type="button" data-track-key="system" data-track-index="3">
            <span class="fishbone-step__index">4</span>
            <span class="fishbone-step__label">数字人系统与应用</span>
          </button>
          <button class="fishbone-step" type="button" data-track-key="character" data-track-index="4">
            <span class="fishbone-step__index">5</span>
            <span class="fishbone-step__label">角色生成</span>
          </button>
        </div>

        <div class="fishbone-track__notes fishbone-track__notes--bottom" aria-hidden="true">
          <span>动作处理 / 重定向 / 生成</span>
          <span>Demo / 交互 / 场景化落地</span>
        </div>
      </div>
    </div>

    <div class="experience-showcase">
      <div class="experience-showcase__header">
        <div>
          <p class="portfolio-eyebrow">ACTIVE TRACK</p>
          <h3 data-track-title>数字人系统与应用</h3>
          <p data-track-description>把角色、驱动、交互和场景化展示真正串起来，让数字人能力不只停留在单点算法，而能进入可演示的系统形态。</p>
        </div>
        <a class="experience-showcase__link" href="/portfolio/">查看独立项目详情页</a>
      </div>
      <div class="experience-showcase__list" data-track-projects></div>
    </div>
  </section>

  <section class="portfolio-section">
    <div class="section-heading section-heading--wide">
      <p class="section-heading__eyebrow">OUTPUTS</p>
      <h2>论文 / 专利</h2>
      <p>保留最直接的结果索引，用于快速补充简历中的代表性产出。</p>
    </div>
    <div class="resume-proof resume-proof--full">
      <article class="resume-proof__card">
        <h3>论文</h3>
        <ul class="resume-proof__list">
          <li>
            <strong>StableMoFusion: Towards Robust and Efficient Diffusion-based Motion Generation Framework</strong>
            <p>第二作者，ACM MM 2024 Oral</p>
          </li>
          <li>
            <strong>HardMo++: A Large-Scale Hardcase Dataset for Motion Capture</strong>
            <p>参与动作重建与大规模 Hardcase 动捕数据集工作。</p>
          </li>
          <li>
            <strong>OOD-HOI: Text-Driven 3D Whole-Body Human-Object Interaction Generation Beyond Training Domains</strong>
            <p>参与域外人-物交互生成研究。</p>
          </li>
          <li>
            <strong>DigitSurge: A Digital Operating Room for Surgery Simulation</strong>
            <p>参与数字化手术室模拟系统研究。</p>
          </li>
        </ul>
      </article>
      <article class="resume-proof__card">
        <h3>专利</h3>
        <ul class="resume-proof__list">
          <li>
            <strong>一种虚拟人驱动方法，装置，设备及可读存储介质</strong>
            <p>专利号：202310098261.0</p>
          </li>
          <li>
            <strong>一种将视频中的人物替换为3D虚拟角色的方法</strong>
            <p>专利号：CN202411064734.6</p>
          </li>
          <li>
            <strong>动作序列生成方法、装置、电子设备及存储介质</strong>
            <p>专利号：ZL202510942578.7</p>
          </li>
        </ul>
      </article>
    </div>
  </section>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var trackData = {
      character: {
        title: "角色生成",
        description: "这一段关注的是角色从哪里来，以及生成结果能不能真的接到数字人系统里，而不是只停留在孤立的建模或重建结果。",
        projects: [
          {
            title: "图片到可驱动 3D 角色流程探索",
            summary: "预研 FaceBuilder → Mesh to MetaHuman → Character Assembly，验证单张图片生成的角色能否直接进入实时数字人链路。",
            involvement: "技术预研负责",
            level: 82,
            tags: ["FaceBuilder", "Mesh to MetaHuman", "Character Assembly"],
            image: "/images/projects/image-to-3d-cover.svg",
            link: "/portfolio/image-to-3d-character-pipeline/"
          },
          {
            title: "2D 数字人形象构建",
            summary: "基于 MuseTalk 和 LiveTalking 做 2D 数字人形象构建，支持由图片或视频生成可对话形象，作为系统接入的前置环节。",
            involvement: "核心实现",
            level: 78,
            tags: ["MuseTalk", "LiveTalking", "2D Avatar"],
            image: "/images/projects/thumb-character.svg"
          },
          {
            title: "持续探索：图片 → 3D Gaussian → 可编辑角色",
            summary: "持续关注更低门槛的角色生成路线，希望把图像输入进一步推向可编辑、可驱动、可接入系统的 3D 角色表达。",
            involvement: "持续探索",
            level: 62,
            tags: ["3D Gaussian", "Editable Avatar", "Character Pipeline"],
            image: "/images/projects/thumb-character.svg"
          }
        ]
      },
      drive: {
        title: "骨骼动画",
        description: "这一段主要解决动作怎么来、怎么处理、怎么重定向、怎么生成得更自然，覆盖了数据处理、动作生成和角色驱动三层工作。",
        projects: [
          {
            title: "Xsens 动作处理与 FBX 管线",
            summary: "把 Xsens 采集动作批量重定向到 SMPLH 骨骼，并从 FBX 中读取动画数据，转成 HumanML3D 可用格式，支撑后续动作数据制作。",
            involvement: "负责实现",
            level: 80,
            tags: ["Xsens", "FBX", "SMPLH", "HumanML3D"],
            image: "/images/projects/thumb-drive.svg"
          },
          {
            title: "Text2Motion 与去脚滑优化",
            summary: "在 Diffusion 动作生成链路中做采样加速、文本特征缓存和脚步接地判断，兼顾生成质量与工业场景可用性。",
            involvement: "核心负责",
            level: 86,
            tags: ["Diffusion", "DPM-Solver++", "Foot Contact", "SMPLH"],
            image: "/images/projects/motion-cover.svg",
            link: "/portfolio/text2motion-footskate-optimization/"
          },
          {
            title: "视频人物动作估计与动作重定向",
            summary: "围绕视频人物替换任务，串联 3D 姿态估计、SMPLX、中间骨架表达与 Mixamo / MetaHuman 的动作重定向流程。",
            involvement: "核心实现",
            level: 76,
            tags: ["WHAM", "SMPLX", "Mixamo", "MetaHuman"],
            image: "/images/projects/video-replacement-cover.svg",
            link: "/portfolio/video-to-3d-avatar-replacement/"
          },
          {
            title: "持续探索：Music2Dance / Speech2Gesture / Text2HOI",
            summary: "持续围绕音乐、语音和人-物交互等更复杂的动作生成场景做探索，扩展数字人在泛动作方向上的表达能力。",
            involvement: "持续探索",
            level: 64,
            tags: ["Music2Dance", "Speech2Gesture", "Text2HOI"],
            image: "/images/projects/thumb-drive.svg"
          }
        ]
      },
      face: {
        title: "面部",
        description: "这一段关注实时对话数字人的表情、口型和语音协同问题，目标是让角色在中文场景和实时交互场景下更像一个真正可交流的数字人。",
        projects: [
          {
            title: "中文口型同步优化",
            summary: "构建 5.57h 中文口型数据集，完成样本清洗、音画 offset 校正与两阶段微调，重点改善双唇音、撮口音和快语速场景。",
            involvement: "主导推进",
            level: 88,
            tags: ["MuseTalk", "LatentSync", "Lip Sync", "Alignment"],
            image: "/images/projects/lipsync-cover.svg",
            link: "/portfolio/chinese-lipsync-optimization/"
          },
          {
            title: "2D 数字人实时对话",
            summary: "基于 MuseTalk 和 LiveTalking 做 2D 数字人实时对话系统，支持实时对话、打断、背景切换与自定义形象接入。",
            involvement: "核心负责",
            level: 80,
            tags: ["Realtime Dialogue", "2D Avatar", "Interrupt"],
            image: "/images/projects/thumb-face.svg"
          },
          {
            title: "3D 数字人实时对话 / 情绪控制",
            summary: "把实时音频、面部动画和交互状态串到 MetaHuman 中，进一步验证 3D 数字人的情绪和交互响应表现。",
            involvement: "负责验证与打通",
            level: 78,
            tags: ["MetaHuman", "Face Animation", "Emotion State"],
            image: "/images/projects/chat-system.png",
            link: "/portfolio/realtime-3d-avatar-demo/"
          }
        ]
      },
      system: {
        title: "数字人系统与应用",
        description: "这一段聚焦怎么把数字人的各个能力真正变成一个系统或场景化应用，包括交互控制、内容生产和医疗场景系统探索。",
        projects: [
          {
            title: "3D 数字人实时对话 Demo",
            summary: "基于 Unreal Engine + MetaHuman 打通角色接入、音频驱动面部动画、Live Link、交互状态与前端展示，是整条链路的系统承载项目。",
            involvement: "主导 Demo 打通",
            level: 84,
            tags: ["Unreal Engine", "MetaHuman", "Live Link", "Pixel Streaming"],
            image: "/images/projects/chat-system.png",
            link: "/portfolio/realtime-3d-avatar-demo/"
          },
          {
            title: "视频人物替换为 3D 虚拟角色",
            summary: "把视频中的人物动作迁移到 3D 虚拟角色并重新合成背景，形成从捕捉到渲染到合成的完整应用流程。",
            involvement: "核心实现",
            level: 78,
            tags: ["SAM", "ProPainter", "WHAM", "Blender Python"],
            image: "/images/projects/video-replacement-cover.svg",
            link: "/portfolio/video-to-3d-avatar-replacement/"
          },
          {
            title: "实时打断 / 背景切换 / 交互控制",
            summary: "围绕实际演示需求设计系统交互能力，让数字人具备更完整的可展示性，而不是只有静态生成或单轮响应。",
            involvement: "系统链路负责",
            level: 76,
            tags: ["Interrupt", "Background Switch", "State Control"],
            image: "/images/projects/chat-architecture.png"
          },
          {
            title: "手术室模拟系统 DigitSurge",
            summary: "在 Unreal 中搭建手术室环境，结合 LLM 做任务分解，并通过动作生成模块完成医学场景下的数字人系统探索。",
            involvement: "第一作者方向推进",
            level: 82,
            tags: ["Unreal Engine", "LLM", "Motion Planning", "Medical Scene"],
            image: "/images/projects/thumb-system.svg"
          }
        ]
      },
      data: {
        title: "数据",
        description: "这一段支撑前面所有方向，包括中文口型数据、多源动作数据、Hardcase 校准和医疗动作数据集构建，属于我在数字人方向上的底层支撑工作。",
        projects: [
          {
            title: "中文口型数据清洗与对齐校正",
            summary: "构建中文口型数据集，清理磨皮美颜、字幕挡脸、手挡脸、模糊样本，并做音画对齐校正，提升训练监督质量。",
            involvement: "主导推进",
            level: 86,
            tags: ["Lip Data", "Cleaning", "Offset Correction"],
            image: "/images/projects/thumb-data.svg"
          },
          {
            title: "多源动作数据采集与整合",
            summary: "收集整合 Music2Dance 相关数据源，并持续关注 Speech2Gesture、CyanPuppets 等方向，形成更丰富的动作数据来源。",
            involvement: "负责整合",
            level: 74,
            tags: ["Music2Dance", "Speech2Gesture", "Dataset Integration"],
            image: "/images/projects/thumb-data.svg"
          },
          {
            title: "HardMo++ 标注校准",
            summary: "围绕手腕、脚踝、侧身等困难场景做标注校准和数据增强，提升动作重建数据在 hardcase 场景下的可用性。",
            involvement: "核心参与",
            level: 70,
            tags: ["HardMo++", "ScoreHMR", "Annotation Calibration"],
            image: "/images/projects/thumb-data.svg"
          },
          {
            title: "医学动作数据集构建",
            summary: "结合外科培训视频、HMR 方法和 VideoLLaMA2 生成文本描述，构建医疗场景特有的动作文本数据集，服务 DigitSurge 系统。",
            involvement: "主导构建",
            level: 83,
            tags: ["Medical Dataset", "VideoLLaMA2", "SMPLX"],
            image: "/images/projects/thumb-data.svg"
          }
        ]
      }
    };

    var stage = document.querySelector("[data-fishbone]");
    if (!stage) return;

    var buttons = Array.prototype.slice.call(stage.querySelectorAll("[data-track-key]"));
    var titleNode = document.querySelector("[data-track-title]");
    var descriptionNode = document.querySelector("[data-track-description]");
    var listNode = document.querySelector("[data-track-projects]");

    function renderTrack(key) {
      var track = trackData[key];
      if (!track || !listNode) return;

      buttons.forEach(function (button) {
        var active = button.getAttribute("data-track-key") === key;
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
      });

      if (titleNode) titleNode.textContent = track.title;
      if (descriptionNode) descriptionNode.textContent = track.description;

      listNode.innerHTML = track.projects
        .map(function (project) {
          var titleMarkup = project.link
            ? '<a class="experience-row__title" href="' + project.link + '">' + project.title + "</a>"
            : '<span class="experience-row__title">' + project.title + "</span>";

          var tagsMarkup = project.tags
            .map(function (tag) {
              return '<span>' + tag + "</span>";
            })
            .join("");

          return (
            '<article class="experience-row">' +
              '<div class="experience-row__media">' +
                '<img src="' + project.image + '" alt="' + project.title + '">' +
              "</div>" +
              '<div class="experience-row__body">' +
                '<div class="experience-row__top">' +
                  '<div class="experience-row__main">' +
                    titleMarkup +
                    '<p class="experience-row__summary">' + project.summary + "</p>" +
                    '<div class="experience-row__tags">' + tagsMarkup + "</div>" +
                  "</div>" +
                  '<div class="experience-row__involvement">' +
                    '<span>参与度</span>' +
                    '<strong>' + project.involvement + "</strong>" +
                    '<div class="experience-row__meter"><span style="width:' + project.level + '%"></span></div>' +
                  "</div>" +
                "</div>" +
              "</div>" +
            "</article>"
          );
        })
        .join("");
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        renderTrack(button.getAttribute("data-track-key"));
      });
    });

    renderTrack("system");
  });
</script>
