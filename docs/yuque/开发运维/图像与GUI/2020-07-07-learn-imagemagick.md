---
title: ImageMagick 图像处理安装与使用
urlname: 2020-07-07-learn-imagemagick
author: 章鱼猫先生
date: 2020-07-07
updated: 2024-09-10
---

什么是 ImageMagick，先来看一段官网的介绍。

> Use ImageMagick[®](http://tarr.uspto.gov/servlet/tarr?regser=serial&entry=78333969) to create, edit, compose, or convert bitmap images. It can read and write images in a variety of [formats](https://imagemagick.org/script/formats.php) (over 200) including PNG, JPEG, GIF, HEIC, TIFF, [DPX](https://imagemagick.org/script/motion-picture.php), [EXR](https://imagemagick.org/script/high-dynamic-range.php), WebP, Postscript, PDF, and SVG. Use ImageMagick to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves.

简单的来说，ImageMagick 就是：

- ImageMagick（简称 IM）是一个支持 GPL 协议的开源免费软件包。全部源码开放，可以自由使用，复制，修改，发布。
- 它由一组命令行工具组成的。
- 它可以对超过 200 种的图像格式（包括 DPX, EXR, GIF, JPEG, JPEG-2000, PDF, PhotoCD, PNG, Postscript, SVG, 和 TIFF 等等），进行读、写、编辑和转换的操作。
- 它支持多数主流操作系统，其中包括 UNIX、Mac OS X 、Windows，以及 IOS、Android 等。

相比 PhotoShop 和 GIMP 提供的图形用户接口 (GUI) 编辑图像，ImageMagick 通过一组命令行工具来操作图片，更有助于批量化的图片处理。你当然可以用 PhotoShop 或 GIMP 这样的软件来处理图像。没人禁止你这么做，就像没人禁止你用大炮打蚊子一样。不过依我看，打蚊子最好还是用电蚊拍，而要处理大量图像的话，尤其当你只想批量转换一些图片格式，或者批量生成缩略图，调整分辨率，我推荐 ImageMagick。

**支持的程序语言**：Perl, C, C++, Python, PHP, R 等。     

[**ImageMagick 接口**](https://imagemagick.org/script/develop.php)：[PerlMagick](https://imagemagick.org/script/develop.php#perl) (Perl), [IMagick](https://imagemagick.org/script/develop.php#php) (PHP), [PythonMagick](https://imagemagick.org/script/develop.php#python) (Python), [magick](https://imagemagick.org/script/develop.php#r) (R), 等。

## 1. 安装 ImageMagick

这里主要介绍一下 CentOS 7 下的 ImageMagick 安装，其他平台下的安装可以自行谷歌。

### 1.1 源码安装

如果你没有 root 权限，可以在 ImageMagick 安装过程中发现缺乏什么依赖，就手动去下载安装该依赖。过程可能很繁琐，环境配置起来可能也很复杂。

```bash
# 安装依赖
$ yum -y install bzip2-devel freetype-devel libjpeg-devel libpng-devel libtiff-devel giflib-devel zlib-devel ghostscript-devel djvulibre-devel libwmf-devel jasper-devel libtool-ltdl-devel libX11-devel libXext-devel libXt-devel lcms-devel libxml2-devel librsvg2-devel OpenEXR-devel php-devel

# 可以直接通过 github 下载最新版本
$ git clone https://github.com/ImageMagick/ImageMagick.git 

# 下载并安装制定版本 ImageMagick
$ wget https://download.imagemagick.org/archive/releases/ImageMagick-7.0.10-23.tar.xz
$ tar xvJf ImageMagick-7.0.10-23.tar.xz
$ cd ImageMagick-7.0.10-23
$ ./configure --prefix=/data/software/imagemagick-7.0.10-23
$ make
$ make install
```

### 1.2 conda 安装

没有 root 的权限，使用 `conda` 安装 ImageMagick 是最快捷有效的方式，推荐使用。

```bash
$ conda search imagemagick
$ conda create -n imagemagick imagemagick
```

## 2. 使用体验

ImageMagick 的使用网络上教程非常非常多，这里就不一一再重复了，需要的自己去百度或者谷歌。说几点使用过程中的小发现。

1. 从 ImageMagick 7 起，`magick` 命令替换了原来的 `convert` 命令，但 `convert` 命令依然可以使用。       
   ![imagemagick-7.0.10-23.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjVqFwYsqGwrbxwL3YgEK2z9C5wu.png)

2. ImageMagick 6.7.8-9 版本的 `convert` 命令存在一些 bug，例如本人在执行 PDF→TIFF 的转换过程经常会出现一些莫名其妙的报错；升级成 7.0.10-23 的 `magick` 后，恢复正常！
3. ImageMagick 中的 `convert`/`magick` 一个命令就包含了超过 200 多个子命令（参数），功能非常强悍，也让人眼花缭乱。
4. `convert`/`magick` 不同的参数排列顺序，有时候会得到截然不同的处理性能和效果，这是让人非常头疼的一个问题，有时候你都不知道这个参数到底是放在输入文件前，还是放在输入文件后！
5. 正常来说，一个图片当总像素大小保持不变，提高 dpi 会导致图片的物理尺寸变小。在 ImageMagick 中以 dpi 为变量，如何保证总像素大小不变前提下，自动转换图片格式，目前没找到更好的解决方法。
   ![ImageMagick-dpi](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkQpB1Ot1G8fM73zjHqNXB5uCUet.png)

## 3. 题外话

一般的杂志期刊对于投稿图片都是有要求的，如果想要得到发文级别分辨率和尺寸的图片，除了在画图时进行参数设置，或手动 PS 以外，或许还有一些可以自动完成这一系列操作的平台，或者 AI 神器吧！遗憾的是，目前我还没找到！
