---
title: LaTeX 安装教程
urlname: 2019-07-01-latex-2018-tutorial
author: 章鱼猫先生
date: 2019-07-01
updated: "2023-04-26 15:07:23"
---

## 一、背景

前两天在自己的 Jupyter 服务器上想要把 notebook(.ipynb) 导出为 pdf 时发现 xelatex 没有安装：

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp9hxWhI_H98Nn23qhXB_PF-t6FC.png)
500 : Internal Server Error 如下：
```bash
nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.
```

另外一点就是，对于经常做生信分析的童鞋而言，LaTeX，或者 Html+wkhtmltopdf 也许是当前生信报告生成与交付的两种主要解决方案（如果还有其他更好的，欢迎留言告诉我）。因此对于生信分析而言，LaTeX 也许并不陌生，但真正熟悉和掌握它的人却寥寥无几。

## 二、概念

TEX 是诞生于 20 世纪 70 年代末到 80 年代初的一款计算机排版软件，而且是命令行格式的，用来排版高质量的书籍，特别是包含有数学公式的书籍。TEX 以追求高质量为目标，很早就实现了矢量描述的计算机字体、细致的分页断行算法和数学排版功能，因其数学排版能力得到了学术界的广泛使用，也启发了后来复杂的商业计算机排版软件。

LATEX 开始于 20 世纪 80 年代初，是 Leslie Lamport 博士为了编写自己的一部书籍而设计的。LATEX 是对 TEX 的封装和拓展，实际上就是用 TEX 语言编写的一组宏代码，拥有比原来 TEX 格式（Plain TEX）更为规范的命令和一整套预定义的格式，隐藏了不少排版方面的细节，可以让完全不懂排版理论的学者们也可以比较容易地将书籍和文稿排版出来。

TEXLive 是 Tex 的一种比较流行的发行版，它是由 TUG（TEX User Group，TEX 用户组）发布的，可以在类 UNIX/Linux、Mac OS X 和 Windows 等不同的操作系统平台下安装使用，并且提供相当可靠的工作环境。

|  引擎  | (Knuth)TeX       | 真正的(原始的)TeX                                                                                                                                  |
| :----: | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|        | ε-TeX            | 相对于原始的 TeX 它提供了一种扩展模式                                                                                                              |
|        | pdfTeX           | 它从 tex 文件不通过 dvi 文件直接生成 pdf 文件（开发者已经转向 LuaTeX）                                                                             |
|        | **XeTeX**        | 相对于原始的 TeX，主要增加了 Unicode 和 OpenType 的支持                                                                                            |
|        | LuaTeX           | 它使用 Lua 作为扩展语言，对于 LaTeX 支持尚不完善？                                                                                                 |
|        | ......           | ......                                                                                                                                             |
|  宏集  | plain TeX        | 最古老的 TeX 宏集，提供了一些最基本的命令                                                                                                          |
|        | AMSTeX           | 是美国数学会提供的一个 TeX 宏集，它添加了许多数学符号和数学字体                                                                                    |
|        | **LaTeX**        | 相对于 PlainTeX，它使得科技文档的排版更加直观和方便                                                                                                |
|        | ConTeXt          | 和 LaTeX 相比，它更加灵活和自由。                                                                                                                  |
|        | ctex             | 小写的 ctex 是可以很好支持中文的宏包。                                                                                                             |
|        | ......           | ......                                                                                                                                             |
| 发行版 | **TeX Live**     | 国际 TeX 用户组织 TUG 开发，支持不同的操作系统。                                                                                                   |
|        | MiKTeX           | Windows 下广泛使用的一个 TeX 发行版。                                                                                                              |
|        | ConTeXt Minimals | 它包含了最新版本的 ConTeXt。                                                                                                                       |
|        | teTeX            | 一个 Unix 下的 TeX 发行版，现在已经停止更新且并入 TeXLive。                                                                                        |
|        | fpTeX            | 一个 Windows 的 TeX 发行版，已不再更新。                                                                                                           |
|        | CTeX             | [CTeX](http://www.ctex.org/CTeX)  是基于 Windows 下的  [MiKTeX](http://www.ctex.org/MiKTeX)  系统的一个中文套装（ctex 是可以很好支持中文的宏包）。 |
|        | ......           | ......                                                                                                                                             |

[CTeX](http://www.ctex.org/CTeX)  中文套装是基于 Windows 下的  [MiKTeX](http://www.ctex.org/MiKTeX)  系统，集成了编辑器  [WinEdt](http://www.ctex.org/WinEdt)  和  [PostScript](http://www.ctex.org/PostScript/edit)  处理软件 Ghostscript 和 GSview 等主要工具。 [CTeX](http://www.ctex.org/CTeX)  中文套装在  [MiKTeX](http://www.ctex.org/MiKTeX)  的基础上增加了对中文的完整支持。 [CTeX](http://www.ctex.org/CTeX)  中文套装支持 CJK, xeCJK, CCT, TY 等多种中文  [TeX](http://www.ctex.org/TeX)  处理方式。

## 三、安装

TEXLive 常用有两种安装方式：从 TEXLive 光盘进行安装和从网络在线安装。这里我们以 TexLive 2018 版本为例介绍第二种安装方法。

### 1. 镜像文件下载

TexLive 历史版本下载地址：<https://www.tug.org/historic/>。

TexLive 的镜像文件下载推荐使用 [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)，国内下载速度极快。

- 最新版本：<https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/>
- 历史版本：<https://mirrors.tuna.tsinghua.edu.cn/tex-historic-archive/systems/texlive/>

### 2. 镜像挂载

TEXLive 镜像文件下载完之后，推荐使用 root 用户进行安装。

```bash
$ sudo mkdir /mnt/textlive
$ sudo mount -o loop texlive2018.iso /mnt/textlive
mount: /dev/loop0 is write-protected, mounting read-only
```

注意：
使用 mount 挂载出现以上提示 `mount: /dev/loop0 is write-protected, mounting read-only`。这是因为 mount 命令默认以读写方式挂载一个设备，而光盘是只读的，所以在挂载光盘这个块设备时会出现上述从读写方式切换为以只读方式挂载光盘的提示。我们可以忽视不必管它。

如果不想看到这个提示，就请在 mount 命令后面添加参数,指定以只读方式来挂载设备。

```bash
$ sudo mount -o loop texlive2018.iso /mnt/textlive -o ro
```

### 3. 镜像安装

TEXLive 镜像的安装有两种方法：一是可以启动安装程序的图形化界面进行安装配置；二是直接在命令行中进行。这里主要介绍一下命令行下的安装。

```bash
$ cd /mnt/textlive
$ sudo ./install-tl
Loading ./tlpkg/texlive.tlpdb
Installing TeX Live 2018 from: . (verified)
Platform: x86_64-linux => 'GNU/Linux on x86_64'
Distribution: inst (compressed)
Directory for temporary files: /tmp/j3dA84tbet
======================> TeX Live installation procedure <=====================
======>   Letters/digits in  indicate   <=======
======>   menu items for actions or customizations      <=======
 Detected platform: GNU/Linux on x86_64
  set binary platforms: 1 out of 8
  set installation scheme: scheme-full
  set installation collections:
     40 collections out of 41, disk space required: 5381 MB
  set directories:
   TEXDIR (the main TeX directory):
     /usr/local/texlive/2018
   TEXMFLOCAL (directory for site-wide local files):
     /usr/local/texlive/texmf-local
   TEXMFSYSVAR (directory for variable and automatically generated data):
     /usr/local/texlive/2018/texmf-var
   TEXMFSYSCONFIG (directory for local config):
     /usr/local/texlive/2018/texmf-config
   TEXMFVAR (personal directory for variable and automatically generated data):
     ~/.texlive2018/texmf-var
   TEXMFCONFIG (personal directory for local config):
     ~/.texlive2018/texmf-config
   TEXMFHOME (directory for user-specific files):
     ~/texmf
  options:
   [ ] use letter size instead of A4 by default
   [X] allow execution of restricted list of programs via \write18
   [X] create all format files
   [X] install macro/font doc tree
   [X] install macro/font source tree
   [ ] create symlinks to standard directories
   [X] after install, use tlnet on CTAN for package updates
  set up for portable installation
Actions:
  start installation to hard disk
  save installation profile to 'texlive.profile' and exit
  help
  quit
Enter command: D
===============================================================================
Directories customization:
 <1> TEXDIR:       /usr/local/texlive/2018
     support tree: /usr/local/texlive/2018/texmf-dist
 <2> TEXMFLOCAL:     /usr/local/texlive/texmf-local
 <3> TEXMFSYSVAR:    /usr/local/texlive/2018/texmf-var
 <4> TEXMFSYSCONFIG: /usr/local/texlive/2018/texmf-config
 <5> TEXMFVAR:       ~/.texlive2018/texmf-var
 <6> TEXMFCONFIG:    ~/.texlive2018/texmf-config
 <7> TEXMFHOME:      ~/texmf
 Note: ~ will expand to $HOME (or to %USERPROFILE% on Windows)
Actions:
  return to main menu
  quit
Enter command: 1
New value for TEXDIR [/usr/local/texlive/2018]: /usr/local/software/texlive/2018
===============================================================================
Directories customization:
 <1> TEXDIR:       /usr/local/software/texlive/2018
     support tree: /usr/local/software/texlive/2018/texmf-dist
 <2> TEXMFLOCAL:     /usr/local/software/texlive/texmf-local
 <3> TEXMFSYSVAR:    /usr/local/software/texlive/2018/texmf-var
 <4> TEXMFSYSCONFIG: /usr/local/software/texlive/2018/texmf-config
 <5> TEXMFVAR:       ~/.texlive2018/texmf-var
 <6> TEXMFCONFIG:    ~/.texlive2018/texmf-config
 <7> TEXMFHOME:      ~/texmf
 Note: ~ will expand to $HOME (or to %USERPROFILE% on Windows)
Actions:
  return to main menu
  quit
Enter command: R
......
Actions:
  start installation to hard disk

 save installation profile to 'texlive.profile' and exit
  help
  quit
Enter command: I
Installing to: /usr/local/software/texlive/2018
Installing [0001/3590, time/total: ??:??/??:??]: 12many [376k]
Installing [0002/3590, time/total: 00:00/00:00]: 2up [66k]
Installing [0003/3590, time/total: 00:00/00:00]: Asana-Math [482k]
Installing [0004/3590, time/total: 00:00/00:00]: ESIEEcv [137k]
Installing [0005/3590, time/total: 00:00/00:00]: FAQ-en [4971k]
......
finished with package-specific postactions
Welcome to TeX Live!
......
```

**FAQ-1：Digest::MD5**

```bash
Can't locate Digest/MD5.pm in @INC (@INC contains: ./tlpkg /usr/local/lib64/perl5 /usr/local/share/perl5 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5 .) at tlpkg/TeXLive/TLCrypto.pm line 9.
BEGIN failed--compilation aborted at tlpkg/TeXLive/TLCrypto.pm line 9.
Compilation failed in require at tlpkg/TeXLive/TLPOBJ.pm line 16.
BEGIN failed--compilation aborted at tlpkg/TeXLive/TLPOBJ.pm line 16.
Compilation failed in require at ./install-tl line 55.
BEGIN failed--compilation aborted at ./install-tl line 55.
```

`Can't locate Digest/MD5.pm`  是因为系统的 perl(`/usr/bin/perl`) 中没有安装 `Digest::MD5`  模块，我们可以去 [CPAN](https://metacpan.org/pod/Digest::MD5)  下载手动安装，也可以在线安装：

```bash
$ sudo yum install perl-Digest-MD5
```

**FAQ-2：perl-TK**

```bash
Error message from loading Tk:
  Can't locate Tk.pm in @INC (@INC contains: ./tlpkg /usr/local/lib64/perl5 /usr/local/share/perl5 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5 .) at ./install-tl line 398.
```

在线安装 Tk 的 perl 模块(通过 [CPAN](https://metacpan.org/pod/distribution/Tk/Tk.pod)手动安装，这里不详述，有兴趣的可自行谷歌一下)：
```bash
$ sudo yum install perl-Tk
$ perl -e "use Tk"   # 测试 TK 是否安装成功
```

最后，卸载镜像：

```bash
$ sudo umount /mnt/textlive/
umount: /mnt/textlive: target is busy.
        (In some cases useful info about processes that use
         the device is found by lsof(8) or fuser(1))
# fuser/lsof 能识别出正在对某个文件或端口访问的进程
$ sudo fuser -m /mnt/textlive/
/mnt/textlive:        6436c  6548c  6549c
$ ps aux|grep 6436
shenwei+  6436  0.0  0.0 115568  2220 pts/3    Ss   10:36   0:00 -bash
shenwei+ 18041  0.0  0.0 112704   952 pts/1    S+   11:11   0:00 grep --color 6436
$ ps aux|grep 6548
root      6548  0.0  0.1 218528  4020 pts/3    S+   10:37   0:00 sudo ./install-tl
shenwei+ 18062  0.0  0.0 112704   952 pts/1    S+   11:11   0:00 grep --color 6548
# 杀掉占用此设备的进程
$ sudo fuser -m -v -k /mnt/textlive/
# 执行 umount 就可以正常卸载
$ sudo umount /mnt/textlive/
```

这里有一个更加详细的[TEX Live 指南](https://www.tug.org/texlive/doc/texlive-zh-cn/texlive-zh-cn.pdf)，其中也有详细介绍各平台各种安装方法。

## 四、设置环境变量

将 texlive 部分目录添加到环境变量(\~/.bashrc)，编辑完记得 source 刷新一下：

```bash
export PATH=/usr/local/software/texlive/2018/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/software/texlive/2018/texmf-dist/doc/man:$MANPATH
export INFOPATH=/usr/local/software/texlive/2018/texmf-dist/doc/info:$INFOPATH
```

## 五、使用与测试

编辑一个 tex-test.tex 文件：

```katex
\documentclass{article}
\begin{document}
Hello \LaTeX! 你好，这是一个测试文档。
\end{document}
```

使用命令，最后打开生成的 tex-test.pdf 文件：
```bash
xelatex tex-test.tex
```

## 六、中文支持

LaTeX 默认是不支持中文的，想要支持中文排版，这里需要引入一个"宏包" 的概念。关于宏包，我们可以理解为一些指令的集合，用于专门处理某个特定的专题（如排版，字体等方面的细节问题），使用者可以方便地根据需要选用某个宏包。

LaTeX 中比较常用的中文排版处理宏包主要有 ctex、CJK、xeCJK 等等，这里主要介绍一下后面两个。CJK 是由 Werner Lemberg 开发的，是中文（Chinese）、日文（Japanese）、韩文（Korean）三国文字的缩写。顾名思义，它能够支持这三种文字。实际上，CJK 能够支持在 LaTeX 中使用包括中文、日文、韩文在内的多种亚洲双字节文字。

CJK 宏包提供了两种环境：CJK 环境和 CJK\* 环境，这两种环境的区别为：对于汉字后面的空格，前者不忽略，后者忽略，我们推荐使用 CJK\* 环境。

xeCJK 是在 CCT 和 CJK 包基础上发展起来的，支持多种标点格式。也有人说，xeCJK package 搭上 XeLaTeX 是最好的中文 TeX 处理方式。总的来说 xeCJK 主要特点：

1. 分别设置 CJK 和英文字体；
2. 自动忽略 CJK 文字间的空格而保留其它空格，允许在非标点汉字和英文字母 (a-z, A-Z) 间断行；
3. 提供多种标点处理方式：全角式、半角式、开明式、行末半角式；
4. 自动调整中英文间空白。
5. TexLive 2018 已经默认安装了 xeCJK，我们可以使用下面的命令查看 TexLive 已经安装的包以及包的具体信息：

```bash
# 查看 TexLive 所有已经安装的包
$ tlmgr list --only-installed
# 查看具体某个包的信息
$ tlmgr info xecjk
# 安装新的宏包
$ tlmgr install pkgname
```

结合 xeCJK 宏包来配置字体，下面是一个小例子：
```katex
\documentclass{article}
\usepackage{xeCJK}
\setCJKmainfont{SimSun}
\begin{document}
你好，TeX Live 2018！
\end{document}
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrniQGthPg4PVIqBj2AHm_GWJUk_.png)


## 七、参考资料

- CTAN，[xecjk – Support for CJK documents in XeLaTeX](https://ctan.org/pkg/xecjk)
- Tass，Regular Tass Office Hour，《[CJK, xeCJK 與 cwTeX 對於中文支援的比較](http://rtassoh.blogspot.com/2010/08/cjk-xecjk-cwtex.html)》
- [CTEX.ORG](http://CTEX.ORG)，《[xeCJK 宏包（中文文档）](http://mirrors.sjtug.sjtu.edu.cn/ctan/macros/xetex/latex/xecjk/xeCJK.pdf)》
- CTAN，[xecjk – Support for CJK documents in XELATEX](https://ctan.org/pkg/xecjk)
- Jiedong Hao，jdhao blog，[LaTeX 中如何使用中文](https://jdhao.github.io/2018/03/29/latex-chinese.zh/)
