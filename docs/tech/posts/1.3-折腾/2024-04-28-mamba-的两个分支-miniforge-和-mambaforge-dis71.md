---
title: mamba 的两个分支 miniforge 和 mambaforge
number: 71
slug: discussions-71/
url: https://github.com/shenweiyan/Digital-Garden/discussions/71
date: 2024-04-28
authors: [shenweiyan]
categories: 
  - 折腾
tags: ['1.3.22-虚拟环境']
---

在安装 mamba 的时候在 [release](https://github.com/conda-forge/miniforge/releases) 页面和[官方的安装页面](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) 总是看到关于 miniforge 和 mambaforge 的选择问题，傻傻搞不明白。

<!-- more -->

## Miniforge 和 Mambaforge

参考：<https://github.com/conda-forge/miniforge?tab=readme-ov-file#faq>

> **What's the difference between Mambaforge and Miniforge?**    
> After the release of Miniforge 23.3.1 in August 2023, Miniforge and Mambaforge are essentially identical. The only difference is the name of the installer and subsequently the default installation path.
> 
> 2023 年 8 月发布 Miniforge 23.3.1 后，Miniforge 和 Mambaforge 基本相同。唯一的区别是安装程序的名称以及随后的默认安装路径(一个默认是 miniforge3，一个默认是 mambaforge3)。
> 
> Before that release, Miniforge only shipped conda, while Mambaforge added mamba on top. Since Miniconda started shipping conda-libmamba-solver in July 2023, Miniforge followed suit and started shipping it too in August. At that point, since conda-libmamba-solver depends on libmambapy, the only difference between Miniforge and Mambaforge was the presence of the mamba Python package. To minimize surprises, we decided to add mamba to Miniforge too.    
> 
> 在之前的版本中，Miniforge 仅提供 conda，而 Mambaforge 在此基础上增加了 mamba。自 2023 年 7 月 Miniconda 开始提供 conda-libmamba-solver 以来，Miniforge 也紧随其后，于 8 月开始提供此功能。那时，由于 conda-libmamba-solver 依赖于libmambapy，Miniforge 和 Mambaforge 之间的唯一区别就是是否包含 mamba Python 包。为了尽量减少意外情况，我们决定也在 Miniforge 中添加 mamba。
> 
> **Should I choose one or another going forward at the risk of one of them gettting deprecated?**     
> Given its wide usage, there are no plans to deprecate Mambaforge. If at some point we decide to deprecate Mambaforge, it will be appropriately announced and communicated with sufficient time in advance.
> 
> 鉴于 Mambaforge 的广泛使用，目前没有计划将其弃用。如果未来我们决定弃用 Mambaforge，我们会提前充分公告并通知相关用户。
> 
> That said, if you had to start using one today, we recommend to stick to Miniforge.
> 
> 不过，如果你今天需要开始使用其中一个，我们建议你坚持使用 Miniforge。

## Miniforge 和 Miniconda

参考：[What’s the difference between Anaconda, conda, Miniconda, mamba, Mambaforge, micromamba?](https://bioconda.github.io/faqs.html#what-s-the-difference-between-anaconda-conda-miniconda-mamba-mambaforge-micromamba) - bioconda#Faqs

Miniforge 是社区 (conda-forge) 驱动的简约 conda 安装程序。Miniforge 与 Miniconda 类似，但预配置了 `conda-forge` 通道，并且所有包都来自 conda-forge 而不是 `defaults` 通道。现在它还包含了 mamba 和 libmamba。

Miniconda 是公司 (Anaconda) 驱动的简约 conda 安装程序。随后的软件包安装来自 anaconda 频道（默认或其他）。

## 一句话

总的一句话来说，Mambaforge 类似于 Miniforge，但将 mamba 安装到基础环境中。虽然没有严格弃用，但从 **2023 年 9 月**起不鼓励使用它（请参阅 miniforge 自述 [README](https://github.com/conda-forge/miniforge) 文件）。

## 版本选择

Miniforge3 的 [Release 24.5.0-0](https://github.com/conda-forge/miniforge/releases/tag/24.5.0-0) 要求 **Linux-x86_64: glibc >= 2.17**，也就是对于 CentOS/RHEL 6.x (glibc = 2.12) 的旧服务器将无法正常安装使用。

```bash
$ lsb_release -a
LSB Version:    :core-4.1-amd64:core-4.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 7.7.1908 (Core)
Release:        7.7.1908
Codename:       Core

$ ldd --version
ldd (GNU libc) 2.17
Copyright (C) 2012 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.
```

![miniforge3-24.5.0-0](https://kg.weiyan.tech/2025/03/miniforge3-24.5.0-0.webp)


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="71"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
