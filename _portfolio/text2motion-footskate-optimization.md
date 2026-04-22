---
title: "Text2Motion 与去脚滑优化"
collection: portfolio
permalink: /portfolio/text2motion-footskate-optimization/
excerpt: "基于 Diffusion 的文本生成动作项目，完成推理加速与脚步接地建模，并产出 ACM MM Oral 论文。"
header:
  teaser: "projects/stablemofusion-footskate-result.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">在文本生成动作任务中，同时处理“生成速度”和“动作可信度”两个实际问题。前者影响研发迭代与演示效率，后者直接决定角色落地时是否自然。</p>
      <div class="detail-chips">
        <span>Diffusion</span>
        <span>DPM-Solver++ 2M</span>
        <span>Text2Motion</span>
        <span>Foot Contact</span>
        <span>SMPLH</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>模型加速</strong><br>采用 SDE DPM-Solver++ 2M、缓存文本特征和半精度计算，提升推理效率。</li>
        <li><strong>去脚滑</strong><br>引入力学模型判断脚步触地情况，减少动作中的脚滑现象。</li>
        <li><strong>数据基础</strong><br>完成 Xsens 动作到 SMPLH 的重定向和 HumanML3D 风格处理，为数据集制作提供支撑。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <ul class="detail-list">
      <li>先把 Xsens 采集动作批量重定向到 SMPLH 骨骼，并导出为可进一步处理的 FBX 数据。</li>
      <li>通过脚本读取 FBX 动画，转成 HumanML3D 方法可用的数据格式，支撑 Music2Dance / Text2Motion 数据集制作。</li>
      <li>在生成模型阶段采用更高效的采样器、文本特征缓存与半精度推理，降低实验和演示成本。</li>
      <li>额外引入脚步接地判断，对脚滑问题做针对性修正，提升生成动作的可信度与可用性。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果展示</h2>
    <div class="project-visual">
      <img src="/images/projects/stablemofusion-foot-contact.png" alt="Text2Motion 去脚滑建模示意图">
      <p class="project-visual__caption">去脚滑部分引入脚步接地约束，把脚底受力和接触状态显式纳入优化，而不是只看视觉平滑度。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/stablemofusion-speed-fid.png" alt="Text2Motion 推理速度与 FID 对比图">
      <p class="project-visual__caption">加速不是单独追求更快，而是在推理时间和生成质量之间做工程上可落地的平衡。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/stablemofusion-footskate-result.png" alt="Text2Motion 去脚滑前后效果对比图">
      <p class="project-visual__caption">材料中的定性结果图直接展示了脚滑基线与优化后结果的差异，重点是脚步接地更可信。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>项目成果中稿 <strong>2024 ACM MM Oral</strong>，接受率 <strong>&lt; 3.97%</strong>。</li>
      <li>论文题目为 <strong>StableMoFusion: Towards Robust and Efficient Diffusion-based Motion Generation Framework</strong>，本人为第二作者。</li>
      <li>形成了从动作数据制作到生成质量改进的完整研发闭环，而不是只优化单一模型模块。</li>
    </ul>
  </section>
</div>
