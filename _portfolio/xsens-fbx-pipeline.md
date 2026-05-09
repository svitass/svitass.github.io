---
title: "Xsens 动作处理与 FBX 管线"
collection: portfolio
permalink: /portfolio/xsens-fbx-pipeline/
excerpt: "围绕 Xsens 动作数据到 SMPLH 的重定向、骨骼数据提取，以及中英文本增强与 HumanML3D 标准化处理，构建可用于 Text2Motion 方向的数据处理管线。"
header:
  teaser: "projects/xsens-retarget.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">这部分工作的重点不是单纯把动捕文件导出来，而是把 Xsens 采集到的动作，稳定地转成后续模型和数字人系统真正能用的 SMPLH 骨骼表达，并进一步整理成带文本描述、可标准化训练的数据资产。</p>
      <div class="detail-chips">
        <span>Xsens</span>
        <span>FBX</span>
        <span>SMPLH</span>
        <span>HumanML3D</span>
        <span>Text Augmentation</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>重定向管线</strong><br>把 Xsens 采集到的动作批量重定向到 SMPLH 骨骼，统一下游动作表达格式。</li>
        <li><strong>数据提取</strong><br>从 FBX 中提取骨骼动画、位姿和时序信息，转成后续 HumanML3D / Text2Motion 可用的中间表示。</li>
        <li><strong>文本处理</strong><br>将中文描述翻译成英文，并调用 LLM 为每条句子生成 3 条同义表达，再按 HumanML3D 方式提取词性和统一文本字段。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>技术链路</h2>
    <div class="project-visual-grid">
      <div class="project-visual">
        <img src="/images/projects/xsens-retarget.png" alt="Xsens 动作重定向到 SMPLH 骨骼的处理界面">
      </div>
      <div class="project-visual">
        <img src="/images/projects/xsens-smplh-extraction.jpg" alt="SMPLH 骨骼数据提取与映射检查界面">
      </div>
    </div>
    <p class="project-visual__caption">这两张图分别对应 Xsens 动作重定向和后续骨骼数据提取的关键界面：先对齐骨骼语义和参考姿态，检查关节映射、根位移和整体动作稳定性，再把 FBX 动画整理成统一的 SMPLH 表达与后续可消费的结构化数据。</p>
    <ul class="detail-list">
      <li>先从 Xsens 动捕结果导出 FBX，保证原始动作时序、根节点位移和骨骼层级信息完整保留。</li>
      <li>在中间处理环节完成骨骼映射与动画检查，把原始 Xsens 骨架统一到后续使用的 SMPLH 表达。</li>
      <li>提取骨骼序列、旋转和平移等关键时序数据，并转成 HumanML3D / Text2Motion 更容易消费的结构化格式。</li>
      <li>在动作数据落盘前完成中文转英文、同义句增强、词性提取，以及动作原点、朝向、落地状态等标准化处理，避免后续训练阶段再重复清洗。</li>
    </ul>
  </section>
</div>
