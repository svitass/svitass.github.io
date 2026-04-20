---
title: "图片到 3D 角色流程探索"
collection: portfolio
permalink: /portfolio/image-to-3d-character-pipeline/
excerpt: "预研 FaceBuilder -> Mesh to MetaHuman -> Character Assembly 的 3D 角色生成与接入流程。"
header:
  teaser: "projects/image-to-3d-cover.svg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">验证从单张图片快速构建 3D 数字人角色的可行性，目标不是单点算法指标，而是让生成结果能真正进入实时数字人系统并可继续驱动、交互和展示。</p>
      <div class="detail-chips">
        <span>FaceBuilder</span>
        <span>Mesh to MetaHuman</span>
        <span>Character Assembly</span>
        <span>3D Character</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>流程调研</strong><br>梳理单图到 3D 角色可用链路，评估每一步的输入输出约束。</li>
        <li><strong>可行性验证</strong><br>重点验证生成角色是否能顺利进入 MetaHuman 体系并继续用于系统 Demo。</li>
        <li><strong>接入视角</strong><br>把“生成结果是否好看”进一步转成“是否能用在实时数字人系统里”。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>从图片出发构建可编辑人脸或头部模型，确认关键几何与纹理信息能否满足后续角色接入需求。</li>
      <li>通过 Mesh to MetaHuman 进入 MetaHuman 角色体系，减少从算法结果到可用角色之间的断层。</li>
      <li>在 Character Assembly 阶段验证角色装配、绑定和系统兼容性。</li>
      <li>把这条链路与实时对话 Demo 衔接，确保角色不是“只生成不接入”。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果展示</h2>
    <div class="project-visual">
      <img src="/images/projects/image-to-3d-cover.svg" alt="图片到 3D 角色流程图">
      <p class="project-visual__caption">项目关注的是端到端可接入流程：从输入图片到可用于数字人系统的角色资产。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>验证了“图片 -> 角色 -> 系统接入”的核心可行性，而不是停留在孤立的 3D 重建结果展示。</li>
      <li>明确了角色生成流程与实时数字人系统之间的接口边界，为后续角色资产自动化接入提供基础。</li>
      <li>为 3D 数字人 Demo 提供更低门槛的角色来源，减少人工建模成本。</li>
    </ul>
  </section>
</div>
