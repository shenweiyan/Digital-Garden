---
title: 更改 RHEL 6/7 中的时区
urlname: 2021-05-27-centos-rhel-6-7-timezone
author: 章鱼猫先生
date: 2021-05-27
updated: "2021-06-25 10:53:50"
---

这几天在学习折腾 docker 的时候遇到一个很常见的问题，就是 run container 的时候发现大部分 image 默认使用的时间都是 UTC  (Universal Time Coordinated,UTC）世界协调时间，跟平时中使用的 CST  (China Standard Time UTC+8:00) 中国沿海时间(北京时间) 差别有点大，很不适应。

每次去修改的时候又有点不太记得 `timedatectl` 的具体命令，甚至跑一些基于 CentOS/RHEL 6 镜像的流程时发现根本没有 `timedatectl` 这个命令！

虽然之前在《[【原】生信服务器 | Linux 时间戳和标准时间 · 语雀](https://www.yuque.com/bioitee/mp/linux-timestamp-date)》这个推文专门写了一些 `timedatectl` 命令的具体用法，基本都是针对 CentOS/RHEL 7 的系统，不适用于已经停止维护的 CentOS/RHEL 6。

所以，后来专门谷歌了一下，发现除了 `timedatectl`，还有更加简便的一些修改方法，记录一下。

## 在 CentOS/RHEL 6 中改变时区

在 CentOS 6 中，时区文件位于 **/usr/share/zoneinfo** 下。所以，如果你的区域是美国/芝加哥(UTC-6) ，它应该是 **/usr/share/zoneinfo/America/Chicago** 等等。

CentOS 6 使用位于 `/etc` 下的一个名为 "localtime" 的文件来确定当前设置的时区。

    $ ls -la /etc/localtime

这个文件，要么是移动到这个位置的实际时区文件，要么是 zoneinfo 目录下时区的符号链接（即软链接文件）。因此，如果您想要更改时区，首先需要确定使用哪个时区，然后将其符号链接到本地时间。你可以使用以下方法：

```bash
$ rm -f /etc/localtime
$ ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
$ date
```

这将把当前时区设置为 CST 亚洲/上海时区，我所属的时区。

## 在 CentOS/RHEL 7 中改变时区

CentOS 7 附带了一个叫做 timedatectl 的命令工具。这可以用来为您查找和设置符号链接，而不是完成 CentOS 6 中要求的工作。

若要列出可用的时区，请运行：

```bash
$ timedatectl list-timezones
```

你可以找到你想要的时区，如下：

```bash
$ timedatectl list-timezones | grep Shanghai
```

现在，要设置一个时区，使用命令`set-timezone`和`timedatectl`命令。例如，如果我想将时区设置为 Asia/Shanghai，我会运行以下命令：

```bash
$ timedatectl set-timezone Asia/Shanghai
$ date
```

上面的这个操作跟上面提到的 CentOS 6 修改时区一样，会创建一个链接到 zoneinfo 目录的 locatime 文件符号链接：

```bash
$ ls -l /etc/localtime
lrwxrwxrwx 1 root root 35 Apr  1 15:10 /etc/localtime -> ../usr/share/zoneinfo/Asia/Shanghai
```
