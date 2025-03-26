---
title: 腾讯云/阿里云升级 Rocky Linux
urlname: 2021-09-30-cvm-migrate2rocky
author: 章鱼猫先生
date: 2021-09-30
updated: "2022-05-27 12:05:55"
---

昨天在语雀开了一个话题讨论《[CentOS 7 和 8 不维护停止更新之后，服务器选择使用什么系统好？](https://www.yuque.com/bioitee/topics/3)》，在[ V2EX](https://www.v2ex.com/t/805300) 收到不少回复。

在前几天正好入手了腾讯云/阿里云的一个 2 核 4G，80GB SSD 盘的轻量云服务器，首年才 74，作为尝鲜一开始装了个 Debian 10，不得不说，RH 系用久了，回到 Debian/Ubuntu 还真是一下子没适应过来。

也看到不少朋友都已经在生产环境用上了 Rocky Linux 和 CentOS 8 无缝对接，突发奇想也想体验一下，搜了一圈发现虽然 Rocky Linux 迁移和安装的教程不少，但唯独没找到在云服务上的迁移的，而且目前国内的阿里云/腾讯云/华为云都没有提供 Rocky Linux 的镜像，于是开始自己折腾。

## 安装前准备

步骤 1. 首先，把你的服务器变更成 CentOS 8.x 系统。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk1qd_KA0bQQGzVlj9Uu_tQQZ9uy.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqaH_jPUZfUgkZAmwc4ArAdgoh9P.png)

如果你用的是阿里云的 ECS（或者轻量云服务，个人用的是轻量云服务器），可以先升级到 CentOS 8.2 的系统。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtaE7Ybb8ewn_cJAxlYFqd9Zah5B.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjCrRWqy1hrIsHHOYghc8rB78VmF.png)

步骤 2. 然后，让我们先确保您的系统是最新的（如果已经是 CentOS 8.0 及以上，可以不用执行这一步）。

```bash
# 这一步会把系统升级到最新的版本，如果你是 CentOS 8.0，可能会升级到 8.5
sudo dnf update
sudo dnf upgrade
```

步骤 3. 下载 Rocky Linux 8 到 CentOS 8 的迁移脚本。

Rocky Linux 提供了一个名为的工具 [migrate2rocky](https://docs.rockylinux.org/zh/guides/migrate2rocky/)，该工具已在许多 RHEL 变体（例如 CentOS、AlmaLinux 和 Oracle Linux）上成功测试：

```bash
curl https://raw.githubusercontent.com/rocky-linux/rocky-tools/main/migrate2rocky/migrate2rocky.sh -o migrate2rocky.sh
```

或者，可以通过 git 下载：

```bash
dnf install git
git clone https://github.com/rocky-linux/rocky-tools.git
```

## 安装

这可能是最简单的一点。 登录到您的服务器，然后使用命令放终端 cd 到包含 migrate2rocky.sh 文件的文件目录。

然后，确保文件是可执行的：

```bash
sudo chmod +x migrate2rocky.sh
```

接下来，执行脚本：

    ./migrate2rocky.sh -r

- \-r 选项告诉脚本继续安装所有内容 (That "-r" option tells the script to just go ahead and install everything.)。

```bash
$ ./migrate2rocky.sh -r
Preparing to migrate CentOS Linux 8 to Rocky Linux 8.

Determining repository names for CentOS Linux 8.....

Found the following repositories which map from CentOS Linux 8 to Rocky Linux 8:
CentOS Linux 8  Rocky Linux 8
appstream       appstream
baseos          baseos
extras          extras

Getting system package names for CentOS Linux 8.......

Found the following system packages which map from CentOS Linux 8 to Rocky Linux 8:
CentOS Linux 8        Rocky Linux 8
centos-backgrounds    rocky-backgrounds
centos-gpg-keys       rocky-gpg-keys
centos-logos          rocky-logos
centos-indexhtml      rocky-indexhtml
centos-linux-release  rocky-release
centos-linux-repos    rocky-repos
[...]
```

- 如果出现以下的报错信息，则参考 [Invalid configuration value: failovermethod=priority in repo config files](https://bugzilla.redhat.com/show_bug.cgi?id=1961083)，把 failovermethod=priority 一行从 /etc/yum.repos.d/CentOS-epel.repo 中删除。

```shell
[root@iZ7xv4bbjwm8qgx8m72z68Z ~]# ./migrate2rocky.sh -r

Removing dnf cache
Preparing to migrate CentOS Linux 8 to Rocky Linux 8.

Determining repository names for CentOS Linux 8.Invalid configuration value: failovermethod=priority in /etc/yum.repos.d/CentOS-epel.repo; Configuration: OptionBinding with id "failovermethod" does not exist
```

成功迁移 Rocky Linux 后，您应该会看到以下输出：

```bash
...
Complete!

Done, please reboot your system.
A log of this installation can be found at /var/log/migrate2rocky.log
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fr1ZwTn16QfdEweKjhpCu1Yajb9K.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FitnvEWO4d23TX-NSQz-pObx8xuO.png)

然后，运行以下命令来同步已安装的软件包，然后只需重新启动系统：

```bash
sudo dnf distro-sync -y
sudo reboot
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsTMKsGBRiRbvRM3DdeYrEfYgDU0.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fus9rZsnBGvgLohr18SnW1ZKByPu.png)

## 检查操作系统版本

为了确认您已成功迁移到 Rocky Linux，请检查操作系统版本：

```bash
cat /etc/redhat-release
```

输出：

```bash
Rocky Linux release 8.4 (Green Obsidian)
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlNtsYaHWfIDJhP9Vb5x1fq7gtsg.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp801elk1r_VJpvx1bzvp4L0Q-ks.png)

## 参考资料

1.  [Migrating To Rocky Linux - Documentation](https://docs.rockylinux.org/guides/migrate2rocky/)，官方文档
2.  [如何从 CentOS 8 迁移到 Rocky Linux 8](https://www.xtuos.com/2819.html) - 统信 UOS 之家
