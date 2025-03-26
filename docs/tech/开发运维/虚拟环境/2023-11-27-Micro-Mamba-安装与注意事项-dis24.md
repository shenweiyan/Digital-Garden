---
title: Micro/Mamba 安装与注意事项
number: 24
slug: discussions-24/
url: https://github.com/shenweiyan/Digital-Garden/discussions/24
date: 2023-11-27
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.22-虚拟环境']
---

记录一下 Micromamba/Mamba 安装的步骤和注意事项。

## Mamba 安装

Mamba 可以使用 Mambaforge 方法和已有 Mini/conda 的方式安装，官方推荐的是前面一种，即使用 Mambaforge 进行全新安装。

### 全新安装
关于 mamba 的安装，官方推荐 [Fresh install](https://mamba.readthedocs.io/en/latest/mamba-installation.html)，即全新安装。

> We recommend that you start with the [Mambaforge distribution](https://github.com/conda-forge/miniforge#mambaforge). Mambaforge comes with the popular conda-forge channel preconfigured, but you can modify the configuration to use any channel you like. Note that Anaconda channels are generally incompatible with conda-forge, so you should not mix them.        
> 我们建议您从 Mambaforge 发行版开始。 Mambaforge 预配置了流行的 conda-forge 通道，但您可以修改配置以使用您喜欢的任何通道。请注意，Anaconda 通道通常与 conda-forge 不兼容，因此您不应混合使用它们。

其实就是：          
1. 先去 [Mambaforge distribution](https://github.com/conda-forge/miniforge#mambaforge) 下载 Mambaforge-Linux-x86_64.sh。          
2. 执行 `sh Mambaforge-Linux-x86_64.sh` 安装命令。

### 在已有的 conda 中安装

官方文档中明确说不推荐这种安装 Mamba 的方式，他们强烈建议使用 Mambaforge 方法（见上文）。

这种方法，要获取 `mamba` ，其实只需将其从 `conda-forge` 通道安装到基础环境中即可；但是需要注意 **Installing mamba into any other environment than base is not supported**，即**不支持将 mamba 安装到 base 之外的任何其他环境中**。

首先，安装 Miniconda。

参考 <https://docs.conda.io/en/latest/miniconda.html>，下载完 Miniconda3-latest-Linux-x86_64.sh，sh 执行一下就可以安装了。
```
sh Miniconda3-latest-Linux-x86_64.sh
```
然后，安装 mamba。
```
~/miniconda3/bin/conda install -c conda-forge mamba
```

> For both `mamba` and `conda`, the `base` environment is meant to hold their dependencies. It is strongly discouraged to install anything else in the base envionment. Doing so may break `mamba` and `conda` installation.      
> 对于 `mamba` 和 `conda` ， `base` 环境旨在保存它们的依赖关系。强烈建议不要在基础环境中安装任何其他东西。这样做可能会破坏 `mamba` 和 `conda` 安装。

## Micromamba 安装
参考 <https://mamba.readthedocs.io/en/latest/micromamba-installation.html>。

> `micromamba` is a fully statically-linked, self-contained, executable. This means that the `base` environment is completely empty. The configuration for `micromamba` is slighly different, namely all environments and cache will be created by default under the `MAMBA_ROOT_PREFIX` environment variable. There is also no pre-configured `.condarc`/`.mambarc` shipped with micromamba (they are however still read if present).                         
> `micromamba` 是一个完全静态链接的、独立的可执行文件。这意味着 `base` 环境完全是空的。`micromamba` 的配置略有不同，即默认情况下将在 `MAMBA_ROOT_PREFIX` 环境变量下创建所有环境和缓存。`micromamba` 也没有预配置的 `.condarc` / `.mambarc`（但是，如果存在，它们仍然会被读取）。

### 脚本安装

如果您使用的是 macOS、Linux 或 Windows 上的 Git Bash，则有一种简单的安装方法 `micromamba`。只需在您喜欢的 shell 中执行安装脚本即可。

对于 Linux、macOS 或 Windows 上的 Git Bash，请使用以下命令安装：
```
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

### 自动更新
安装后，`micromamba` 可以通过下面的方式更新：
```
micromamba self-update
```
可以指定显式版本：
```
micromamba self-update --version 1.4.6
```
### 手动更新

#### Linux 和 macOS
下载并解压可执行文件（来自官方 `conda-forge` 包）即可。
> 其实，这就等同于我们直接去 <https://github.com/mamba-org/micromamba-releases/releases> 下载对应平台的二进制文件，或者 `tar.bz2` 文件，然后解压缩，把 `bin/micromamba` 部分提出来使用。

确保安装了基本实用程序。我们需要 `curl` 和 `tar` 并支持 `bzip2` 。此外，您还需要一个基于 glibc 的系统，例如 Ubuntu、Fedora 或 Centos（Alpine Linux 本身无法运行）。

以下 magic URL 始终返回 micromamba 的最新可用版本，并且使用 `tar` 自动提取 `bin/micromamba` 部分。
```
# Linux Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
# Linux ARM64:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-aarch64/latest | tar -xvj bin/micromamba
# Linux Power:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-ppc64le/latest | tar -xvj bin/micromamba
# macOS Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-64/latest | tar -xvj bin/micromamba
# macOS Silicon/M1 (ARM64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-arm64/latest | tar -xvj bin/micromamba
```
提取完成后，我们就可以使用 `micromamba` 二进制文件了。

如果您想在临时用例中快速使用 micromamba，您可以运行：
```
export MAMBA_ROOT_PREFIX=/some/prefix  # optional, defaults to ~/micromamba
eval "$(./bin/micromamba shell hook -s posix)"
```
这个 shell hook 会修改您的 shell 变量以包含 micromamba 命令。

如果您想保留这些更改，可以通过运行 `./micromamba shell init ...` 自动将它们写入 `.bashrc` （或 `.zshrc` ）。这还允许您选择自定义 MAMBA_ROOT_ENVIRONMENT，这是包和 repodata 缓存所在的位置。
```
# Linux/bash:
./bin/micromamba shell init -s bash -p ~/micromamba  # this writes to your .bashrc file
# sourcing the bashrc file incorporates the changes into the running session.
# better yet, restart your terminal!
source ~/.bashrc

# macOS/zsh:
./micromamba shell init -s zsh -p ~/micromamba
source ~/.zshrc
```

现在您可以激活基本环境并安装新软件包，或创建其他环境。
```
micromamba activate  # this activates the base environment
micromamba install python=3.6 jupyter -c conda-forge
# or
micromamba create -n env_name xtensor -c conda-forge
micromamba activate env_name
```

专有的 [conda-forge](https://conda-forge.org/) 设置可以配置为：
```
micromamba config append channels conda-forge
micromamba config append channels nodefaults
micromamba config set channel_priority strict
```


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="24"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
