---
title: "[micro]mamba 学习笔记"
urlname: 2023-04-19-tkrdu8xnidryrmqa
author: 章鱼猫先生
date: 2023-04-19
updated: "2023-04-19 15:25:51"
---

由于 conda 的慢，现准备转移到 \[micro]mamba，这是学习和使用过程中得一些笔记。

# 安装

官方的安装文档：<https://mamba.readthedocs.io/en/latest/installation.html>

## mamba

### Fresh install

We strongly recommend to start from Mambaforge, a community project of the conda-forge community.
You can download [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for Windows, macOS and Linux.
Mambaforge comes with the popular conda-forge channel preconfigured, but you can modify the configuration to use any channel you like.

## micromamba

```bash
mkdir /ifs1/micromamba
cd /ifs1/micromamba
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
sudo ln -s /ifs1/micromamba/bin/micromamba /usr/local/bin
```

# 使用

```bash
micromamba -r /ifs1/micromamba create -n singularity -c conda-forge singularity
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoNAPrE0dElBxqdCrxRL6Dv6kIEW.png)

```bash
$ export MAMBA_ROOT_PREFIX=/ifs1/micromamba
$ micromamba run -n singularity singularity
```
