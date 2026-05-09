---
title: "Speech2Gesture"
collection: portfolio
permalink: /portfolio/speech2gesture-exploration/
excerpt: "围绕基于语音素材的骨骼驱动展开，关注语音、文本与说话人风格共同作用下的手势骨骼动画生成。"
header:
  teaser: "projects/speech2gesture-cover.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">这一部分聚焦基于语音素材的骨骼驱动。目标是让数字人在说话时，不只是播放固定动作，而是根据语音、文本和说话人风格生成同步发生的骨骼动作序列。</p>
      <div class="detail-chips">
        <span>Speech-driven Gesture</span>
        <span>Skeletal Animation</span>
        <span>Audio + Text</span>
        <span>6D Rotation</span>
        <span>Virtual Human</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>方法梳理</strong><br>整理语音驱动骨骼动画的输入输出形式、动作表示方式和解码流程。</li>
        <li><strong>驱动链路对接</strong><br>把生成结果放回既有骨骼驱动流程中，保证动作序列能够继续服务数字人角色。</li>
        <li><strong>结果整理</strong><br>围绕骨骼结构、方法链路和结果视频整理展示内容，突出语音驱动部分的技术重点。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>核心思路</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-method-pipeline.png" alt="Speech2Gesture 方法 pipeline 图">
      <p class="project-visual__caption">方法图展示了语音特征、文本特征和说话人嵌入如何进入编码器与动作解码器，以及同步判别器、质量判别器和重建损失如何共同约束生成结果。</p>
    </div>
    <ul class="detail-list">
      <li>模型主链路是：语音特征、文本特征和说话人嵌入共同条件化动作解码器，逐帧生成骨骼动作序列，再由同步、质量和重建相关约束共同拉住生成质量。</li>
      <li>输入侧同时使用语音、文本和说话人信息，而不是只依赖单一音频特征。</li>
      <li>模型重点解决动作静态、抖动、不连续和语义相关性不足几个问题。</li>
      <li>动作用 <strong>6D rotation</strong> 表示，并结合 <strong>Slerp</strong> 后处理，减少欧拉角表示带来的跳变和抖动。</li>
      <li>编码器部分同时尝试了时间维融合和特征维融合两种音频文本融合方式，解码器负责逐帧生成动作序列。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果视频</h2>
    <div class="project-visual">
      <video controls playsinline preload="metadata" poster="/images/projects/speech2gesture-cover.png" style="width:100%; border-radius:16px; background:#111;">
        <source src="/files/speech2gesture-results.mp4" type="video/mp4">
        您的浏览器不支持 HTML5 视频，请直接下载观看。
      </video>
      <p class="project-visual__caption">结果视频展示了语音驱动骨骼动作的实际输出效果，可直接观察动作节奏、上肢摆动和整体连贯性。</p>
    </div>
  </section>

</div>
