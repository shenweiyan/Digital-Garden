---
title: Singularity 初探之安装部署与避坑
urlname: 2023-04-18-try-singularity
author: 章鱼猫先生
date: 2023-04-18
updated: "2023-04-26 15:02:49"
---

## 背景

> 怎么样高效的搭建分析流程且能保证分析流程稳定运行的使用效果呢？目前主流的是 **conda** 和 **容器技术(container)**。
> 
> conda 在很多文章中中已经介绍，在这不再过多叙述。虽然 **conda 能解决大部分生信软件安装问题**，但是若**软件安装多了**，会出现**兼容性**问题以及 **"臃肿"** 现象，为此，引入容器技术 (container) 来解决这些问题。
> 
> 在容器技术中，**docker** 和 **singularity** 是常用的容器软件。但 **docker 不太适合 HPC 环境**。因为在调度管理器上容器无法施加资源限制、多用户（非 root 用户）使用时会出现权限问题、而且 docker 会存在一些不必要的资源开销。
> 
> 为此，引进 **singularity** 容器来解决 docker 的一些缺点。首先，**singularity 可以兼容 docker 的镜像**，同时构建出的镜像可以很容易进行拷贝和转移，且体积更小；此外 singularity 假设用户在一个有 root 权限的系统上构建容器，在一个没有 root 权限的系统上运行容器，兼顾了数据的安全性和便捷性，更加符合实际的应用场景。
> 
> 🔗 来源：《[Singularity——生信流程搭建的幸运儿](https://mp.weixin.qq.com/s/dILzbYZhkzqvDazj4GAHlw)——"生信小尧"公众号》

<br/>
> Singularity 是一种专为科学计算和 HPC 环境设计的容器技术，具有与 HPC 环境的无缝集成、高度的可移植性和兼容性、安全性和可控性等优势。在处理大规模数据、模拟和深度学习等领域中，具有广泛的应用价值。
> 
> 🔗 来源：《[Singularity 使用真简单](https://mp.weixin.qq.com/s/PU3orRKAT5XziBsyJdhP3Q)！——"HPCLIB"公众号》

## 安装

最开始选择从 GitHub 的源码库 <https://github.com/sylabs/singularity/> 中进行**非 root 的普通用户**手动安装。
服务器系统版本和内核版本：

```bash
$ lsb_release -a
LSB Version:    :base-4.0-amd64:base-4.0-noarch:core-4.0-amd64:core-4.0-noarch:graphics-4.0-amd64:graphics-4.0-noarch:printing-4.0-amd64:printing-4.0-noarch
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 6.5 (Santiago)
Release:        6.5
Codename:       Santiago
$ uname -a
Linux log01 2.6.32-431.el6.x86_64 #1 SMP Sun Nov 10 22:19:54 EST 2013 x86_64 x86_64 x86_64 GNU/Linux
```

出现了几个问题：

1. singularity 2.5.0 及以上要求升级 Linux 内核，否则`configure`会出现错误：<br/>
   **The `NO_NEW_PRIVS` bit is supported since Linux 3.5！**
   <br/> 
   ```bash
   $ ./configure --prefix=/home/shenweiyan/software/Singularity-2.5.0
   checking for feature: NO_NEW_PRIVS... no
     
   ERROR!!!!!!

   This host does not support the NO_NEW_PRIVS prctl functions!
   ```
   
2. singularity 2.4.6 虽然能在**非 root 的普通用户**手动安装下安装成功，但很多功能不支持，甚至导致错误：  
    - 在 pull 下载一些镜像时，会引发 urllib2.URLError 的 ssl 异常：

    ```
    $ singularity pull shub://vsoch/hello-world
    测试在嵌套列表中插入代码

    最后一行
    ```

    - build 时候，要求安装 squashfs-tools：

3. 嵌套列表测试

    ```bash
    $ singularity build hello-world.simg shub://vsoch/hello-world
    ERROR: You must install squashfs-tools to build images
    ABORT: Aborting with RETVAL=255
    ```

鉴于以上问题，最后选择了通过 mamba/conda 的方式安装，并最终安装成功 3.7.1 版本。
```bash
$ mamba create -n singularity -c conda-forge singularity
$ singularity version
3.7.1
```

测试了很多次才发现，基于 conda/mamba 安装的 singularity，使用上多少都会出现各种问题（如下面）。

## SetUID

```bash
(singularity) bi.admin@log01 16:14:41 /home/bi.admin/Singularity
$ singularity build --sandbox lolcow/ library://sylabs-jms/testing/lolcow
INFO:    Starting build...
INFO:    Downloading library image
87.9MiB / 87.9MiB [==============================================================================] 100 % 214.0 KiB/s 0s
INFO:    Verifying bootstrap image /home/bi.admin/.singularity/cache/library/sha256.5022b5e7c7249c40119a875c1ace0700ced4099e077acc75d0132190254563a4
WARNING: integrity: signature not found for object group 1
WARNING: Bootstrap image could not be verified, but build will continue.
ERROR:   unpackSIF failed: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found
FATAL:   While performing build: packer failed to pack: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found
```

```bash
[root@log01 Singularity]# singularity build --sandbox lolcow/ library://sylabs-jms/testing/lolcow
INFO:    Starting build...
INFO:    Downloading library image
87.9MiB / 87.9MiB [==============================================================================] 100 % 205.2 KiB/s 0s
INFO:    Verifying bootstrap image /root/.singularity/cache/library/sha256.5022b5e7c7249c40119a875c1ace0700ced4099e077acc75d0132190254563a4
WARNING: integrity: signature not found for object group 1
WARNING: Bootstrap image could not be verified, but build will continue.
ERROR:   unpackSIF failed: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found
FATAL:   While performing build: packer failed to pack: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found

[root@log01 Singularity]# singularity exec ubuntu_20.04.sif date
WARNING: underlay of /etc/localtime required more than 50 (67) bind mounts
FATAL: kernel too old
```

- root/sudo 用户才能 build 建立镜像沙箱？说好的不依赖于 root 呢？
- 以下链接内容说明了非 root 用户也可以安装和使用 singularity：<br/>
  <https://docs.sylabs.io/guides/3.5/admin-guide/installation.html#install-nonsetuid>
[issues 1258: Does Singularity support installation by user without root privileges?](https://github.com/apptainer/singularity/issues/1258)
但有要求：

   1. 内核版本 >=3.8 - <https://apptainer.org/docs/admin/main/user_namespace.html><br/>
To allow unprivileged creation of user namespaces a kernel >=3.8 is required, with >=4.18 being recommended due to support for unprivileged mounting of FUSE filesystems (needed for example for mounting SIF files). The equivalent recommendation on RHEL7 is >=3.10.0-1127 from release 7.8, where unprivileged mounting of FUSE filesystems was backported. To use unprivileged overlayFS for persistent overlays, kernel >=5.11 is recommended, but if that’s not available then Apptainer will use fuse-overlayfs instead. That feature has not been backported to RHEL7.

   2. 默认安装要求安装文件具备 SetUID 权限，这一点暂时没能理解！！！<br/>
[Linux SetUID（SUID）文件特殊权限用法详解](http://c.biancheng.net/view/868.html)

### User Namespace

Singularity 如果不适用 SetUID，那它通过普通用户安装运行是要求开启 User Namespace！

> When singularity/SingularityCE does not use setuid all container execution will use a user namespace.
> 
> 🔗 来源：<https://docs.sylabs.io/guides/3.8/admin-guide/user_namespace.html>

![701e36aec39a4a3be99fe11548aa4da.jpg](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkpKd2AaoQ5kl1HM67TWhEeOrzoq.jpeg)

> **📢 知识点 - User namespace**
> 
> User namespace 是 Linux 3.8 新增的一种 namespace，用于隔离安全相关的资源，包括 **user IDs** and **group IDs**，**keys**, 和 **capabilities**。同样一个用户的 user ID 和 group ID 在不同的 user namespace 中可以不一样(与 PID nanespace 类似)。换句话说，一个用户可以在一个 user namespace 中是普通用户，但在另一个 user namespace 中是超级用户。
> 
> User namespace 可以嵌套(目前内核控制最多 32 层)，除了系统默认的 user namespace 外，所有的 user namespace 都有一个父 user namespace，每个 user namespace 都可以有零到多个子 user namespace。 当在一个进程中调用 unshare 或者 clone 创建新的 user namespace 时，当前进程原来所在的 user namespace 为父 user namespace，新的 user namespace 为子 user namespace。
> 
> 🔗 来源：《[Linux Namespace: User](https://www.cnblogs.com/sparkdev/p/9462838.html) - 博客园》


> 在 CentOS 内核 3.8 或更高版本中，添加了 user namespaces （户名命名空间）功能。但是，该功能默认情况下是禁用的，原因是 Red Hat 希望该功能在社区中孵化更长时间，以确保该功能的稳定性和安全性。目前越来越多的软件开始涉及该功能，例如 Docker 等。
> 
> 🔗 来源：《[CentOS 7 启用 user namespaces（用户命名空间）](https://www.123si.org/os/article/centos-7-enable-user-namespaces/)——123si 博客》

在 CentOS 7.7 + 3.10.0-1062.1.1.el7.x86_64 内核下使用`conda create -n singularity -c conda-forge singularity`安装了 singularity-3.8.6 后发现，pull/shell/exec 都没问题，但 build 会出现异常：

```bash
$ singularity pull docker://ubuntu:20.04
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Getting image source signatures
Copying blob ca1778b69356 done
Copying config 88bd689171 done
Writing manifest to image destination
Storing signatures
2023/04/19 09:59:37  info unpack layer: sha256:ca1778b6935686ad781c27472c4668fc61ec3aeb85494f72deb1921892b9d39e
INFO:    Creating SIF file...

$ singularity build --sandbox blast ubuntu_20.04.sif
INFO:    Starting build...
INFO:    Verifying bootstrap image ubuntu_20.04.sif
WARNING: integrity: signature not found for object group 1
WARNING: Bootstrap image could not be verified, but build will continue.
ERROR:   unpackSIF failed: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found
FATAL:   While performing build: packer failed to pack: root filesystem extraction failed: could not extract squashfs data, unsquashfs not found
```

使用`yum install squashfs-tools`安装了`unsquashfs`并添加到 $PATH 中问题依然没法解决！！！
![16f4cadef5c03cdafaae5847f3e0672.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkbnpUiB0x8v8X1EhUpD3Xm7dznd.png)

### 源码编译

最后还是选择从源码安装。

#### 安装 Go

```bash
wget https://dl.google.com/go/go1.20.1.linux-amd64.tar.gz
tar -xzvf go1.20.1.linux-amd64.tar.gz
sudo ln -s go /usr/local/bin
```

#### 安装 singularity

如果想要非 root 的普通用户也能正常使用，mconfig 时候需要加上 **--without-suid**。

```bash
$ wget https://github.com/apptainer/singularity/releases/download/v3.8.7/singularity-3.8.7.tar.gz
$ tar zvxf singularity-3.8.7.tar.gz
$ cd singularity-3.8.7
$ ./mconfig --prefix=/ifs1/singularity/singularity-3.8.7 --without-suid
$ make -C ./builddir
$ make -C ./builddir install
```

#### 使用测试

初步测试 singularity build 也能正常使用了。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fg7yJ8XqLya8z_7rI38Te4cVl3YG.png)
