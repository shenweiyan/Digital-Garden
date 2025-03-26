---
title: GCC 版本不一致导致的 R magick 包安装错误
number: 87
slug: discussions-87/
url: https://github.com/shenweiyan/Digital-Garden/discussions/87
date: 2024-09-10
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.6-R']
---

在安装 Y 叔的 `yyplot` 时候，发现 `magick` 依赖包安装的时候的一些棘手问题，特此记录一下。

<!-- more -->

## R-4.0.3 安装

```r
> library(remotes)
> remotes::install_github("GuangchuangYu/yyplot")
...
* installing *source* package ‘magick’ ...
** package ‘magick’ successfully unpacked and MD5 sums checked
** using staged installation
Package Magick++ was not found in the pkg-config search path.
Perhaps you should add the directory containing `Magick++.pc'
to the PKG_CONFIG_PATH environment variable
No package 'Magick++' found
Using PKG_CFLAGS=
Using PKG_LIBS=-lMagick++-6.Q16 -lMagickWand-6.Q16 -lMagickCore-6.Q16
--------------------------- [ANTICONF] --------------------------------
Configuration failed to find the Magick++ library. Try installing:
 - deb: libmagick++-dev (Debian, Ubuntu)
 - rpm: ImageMagick-c++-devel (Fedora, CentOS, RHEL)
 - brew: imagemagick or imagemagick@6 (MacOS)
If Magick++ is already installed, check that 'pkg-config' is in your
PATH and PKG_CONFIG_PATH contains a Magick++.pc file. If pkg-config
is unavailable you can set INCLUDE_DIR and LIB_DIR manually via:
R CMD INSTALL --configure-vars='INCLUDE_DIR=... LIB_DIR=...'
-------------------------- [ERROR MESSAGE] ---------------------------
<stdin>:1:22: fatal error: Magick++.h: No such file or directory
compilation terminated.
--------------------------------------------------------------------
ERROR: configuration failed for package ‘magick’
* removing ‘/home/shenweiyan/software/R/R-4.0.3/lib64/R/library/magick’
Error: Failed to install 'yyplot' from GitHub:
  (converted from warning) installation of package ‘magick’ had non-zero exit status
> quit()
Save workspace image? [y/n/c]: n
```

仅在 Bash 环境配置了 `PATH` 和 `PKG_CONFIG_PATH` 是不够的，安装过程会提示动态库的问题。    
```
# export PATH=/home/shenweiyan/software/ImageMagick-7.0.10/bin:$PATH
# export PKG_CONFIG_PATH=/home/shenweiyan/software/ImageMagick-7.0.10/lib/pkgconfig:$PKG_CONFIG_PATH
```

```r
> library(remotes)
> remotes::install_github("GuangchuangYu/yyplot")
...
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
Error: package or namespace load failed for ‘magick’ in dyn.load(file, DLLpath = DLLpath, ...):
 unable to load shared object '/home/shenweiyan/software/R/R-4.0.3/lib64/R/library/00LOCK-magick/00new/magick/libs/magick.so':
  libMagick++-7.Q16HDRI.so.4: cannot open shared object file: No such file or directory
Error: loading failed
Execution halted
ERROR: loading failed
* removing ‘/home/shenweiyan/software/R/R-4.0.3/lib64/R/library/magick’
Error: Failed to install 'yyplot' from GitHub:
  (converted from warning) installation of package ‘magick’ had non-zero exit status
> quit()
Save workspace image? [y/n/c]: n
```
最终解决方案：

1. 手动安装 `ggimage_0.3.1`。
```r
pkg <- 'http://cran.r-project.org/src/contrib/Archive/ggimage/ggimage_0.3.1.tar.gz'
install.packages(pkg, repos=NULL, type="source")
```

2. 配置必要环境。
```bash
export PATH=/home/shenweiyan/software/ImageMagick-7.0.10/bin:$PATH
export PKG_CONFIG_PATH=/home/shenweiyan/software/ImageMagick-7.0.10/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=/home/shenweiyan/software/ImageMagick-7.0.10/lib:$LD_LIBRARY_PATH
```

3. 安装。根据提示，先安装缺失的 `meme` 包，然后再安装 `yyplot`。
```r
> library(remotes)
> options("repos"=c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
> install.packages('meme')
> remotes::install_github("GuangchuangYu/yyplot")
```

## R-4.3.0 安装

R-4.3.0 安装 `magick_2.8.4` 会出现 [ropensci/magick#166](https://github.com/ropensci/magick/issues/166) 的问题。根据 [ropensci/magick#166#issuecomment-457875591](https://github.com/ropensci/magick/issues/166#issuecomment-457875591) 的描述，**编译 ImageMagick 的 gcc 需要跟编译 R 的 gcc 保持版本一致**。

1. 重新编译安装 ImageMagick
```bash
wget https://download.imagemagick.org/archive/releases/ImageMagick-7.0.10-24.tar.xz
extract ImageMagick-7.0.10-24.tar.xz
cd ImageMagick-7.0.10-24
./configure CC=/home/shenweiyan/software/gcc-7.3.0/bin/gcc CXX=/home/shenweiyan/software/gcc-7.3.0/bin/g++ --prefix=/home/shenweiyan/software/ImageMagick-7.0.10-24
make 
make install
```

2. 安装 `magick` 包
```bash
# export PATH=/home/shenweiyan/software/ImageMagick-7.0.10-24/bin:$PATH
# export PKG_CONFIG_PATH=/home/shenweiyan/software/ImageMagick-7.0.10-24/lib/pkgconfig:$PKG_CONFIG_PATH
# export LD_LIBRARY_PATH=/home/shenweiyan/software/ImageMagick-7.0.10-24/lib:$LD_LIBRARY_PATH
/home/shenweiyan/software/R/R-4.3.0/bin/R
> options("repos"=c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
> install.packages('magick')
...
```

3. 根据提示，先安装缺失的 `meme` 包，然后再安装 `yyplot`。
```r
> library(remotes)
> options("repos"=c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
> install.packages('meme')
> remotes::install_github("GuangchuangYu/yyplot")
```

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="87"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
