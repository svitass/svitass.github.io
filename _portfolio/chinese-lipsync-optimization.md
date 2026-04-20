---
title: "中文口型同步优化"
collection: portfolio
permalink: /portfolio/chinese-lipsync-optimization/
excerpt: "针对中文场景口型效果不足的问题，完成数据清洗、音画 offset 校正和两阶段微调。"
header:
  teaser: "projects/lipsync-cover.svg"
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
        <li><strong>数据集构建</strong><br>构建 5.57h 中文口型数据集，覆盖 234 名 speaker，并采用 subject-independent split。</li>
        <li><strong>清洗与同步</strong><br>完成去磨皮美颜、字幕挡脸、手部遮挡、模糊样本清洗与音画 offset 校正。</li>
        <li><strong>模型优化</strong><br>基于 MuseTalk / LatentSync 完成两阶段微调与效果验证。</li>
      </ul>
    </aside>
  </div>

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
    <div class="project-visual">
      <img src="/images/projects/lipsync-cover.svg" alt="中文口型同步优化指标图">
      <p class="project-visual__caption">当前详情页先展示量化结果与关键问题分布，后续可以直接替换为真实口型前后对比视频。</p>
    </div>
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
