---
title: RockyLinux 9 基础配置与使用
number: 60
slug: discussions-60/
url: https://github.com/shenweiyan/Digital-Garden/discussions/60
date: 2024-03-08
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.17-服务器配置使用']
---

今天终于在阿里云入手了一台 2核(vCPU)+ 2GiB + 3Mbps 的 ECS，安装了最新的 Rocky Linux release 9.3 (Blue Onyx)，记录一下开箱后的一些基础配置。

<!-- more -->

![aliyun-99-plan](https://shub.weiyan.tech/kgarden/2024/03/aliyun-99-plan.png)

## Hostname
```
[root@r0sasd1bQi ~]# hostnamectl   # 查看一下当前主机名的情况
[root@r0sasd1bQi ~]# hostnamectl set-hostname shen-server --static
[root@r0sasd1bQi ~]# hostnamectl status
[root@r0sasd1bQi ~]# reboot now    # 重启服务器
```

## 创建新用户

使用 `adduser` 命令将新用户添加到系统中：
```bash
adduser shenweiyan    # 创建新用户
passwd shenweiyan     # 修改密码
```

## 用户添加超级权限

把 `shenweiyan` 用户添加超级权限（`/etc/sudoers`）：
```
shenweiyan      ALL=(ALL)       NOPASSWD: ALL
```

## 自定义快捷方式

在 `~/.bashrc` 最后新增一下用户自定义的快捷方式。

```
# User Specific Alias
alias disp='display'
alias rm='rm -i'
alias la='ls -al'
alias ll='ls -lh'
alias le='less -S'

# Custom History setting
# HISTFILESIZE 定义了在 .bash_history 中保存命令的记录总数
HISTFILESIZE=3000000
# HISTSIZE 定义了 history 命令输出的记录数
HISTSIZE=3000
# 定义 History 输出格式
export HISTTIMEFORMAT='%F %T '
# 使用 HISTCONTROL 从命令历史中剔除连续重复的条目
HISTCONTROL=ignoredups
# 将 bash 内存中历史命令追加到 .bash_history 历史命令文件中， 默认只有退出 shell 是才会保存
PROMPT_COMMAND="history -a"

# Login Style
PS1='\033[35;1m\u@\h \[\e[m\]\t \[\033[36;1m\]$(pwd) \n$ \[\e[m\]'
clear;
```

## epel-release

> 企业版 Linux 附加软件包（Extra Packages for Enterprise Linux，以下简称 EPEL）是一个 Fedora 特别兴趣小组，用以创建、维护以及管理针对企业版 Linux 的一个高质量附加软件包集，面向的对象包括但不限于 [红帽企业版 Linux (RHEL)](https://fedoraproject.org/wiki/Red_Hat_Enterprise_Linux/zh-cn)、 CentOS、Scientific Linux (SL)、Oracle Linux (OL) 。
> 
> 参考：[EPEL/zh-cn - Fedora Project Wiki](https://fedoraproject.org/wiki/EPEL/zh-cn)

```bash
# 下面两个命令都可以安装
sudo dnf install epel-release
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

## Htop 和 Btop

[Htop](https://htop.dev/) 是一个基于 C 编写的跨平台的交互式流程查看器，`htop` 是 `top` 的一个增强替代品，提供了更加友好的用户界面和更多的功能，相比系统自带的 `top` 更加直观好用。 

```bash
sudo dnf install htop
```

`btop` 也是一个改进版的 Linux top 命令，这个命令不仅列出了各种系统使用情况，包括内存、磁盘、网络和进程，而且还允许与鼠标互动。即使是在服务器安装上，你也可以在 `btop` 上指指点点，以树形方式查看进程，隐藏或显示某些显示，并访问选项菜单，在那里你可以调整显示的外观和感觉。
```bash
sudo dnf install btop
```

## Docker 安装与使用

主要参考《[How To Install and Use Docker on Rocky Linux 9](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-rocky-linux-9)》，具体步骤如下：     

- add the official Docker repository
  ```bash
  sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  ```

- install Docker
  ```bash
  sudo dnf install docker-ce docker-ce-cli containerd.io
  ```

- start the Docker daemon
  ```bash
  sudo systemctl start docker
  ```

- Verify that it’s running
  ```bash
  sudo systemctl status docker
  ```
  ```
  Output
  ● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2016-05-01 06:53:52 CDT; 1 weeks 3 days ago
       Docs: https://docs.docker.com
   Main PID: 749 (docker)
  ```

- make sure it starts at every server reboot
  ```bash
  sudo systemctl enable docker
  ```

- 配置非 root 用户使用 Docker
  ```bash
  sudo usermod -aG docker username
  newgrp docker                     #更新docker用户组
  ```

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="60"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
