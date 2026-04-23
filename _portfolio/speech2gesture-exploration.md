---
title: "Speech2Gesture 毕业设计"
collection: portfolio
permalink: /portfolio/speech2gesture-exploration/
excerpt: "硕士毕业设计《基于语音素材的骨骼动作数据生成》，围绕 speech-driven gesture generation、中文数据采集与数字人接入展开。"
header:
  teaser: "projects/speech2gesture-cover.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">这是我的硕士毕业设计《基于语音素材的骨骼动作数据生成》。项目围绕 speech-driven gesture generation 展开，希望让数字人在说话时不仅有口型和表情，还能同步生成更自然的上半身手势、身体节奏和说话风格。</p>
      <div class="detail-chips">
        <span>Speech-driven Gesture</span>
        <span>Skeletal Animation</span>
        <span>Virtual Human</span>
        <span>OPPO Internship</span>
        <span>ShanghaiTech 2023</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>毕业设计研究</strong><br>系统梳理语音驱动手势生成的数据集、动作表示、评估方式和数字人驱动链路，完成论文撰写与实验验证。</li>
        <li><strong>中文数据采集</strong><br>在 OPPO 实习期间参与 Speech2Gesture 中文数据集采集与审核，补足中文语音手势数据稀缺的问题。</li>
        <li><strong>落地接入验证</strong><br>把骨骼动作生成结果放回数字人对话场景中验证，确保不是只停留在离线骨骼序列层面。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>论文摘要</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-cover.png" alt="Speech2Gesture 毕业设计封面图">
      <p class="project-visual__caption">论文题目为《基于语音素材的骨骼动作数据生成》，提交于 2023 年 6 月，聚焦数字人说话时的语音驱动手势生成问题。</p>
    </div>
    <ul class="detail-list">
      <li>论文目标是让虚拟人在讲话过程中同步生成骨骼动作，提升表达力、交互感和沉浸感，而不是只做嘴部驱动。</li>
      <li>方法上围绕动作质量、动作多样性和语义相关性三个核心问题展开，引入动作质量判别器、说话人风格信息和语义判别器。</li>
      <li>论文摘要给出的对比结果显示：动作质量指标相对次优方法提升 <strong>14.71%</strong>，基于语义判别器的客观语义指标提升约 <strong>7%</strong>。</li>
      <li>整套工作不仅覆盖模型设计，也包含前面的虚拟人驱动链路梳理、动画表示和骨骼存储方式整理。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>中文数据采集与处理</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-capture-setup.png" alt="Speech2Gesture 中文数据采集机位示意">
      <p class="project-visual__caption">根据补充材料里的机位图，主副摄像头做了定距和垂直布设验证，用于后续的人体关键点恢复和骨骼动作拟合。</p>
    </div>
    <ul class="detail-list">
      <li>在 OPPO 实习阶段，项目的直接动机是 <strong>Speech2Gesture 中文数据集缺乏</strong>，因此先补数据，再推进建模。</li>
      <li>根据答辩材料记录，累计采集 <strong>437</strong> 条样本，审核通过 <strong>352</strong> 条，形成可继续使用的中文语音手势素材。</li>
      <li>数据处理链路复用了 <code>EasyMocap</code> 与多视角重建思路，将视频样本整理为更规范的 2D/3D 关键点和骨骼动作表示。</li>
      <li>这一阶段的价值不只是“录了数据”，而是把中文语音、动作审核、骨骼拟合和后续训练输入真正接通。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>演示视频</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:20px;">
      <div class="project-visual">
        <video controls playsinline preload="metadata" poster="/images/projects/speech2gesture-cover.png" style="width:100%; border-radius:16px; background:#111;">
          <source src="/files/speech2gesture-dataset-demo.mp4" type="video/mp4">
          您的浏览器不支持 HTML5 视频，请直接下载观看。
        </video>
        <p class="project-visual__caption">骨骼动作序列演示。这里保留了补充材料中可直接上网页的骨骼动画结果，用来展示语音驱动动作在统一骨骼表示下的预览效果。</p>
      </div>
      <div class="project-visual">
        <video controls playsinline preload="metadata" poster="/images/projects/speech2gesture-cover.png" style="width:100%; border-radius:16px; background:#111;">
          <source src="/files/speech2gesture-avatar-demo.mp4" type="video/mp4">
          您的浏览器不支持 HTML5 视频，请直接下载观看。
        </video>
        <p class="project-visual__caption">数字人场景演示。这个视频来自你补充到 <code>材料/</code> 的实录素材，更能说明 Speech2Gesture 结果接入对话数字人后的最终呈现形态。</p>
      </div>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>项目结果</h2>
    <ul class="detail-result">
      <li>完成了从论文研究、中文数据采集到数字人展示接入的完整闭环，而不是只保留方法调研。</li>
      <li>把语音驱动手势生成从“探索方向”沉淀成了正式毕业设计成果，并补充了可展示的图、视频和论文材料。</li>
      <li>页面里保留的资源已经覆盖题目、采集方案、骨骼动画预览和数字人演示，能更完整地说明这项工作的实际产出。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>论文与资料</h2>
    <ul class="detail-list">
      <li><a class="project-link" href="/files/speech-driven-skeletal-animation-generation.pdf">下载硕士论文 PDF</a></li>
      <li><a class="project-link" href="/files/speech2gesture-dataset-demo.mp4">下载骨骼动画演示视频</a></li>
      <li><a class="project-link" href="/files/speech2gesture-avatar-demo.mp4">下载数字人演示视频</a></li>
    </ul>
  </section>
</div>
