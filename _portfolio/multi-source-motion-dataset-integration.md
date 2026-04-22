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
      <li><strong>Music2Dance</strong>：持续整合 AIST++、DanceWithMelody、PhantomDanceDataset、GDance 等公开数据，同时补充自采动捕数据，用于音乐驱动舞蹈动作生成方向。</li>
      <li><strong>Speech2Gesture</strong>：把语音节奏、语义到手势的跨模态映射作为持续关注方向，重点看数据是否适合支撑演讲、对话、播报场景下的上半身动作表达。</li>
      <li><strong>CyanPuppets</strong>：关注这类更偏角色化、风格化的动作数据源，用来补充非写实角色或风格化数字人的动作表达能力。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>Music2Dance 与采集补充</h2>
    <div class="project-visual">
      <img src="/images/projects/music2dance-dataset-table.png" alt="Music2Dance 相关公开数据集统计表">
      <p class="project-visual__caption">材料里保留了公开 Music2Dance 数据源汇总，用于快速判断不同舞蹈数据源的规模和是否值得纳入后续数据池。</p>
    </div>
    <div class="project-visual">
      <img src="/images/projects/music2dance-capture-setup.png" alt="Music2Dance 自采动捕机位摆放示意">
      <p class="project-visual__caption">除公开数据外，我也验证了多机位采集方案，并录制了 5 位虚拟偶像根据音乐跳舞的动作，累计 2889 条片段，用来补充公开舞蹈数据在风格和角色形象上的不足。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>语音与风格化动作方向</h2>
    <div class="project-visual">
      <img src="/images/projects/cyanpuppets-motion.png" alt="CyanPuppets 风格化动作示意">
      <p class="project-visual__caption">CyanPuppets 这类数据源的价值不在于规模本身，而在于它提供了更偏角色化、风格化的动作参考，能补充写实人体数据之外的表达空间。</p>
    </div>
    <ul class="detail-list">
      <li><strong>Speech2Gesture</strong> 更关注语音韵律、语义节奏和手势分布是否匹配，适合服务对话数字人、讲解型数字人等场景。</li>
      <li><strong>CyanPuppets</strong> 更强调角色化动作表现，适合补充 stylized avatar、虚拟偶像或非写实数字人项目的数据参考。</li>
      <li>这两类方向虽然不像舞蹈数据那样有统一标准，但对扩展数字人的动作表达边界很重要。</li>
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
      <li>补充了 MRI 手部、Music2Dance 自采、Speech2Gesture、CyanPuppets 等不同粒度的数据来源，增强了后续项目的数据弹性。</li>
      <li>把“数据收集”这件事从一次性准备工作，转成了长期支持数字人动作方向的底层能力。</li>
    </ul>
  </section>
</div>
