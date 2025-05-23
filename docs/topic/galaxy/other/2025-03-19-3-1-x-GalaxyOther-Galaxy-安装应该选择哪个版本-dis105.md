---
title: 【3.1.x-GalaxyOther】Galaxy 安装应该选择哪个版本
number: 105
slug: discussions-105/
url: https://github.com/shenweiyan/Digital-Garden/discussions/105
date: 2025-03-19
authors: [shenweiyan]
categories: 
  - 3.1-Galaxy
labels: ['3.1.x-GalaxyOther']
---

> Galaxy  是一个用于生物学研究的工作流程开源平台，用网页作为界面，让不熟悉编程语言的生物科学家更容易将手上的资料做进一步分析。Galaxy 的工作流程包含: 资料筛选与整合、资料分析与发布。虽然最早是为了基因组学研究而开发，但现在通常做为一般的生物资讯学工作流程管理系统。  —— [Galaxy (计算生物学)](https://zh.wikipedia.org/wiki/Galaxy_(%E8%A8%88%E7%AE%97%E7%94%9F%E7%89%A9%E5%AD%B8)) · 维基百科

随着新技术的更新换代，[Galaxy Project](https://github.com/galaxyproject/galaxy) 这个项目现在的变化也是越来越大，不管是 UI 界面还是各种框架技术，好像是越来越复杂。从业务角度出发，面对每年至少 2+ 次的 Release 版本，我们应该怎么选呢？

<!-- more -->

首先，在 UI 上 [release_24.0](https://docs.galaxyproject.org/en/master/releases/24.0_announce.html) 和 [release_24.1](https://docs.galaxyproject.org/en/master/releases/24.1_announce.html) 是一个分水岭。

传统三栏界面，以 release_22.x 为例。
![galaxy-21.01](https://kg.weiyan.tech/2025/03/galaxy-21.01.png)

从 [release_24.0](https://docs.galaxyproject.org/en/master/releases/24.0_announce.html) 开始增加了四栏模式（最左侧增加了一栏 **Activity Bar**），但通过管理员可以通过设置保留传统的左中右三栏模式。到 [release_24.1](https://docs.galaxyproject.org/en/master/releases/24.1_announce.html) 后一律强制变成了四栏模式，即 **Activity Bar** 不再支持隐藏（Activity bar is now enabled by default.）。    
![galaxy-24.1](https://kg.weiyan.tech/2024/10/galaxy-24.1.png)

到了 [release_24.2](https://docs.galaxyproject.org/en/master/releases/24.2_announce.html)，更是把中间栏头部的 **Masthead Revision** 导航去掉整合到左侧的 **Activity Bar** 里面去了。    
![galaxy-24.2.3.dev0](https://kg.weiyan.tech/2025/03/galaxy-24.2.3.dev0.png)

第二，release_24.x 在安装过程中对 CPU 要求更高，以前的 2 核 4G 服务器现在基本没法安装。  
  
![galaxy-24-sigkill](https://kg.weiyan.tech/2025/03/galaxy-24-sigkill.png)

可以说，从 release_24.x 起 Galaxy 开始真正贯彻 **Galaxy = workflows** 的理念 - Create complex workflows and deploy via [UI](https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/workflow-editor/tutorial.html) or [CLI](https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/workflow-automation/tutorial.html). 

![galaxy-more-than-you-think](https://kg.weiyan.tech/2025/03/galaxy-more-than-you-think.png)

所以，总的来说，如果只是想借助 Galaxy 的平台完成命令行工具(程序)到 UI 可视化操作这一业务需求，可以简单选择 **≤** release_24.0 的版本；如果更加侧重 **workflows**，或者两者兼顾，可以选择 release_24.1 或者更高的版本 - 从颜值上个人更喜欢 24.2 这一个对 **Masthead Revision** 导航优化后的布局。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="105"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
