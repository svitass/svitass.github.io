---
title: "3D数字人实时对话 Demo"
collection: portfolio
permalink: /portfolio/realtime-3d-avatar-demo/
excerpt: "基于 Unreal Engine + MetaHuman 打通角色资产接入、面部驱动、交互控制与可对话 Demo 验证。"
header:
  teaser: "projects/3d-digital-human-demo-poster.jpg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">围绕 3D 数字人的真实可演示链路做系统打通，让角色资产接入、音频驱动面部动画、交互状态切换和实时对话能够在一个 Demo 里连续工作。</p>
      <div class="detail-chips">
        <span>Unreal Engine</span>
        <span>MetaHuman</span>
        <span>Live Link</span>
        <span>Pixel Streaming</span>
        <span>Realtime Dialogue</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>角色接入</strong><br>打通 Character Assembly 与可对话角色的基础接入流程。</li>
        <li><strong>驱动链路</strong><br>完成音频驱动面部动画、Live Link 与交互控制的关键链路验证。</li>
        <li><strong>系统 Demo</strong><br>完成能够进行对话演示的 3D 数字人 Demo 验证。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>以 Unreal Engine + MetaHuman 为渲染与角色基础，确认角色资产、装配和运行时控制接口。</li>
      <li>围绕音频输入与面部动画驱动，打通音频到口型/面部表情的响应链路。</li>
      <li>设计对话状态机，支持 Idle、Listening、Thinking、Talking 等交互状态切换。</li>
      <li>结合 Pixel Streaming / Web 对话界面，验证网页侧触发、角色响应与演示展示的一致性。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>角色资产接入探索</h2>
    <div class="project-visual">
      <img src="/images/projects/image-to-3d-cover.svg" alt="FaceBuilder 到 MetaHuman 的角色接入流程">
      <p class="project-visual__caption">这部分不是独立的自动角色生成项目，而是为 3D 对话 Demo 补齐可用角色来源。我基于 FaceBuilder、Mesh to MetaHuman 和 Character Assembly 做了接入验证，确认单图出发的角色资产能否进入 MetaHuman 体系并继续用于实时驱动。</p>
    </div>
    <ul class="detail-list">
      <li>以 FaceBuilder 生成可编辑头部基础，再通过 Mesh to MetaHuman 接入 MetaHuman 角色体系，减少从静态素材到可驱动角色之间的断层。</li>
      <li>重点关注的是“能不能接入系统”而不是“能不能自动生成得很完整”，因此后处理、拓扑修正和材质细调仍然需要较多手动修正。</li>
      <li>这条链路依赖现成软件能力和人工校正，更适合作为 Demo 资产准备方案，而不是单独包装成一条成熟的角色生成主线。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>关键实现截图</h2>
    <div class="project-visual">
      <img src="/images/projects/realtime-3d-face-driving.png" alt="3D 数字人面部驱动调试界面">
      <p class="project-visual__caption">在 Unreal Engine 中先验证脸部变形目标和权重写入是否稳定，确保后续音频驱动不会停留在理论链路上。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/realtime-3d-livelink.png" alt="3D 数字人 Live Link 骨骼驱动节点">
      <p class="project-visual__caption">身体侧通过 Live Link 接入姿态流，把外部驱动和角色动画图真正接起来，而不是只做离线导入。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/realtime-3d-video-driver.png" alt="3D 数字人视频驱动角色流程图">
      <p class="project-visual__caption">围绕视频或外部姿态信号做驱动链路验证，覆盖输入解析、去抖、动画补全和角色运行时输出。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>效果展示</h2>
    <div class="project-visual">
      <video controls playsinline preload="metadata" poster="/images/projects/3d-digital-human-demo-poster.jpg" style="width:100%; border-radius:16px; background:#000;">
        <source src="/files/3d-digital-human-demo.mp4" type="video/mp4">
        您的浏览器不支持 HTML5 视频，请直接下载观看。
      </video>
      <p class="project-visual__caption">3D 数字人 Demo 视频，可直接在页面内播放。也可<a href="/files/3d-digital-human-demo.mp4" target="_blank" rel="noopener noreferrer">单独打开</a>查看原视频。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>完成可对话 3D 数字人 Demo，覆盖角色接入、面部语音驱动、交互状态和展示界面。</li>
      <li>验证了 Character Assembly、Live Link、交互控制等关键模块可以作为后续工程化扩展基础。</li>
      <li>补齐了基于 FaceBuilder / MetaHuman 的角色资产接入方案，让 Demo 具备可替换角色来源与完整演示闭环。</li>
    </ul>
  </section>
</div>
