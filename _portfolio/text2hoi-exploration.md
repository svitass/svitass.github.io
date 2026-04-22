---
title: "Text2HOI / OOD-HOI 探索"
collection: portfolio
permalink: /portfolio/text2hoi-exploration/
excerpt: "围绕文本驱动的人-物交互动作生成做探索，重点关注超出训练域的 HOI 生成能力与交互合理性。"
header:
  teaser: "projects/text2hoi-method.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">Text2HOI 关注的不是单纯“人怎么动”，而是文本如何同时约束人体姿态与物体交互关系。这个方向的难点在于，生成结果不仅要看起来像动作，还要满足手和物体之间的接触、抓取和相对运动逻辑。</p>
      <div class="detail-chips">
        <span>Text2HOI</span>
        <span>OOD-HOI</span>
        <span>Human-Object Interaction</span>
        <span>Out-of-Domain</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>方向参与</strong><br>参与文本驱动人-物交互动作生成相关研究与结果分析，关注超出训练域的动作表达能力。</li>
        <li><strong>效果理解</strong><br>重点看物体接触、交互合理性和 unseen object 场景下的稳定性，而不只盯人体姿态是否流畅。</li>
        <li><strong>数字人视角</strong><br>把 HOI 任务理解成未来数字人和外部物体交互能力的延展，而不是孤立的生成基准。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>方法框架</h2>
    <div class="project-visual">
      <img src="/images/projects/text2hoi-method.png" alt="Text2HOI 方法框架图">
      <p class="project-visual__caption">材料里的方法图展示了这个方向的核心：文本和物体几何一起作为输入，分别约束人体姿态分支与物体姿态分支，再通过接触引导和交互优化去减少悬浮与穿插问题。</p>
    </div>
    <ul class="detail-list">
      <li>文本输入不只是普通 caption，而是需要同时约束动作类型、交互对象和动作发生方式。</li>
      <li>生成过程中人体和物体不是独立采样，而是需要在接触关系上相互约束。</li>
      <li>交互细化阶段会重点处理 floating object、穿模和接触不合理等典型问题。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果对比</h2>
    <div class="project-visual">
      <img src="/images/projects/text2hoi-results.png" alt="Text2HOI 结果对比图">
      <p class="project-visual__caption">这张结果图里可以直接看到 novel textual descriptions 和 unseen objects 两类场景，对比基线方法与 ours 在抓取、接触和姿态稳定性上的差异。</p>
    </div>
    <ul class="detail-list">
      <li>在新文本描述场景下，模型需要理解动作语义变化，而不是只复述训练集里见过的模板。</li>
      <li>在未见过的物体场景下，难点是保持物体接触关系仍然成立，而不是让人体和物体各自“看起来合理”。</li>
      <li>这类能力对后续数字人和工具、道具、环境进行真实交互很重要。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>为什么值得做</h2>
    <ul class="detail-result">
      <li>Text2HOI 把动作生成从“人怎么动”推进到“人如何和物体交互”，这对更完整的数字人行为能力是关键补充。</li>
      <li>超出训练域的文本和物体泛化能力，决定了系统能否在真实应用里处理更开放的交互需求。</li>
      <li>这类研究也为后续数字人和环境、道具、任务目标结合提供了动作层面的基础能力。</li>
    </ul>
  </section>
</div>
