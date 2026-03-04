---
title: 用 Docker 来解决 LinearDesign 的 GLIBC 版本过低问题
number: 179
slug: discussions-179/
url: https://github.com/shenweiyan/Digital-Garden/discussions/179
date: 2026-03-03
authors: 
  - shenweiyan
categories: 
  - 折腾
tags: ['1.3.1-Docker']
---

## LinearDesign 介绍

LinearDesign 是一款用于优化 mRNA 设计的软件，旨在提高 mRNA 的稳定性和免疫原性。该项目由 He Zhang、Liang Zhang、Ang Lin 等研究人员开发，并已在 Nature杂志上发表相关研究成果。LinearDesign 通过算法优化 mRNA 序列，使其在保持高翻译效率的同时，具有更好的结构稳定性。

GitHub 地址：<https://github.com/LinearDesignSoftware/LinearDesign>

## 项目快速启动 

确保你的系统满足以下依赖要求：
- Clang 11.0.0 或更高版本，或 GCC 4.8.5 或更高版本         
- Python 2.7          
- GLIBC≥2.29          

> glibc (GNU C Library) 是 GNU 发布的 C 标准运行库，是 Linux 系统中最底层、最核心的 API，几乎所有应用软件都依赖它。它主要负责封装 Linux 内核系统调用，并提供内存管理、字符串操作、文件操作等标准函数。

在 Ubuntu 18.04.6 LTS 中，GLIBC 最高只有 2.27，在不升级系统更新 GLIBC 风险太大，因此可以考虑用 Docker 的方式来解决 LinearDesign 的 GLIBC 版本过低问题。

<!-- more -->

## 构建 LinearDesign 的 Docker 镜像

### 编写 Dockerfile

```yaml
# GUESSING....
# dfimage shenweiyan/lineardesign:1.0
# WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
# FROM shenweiyan/lineardesign:1.0

FROM ubuntu:jammy-20230425

ARG RELEASE
ARG LAUNCHPAD_BUILD_ARCH
LABEL org.opencontainers.image.ref.name=ubuntu
LABEL org.opencontainers.image.version=22.04
# ADD file:2fc6364d149eccc7f94ead482a0dcf24b0e44cc0d00ac6a2c1797776153e9608 in /

RUN apt-get update && apt-get install -y git

# Need to add Python2 (should be 2.7.18)
# https://linuxconfig.org/install-python-2-on-ubuntu-22-04-jammy-jellyfish-linux

RUN apt-get install -y python2

# Need to add GCC
# https://linuxconfig.org/how-to-install-gcc-the-c-compiler-on-ubuntu-22-04-lts-jammy-jellyfish-linux

RUN apt-get install -y build-essential

RUN apt-get clean

RUN git clone https://gitcode.com/bio-mirrors/LinearDesign.git /lineardesign # buildkit

RUN cd /lineardesign && make

RUN mkdir /mnt/data             # buildkit
WORKDIR /lineardesign
VOLUME [/mnt/data]
CMD ["/bin/bash"]
```

### 构建镜像

```bash
$ docker build -t lineardesign:1.0 .
```
![docker-build-lineardesign](https://gi.weiyan.tech/2026/03/docker-build-lineardesign.png)


### 查看镜像

```bash
docker images
```

### 运行容器

可以使用下面的方式开启 docker 容器。

1. 交互方式
   ```bash
   $ docker run  -it -v /home/steven/data:/data lineardesign:1.0 bash
   ```
   这种方式，通过 `exit` 退出容器后，容器被终止，可以通过 `docker ps -a` 来看终止状态的容器，可以通过 `docker rm <CONTAINER ID>` 删除终止状态的容器。

2. Daemon 方式，守护态运行
   ```bash
   $ docker run -d -it -v /home/steven/data:/data lineardesign:1.0 bash
   ```
   守护态运行运行的容器，在容器内 `exit` 退出后，容器不会终止，可以使用 `docker exec -it <CONTAINER ID> bash` 再次进入容器。      
   这种方式可以让软件作为长时间服务运行，可通过 `ocker stop <CONTAINER ID>`终止容器，通过 `ocker rm <CONTAINER ID>`删除终止状态的容器。

## 将本地镜像推送到远程仓库

这是指把我们构建好的镜像 push 到 Docker Hub、阿里云 ACR、Harbor 等远程 Registry，这里我们 push 到 Docker Hub。

### 登录远程仓库

首次登录会提示输入用户名/密码或 Access Token。

```bash
# Docker Hub
docker login

# 阿里云 ACR
docker login registry.cn-hangzhou.aliyuncs.com

# 私有 Harbor
docker login harbor.yourcompany.com
```

### 为镜像打标签

远程仓库要求镜像名称格式为：`<registry>/<namespace>/<repo>:<tag>`。

```bash
# 推送到 Docker Hub（用户名：shenweiyan）
docker tag lineardesign:1.0 shenweiyan/lineardesign:1.0

# 推送到阿里云 ACR
docker tag lineardesign:1.0 registry.cn-hangzhou.aliyuncs.com/shen-lab/lineardesign:1.0
```

### 推送镜像

```bash
# 推送到 Docker Hub
$ docker push shenweiyan/lineardesign:1.0
The push refers to repository [docker.io/shenweiyan/lineardesign]
5f70bf18a086: Pushed
f307a02003d0: Pushed
67721cd40298: Pushed
593672012667: Pushed
52bfb0e9f36b: Pushed
5dd52f89c1a9: Pushed
8fb8ac00d103: Pushed
c90d82bb7e29: Pushed
b8a36d10656a: Pushed
1.0: digest: sha256:aa43b247010b964a9b3faf434409463df12002bd9ecf03b1d41bf55f74df988e size: 2204

# 推送到阿里云
$ docker push registry.cn-hangzhou.aliyuncs.com/shen-lab/lineardesign:1.0
```

### 验证推送

```bash
# 查看远程仓库（网页或 CLI）
# 或拉取测试：
docker pull shenweiyan/lineardesign:1.0
```
![lineardesign-shenweiyan](https://gi.weiyan.tech/2026/03/lineardesign-shenweiyan.png)

![run-docker-lineardesign](https://gi.weiyan.tech/2026/03/run-docker-lineardesign.png)


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="179"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
