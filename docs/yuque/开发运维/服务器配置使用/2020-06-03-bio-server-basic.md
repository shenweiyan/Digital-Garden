---
title: 生信服务器入门级基本设置
urlname: 2020-06-03-bio-server-basic
author: 章鱼猫先生
date: 2020-06-03
updated: "2021-07-19 11:20:16"
---

前两天拿到了云筏科技提供的一台 4 核 16G 内存，1TB 硬盘，300M 带宽的服务器（看了一下 IP，应该是位于加拿大的服务器）！虽然是国外的服务器，但从国内 ssh 上去后的各种操作还是非常流畅的，而且前期白菜般的体验价格和飞一般的带宽的确也很有吸引力，像我用来做 Galaxy 和一些 web 开发测试完全是没问题。另外该服务器还自带了一个开箱即用的 RStudio-Server，对生信入门者来说也算是比较友好了，最起码节省了不少部署设置的功夫。

作为体验性服务器，这里简单介绍一下拿到服务器后的一些基本设置。
![cr-rstudio.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fl7tAv0j29yaClshZLBsurEvzHKR.png)

## 1. 查看配置信息

- 查看内核版本

```bash
[root@r0sasd1bQi ~]# cat /proc/version  # 可以看到该服务器为 Redhat/CentOS 发行版本
Linux version 3.10.0-957.el7.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-36) (GCC) ) #1 SMP Thu Nov 8 23:39:32 UTC 2018
```

- 查看详细版本信息

```bash
# 如果 lsb_release command not found，通过下面的方式安装
[root@r0sasd1bQi ~]# yum install redhat-lsb -y

[root@r0sasd1bQi ~]# lsb_release -a		# 列出所有版本信息
LSB Version:    :core-4.1-amd64:core-4.1-noarch:cxx-4.1-amd64:cxx-4.1-noarch:desktop-4.1-amd64:desktop-4.1-noarch:languages-4.1-amd64:languages-4.1-noarch:printing-4.1-amd64:printing-4.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 7.6.1810 (Core)
Release:        7.6.1810
Codename:       Core
```

- 查看 cpu 数

```bash
# 总核数 = 物理CPU个数 X 每颗物理CPU的核数
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l
```

- 查看内存（可用 `top`  命令直接查看，或者安装 `htop`  查看）

```bash
# 在 CentOS 7 上启用 epel 版本
[root@r0sasd1bQi ~]# yum -y install epel-release

# 安装 htop
[root@r0sasd1bQi ~]# yum -y install htop

# 查看内存、CPU
[root@r0sasd1bQi ~]# htop
```

![htop.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqKKMNZ9J75Qb40n5iChJmY3cSIH.png)

## 2. 账号与用户名管理

拿到服务器第一件事就是修改用户名密码，以及创建新账号，毕竟 root 权限太大！

- 修改 root 密码

```bash
[root@r0sasd1bQi ~]# passwd
Changing password for user root.
New password: <输入新的密码>
Retype new password: <再次输入新的密码>
passwd: all authentication tokens updated successfully.
```

- 创建用户与工作组

```bash
# 创建工作组
[root@r0sasd1bQi ~]# groupadd bioinfo 	//新建 bioinfo 工作组

# 新建用户并指定工作组(-g 所属组；-d 家目录；-s 所用的 SHELL)
[root@r0sasd1bQi ~]# useradd shenweiyan -g bioinfo   //新建 shenweiyan 用户并增加到 bioinfo 工作组

# 查看用户信息
[root@r0sasd1bQi ~]# id shenweiyan
uid=1001(shenweiyan) gid=1001(bioinfo) groups=1001(bioinfo)

# 修改用户密码
[root@r0sasd1bQi ~]# passwd shenweiyan
Changing password for user shenweiyan.
New password: <输入新的密码>
Retype new password: <再次输入新的密码>
passwd: all authentication tokens updated successfully.
```

## 3. 个性化设置

### 变更 hostname

新的服务器一般自带的 hostname 都是一串无规律的字符串，很难记也不好看（例如我们这个服务器的 r0sasd1bQi ），对于有强迫症的童鞋可以参考下面的方法去修改。

> 在 CentOS 7 中，有三种定义的主机名：静态的（static）、瞬态的（transient）、灵活的（pretty）。“静态”主机名也称为内核主机名，是系统在启动时从 /etc/hostname 自动初始化的主机名。“瞬态”主机名是在系统运行时临时分配的主机名，例如，通过 DHCP 或 mDNS 服务器分配。静态主机名和瞬态主机名都遵从作为互联网域名同样的字符限制规则。而另一方面，“灵活”主机名则允许使用自由形式（包括特殊/空白字符）的主机名，以展示给终端用户。
>
> - 方法一，通过 `hostnamectl`  来修改主机名。修改后需要重启服务器。

```bash
[root@r0sasd1bQi ~]# hostnamectl   #查看一下当前主机名的情况
   Static hostname: r0sasd1bQi
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b6302a1a586547a09aae75efbfa34901
           Boot ID: f75d72657c524500b47edc250c13c6f2
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.el7.x86_64
      Architecture: x86-64

[root@r0sasd1bQi ~]# hostnamectl set-hostname bioitee-server --static
[root@r0sasd1bQi ~]# hostnamectl status
   Static hostname: bioitee-server
         Icon name: computer-vm
           Chassis: vm
        Machine ID: b6302a1a586547a09aae75efbfa34901
           Boot ID: f75d72657c524500b47edc250c13c6f2
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-957.el7.x86_64
      Architecture: x86-64

[root@r0sasd1bQi ~]# reboot now    # 重启服务器
```

> - 方法二，通过修改文件 `/etc/hostname`  来实现主机名的修改。把该文件内容替换成自己想要的主机名重启即可。

```bash
[root@r0sasd1bQi ~]# vim /etc/hostname		# 修改 hostname
[root@r0sasd1bQi ~]# reboot now    				# 重启服务器
```

> ————————————————
> 版权声明：本文为 CSDN 博主「点亮梦想那束光」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
> 原文链接：<https://blog.csdn.net/solaraceboy/java/article/details/78563537>

![hostname.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmcf0bFiRfvZF4V66GmwxJvEj8GG.png)

### 个性化命令行提示符

bash 中命令行提示符的格式是由 PS1 来控制的。 `/etc/bashrc`  中 PS1 的格式定义用于控制全局用户的命令行提示符样式；而针对个人用户的  PS1 设置，位于 `~/.bashrc`  中。

我自己的 PS1 定义：

```bash
PS1='\033[35;1m\u@\h \[\e[m\]\t \[\033[36;1m\]$(pwd) \n$ \[\e[m\]'
cd /data; clear;
```

![bashrc.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvpFQwosMTxV8Ulwu342gWjOXSkg.png)

有关于 PS1 的格式介绍如下：

```bash
序列					说明
\a			ASCII 响铃字符（也可以键入 \007）
\d			"Wed Sep 06" 格式的日期
\e			ASCII 转义字符（也可以键入 \033）
\h			主机名的第一部分（如 "mybox"）
\H			主机的全称（如 "mybox.mydomain.com"）
\j			在此 shell 中通过按 ^Z 挂起的进程数
\l			此 shell 的终端设备名（如 "ttyp4"）
\n			换行符
\r			回车符
\s			shell 的名称（如 "bash"）
\t			24 小时制时间（如 "23:01:01"）
\T			12 小时制时间（如 "11:01:01"）
\@			带有 am/pm 的 12 小时制时间
\u			用户名
\v			bash 的版本（如 2.04）
\V			Bash 版本（包括补丁级别）
\w			当前工作目录（如 "/home/shenweiyan"）
\W			当前工作目录的 "basename"（如 "shenweiyan"）
\!			当前命令在历史缓冲区中的位置
\#			命令编号（只要您键入内容，它就会在每次提示时累加）
\$			如果您不是超级用户 (root)，则插入一个 "$"；如果您是超级用户，则显示一个 "#"
\xxx		插入一个用三位数 xxx（用零代替未使用的数字，如 "\007"）表示的 ASCII 字符
\\			反斜杠
\[			这个序列应该出现在不移动光标的字符序列（如颜色转义序列）之前。它使 bash 能够正确计算自动换行。
\]			这个序列应该出现在非打印字符序列之后。
```

以上就是今天关于服务器入门的一些基本设置。在个性化设置上我们还可以进行 Alias、History、PATH 环境变量等的配置；在更高水平上的一些服务器安全策略，欢迎参考相关链接。

随着使用的不断深入，如果你发现了其他一些更强大更好玩的服务器使用或者设置小技巧，不妨在留言区写下你的分享！
