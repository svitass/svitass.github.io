---
title: "中文口型同步优化"
collection: portfolio
permalink: /portfolio/chinese-lipsync-optimization/
excerpt: "针对中文场景口型效果不足的问题，完成数据清洗、音画 offset 校正和两阶段微调。"
header:
  teaser: "projects/chinese-lipsync-compare-cover.jpg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">针对 MuseTalk 中文场景下口型不同步、关键音素表现弱的问题，从数据质量、同步预处理和模型微调三个层面联合优化，提升中文发音的可用性。</p>
      <div class="detail-chips">
        <span>MuseTalk</span>
        <span>LatentSync</span>
        <span>Data Cleaning</span>
        <span>Alignment</span>
        <span>Chinese Lip Sync</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>数据集构建</strong><br>构建中文口型训练数据，完成训练划分整理，并采用 subject-independent split。</li>
        <li><strong>清洗与同步</strong><br>完成去磨皮美颜、字幕挡脸、手部遮挡、模糊样本清洗与音画 offset 校正。</li>
        <li><strong>模型优化</strong><br>基于 MuseTalk / LatentSync 完成两阶段微调与效果验证。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>训练数据统计</h2>
    <p class="project-detail__lead">这部分统计只按 <code>dataset/TalkVid/train.txt</code> 与 <code>dataset/JoyGen/train.txt</code> 中实际参与训练、且同时具备 <code>json + mp4 + wav</code> 的样本计算，不包含仓库中被过滤掉的库存视频。</p>
    <div class="dataset-showcase">
      <div class="dataset-showcase__intro">
        <article class="dataset-panel dataset-panel--highlight">
          <p class="portfolio-eyebrow">TRAIN SPLIT</p>
          <h3>实际训练使用的中文说话视频</h3>
          <p>重算后共有 <strong>2262</strong> 个视频片段，累计 <strong>8.98 小时</strong>，覆盖 <strong>325 个说话人</strong>。其中 TalkVid 按源视频 ID 归并为 234 人，JoyGen 按源前缀归并为 91 人。</p>
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
              <strong>325</strong>
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
        <p class="dataset-speakers__caption">总览图仅基于训练集样本生成。JoyGen 按源视频前缀归并；TalkVid 按去除 <code>clipxxx_</code> 后的源视频 ID 归并。此前按 <code>clip</code> 前缀统计会把同一身份拆成多组，这一版已修正。</p>
      </article>
    </div>

    <div class="dataset-breakdown">
      <article class="dataset-card">
        <p class="portfolio-eyebrow">TALKVID PROCESSED</p>
        <h3>TalkVid 子集</h3>
        <ul class="dataset-card__list">
          <li><strong>5.57 小时 / 1017 段训练视频</strong>，全部来自 <code>dataset/TalkVid/train.txt</code>，训练清单与本地文件完全对齐。</li>
          <li><strong>234 个说话人</strong>，按去除 <code>clipxxx_</code> 后的源视频 ID 归并；该口径与我最初项目记录中的 234 speakers 对齐。</li>
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

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>先从中文场景失败案例出发，定位关键问题集中在素材质量、遮挡、音画错位和特定音素表达不足。</li>
      <li>对数据做系统清洗，重点处理磨皮美颜、字幕挡脸、手挡脸、模糊样本等会影响口型监督信号的噪声。</li>
      <li>做同步预处理与 offset 校正，减少标签偏移带来的训练误差。</li>
      <li>在 MuseTalk / LatentSync 上做两阶段微调，并对双唇音、撮口音、大开口元音、儿化音、快语速场景进行针对性观察。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果展示</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
      <div class="project-visual">
        <video controls playsinline preload="metadata" poster="/images/projects/chinese-lipsync-before-poster.jpg" style="width:100%; border-radius:16px; background:#000;">
          <source src="/files/chinese-lipsync-before.mp4" type="video/mp4">
          您的浏览器不支持 HTML5 视频，请直接下载观看。
        </video>
        <p class="project-visual__caption">优化前：直接使用原始链路时，中文场景下更容易出现口型跟随不稳、关键音素闭合不到位等问题。</p>
      </div>
      <div class="project-visual">
        <video controls playsinline preload="metadata" poster="/images/projects/chinese-lipsync-after-poster.jpg" style="width:100%; border-radius:16px; background:#000;">
          <source src="/files/chinese-lipsync-after.mp4" type="video/mp4">
          您的浏览器不支持 HTML5 视频，请直接下载观看。
        </video>
        <p class="project-visual__caption">优化后：经过数据清洗、音画 offset 校正和两阶段微调后，唇形闭合、撮口与快语速下的稳定性都有明显改善。</p>
      </div>
    </div>
    <p class="project-visual__caption">上面保留的是你补充到 <code>材料/</code> 里的真实前后对比视频，页面内可以直接播放，也能更直观看到中文口型优化带来的差异。</p>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>同步预处理后平均绝对偏移由 <strong>1.95 帧</strong> 降至 <strong>0.62 帧</strong>。</li>
      <li>完全对齐占比由 <strong>15.76%</strong> 提升至 <strong>40.08%</strong>。</li>
      <li>在双唇音、撮口音、大开口元音、儿化音和快语速场景下均有明显改善。</li>
      <li>形成了可继续扩充的中文口型数据清洗与同步流程，而不是只得到一次性的单模型结果。</li>
    </ul>
  </section>
</div>
