---
title: "手术室模拟系统 DigitSurge"
collection: portfolio
permalink: /portfolio/digitsurge-surgical-room-simulation/
excerpt: "围绕手术室场景做研究型数字人 demo，结合任务规划、动作生成与 Unreal 场景，用于验证医疗场景下的系统串联效果。"
header:
  teaser: "projects/digitsurge-overview.png"
author_profile: false
---

<div class="project-detail">
  <div class="project-detail__intro">
    <section class="project-detail__block">
      <h2>项目定位</h2>
      <p class="project-detail__lead">这部分更接近研究型 demo 验证，而不是完整产品。目标是把任务规划、动作生成和手术室场景串起来，验证数字人在医疗场景下能否形成一条可演示的系统链路。</p>
      <div class="detail-chips">
        <span>Unreal Engine</span>
        <span>Medical Scene</span>
        <span>Task Planning</span>
        <span>Motion Generation</span>
        <span>Research Demo</span>
      </div>
    </section>
    <aside class="project-detail__block">
      <h2>我的职责</h2>
      <ul class="detail-meta">
        <li><strong>场景搭建</strong><br>参与 Unreal 手术室环境与基础演示流程搭建，补齐研究 demo 所需的场景承载层。</li>
        <li><strong>模块接入</strong><br>配合任务规划与动作生成方向，把文本、轨迹和局部动作结果接到场景里做演示验证。</li>
        <li><strong>效果整理</strong><br>整理方法图、场景画面和演示视频，用于汇报和论文材料展示。</li>
      </ul>
    </aside>
  </div>

  <section class="project-detail__block">
    <h2>系统概览</h2>
    <div class="project-visual">
      <img src="/images/projects/digitsurge-overview.png" alt="DigitSurge 方法与系统概览图">
      <p class="project-visual__caption">现有材料里的概览图展示了这套研究 demo 的基本结构：上游由文本任务规划拆分出轨迹目标和局部动作，再通过动作模型生成结果，最后落到 Unreal 手术室环境里做场景化验证。</p>
    </div>
    <ul class="detail-list">
      <li>输入端不是直接生成整段复杂手术流程，而是先把任务拆成更容易控制的轨迹目标和局部动作描述。</li>
      <li>中间层使用动作生成模型分别处理轨迹和局部动作，再把结果映射到场景角色上做演示。</li>
      <li>场景层主要承担“把研究结果看见”的作用，用来验证人物动作、空间位置和手术室环境能否基本对上。</li>
    </ul>
  </section>

  <section class="project-detail__block">
    <h2>效果演示</h2>
    <div class="project-visual">
      <video controls playsinline preload="metadata" poster="/images/projects/digitsurge-demo-poster.jpg">
        <source src="/files/digitsurge-demo.mp4" type="video/mp4">
        您的浏览器不支持 HTML5 视频，请直接下载观看。
      </video>
      <p class="project-visual__caption">这段视频对应材料里保留下来的 DigitSurge 演示内容，重点是展示手术室环境、角色动作和文本驱动说明如何被放进同一套研究 demo 里。也可<a href="/files/digitsurge-demo.mp4" target="_blank" rel="noopener noreferrer">单独打开</a>查看原视频。</p>
    </div>
  </section>

  <section class="project-detail__block">
    <h2>说明</h2>
    <ul class="detail-result">
      <li>这部分工作的价值主要在于把医疗场景研究方向做成了可汇报、可演示的系统样例，而不是追求产品级完整度。</li>
      <li>我的参与集中在场景与 demo 串联这部分，更多是研究协作和系统验证角色。</li>
      <li>它和前面的动作生成、数据处理工作形成了互补，让数字人能力可以在更具体的医疗场景里被展示出来。</li>
    </ul>
  </section>
</div>
