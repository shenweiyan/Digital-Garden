---
title: 非 root 用户手动编译安装 GCC
urlname: 2019-07-01-linux-gcc-install
author: 章鱼猫先生
date: 2019-07-01
updated: "2023-03-24 09:44:07"
---

我们知道，关于 GCC 在 CentOS 下通过 yum 安装默认版本号，CentOS 5 是 4.1.2；CentOS 6 是 4.4.7；CentOS 7 是 4.8.3。很多时候在编译安装软件都需要高版本的 GCC，否则就会报错。那么如何升级 GCC 的版本呢？

首先要确认升级到的 GCC 版本号。目前 GCC 的最新版已经到了 9.1（2019-05-03），而 CentOS 7 则依然使用其 4.8，所以基于兼容性考虑，可以选择升级到 4.8.5。GCC 官网：[https://gcc.gnu.org](https://gcc.gnu.org/)。

需要注意，编译安装 GCC 内存不小于 1GB，Swap 不小于 1GB，硬盘最低不小于 10GB，否则极有可能会中途报错退出。编译安装完后，目录 GCC-4.8.5 将会有 5GB 之多。

## 1. 下载源码

源码地址：<https://ftp.gnu.org/gnu/gcc/>

```shell
wget ftp://ftp.gnu.org/gnu/gcc/gcc-4.8.5/gcc-4.8.5.tar.gz --no-check-certificate
```

## 2. 下载依赖包

编译安装 GCC 需要依赖 mpc，mpfr，gmp，isl 包。前四个包是 GNU 软件，使用 GCC 源码里自带脚本（**./contrib/download_prerequisites**）可以轻松下载；对于下载不成功的，需要我们手动去下载。

```shell
$ tar zxf gcc-4.8.5.tar.gz
$ cd gcc-4.8.5
$ ./contrib/download_prerequisites
--2019-06-06 16:18:09--  ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-2.4.2.tar.bz2
           => “mpfr-2.4.2.tar.bz2”
Resolving gcc.gnu.org... 209.132.180.131
Connecting to gcc.gnu.org|209.132.180.131|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /pub/gcc/infrastructure ... done.
==> SIZE mpfr-2.4.2.tar.bz2 ... 1077886
==> PASV ... done.    ==> RETR mpfr-2.4.2.tar.bz2 ... done.
Length: 1077886 (1.0M) (unauthoritative)

100%[=================================================================================>] 1,077,886    249K/s   in 4.2s

2019-06-06 16:18:19 (249 KB/s) - “mpfr-2.4.2.tar.bz2” saved [1077886]

--2019-06-06 16:18:20--  ftp://gcc.gnu.org/pub/gcc/infrastructure/gmp-4.3.2.tar.bz2
           => “gmp-4.3.2.tar.bz2”
Resolving gcc.gnu.org... 209.132.180.131
Connecting to gcc.gnu.org|209.132.180.131|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /pub/gcc/infrastructure ... done.
==> SIZE gmp-4.3.2.tar.bz2 ... 1897483
==> PASV ... done.    ==> RETR gmp-4.3.2.tar.bz2 ... done.
Length: 1897483 (1.8M) (unauthoritative)

100%[=================================================================================>] 1,897,483    210K/s   in 7.7s

2019-06-06 16:18:30 (239 KB/s) - “gmp-4.3.2.tar.bz2” saved [1897483]

--2019-06-06 16:18:31--  ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-0.8.1.tar.gz
           => “mpc-0.8.1.tar.gz”
Resolving gcc.gnu.org... 209.132.180.131
Connecting to gcc.gnu.org|209.132.180.131|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD (1) /pub/gcc/infrastructure ... done.
==> SIZE mpc-0.8.1.tar.gz ... 544950
==> PASV ... done.    ==> RETR mpc-0.8.1.tar.gz ... done.
Length: 544950 (532K) (unauthoritative)

100%[=================================================================================>] 544,950      286K/s   in 1.9s

2019-06-06 16:18:35 (286 KB/s) - “mpc-0.8.1.tar.gz” saved [544950]

$ wget http://isl.gforge.inria.fr/isl-0.14.tar.gz
$ tar zvxf isl-0.14.tar.gz
$ ln -s lsl isl-0.14
```

在此脚本里可以看到依赖包的版本号依次是 mpc-0.8.1，mpfr-2.4.2，gmp-4.3.2；另外我们下载 isl-0.14。

在 GCC-7.3.0 中，所有的依赖包都可以通过 **`./contrib/download_prerequisites`** 一键完成下载。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fm6vKB8MMGgGNgdn0wvGcoiSL5EF.png)

## 3. 编译安装

为了避免在编译过程中，受原来系统自定义的一堆环境影响，建议先 **unset** 这些环境设置：

```shell
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE
```

参考：<https://stackoverflow.com/questions/12255058/g-4-7-1-compilation-error-conflicting-types-for-strsignal>

完整编译安装步骤如下：

```shell
$ mkdir gcc-build-4.8.5
$ cd gcc-build-4.8.5
$ unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE

$ ../configure -enable-checking=release -enable-languages=c,c++ -disable-multilib --prefix=/Bioinfo/SoftWare/gcc-4.8.5

# 如果想升级 gfortran，切记加上fortran！！！
$ ../configure -enable-checking=release -enable-languages=c,c++,fortran -disable-multilib --prefix=/Bioinfo/SoftWare/gcc-4.8.5

$ make
$ make install
.....
----------------------------------------------------------------------
Libraries have been installed in:
   /Bioinfo/SoftWare/gcc-4.8.5/lib/../lib64

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
......
```

**⚠️ 注意：**

- **如果想升级 gfortran，configure 时切记加上 fortran！！！**

如果需要重新 **configure** 或在 **make** 中途出错需要退出，最好把当前目录下的所有东西都删除干净。可以执行下面指令清空 编译目录下的相关文件，包括 makefile：

```shell
make distclean
```

## 4. 配置环境变量

GCC 安装完成后，需要包新安装的 gcc 添加到  `PATH`  个人相应的 **`LD_LIBRARY_PATH`**：

```shell
export PATH=/Bioinfo/SoftWare/gcc-4.8.5/bin:$PATH
export LD_LIBRARY_PATH=/Bioinfo/SoftWare/gcc-4.8.5/lib64:$LD_LIBRARY_PATH
```

如果不想把新装 GCC 添加到 **`~/.bashrc`** 中的 **`PATH`** 和 **`LD_LIBRARY_PATH`** 让它永久起作用，但是在安装软件时又想使用新安装的高级版本的 GCC 来编译软件，可以：

- 在软件编译前先执行上面两个  **export**  语句，再执行后面的编译安装命令；
- 或者在软件编译安装时直接在编译参数中添加 gcc/g++ 和其动态库的路径就可以。

到这里新版本的 GCC 就已经安装完了，在下一篇文章中我们将会跟大家分享一下怎么使用新版本的 GCC 在 Linux 下源码编译安装最新版本的 R-3.6.0。

## 5. 参考资料

1.  秋水逸冰，《[在 CentOS 下编译安装 GCC](https://teddysun.com/432.html)》，WorldPress 博客
2.  佚名，《[How can I understand these dreadful errors when building gcc-4.8.2?](https://stackoverflow.com/questions/21685255/how-can-i-understand-these-dreadful-errors-when-building-gcc-4-8-2)》，StackOverflow
3.  ljpwinxp，《[Centos 6.9 编译安装 gcc 4.8.5](http://blog.51cto.com/191226139/2066137)》，51CTO
4.  代码日志，《[c – 构建 gcc-4.8.2 时如何理解这些可怕的错误？](https://codeday.me/bug/20190121/548141.html)》, 博客
5.  Benjamin Berhault, 《[Build and Install the Last GCC on RHEL/CentOS 7](http://benjaminberhault.com//post/2018/06/22/install-gcc-on-rhel-centos-7.html)》，Ben's Jekyll Blog
