---
title: "3D数字人实时对话 Demo"
collection: portfolio
permalink: /portfolio/realtime-3d-avatar-demo/
excerpt: "基于 Unreal Engine + MetaHuman 打通角色接入、实时对话、情绪控制、动作控制、背景切换以及人物与相机控制。"
header:
  teaser: "projects/3d-digital-human-demo-poster.jpg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">围绕 3D 数字人的真实可演示链路做系统打通，让角色资产接入、实时对话、情绪控制、动作控制、背景切换以及人物与相机控制能够在一个 Demo 里连续工作。</p>
      <div class="detail-chips">
        <span>Unreal Engine</span>
        <span>MetaHuman</span>
        <span>Live Link</span>
        <span>Pixel Streaming</span>
        <span>Realtime Dialogue</span>
        <span>Emotion Control</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>角色接入</strong><br>打通 Character Assembly 与可对话角色的基础接入流程。</li>
        <li><strong>驱动链路</strong><br>完成音频驱动面部动画、动作控制、人物与相机控制等关键链路验证。</li>
        <li><strong>系统 Demo</strong><br>完成支持对话、情绪控制、背景切换和交互展示的 3D 数字人 Demo 验证。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>当前支持功能</h2>
    <ul class="detail-list">
      <li><strong>实时对话</strong>：支持网页侧输入触发角色响应，完成 Listening、Thinking、Talking 等基本交互闭环。</li>
      <li><strong>情绪控制</strong>：支持根据交互状态或控制指令切换角色情绪表现，增强表达层次。</li>
      <li><strong>动作控制</strong>：支持对角色动作进行调用与切换，不只停留在静态站姿或单一播报状态。</li>
      <li><strong>背景切换</strong>：支持在不同展示背景之间切换，便于 Demo 演示不同场景。</li>
      <li><strong>人物与相机控制</strong>：支持角色与镜头的基础控制，便于调整展示构图和演示视角。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>以 Unreal Engine + MetaHuman 为渲染与角色基础，确认角色资产、装配和运行时控制接口。</li>
      <li>围绕音频输入与面部动画驱动，打通音频到口型、表情和情绪表现的响应链路。</li>
      <li>设计对话状态机，支持 Idle、Listening、Thinking、Talking 等交互状态切换，并与动作控制联动。</li>
      <li>补充背景切换、人物控制和相机控制接口，让 Demo 更适合实际演示和场景展示。</li>
      <li>结合 Pixel Streaming / Web 对话界面，验证网页侧触发、角色响应与演示展示的一致性。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>人脸重建与角色接入</h2>
    <p class="project-detail__lead">这部分不再放泛化的调试截图，而是直接展示我在 FaceBuilder 到 MetaHuman 这条链路里实际做的人脸重建与角色接入步骤。</p>
    <div class="project-visual">
      <img src="/images/projects/facebuilder-marker.png" alt="FaceBuilder 中的人脸标点与头模拟合">
      <p class="project-visual__caption">第一步是在 FaceBuilder 中做单图标点和头模拟合，先把照片中的五官轮廓、脸型和头部结构对到可编辑网格上，得到可继续处理的头部基础模型。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/facebuilder-ue-import.png" alt="FaceBuilder 头模导入 Unreal Engine 预览">
      <p class="project-visual__caption">得到头模后，我会先导入 Unreal Engine 做预览，检查基础材质、UV、法线和头部比例是否已经达到可进入 MetaHuman 流程的程度。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/facebuilder-metahuman-identity.png" alt="Mesh to MetaHuman 身份解算界面">
      <p class="project-visual__caption">核心步骤是 Mesh to MetaHuman 的身份解算。这里要把导入头模和 MetaHuman 身份骨架对齐，让系统识别出可重建的人脸结构，而不是只停留在静态头模展示。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/facebuilder-final-assembly.png" alt="MetaHuman 最终角色装配结果">
      <p class="project-visual__caption">解算完成后再做最终装配，把头部、身体和默认服装组合成完整角色。到这一步，角色才真正能进入后续实时对话和驱动验证流程。</p>
    </div>
    <ul class="detail-list">
      <li>这条链路的重点不是“自动一键生成”，而是把照片出发的人脸重建结果稳定接进 MetaHuman 体系。</li>
      <li>真正费时间的部分主要在标点精修、导入检查、身份解算以及最终装配衔接，而不是单一步骤本身。</li>
      <li>整理完这套流程后，3D 对话 Demo 就不再依赖固定角色资产，而是具备了从人脸重建到角色接入的补链能力。</li>
    </ul>
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
      <li>完成可对话 3D 数字人 Demo，当前已支持对话、情绪控制、动作控制、背景切换以及人物与相机控制。</li>
      <li>验证了 Character Assembly、Live Link、交互控制等关键模块可以作为后续工程化扩展基础。</li>
      <li>补齐了基于 FaceBuilder / MetaHuman 的角色资产接入方案，让 Demo 具备可替换角色来源与完整演示闭环。</li>
    </ul>
  </section>
</div>
