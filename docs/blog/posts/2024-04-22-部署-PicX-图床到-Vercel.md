---
title: 部署 PicX 图床到 Vercel
number: 68
slug: discussions-68/
url: https://github.com/shenweiyan/Digital-Garden/discussions/68
date: 2024-04-22
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

由于 [PicX](https://github.com/XPoet/picx) 自 v3.0 起，不再支持自由选择仓库和分支，统一使用内置的仓库和分支。所以出于自定义的仓库和分支使用需求，这里主要对 [PicX v2.0](https://github.com/XPoet/picx/tree/v2) 进行 Vercel 自定义部署。

<!-- more -->

项目地址：https://github.com/XPoet/picx/tree/v2

利用 PicX 图床，直接把图片托管到 GitHub 上去。至于安装，参考[子舒 Blog](https://zburu.com/)的《[安装一个基于 Github 的静态图床程序](https://zburu.com/blog/172.html/)》这两篇文章。可以把程序和图床直接托管在 GitHub 上，也可以把程序搭建在自己的服务器上，但是图片还是只能托管到 GitHub 上。PicX 图床不像简单图床和兰空图床，图片生成的链接可以是自己的域名链接，而因为图片是托管到 GitHub 上，所以 PicX 生成的图片外链接只能是 staticaly 和 cloudfalre 的 CDN 的外链。所以个人感觉也就没有必要再把程序上传到自己的服务器上了，直接使用 GitHub 不是更好嘛。

## 操作步骤

主要的操作步骤如下： 

- 1 个 GitHub 账号；
- 1 个 Vercel 账号，可能需要科学上网环境；
- Fork PicX v2 源码 (https://github.com/XPoet/picx/tree/v2) 到个人 GitHub 仓库；
- 在 Vercel 新建项目，绑定个人 GitHub 仓库的 PicX v2 源码；Framework Preset 选择 "Vue.js"；
- 部署完成后为域名添加一条 CNAME 到 `cname-china.vercel-dns.com`。

基于以上的步骤，个人成功部署的一个 PicX 站点，以供参考和使用：

- https://github.com/shenweiyan/PicX
- 链接1：<https://v2picx.vercel.app/>
- 链接2：<https://picx.weiyan.cc/>

![picx-weiyan-cc](https://kg.weiyan.cc/2024/05/picx-weiyan-cc.webp)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="68"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
