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
        <li><strong>结果整理</strong><br>从已有材料中抽取骨骼结构图和结果视频，保留真正属于语音驱动部分的内容。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>核心思路</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-skeleton-structure.png" alt="Speech2Gesture 骨骼结构示意">
      <p class="project-visual__caption">语音驱动输出的不是贴图或视频特效，而是可继续驱动角色的骨骼动作序列，因此动作表示和骨骼结构需要先统一下来。</p>
    </div>
    <ul class="detail-list">
      <li>输入侧同时使用语音、文本和说话人信息，而不是只依赖单一音频特征。</li>
      <li>模型重点解决动作静态、抖动、不连续和语义相关性不足几个问题。</li>
      <li>动作用 <strong>6D rotation</strong> 表示，并结合 <strong>Slerp</strong> 后处理，减少欧拉角表示带来的跳变和抖动。</li>
      <li>编码器部分同时尝试了时间维融合和特征维融合两种音频文本融合方式，解码器负责逐帧生成动作序列。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>驱动表示</h2>
    <div class="project-visual">
      <img src="/images/projects/speech2gesture-cover.png" alt="Speech2Gesture 骨骼动作结果预览">
      <p class="project-visual__caption">语音驱动阶段输出的是骨骼动作结果预览。后续只要保持统一的关节点名称、父节点关系、位置/旋转/缩放格式，就可以继续接入角色驱动链路。</p>
    </div>
    <ul class="detail-list">
      <li>语音驱动并不直接替代骨骼系统，而是复用现有骨骼动画输入格式，把生成动作送回角色。</li>
      <li>这样做的好处是方法层和引擎层解耦，模型侧关注“生成什么动作”，角色侧关注“如何正确播放这些动作”。</li>
      <li>这也是它能与既有数字人骨骼驱动流程衔接的关键，而不是变成单独的离线演示。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>结果视频</h2>
    <div class="project-visual">
      <video controls playsinline preload="metadata" poster="/images/projects/speech2gesture-cover.png" style="width:100%; border-radius:16px; background:#111;">
        <source src="/files/speech2gesture-results.mp4" type="video/mp4">
        您的浏览器不支持 HTML5 视频，请直接下载观看。
      </video>
      <p class="project-visual__caption">这里保留的是 PPT 中“骨骼驱动 / 语音驱动 / 结果”对应的视频素材，用来展示语音驱动骨骼动作的实际输出效果。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>项目结果</h2>
    <ul class="detail-result">
      <li>把语音驱动部分从整套数字人流程里单独抽出来展示，边界更清晰，不再混入无关的采集内容。</li>
      <li>页面现在只保留骨骼结构、动作表示和结果视频三类素材，和这部分工作的实际内容一致。</li>
      <li>结果页展示的是“如何由语音得到骨骼动作”，而不是其他项目阶段的补充材料。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>资料</h2>
    <ul class="detail-list">
      <li><a class="project-link" href="/files/speech2gesture-results.mp4">下载结果视频</a></li>
    </ul>
  </section>
</div>
