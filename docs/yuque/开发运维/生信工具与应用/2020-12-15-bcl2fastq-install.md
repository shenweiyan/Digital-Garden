---
title: 测序数据学习笔记：bcl2fastq 安装
urlname: 2020-12-15-bcl2fastq-install
author: 章鱼猫先生
date: 2020-12-15
updated: "2021-11-24 09:20:00"
---

相比二进制的 bcl2fastq2，基于 Perl 语言的 bcl2fastq-1.8.4 或许是从源码层面学习了解 Illumina 测序数据处理一个不错的选择。源码版本的 bcl2fastq-1.8.4.tar.bz2 目前没能安装成功，这是基于 bcl2fastq-1.8.4-Linux-x86_64.rpm 的一些折腾记录。

## 安装前准备

- 操作系统：CentOS Linux release 7.8.2003
- GCC 版本：gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-39)

安装前需要解决的依赖：

```bash
yum install -y doxygen texlive texlive-latex readline-devel gd-devel lua-devel cairo-devel pango-devel wxGTK-devel libcaca-devel svgalib-devel
```

参考 Illumina 官方提供的 [bcl2fastq Conversion User Guide](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq_letterbooklet_15038058brpmi.pdf) 文档 Appendix: Requirements and Software Installation on page 26 部分的内容，安装以下依赖：

```bash
libxslt libxslt-devel libxml2 libxml2-devel bzip2 bzip2-devel bzip2-devel-zlib zlib zlib-devel
```

> bcl2fastq has been primarily developed and tested on CentOs 5, Illumina's recommended
> and supported platform. It may be possible to install and run bcl2fastq on other 64-bit
> Linux distributions (particularly on similar distributions such as RedHat and Fedora) or
> on other Unix variants, if all of the prerequisites described in this section are met.
> The following software is required to run bcl2fastq; check whether it has been installed:
>
> - GNU make (3.81 recommended)
> - Perl (>= 5.8)
> - libxslt
> - libxslt-devel
> - libxml2
> - libxml2-devel
> - gcc (4.0.0 or newer, except 4.0.2), with c++
> - ImageMagick
> - bzip2
> - bzip2-devel
> - zlib
> - zlib-devel

## 安装过程异常解决

安装过程中出现的异常：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiQYnYkHfXBaGGN90hjP30zICxk_.png)

### ImageMagick 的坑

服务器本来就通过源码的方式安装了 ImageMagick 7.0.10-23，但是不管是命令行还是在 **\~/.bashrc** 中设置 **PATH** 环境变量，bcl2fastq 的 rpm 就是无法识别。

```bash
# 命令行还是在 ~/.bashrc 中设置 PATH, bcl2fastq 的 rpm 就是无法识别
export PATH=/data/software/imagemagick-7.0.10-23/bin:$PATH
```

最后的解决方法：

```bash
yum install ImageMagick
```

### gnuplot 的坑

源码的方式安装 **gunplot** 比较繁琐，懒得去折腾，使用 **yum** 的方式安装。

```bash
yum install gnuplot
```

### boost 的坑

考虑最简单的安装方式：

```bash
yum install cmake boost boost-thread boost-thread-devel boost-devel
```

现问题还是没解决，最终通过 Bing 找到了正确的答案，还要继续安装：

```bash
yum install gcc-c++.x86_64 gperf
```

### Qt5 的坑

源码安装 bcl2fastq-1.8.4.tar.bz2，configure 时遇到 Qt 的一系列错误。

```shell
Package requirements (Qt5Core Qt5Gui Qt5Network Qt5Svg Qt5PrintSupport) were not met...
```

使用 **yum** 的方式安装 Qt 相关依赖：

```bash
yum install -y qt qt-devel qt5-qtbase qt5-qtbase-devel qt5-qtsvg qt5-qtsvg-devel
```

## 安装成功

![install-bcl2fastq.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmC-y6Fl8u_twEHPo8Kkryiz9v4i.png)

## 后话

RTA（Real Time Analysis），是指 Illumina 测序在边合成边测序化学过程中，仪器上的实时分析（RTA）软件对每个簇的每个循环进行碱基检出和存储。RTA 以单个读取碱基（base call，或称 BCL）文件的形式存储碱基检出数据。测序完成后，必须将 BCL 文件中的测定的碱基转换为序列数据。 此过程称为 BCL 到 FASTQ 的转换。
![seq-1.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Frx1EUlw3zRBY6aY-k_Q7HEJp4db.png)
![seq-2.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fr8gllX_Vof1EuVgnZtjUn-2u2Rg.png)

> **The bcl2fastq2 Conversion Software v2.18 can be used to convert BCL files from MiniSeq, MiSeq, NextSeq, and HiSeq sequening systems. For conversion of data generated on Illumina sequencing systems using versions of RTA earlier than RTA 1.18.54, use bcl2fastq v1.8.4.**

如果你的 RTA 版本大于 1.18.54，可以考虑安装 bcl2fastq2，我在这里安装了 bcl2fastq v1.8.4 主要是想从源码层面对 Illumina 测序数据的转化作进一步了解学习。

从信号处理到 basecalling 每一步都是一个大工程，路漫漫其修远兮，还需要继续努力搬砖！
