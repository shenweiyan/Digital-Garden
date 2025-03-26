---
title: 我的独立站点 Knowledge-Garden
number: 69
slug: discussions-69/
url: https://github.com/shenweiyan/Digital-Garden/discussions/69
date: 2024-04-22
authors: [shenweiyan]
categories: 
  - 乱弹
labels: []
---

使用 GitHub Discussions 写作文章大半年以来，越来越得心应手，最近起用了新的一个仓库，用于 [Knowledge-Garden](https://github.com/shenweiyan/Knowledge-Garden/discussions) 静态资源的保存和使用。

<!-- more -->

## 文章

所有的文章都是以 markdown 的格式进行保存，实际上就一堆 text 文本，占用不了多少的空间。

## 静态资源

文章的静态资源，主要是图片，才是一个最耗流量和存储空间的东西。

前一段时间经历了[腾讯云 cos 对象存储被盗刷](https://github.com/shenweiyan/Knowledge-Garden/discussions/63) 的事件后，对于对象存储的使用也就越来越谨慎，今天终于狠下决心来把 [Knowledge-Garden](https://github.com/shenweiyan/Knowledge-Garden/discussions) 这个仓库的所有包括图片在内的静态资源开始保存到另外一个 GitHub 仓库 [PicKG](https://github.com/shenweiyan/PicKG)，同时借助 Cloudflare Pages 来为图片提供访问链接。

也尝试了一下 Cloudflare 的 [R2](https://www.cloudflare.com/zh-cn/developer-platform/r2/) 这个号称零出口费用的对象存储，免费额度很有吸引力，但目前 Cloudflare R2 还没能找到一个比较顺手的图片管理工具，例如阿里云的 [oss-browser](https://github.com/aliyun/oss-browser)、腾讯云的 [cos-browser](https://cosbrowser.cloud.tencent.com/)。虽然尝试了一些折中的方案，如 [Picx4R2](https://github.com/shenweiyan/Picx4R2)，但还是不太满意。

所以目前的解决方法就是 GitHub + [PicX](https://github.com/shenweiyan/Knowledge-Garden/discussions/68) + Cloudflare Pages 进行组合，GitHub 单个仓库 5G 的存储空间应该应该也足够使用了，如果实在不够了再来考虑其他方案。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="69"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
