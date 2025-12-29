---
title: hisat2-build RAM 不足
number: 91
slug: discussions-91/
url: https://github.com/shenweiyan/Digital-Garden/discussions/91
date: 2024-10-23
authors: [shenweiyan]
categories: 
  - 生信
tags: []
---

在 96G RAM 的节点跑 T2T-CHM13v2.0 的 HISAT2 index 时候，发现任务居然被系统 Killed 掉了。

<!-- more -->

排查一下才发现是因为 RAM 内存不够！      
![hisat2-resource-usage-summary](https://gi.weiyan.tech/2024/10/hisat2-resource.png)

> Note: If you use [--snp](https://open.bioqueue.org/home/knowledge/showKnowledge/sig/hisat2-build#--snp), [--ss](https://open.bioqueue.org/home/knowledge/showKnowledge/sig/hisat2-build#--ss), and/or [--exon](https://open.bioqueue.org/home/knowledge/showKnowledge/sig/hisat2-build#--exon), hisat2-build will need about **200 GB** RAM for the human genome size as index building involves a graph construction. Otherwise, you will be able to build an index on your desktop with 8GB RAM.
>    
> From [hisat2-build manual with usage examples | BioQueue Encyclopedia](https://open.bioqueue.org/home/knowledge/showKnowledge/sig/hisat2-build)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="91"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
