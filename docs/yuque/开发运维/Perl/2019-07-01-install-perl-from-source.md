---
title: 各个平台下 Perl 源码安装教程
urlname: 2019-07-01-install-perl-from-source
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 10:42:16"
---

!![How-To-Install-Perl.jpeg](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpxbOJPB_b-KaVp9LYgc4uRgF1a0.jpeg)
Perl 是一种功能丰富的计算机程序语言，运行在超过 100 种计算机平台上，适用广泛，从大型机到便携设备，从快速原型创建到大规模可扩展开发。在生物信息分析领域，Perl 主要是做数据预处理、文本处理和格式转换、对算法效率要求不高的分析软件开发，系统管理和 pipeline 搭建等工作。这里对 Linux（主要是 CentOS）、windows 下 Perl 的安装做一个备忘。

# 一、CentOS 7 下安装 Perl

## 1. 源码包下载

在官方网站下载新版本的源码包：<http://www.perl.org/get.html>，我下载的是 [perl-5.26.1.tar.gz](http://www.cpan.org/src/5.0/perl-5.26.1.tar.gz)。

## 2. 解压，设置源码

```bash
$ tar zvxf perl-5.26.1.tar.gz
$ cd perl-5.26.1
$ ./Configure --help
Usage: Configure [-dehrsEKOSV] [-f config.sh] [-D symbol] [-D symbol=value]
                 [-U symbol] [-U symbol=] [-A command:symbol...]
  -d : use defaults for all answers.
  -e : go on without questioning past the production of config.sh.
  -f : specify an alternate default configuration file.
  -h : print this help message and exit (with an error status).
  -r : reuse C symbols value if possible (skips costly nm extraction).
  -s : silent mode, only echoes questions and essential information.
  -D : define symbol to have some value:
         -D symbol         symbol gets the value 'define'
         -D symbol=value   symbol gets the value 'value'
       common used examples (see INSTALL for more info):
         -Duse64bitint            use 64bit integers
         -Duse64bitall            use 64bit integers and pointers
         -Dusethreads             use thread support
         -Dinc_version_list=none  do not include older perl trees in @INC
         -DEBUGGING=none          DEBUGGING options
         -Dcc=gcc                 choose your compiler
         -Dprefix=/opt/perl5      choose your destination
  -E : stop at the end of questions, after having produced config.sh.
  -K : do not use unless you know what you are doing.
  -O : ignored for backward compatibility
  -S : perform variable substitutions on all .SH files (can mix with -f)
  -U : undefine symbol:
         -U symbol    symbol gets the value 'undef'
         -U symbol=   symbol gets completely empty
       e.g.:  -Uversiononly
  -A : manipulate symbol after the platform specific hints have been applied:
         -A append:symbol=value   append value to symbol
         -A symbol=value          like append:, but with a separating space
         -A define:symbol=value   define symbol to have value
         -A clear:symbol          define symbol to be ''
         -A define:symbol         define symbol to be 'define'
         -A eval:symbol=value     define symbol to be eval of value
         -A prepend:symbol=value  prepend value to symbol
         -A undef:symbol          define symbol to be 'undef'
         -A undef:symbol=         define symbol to be ''
       e.g.:  -A prepend:libswanted='cl pthread '
              -A ccflags=-DSOME_MACRO
  -V : print version number and exit (with a zero status).

# 设置源码
$ ./Configure -des -Dprefix=/usr/local/software/Perl-5.26 -Dusethreads -Uversiononly
```

## 3. 编译安装

```bash
$ make
......
make[1]: *** [IO.o] Error 1
make[1]: Leaving directory `/users/rmi1/build/perl-5.12.0/dist/IO'
Unsuccessful make(dist/IO): code=512 at make_ext.pl line 449.
make: *** [lib/auto/IO/IO.so] Error 2
```

如果在 make 编译过程中出现如上报错，请参考 [Make error when compiling Perl 5.12.1 (RHEL 5.5)](https://serverfault.com/questions/145288/make-error-when-compiling-perl-5-12-1-rhel-5-5) 执行下面操作：

```bash
$ make clean
$ unset C_INCLUDE_PATH
$ ./Configure -des -Dprefix=/usr/local/software/Perl-5.26 -Dusethreads -Uversiononly
$ make
```

继续验证编译，执行安装：

```bash
$ make test
$ make install   # 命令完成后，基本安装就完成了
```

## 4. 调整环境变量

在 \~/.bashrc 中把 perl 添加到 PATH 中，然后 source \~/.bashrc 刷新。

```bash
export PATH="/usr/local/software/Perl-5.26/bin:$PATH"
```

## 5. 安装完成

```bash
$ perl -version

This is perl 5, version 26, subversion 1 (v5.26.1) built for x86_64-linux-thread

Copyright 1987-2017, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
```

查看 perl 配置汇总信息：

```bash
$ perl -V    # 该命令会把对应 perl 配置、模块路径所有信息汇总打印出来
Summary of my perl5 (revision 5 version 26 subversion 0) configuration:

  Platform:
    osname=linux
    osvers=2.6.32-696.10.1.el6.x86_64
......

Built under linux
  Compiled at Sep 17 2017 16:35:49
  @INC:
    /usr/local/software/Perl-5.26/lib/perl5/site_perl/5.26.1/x86_64-linux
    /usr/local/software/Perl-5.26/lib/perl5/site_perl/5.26.1
    /usr/local/software/Perl-5.26/lib/perl5/5.26.1/x86_64-linux
    /usr/local/software/Perl-5.26/lib/perl5/5.26.1
```

# 二、Windows 7 下安装 Perl

windows 下的 Perl 安装推荐使用 ActivePerl（<https://www.activestate.com/products/activeperl/>），安装步骤如下。

## 2.1 安装包下载

在这里我们下载 64-bit 的 [Perl-5.26.3](https://www.activestate.com/products/activeperl/downloads/thank-you/?dl=https://downloads.activestate.com/ActivePerl/releases/5.26.3.2603/ActivePerl-5.26.3.2603-MSWin32-x64-a95bce075.exe)。

## 2.2 安装与设置

ActivePerl-5.26.3.2603-MSWin32-x64-a95bce075.exe 安装包下载完后，我们直接点击进行安装。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FltQ3ily8fUf7jsc8lkAaa1S6j2C.png)

选择 "Custom" 自定义安装：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjxzUF9spJfd0_xw1Gj1ebX64IC6.png)

自定义安装路径：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlguUA_zw4HQ8RezvB8nGElAjhdt.png)

把 Perl 添加到系统环境变量：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlrvxARXJt3KCsxePwpEpKe6ZEJM.png)

Perl 安装完成后，我们在 DOC 命令行输入 perl -V，可以看到详细的相关信息：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtVmx_MsNHaXijdtfSGVjZM3irE3.png)

如果我们在安装过程中没有勾选把 Perl 添加到系统环境变量，DOC 中直接执行 perl -V 会出现 **"'perl' is not recognized as an internal or external command"** 提示，这时候我们需要手动把 perl 添加到 Windows 的系统环境变量中就可以了。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FozuAmdNUImdIzTJhZmE2SIVFA6o.png)

## 2.3 配置 cpan

为了更好对 Perl 进行扩展，方便以后的模块安装，我们最好配置一下 cpan。ActivePerl 有个好处就是在初始化 cpan 的时候会自动把 dmake、gcc、g++、mingw32-make 等 windows 常用的编译工具一起安装到 "**$Dprefix/site/bin**" 目录下，免去了我们手动安装这些编译器的各种麻烦。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk2vzpGMiygw3YHFIf3vV7_hj-5-.png)

## 2.4 安装完成

到这里，windows 下的 ActivePerl（perl-5.26）就安装完成了！
