---
title: "HardMo++ 标注标准与困难场景校准"
collection: portfolio
permalink: /portfolio/hardmo-plus-annotation-calibration/
excerpt: "围绕 HardMo++ 的困难动作场景，参与标注标准校准、关键部位细化和多模块整合，提升 hardcase 动作重建结果的可用性。"
header:
  teaser: "projects/hardmo-pipeline.jpg"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">HardMo++ 关注的不是常规、干净、无遮挡的人体动作，而是更难的 hardcase 场景。项目目标是让原本在复杂姿态、手部细节、脚部接地和多视角条件下容易失真的重建结果，变成更稳定、可用于后续数字人任务的动作表达。</p>
      <div class="detail-chips">
        <span>HardMo++</span>
        <span>4DHumans</span>
        <span>HaMeR</span>
        <span>ScoreHMR</span>
        <span>SMPL</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>标注标准校准</strong><br>围绕手部、脚部和困难姿态场景参与标注标准对齐，减少 hardcase 样本在数据侧的噪声。</li>
        <li><strong>关键部位细化</strong><br>关注手部与脚部关键点在重建中的约束作用，帮助后续模型更稳定地处理复杂动作。</li>
        <li><strong>流程参与</strong><br>参与从基础人体重建到手部/脚部细节补强、再到最终 SMPL 优化整合的完整链路理解和校验。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <div class="project-visual">
      <img src="/images/projects/hardmo-pipeline.jpg" alt="HardMo++ 方法流程图">
      <p class="project-visual__caption">材料里保留下来的流程图展示了这条链路的核心思路：先结合 HardMo-4DHumans 和 2D Pose Estimation 得到基础人体，再通过 HaMeR、ScoreHMR、多视角引导和 SMPL 优化把手部、脚部和整体姿态整合起来。</p>
    </div>
    <ul class="detail-list">
      <li>以 4DHumans 为基础人体重建入口，先获得可用的全身 SMPL 结果，而不是一开始就直接处理所有细节。</li>
      <li>同时引入 2D pose、手部关键点和脚部关键点，把 hardcase 样本里最容易出错的区域单独拉出来加强约束。</li>
      <li>手部侧通过 HaMeR 补充 MANO 相关细节，脚部和整体姿态侧通过 ScoreHMR 与多视角信息辅助校正。</li>
      <li>最终把各模块结果做统一整合和 SMPL 优化，让复杂动作样本在下游任务里更可用。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果对比</h2>
    <div class="project-visual">
      <img src="/images/projects/hardmo-results.jpg" alt="HardMo++ 效果对比图">
      <p class="project-visual__caption">这张结果图对应材料里的 HardMo++ 页面，按输入、4DHumans、HardMo、HardMoPlus 和最终 pipeline 的顺序展示对比，能直观看到在复杂动作、肢体张开和足部接地场景下，结果会逐步稳定下来。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>为什么难</h2>
    <ul class="detail-list">
      <li>hardcase 场景往往伴随大幅度动作、遮挡、侧身、手脚细节丢失，常规人体重建方法容易在这些位置崩掉。</li>
      <li>如果标注标准不统一，困难样本本身就会带入额外噪声，后面再强的模型也很难稳定收敛。</li>
      <li>所以 HardMo++ 这类工作不只是模型堆叠，更依赖数据标准、关键部位约束和整合流程的共同校准。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>参与了 HardMo++ 困难场景数据与重建流程相关工作，重点聚焦手部、脚部和困难姿态样本的可用性提升。</li>
      <li>把“难样本”从单纯的失败案例，转成了可以系统分析、校准和优化的数据与重建问题。</li>
      <li>这类 hardcase 处理经验也为后续动作生成、角色驱动和视频动作迁移项目打下了更稳的底层基础。</li>
    </ul>
  </section>
</div>
