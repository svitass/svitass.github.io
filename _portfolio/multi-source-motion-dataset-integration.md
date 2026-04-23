---
title: "多源动作数据采集与整合"
collection: portfolio
permalink: /portfolio/multi-source-motion-dataset-integration/
excerpt: "围绕 MRI 手部数据、Music2Dance 与 Speech2Gesture 等方向持续收集和整理动作数据来源，为数字人动作生成与驱动提供更丰富的数据基础。"
header:
  teaser: "projects/multi-source-motion-datasets-cover.jpg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">这部分工作的目标不是只做单一数据集下载，而是围绕数字人的动作表达，把来源、粒度和应用场景都不同的数据源持续整理到一个可用的数据池里，支撑后续的动作重建、动作生成和角色驱动任务。</p>
      <div class="detail-chips">
        <span>MRI Hand Data</span>
        <span>Music2Dance</span>
        <span>Speech2Gesture</span>
        <span>OPPO Internship</span>
        <span>Dataset Integration</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>数据源梳理</strong><br>持续收集和整理不同动作方向的数据来源，明确它们的粒度、场景和可复用价值。</li>
        <li><strong>采集与补充</strong><br>结合项目需要补充自采数据，例如 Music2Dance 方向的动捕录制和多机位采集方案验证。</li>
        <li><strong>整合视角</strong><br>从数字人任务出发评估这些数据能否服务于动作生成、手部细节建模和语音驱动手势表达。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>数据源拆解</h2>
    <div class="project-visual">
      <img src="/images/projects/mri-hand-data.png" alt="MRI 手部数据采集示意">
      <p class="project-visual__caption">MRI 手部数据主要补足常规全身动作数据对细粒度手部形态和关节表达覆盖不足的问题，更适合做高精度手部动作或医疗相关交互研究。</p>
    </div>
    <ul class="detail-list">
      <li><strong>MRI 手部数据采集</strong>：重点关注手部动作和手型重建所需的高精度数据，价值在于能补充常规全身数据难以覆盖的手指细节和关节形态。</li>
      <li><strong>Music2Dance</strong>：持续汇总 AIST++、DanceWithMelody、PhantomDanceDataset、GDance 等公开舞蹈数据集，重点比较规模、风格和动作表示形式，并额外验证普通视频采集方案的边界。</li>
      <li><strong>Speech2Gesture</strong>：这部分对应我在 OPPO 实习参与的中文数据集采集工作，重点不是算法训练，而是围绕多视角视频做审核、筛选和可用性整理，为后续语音驱动手势任务准备可训练数据。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>Music2Dance 数据集汇总与示例视频</h2>
    <div class="project-visual-grid">
      <div class="project-visual">
        <img src="/images/projects/music2dance-dataset-table.png" alt="Music2Dance 相关公开数据集统计表">
        <p class="project-visual__caption">材料里保留了公开 Music2Dance 数据源汇总，用于快速判断不同舞蹈数据源的规模，并对比它们各自动作表示形式是否适合纳入后续数据池。</p>
      </div>
      <div class="project-visual">
        <video controls playsinline preload="metadata" poster="/images/projects/music2dance-dataset-demo-poster.jpg">
          <source src="/files/music2dance-dataset-demo.mp4" type="video/mp4">
          您的浏览器不支持 HTML5 视频，请直接下载观看。
        </video>
        <p class="project-visual__caption">这段跳舞视频对应材料里 Music2Dance 方向保留下来的动作预览，用来说明这部分工作关注的是音乐驱动舞蹈动作数据及其表现形式。也可<a href="/files/music2dance-dataset-demo.mp4" target="_blank" rel="noopener noreferrer">单独打开</a>查看原视频。</p>
      </div>
    </div>
    <div class="project-visual">
      <img src="/images/projects/music2dance-capture-setup.png" alt="Music2Dance 自采动捕机位摆放示意">
      <p class="project-visual__caption">这部分自采内容主要用于验证多机位视频采集方案，而不是作为稳定可用的数据补充。实际验证后证明，这种基于普通视频的方式并不可靠：算法会预测被遮挡的部位，导致帧间动作不连续，容易出现跳变，因此没有继续作为后续数据池的核心来源。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>Speech2Gesture 数据集采集（OPPO 实习）</h2>
    <p class="project-detail__lead">这部分对应的是中文多视角数据集采集与审核工作，重点是围绕 6 个视角下的视频做数据筛选和可用性整理，而不是展示单人动作结果预览。</p>
    <ul class="detail-list">
      <li><strong>工作背景</strong>：Speech2Gesture 领域中文数据集缺乏，因此在 OPPO 实习阶段补了一部分中文语音驱动手势数据采集与整理工作。</li>
      <li><strong>工作内容</strong>：围绕 6 个视角下的视频做审核、筛选和可用性判断，确保留下来的片段能够服务后续手势生成与驱动任务。</li>
      <li><strong>结果</strong>：累计采集 437 条数据，最终合格 352 条，形成了可继续处理和训练的中文数据基础。</li>
      <li><strong>后处理</strong>：后续数据处理沿用 <code>EasyMocap</code> 这条链路，把视频进一步整理成可用的动作表示。</li>
    </ul>
  </section>

</div>
