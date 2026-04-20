---
permalink: /
title: "YH"
layout: splash
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---
<div id="top" class="portfolio-home">
  <section class="portfolio-hero">
    <div class="portfolio-hero__copy">
      <p class="portfolio-eyebrow">PERSONAL PORTFOLIO</p>
      <h1 class="portfolio-title">YH</h1>
      <p class="portfolio-subtitle">3D数字人 / 虚拟人算法工程师，聚焦角色生成与接入、面部语音驱动、动作生成与系统 Demo。</p>
      <p class="portfolio-summary">做过实时对话数字人、中文口型同步优化、图片到 3D 角色流程探索、Text2Motion 去脚滑和视频人物替换为 3D 虚拟角色，兼顾研究原型与工程落地。</p>
      <div class="portfolio-actions">
        <a class="btn btn--inverse" href="https://github.com/svitass">GitHub</a>
        <a class="btn btn--light-outline" href="#projects">查看项目</a>
      </div>
      <ul class="portfolio-contact">
        <li><strong>方向</strong><span>3D数字人 / 虚拟人系统</span></li>
        <li><strong>重点</strong><span>角色生成、驱动与动作</span></li>
        <li><strong>形式</strong><span>研究原型 + 工程 Demo</span></li>
      </ul>
    </div>
    <div class="portfolio-hero__panel">
      <div class="metric-card">
        <span class="metric-card__label">中文口型数据集</span>
        <strong>5.57h</strong>
        <span>234 speakers / subject-independent split</span>
      </div>
      <div class="metric-grid">
        <div class="metric-grid__item">
          <span>平均绝对偏移</span>
          <strong>1.95 帧 → 0.62 帧</strong>
        </div>
        <div class="metric-grid__item">
          <span>完全对齐占比</span>
          <strong>15.76% → 40.08%</strong>
        </div>
        <div class="metric-grid__item">
          <span>论文成果</span>
          <strong>ACM MM 2024 Oral</strong>
        </div>
        <div class="metric-grid__item">
          <span>专利</span>
          <strong>3 项</strong>
        </div>
      </div>
      <div class="focus-list">
        <span>角色生成与接入</span>
        <span>面部语音驱动</span>
        <span>动作生成与去脚滑</span>
        <span>视频角色替换</span>
        <span>Unreal Engine + Blender + PyTorch</span>
      </div>
    </div>
  </section>

  <section id="overview" class="portfolio-section">
    <div class="section-heading">
      <p class="section-heading__eyebrow">OVERVIEW</p>
      <h2>数字人方向项目概览</h2>
      <p>把项目放在同一条技术链上看，会更清楚我覆盖的是“角色、驱动、动作、系统、落地展示”这五个环节。</p>
    </div>
    <div class="overview-card">
      <img src="/images/projects/digital-human-overview.svg" alt="数字人方向项目概览图">
    </div>
  </section>

  <section id="projects" class="portfolio-section">
    <div class="section-heading">
      <p class="section-heading__eyebrow">SELECTED PROJECTS</p>
      <h2>项目卡片</h2>
      <p>首页只保留面试官最关心的内容：封面、定位、技术关键词和详情入口。</p>
    </div>
    <div class="project-grid">
      <article class="project-card">
        <a class="project-card__media" href="/portfolio/realtime-3d-avatar-demo/"><img src="/images/projects/chat-system.png" alt="3D数字人实时对话 Demo"></a>
        <div class="project-card__body">
          <h3><a href="/portfolio/realtime-3d-avatar-demo/">3D数字人实时对话 Demo</a></h3>
          <p>基于 Unreal Engine + MetaHuman 打通角色接入、面部驱动、交互状态和对话 Demo 链路。</p>
          <p class="project-tags">Unreal Engine / MetaHuman / Live Link / Pixel Streaming</p>
          <a class="project-link" href="/portfolio/realtime-3d-avatar-demo/">点进去看详情</a>
        </div>
      </article>

      <article class="project-card">
        <a class="project-card__media" href="/portfolio/chinese-lipsync-optimization/"><img src="/images/projects/lipsync-cover.svg" alt="中文口型同步优化"></a>
        <div class="project-card__body">
          <h3><a href="/portfolio/chinese-lipsync-optimization/">中文口型同步优化</a></h3>
          <p>围绕中文口型不同步问题做数据清洗、音画校正与两阶段微调，显著改善关键发音场景表现。</p>
          <p class="project-tags">MuseTalk / LatentSync / Data Cleaning / Alignment</p>
          <a class="project-link" href="/portfolio/chinese-lipsync-optimization/">点进去看详情</a>
        </div>
      </article>

      <article class="project-card">
        <a class="project-card__media" href="/portfolio/image-to-3d-character-pipeline/"><img src="/images/projects/image-to-3d-cover.svg" alt="图片到 3D 角色流程探索"></a>
        <div class="project-card__body">
          <h3><a href="/portfolio/image-to-3d-character-pipeline/">图片到 3D 角色流程探索</a></h3>
          <p>验证从单张图片构建 3D 数字人角色的可行性，重点打通 FaceBuilder 到 Character Assembly 的接入流程。</p>
          <p class="project-tags">FaceBuilder / Mesh to MetaHuman / Character Assembly</p>
          <a class="project-link" href="/portfolio/image-to-3d-character-pipeline/">点进去看详情</a>
        </div>
      </article>

      <article class="project-card">
        <a class="project-card__media" href="/portfolio/text2motion-footskate-optimization/"><img src="/images/projects/motion-cover.svg" alt="Text2Motion 与去脚滑优化"></a>
        <div class="project-card__body">
          <h3><a href="/portfolio/text2motion-footskate-optimization/">Text2Motion 与去脚滑优化</a></h3>
          <p>围绕 Diffusion 动作生成做推理加速与脚步接地建模，兼顾训练效率、生成质量和演示可用性。</p>
          <p class="project-tags">Diffusion / DPM-Solver++ / Foot Contact / SMPLH</p>
          <a class="project-link" href="/portfolio/text2motion-footskate-optimization/">点进去看详情</a>
        </div>
      </article>

      <article class="project-card">
        <a class="project-card__media" href="/portfolio/video-to-3d-avatar-replacement/"><img src="/images/projects/video-replacement-cover.svg" alt="视频人物替换为 3D 虚拟角色"></a>
        <div class="project-card__body">
          <h3><a href="/portfolio/video-to-3d-avatar-replacement/">视频人物替换为 3D 虚拟角色</a></h3>
          <p>把真实视频中的人物动作迁移到 3D 角色并重新合成背景，形成可展示的角色替换流程。</p>
          <p class="project-tags">SAM / ProPainter / WHAM / Blender Python / Mixamo</p>
          <a class="project-link" href="/portfolio/video-to-3d-avatar-replacement/">点进去看详情</a>
        </div>
      </article>
    </div>
  </section>

  <section id="papers" class="portfolio-section">
    <div class="section-heading">
      <p class="section-heading__eyebrow">ADDITIONAL INFO</p>
      <h2>论文 / 专利 / 技术栈</h2>
      <p>补充信息放在同一屏，方便面试官快速判断成果深度与工程能力。</p>
    </div>
    <div class="info-grid">
      <div class="info-card">
        <h3>论文</h3>
        <ul>
          <li><strong>StableMoFusion</strong>: Towards Robust and Efficient Diffusion-based Motion Generation Framework</li>
          <li><strong>HardMo++</strong>: A Large-Scale Hardcase Dataset for Motion Capture</li>
          <li><strong>OOD-HOI</strong>: Text-Driven 3D Whole-Body Human-Object Interaction Generation Beyond Training Domains</li>
          <li><strong>DigitSurge</strong>: A Digital Operating Room for Surgery Simulation</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>专利</h3>
        <ul>
          <li>一种虚拟人驱动方法、装置、设备及可读存储介质</li>
          <li>一种将视频中的人物替换为 3D 虚拟角色的方法</li>
          <li>动作序列生成方法、装置、电子设备及存储介质</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>技术栈</h3>
        <div class="stack-cloud">
          <span>Python</span>
          <span>PyTorch</span>
          <span>Unreal Engine</span>
          <span>MetaHuman</span>
          <span>Blender</span>
          <span>MuseTalk</span>
          <span>LatentSync</span>
          <span>SMPL / SMPLH / SMPLX</span>
          <span>Live Link</span>
          <span>Text2Motion</span>
          <span>SAM</span>
          <span>ProPainter</span>
          <span>WHAM</span>
        </div>
      </div>
      <div class="info-card info-card--actions">
        <h3>链接</h3>
        <a class="btn btn--inverse btn--block" href="https://github.com/svitass">GitHub 主页</a>
        <a class="btn btn--light-outline btn--block" href="/portfolio/">查看全部项目详情</a>
      </div>
    </div>
  </section>
</div>
