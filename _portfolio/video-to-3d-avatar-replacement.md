---
title: "视频人物替换为 3D 虚拟角色"
collection: portfolio
permalink: /portfolio/video-to-3d-avatar-replacement/
excerpt: "使用背景恢复、动作捕捉和 Blender 自动化脚本，将真实视频中的人物替换成 3D 虚拟角色。"
header:
  teaser: "projects/video-replacement-pipeline.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">把真实视频中的人物动作迁移到 3D 虚拟角色，并与背景重新合成，目标是形成一条稳定、可自动化处理的视频角色替换流程。</p>
      <div class="detail-chips">
        <span>SAM</span>
        <span>ProPainter</span>
        <span>WHAM</span>
        <span>Blender Python</span>
        <span>Mixamo</span>
        <span>SMPLX</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>背景恢复</strong><br>使用 SAM、ProPainter 获取去除人物后的背景内容。</li>
        <li><strong>动作获取</strong><br>使用 WHAM 捕捉视频人物动作，并统一到后续角色驱动流程。</li>
        <li><strong>自动化封装</strong><br>通过 Blender Python 脚本封装 SMPLX、Mixamo、Auto-Rig Pro 等插件操作。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>从原始视频中分离人物与背景，先得到后续合成所需的背景素材。</li>
      <li>通过 WHAM 捕捉人物动作，并转为可驱动 3D 角色的中间表示。</li>
      <li>在 Blender 中用 Python 脚本串联 SMPLX、Mixamo、Auto-Rig Pro 等工具，完成动作重定向与角色渲染。</li>
      <li>最终把渲染后的 3D 虚拟角色动作与背景重新组合，得到替换结果。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果展示</h2>
    <div class="project-visual">
      <img src="/images/projects/video-replacement-pipeline.png" alt="视频人物替换为 3D 虚拟角色流程图">
      <p class="project-visual__caption">材料里保留下来的实际流程图，覆盖人物分离、背景恢复、动作获取、角色重定向和最终合成几个关键环节。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/video-replacement-before.png" alt="视频人物替换原始视频画面">
      <p class="project-visual__caption">输入端是真实人物视频，先提取背景和人体运动，再进入 3D 角色驱动流程。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/video-replacement-after.png" alt="视频人物替换后的 3D 角色结果">
      <p class="project-visual__caption">输出端替换为 3D 虚拟角色，同时尽量保留原视频动作节奏和背景语义。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>项目成功申请发明专利：<strong>一种将视频中的人物替换为 3D 虚拟角色的方法</strong>。</li>
      <li>沉淀出基于 Blender Python 的流程封装经验，降低了多插件串联时的人工操作成本。</li>
      <li>为 3D 虚拟角色内容生产提供了“视频驱动角色”的可复用能力。</li>
    </ul>
  </section>
</div>
