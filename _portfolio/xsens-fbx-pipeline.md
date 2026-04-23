---
title: "Xsens 动作处理与 FBX 管线"
collection: portfolio
permalink: /portfolio/xsens-fbx-pipeline/
excerpt: "围绕 Xsens 动作数据到 SMPLH 的重定向、骨骼数据提取，以及中英文本增强与 HumanML3D 标准化处理，构建可用于 Text2Motion 方向的数据处理管线。"
header:
  teaser: "projects/xsens-fbx-pipeline-cover.jpg"
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
    <div class="project-visual">
      <img src="/images/projects/xsens-fbx-pipeline-cover.jpg" alt="Xsens 到 SMPLH 与 FBX 处理流程拼图">
      <p class="project-visual__caption">材料里能对应上的图主要覆盖三步：Xsens 采集动作导入、在中间工具里做骨骼与动画曲线处理、再把结果映射到目标 SMPLH 骨骼或统一骨架。</p>
    </div>
    <ul class="detail-list">
      <li>先从 Xsens 动捕结果导出 FBX，保证原始动作时序、根节点位移和骨骼层级信息完整保留。</li>
      <li>在中间处理环节完成骨骼映射与动画检查，把原始 Xsens 骨架统一到后续使用的 SMPLH 表达。</li>
      <li>提取骨骼序列、旋转和平移等关键时序数据，并转成 HumanML3D / Text2Motion 更容易消费的结构化格式。</li>
      <li>在动作数据落盘前完成中文转英文、同义句增强、词性提取，以及动作原点、朝向、落地状态等标准化处理，避免后续训练阶段再重复清洗。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>Xsens 到 SMPLH 重定向</h2>
    <div class="project-visual">
      <img src="/images/projects/xsens-retarget.png" alt="Xsens 到目标骨骼的重定向界面">
      <p class="project-visual__caption">这张图对应的是把源骨骼映射到目标骨骼的关键步骤。重点不是简单改个名字，而是把关节语义、层级关系和动作幅度稳定对齐到可复用的骨架标准上。</p>
    </div>
    <ul class="detail-list">
      <li>重定向阶段需要先对齐参考姿态，避免源骨架与目标骨架的初始站姿差异把误差放大到整段动作上。</li>
      <li>脚、手、骨盆和脊柱是最容易暴露问题的部位，必须优先检查接地、摆臂、根位移和转身时的稳定性。</li>
      <li>统一到 SMPLH 之后，动作才能更顺利进入后续生成模型、重定向流程或数字人角色驱动链路。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>SMPLH 骨骼数据提取</h2>
    <div class="project-visual">
      <img src="/images/projects/xsens-smplh-extraction.jpg" alt="SMPLH 骨骼数据提取与动画曲线处理界面">
      <p class="project-visual__caption">材料里这张界面图能支撑“骨骼数据提取”这一段：动作不是只保留可视化效果，而是需要把骨骼层级、动画曲线和时序信息拆出来，变成后续训练可直接使用的数据。</p>
    </div>
    <ul class="detail-list">
      <li>从 FBX 中读取骨骼动画时，需要明确每一帧的关节旋转、位移和根节点运动，避免只保存渲染结果而丢掉训练所需的结构信息。</li>
      <li>提取阶段同时要处理坐标系、单位、朝向和帧率统一，否则同一批动作会在后续处理时表现出明显分布偏差。</li>
      <li>这一步决定了动作数据能否真正转成 HumanML3D 风格样本，而不是停留在软件内部可播放、但模型不可用的状态。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>文本增强与标准化</h2>
    <ul class="detail-list">
      <li>在动作片段整理完成后，我会先把中文描述翻译成英文，再调用 LLM 对每条句子做数据增强，生成 3 条语义一致但表达不同的英文同义句。</li>
      <li>随后沿用 HumanML3D 的文本处理方式，提取词性等语言特征，把增强后的文本转成后续 Text2Motion 训练可直接使用的字段格式。</li>
      <li>动作侧也按 HumanML3D 的标准化流程处理，包括统一原点、统一朝向、把角色放到地面，并整理时序表达，减少不同采集片段之间的分布偏差。</li>
      <li>这部分增强和标准化不是为了把描述“写得更花”，而是为了让文本语义与动作表达都更稳定，方便后续模型训练和数据复用。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果</h2>
    <ul class="detail-result">
      <li>完成了 Xsens 动作到 SMPLH 骨架的统一重定向思路，减少不同来源动作数据在骨骼表达上的断层。</li>
      <li>把 FBX 动画进一步拆成后续训练可消费的骨骼时序数据，而不是停留在单一软件内播放。</li>
      <li>结合中英文本增强、词性提取与动作标准化处理，为 HumanML3D / Text2Motion 方向的数据制作提供了更稳定的底层管线。</li>
    </ul>
  </section>
</div>
