---
title: 远程挂载 NFS 共享目录引发死机问题
urlname: 2020-05-18-nfs-umount
author: 章鱼猫先生
date: 2020-05-18
updated: "2021-06-25 10:54:51"
---

> 集群的存储空间有限，把一些历史的归档数据放在了公司的另外一台老旧存储服务器上，并使用 NFS 把它挂载到了 log 节点。周末的时候机房空调故障，旧存储服务器挂掉了！周一上班，在集群登陆节点使用 df -Th 查看磁盘使用情况，发现 df 命令卡死，查看挂载盘目录的时候也卡死，本文为本次异常的一些处理记录。

## 环境描述

A 机器（192.168.1.103）为数据的实际存储服务器。
B 机器（即集群登 log 陆节点）上挂载了 A 机器上的 hiseq3000 目录到本机的 /mnt/hiseq3000 目录（命令： `mount -t nfs 192.168.1.103:/hiseq3000 /mnt/hiseq3000`）

## 故障描述

现在因 A 机器（数据实际存储服务器）因故障无法访问，登录 B 机器以后执行 `mount` ， `df -h` ， `ll  /mnt/hiseq3000`  等关于 /mnt 挂载点的时候都会卡住，ctrl + c  、 ctrl + z 都不能结束，只能退出重新登录。

## 解决方法

```bash
[root@log ~]# umount -f /mnt/hiseq3000
umount2: Device or resource busy
umount.nfs: /mnt/hiseq3000: device is busy
[root@log ~]# umount -f /mnt/hiseq3000
umount2: Device or resource busy
umount.nfs: /mnt/hiseq3000: device is busy
[root@log ~]# umount -f /mnt/hiseq3000
umount2: Device or resource busy
umount.nfs: /mnt/hiseq3000: device is busy
[root@log ~]# umount -f /mnt/hiseq3000
umount2: Invalid argument
umount: /mnt/hiseq3000: not mounted

```

**前面貌似执行  umount -f /mnt/hiseq3000 强制卸载时不起作用的，但是最后是能卸载掉的！！！**
\*\*
\*\*

## 原因分析

**
当 NFS 服务端（即数据实际存储的 A 服务器）停止提供挂载服务时，客户端（集群登陆 log 挂载节点）会出现卡死的情况，导致文件系统不能查看相关信息，此时可以重新启动 nfs 服务端来恢复客户端的查询功能；如果不重启  nfs 服务端的话，只能通过上面的 `umount -f`  进行强制卸载。
**
**有人说为了避免这个问题，挂载的时候要加和上 soft 选项。（没亲自试过）**

> 而导致此问题的原因是在使用 nfs 挂载的时候使用的是默认的 hard-mount 挂载功能，当服务端停止服务时，客户端加载 nfs 不成功，就会不断的重试，直到服务端恢复之前，挂载目录都会出现卡死的情况。hard-mount 是系统的缺省值。在选定 hard-mount 时，最好同时选 intr , 允许中断系统的调用请求，避免引起系统的挂起。当 NFS 服务器不能响应 NFS 客户端的 hard-mount 请求时， NFS 客户端会显示 "NFS server hostname not responding, still trying"。
>
> 因此需要在挂载时更换为 soft-mount，使用此功能挂载后，当服务端出现停止服务的情况时，会重试 retrans 设定的固定次数。如果 retrans 次都不成功，则放弃此操作，返回错误信息 "Connect time out"。
>
> 挂载命令（retry 和 retrans 两个参数的区别？？？）：

```bash
mount -t nfs  -o rw,intr,soft,timeo=30,retry=3 nfs-server://share-path local-path
```

> /etc/fstab：

```bash
nfs-server:/share-path    /local-path    nfs    rw,soft,intr    0 0
```

## **NFS 服务器的故障排除**

NFS 出现了故障，可以从以下几个方面着手检查：

1.  NFS 客户机和服务器的负荷是否太高，服务器和客户端之间的网络是否正常。

我们可以使用常见的网络连接和测试工具 ping 及 tracerroute 来测试网络连接及速度是否正常，网络连接正常是 NFS 作用的基础。

2.  /etc/exports 文件的正确性。
3.  必要时重新启动 NFS 或 portmap 服务。运行下列命令重新启动 portmap 和 NFS：

```bash
# /etc/init.d/portmap restart		# 适用RHEL/CentOS 5.x
# /etc/init.d/nfs restart
# /etc/init.d/rpcbind restart 	# 在RHEL/CentOS 6.x里面
# chkconfig portmap on
# chkconfig nfs on
# chkconfig rpcbind on 	# 在RHEL/CentOS 6.x里面
```

注意：在 RHEL/CentOS 6.x 里面，portmap 服务改名为 rpcbind 服务了；顺便说一下，rpcbind 服务也是图形界面的关键基础服务，不启动此服务，不能启动图形桌面。

4.  检查客户端中的 mount 命令或 /etc/fstab 的语法是否正确。
5.  查看内核是否支持 NFS 和 RPC 服务。一般正常安装的 Linux 系统都会默认支持 NFS 和 RPC 服务，除非你自己重新编译的内核，而且没选择 nfs 支持选项编译。
