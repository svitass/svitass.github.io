---
title: "多源动作数据采集与整合"
collection: portfolio
permalink: /portfolio/multi-source-motion-dataset-integration/
excerpt: "围绕 MRI 手部数据、Music2Dance、Speech2Gesture 与 CyanPuppets 等方向持续收集和整理动作数据来源，为数字人动作生成与驱动提供更丰富的数据基础。"
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
        <span>CyanPuppets</span>
        <span>Dataset Integration</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>数据源梳理</strong><br>持续收集和整理不同动作方向的数据来源，明确它们的粒度、场景和可复用价值。</li>
        <li><strong>采集与补充</strong><br>结合项目需要补充自采数据，例如 Music2Dance 方向的动捕录制和多机位采集方案验证。</li>
        <li><strong>整合视角</strong><br>从数字人任务出发评估这些数据能否服务于动作生成、手部细节建模、语音驱动手势和风格化角色动作表达。</li>
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
      <li><strong>Speech2Gesture</strong>：围绕中文语音驱动手势的数据采集与整理持续推进，重点看数据是否适合支撑演讲、对话、播报场景下的上半身动作表达。</li>
      <li><strong>CyanPuppets</strong>：这部分对应角色化方向的采集动作数据，更偏虚拟偶像或非写实角色动作素材整理，不是这里 Music2Dance 跳舞视频对应的内容。</li>
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
    <h2>Speech2Gesture 与角色化动作采集</h2>
    <ul class="detail-list">
      <li><strong>Speech2Gesture</strong> 对应的是中文语音驱动手势数据采集与筛选，核心场景是演讲、对话、播报这类上半身动作为主的表达任务，而不是舞蹈动作。</li>
      <li><strong>CyanPuppets</strong> 对应的是角色化方向的采集动作数据，更偏虚拟偶像和非写实角色动作素材整理，用来补充写实人体数据之外的角色动作参考。</li>
      <li>这两类方向服务的任务和 Music2Dance 不同：前者偏语音驱动手势，后者偏角色化动作素材，因此不再和上面的舞蹈视频混放。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>整合方式</h2>
    <ul class="detail-list">
      <li>先按任务维度拆分数据价值，例如手部、舞蹈、语音驱动手势、风格化角色动作，不把所有数据混成一类。</li>
      <li>统一评估数据的动作粒度、是否有骨骼/关键点/视频配套、能否转成后续模型训练可用的中间格式。</li>
      <li>把公开数据和自采数据结合使用，避免完全受限于开源数据的分布和表达类型。</li>
      <li>为后续 Text2Motion、Speech2Gesture、角色驱动和数字人系统任务提供更稳定的数据来源储备。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>形成了按动作类型和应用场景拆分的数据源地图，而不是零散下载几个开源数据集。</li>
      <li>补充调研并验证了 MRI 手部、Music2Dance、Speech2Gesture、CyanPuppets 等不同粒度的数据来源；其中 Music2Dance 自采部分主要用于验证方案边界，并证明普通视频采集难以稳定支撑后续动作建模。</li>
      <li>把“数据收集”这件事从一次性准备工作，转成了长期支持数字人动作方向的底层能力。</li>
    </ul>
  </section>
</div>
