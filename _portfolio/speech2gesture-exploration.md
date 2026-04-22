---
title: "Speech2Gesture 探索"
collection: portfolio
permalink: /portfolio/speech2gesture-exploration/
excerpt: "围绕语音韵律、语义到上半身动作的映射做持续探索，重点关注可用于数字人对话与讲解场景的手势生成方向。"
header:
  teaser: "projects/speech2gesture-cover.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">Speech2Gesture 这部分更偏探索型项目，目标是让数字人在对话、讲解、播报等场景下，不只有嘴部和表情，而是能根据语音韵律和语义内容生成更自然的上半身手势与身体节奏。</p>
      <div class="detail-chips">
        <span>Speech2Gesture</span>
        <span>Upper-body Motion</span>
        <span>SMPLH</span>
        <span>Dialogue Avatar</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>方向梳理</strong><br>从数字人对话场景出发，拆解 Speech2Gesture 对数据、骨骼表达和文本语义的需求。</li>
        <li><strong>数据准备</strong><br>结合 Xsens 到 SMPLH 的管线，把后续可用于语音手势任务的动作序列整理成统一表示。</li>
        <li><strong>场景适配</strong><br>重点关注这些手势动作能否服务于讲解型、对话型数字人，而不是只做离线动作展示。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>探索重点</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-cover.png" alt="Speech2Gesture 方向使用的动作参考">
      <p class="project-visual__caption">材料里没有单独命名为 Speech2Gesture 的成型结果页，这里保留的是与该方向强相关的动作参考素材。它更像是在说明我关注的动作表达形态，而不是冒充成已经完成的最终论文结果。</p>
    </div>
    <ul class="detail-list">
      <li>关注语音节奏、停顿、强调和语义焦点如何映射到手势节拍与身体重心变化。</li>
      <li>重点看上半身、手臂和躯干动作是否能提升数字人在讲解和对话时的表达感，而不是只堆全身动作幅度。</li>
      <li>任务定义上强调可接入数字人系统，因此动作表达需要和语音驱动、表情驱动链路兼容。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>数据与表示基础</h2>
    <div class="project-visual">
      <img src="/images/projects/xsens-smplh-extraction.jpg" alt="Speech2Gesture 可复用的 SMPLH 动作提取基础">
      <p class="project-visual__caption">Speech2Gesture 的一个关键前提是动作序列必须先被整理成统一骨骼表示。这里复用了 Xsens 到 SMPLH 的提取链路，让后续语音到手势建模不会卡在数据格式层面。</p>
    </div>
    <ul class="detail-list">
      <li>先把动作序列统一到 SMPLH 或等价的结构化骨骼表达，再考虑和语音文本对齐。</li>
      <li>需要对动作片段和文本描述做标准化，减少语义标签混乱导致的训练噪声。</li>
      <li>数据侧更偏上半身、手势节奏和交互表达，而不是单纯追求大幅度全身运动。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>当前结论</h2>
    <ul class="detail-result">
      <li>Speech2Gesture 在我的项目里属于明确持续推进的方向，但当前更偏数据与任务定义探索，而不是已经闭环的单篇成果。</li>
      <li>已经明确了它与 Xsens/SMPLH 管线、数字人实时对话场景和多源动作数据整理之间的连接关系。</li>
      <li>后续最有价值的推进方向是把语音韵律、语义标签和可复用手势骨骼序列真正组织成可训练样本。</li>
    </ul>
  </section>
</div>
