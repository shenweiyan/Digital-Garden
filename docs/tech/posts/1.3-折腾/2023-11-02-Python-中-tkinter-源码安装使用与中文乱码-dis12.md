---
title: Python 中 tkinter 源码安装使用与中文乱码
number: 12
slug: discussions-12/
url: https://github.com/shenweiyan/Digital-Garden/discussions/12
date: 2023-11-02
authors: 
  - shenweiyan
categories: 
  - 折腾
tags: ['1.3.5-Python']
---

主要是因为下面这两个原因，所以决定从源码编译安装去折腾一下 tkinter，以下是一些记录。

## _tkinter not found

Python 3 源码编译安装，执行 `make` 过程中提示 `_tkinter not found`，如下：
```bash
$ make
......
Python build finished successfully!
The necessary bits to build these optional modules were not found:
_tkinter 
```

<!-- more -->

## 中文乱码

使用 Anaconda 3（conda 4.5.11）的 tkinter python 包（conda install -c conda-forge tk）开发 GUI 界面程序过程中，发现 UI 界面出现的中文 Unicode 乱码一直没办法解决。

```python
#-*- coding: utf-8 -*-

import sys

from tkinter import *
top=Tk()
top.wm_title("菜单")
top.geometry("800x600+300+100") # 创建一个菜单项，类似于导航栏
menubar=Menu(top) # 创建菜单项
fmenu1=Menu(top)
# 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单
for item in ['新建文件', '打开文件','结果保存']:
    fmenu1.add_command(label=item)

fmenu2=Menu(top)
for item in ['程序设置','程序运行']:
    fmenu2.add_command(label=item)

fmenu3=Menu(top)
for item in ['使用教程', '版权信息', '检查更新']:
    fmenu3.add_command(label=item)

# add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上
# 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label='文件', menu=fmenu1)
menubar.add_cascade(label="程序", menu=fmenu2)
menubar.add_cascade(label="帮助", menu=fmenu3)

# 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
top['menu']=menubar
top.mainloop()
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fh22i487OzvY-uSXvAuFs6rEXXvu.png)

我们也可以确认一下是不是 Tk 本身的问题：
```
echo 'pack [button .h -text "Hello, World! 显示中文" -command exit]' | wish
```
- 正常显示
  ![TK 正常显示](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/KGarden/2023/tk-ok.png)

- 中文乱码
  ![TK 中文乱码](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/KGarden/2023/tk-error.png)

**一些参考资料：**

- Python 3.x 中文编码转换的问题：<https://bbs.bccn.net/thread-479560-1-1.html>
- Python 2.6 Tk 中文乱码解決方法：<http://blogkrogh.blogspot.com/2011/03/python-26-tk.html>
- tkinter 乱码，pyqt4 乱码：<http://aboutweb.lofter.com/post/11743e_6f7e4a5>

上面几种方法测试后，问题依然存在。在 google 上一番搜索和来回测试之后，发现了几点信息：

- 有人说，可能是 tcl/tk 安装不完整造成的。
- tcl/tk 重装后需要对 Python 重新编译 tkinter 才能起作用。
- conda install -c conda-forge tk，虽然没有任何报错，python2 中 import tkinter 也正常，但 conda 的软件安装就像一个黑盒子，无法确认 tcl/tk 是否完整安装。
- python 的 PyPI 仓库中是没有 tkinter 包的，想要使用 `pip install tkinter` 卸载或者重装都是行不通的。
- 网上也有人说可以使用 `yum install python3-tk/python-tk` 解决，但对于本人来说，没用。

## 什么是 tcl, tk, tkinter

> The [tkinter](https://docs.python.org/3.6/library/tkinter.html#module-tkinter) package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and [tkinter](https://docs.python.org/3.6/library/tkinter.html#module-tkinter) are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)
>
> Running `python -m tkinter` from the command line should open a window demonstrating a simple Tk interface, letting you know that [tkinter](https://docs.python.org/3.6/library/tkinter.html#module-tkinter) is properly installed on your system, and also showing what version of Tcl/Tk is installed, so you can read the Tcl/Tk documentation specific to that version.
>
> From <https://docs.python.org/3/library/tkinter.html>

Tcl 是"工具控制语言（Tool Control Language）"的缩写。Tk 是 Tcl "图形工具箱" 的扩展，它提供各种标准的 GUI 接口项，以利于迅速进行高级应用程序开发。

tkinter 包（"Tk 接口"）是 Tk GUI 工具包的标准 Python 接口。 Tk 和  tkinter 在大多数 Unix 平台以及 Windows 系统上都可用（Tk 本身不是 Python 的一部分，它在 ActiveState 中维护）。您可以通过从命令行运行  `python -m tkinter`来检查  tkinter 是否已正确安装在系统上。如果已经安装该命令会打开一个简单的 Tk 界面，该界面除了让我们知道 tkinter 已正确安装，并且还显示安装了哪个版本的 Tcl/Tk，因此我们可以阅读特定于该版本的 Tcl/Tk 文档。

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpWx6rSTKaQ1BXXPQJzchNbviKYd.png)

如果  tkinter  没有安装，则会提示找不到该包（注意在 Python 2 中该包包名为 Tkinter，Python 3 中为 tkinter）：

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrRwzLFA1tIq2VfwS4p7i0dVLTjP.png)

接下来我们将尝试在 Python 2/3 中安装 Tcl/Tk，并重新编译 Python 2/3，已完成 Tkinter 安装（tkinter 为 Python 的标准库，标准库的安装需要重新编译 Python ？）。

## ActiveTcl 安装

ActiveTcl 是 ActiveState 发布的关于 Tcl/Tk 的发行版本，该发行版本包含了最新版本的 Tk 和 Tcl 程序，我们下载其免费的社区版本进行安装即可。

参考下载链接：<https://www.activestate.com/products/activetcl/downloads/>
参考安装教程：<https://tkdocs.com/tutorial/install.html>

以下为 CentOS 6.5 下 **ActiveTcl-8.6.9** 的一些安装记录，仅作参考。

```bash
$ curl -fL "https://shenweiyan-generic.pkg.coding.net/btscl/activetcl/ActiveTcl-8.6.9.8609.2-x86_64-linux-glibc-2.5-dcd3ff05d.tar.gz?version=8.6.9.8609.2" -o ActiveTcl-8.6.9.8609.2-x86_64-linux-glibc-2.5-dcd3ff05d.tar.gz
$ tar zvxf ActiveTcl-8.6.9.8609.2-x86_64-linux-glibc-2.5-dcd3ff05d.tar.gz
$ cd ActiveTcl-8.6.9.8609.2-x86_64-linux-glibc-2.5-dcd3ff05d
$ ./install.sh
......
Cancel         [no]  => [RET]
Accept License [yes] => 'A' >>A

Please specify the installation directory.
Path [/opt/ActiveTcl-8.6]: /home/shenweiyan/software/ActiveTcl-8.6.9

Please specify the directory for the demos.
Path [/home/shenweiyan/software/ActiveTcl-8.6.9/demos]:

Please specify the runtime installation directory.

This is the directory the applications will see as their installation directory
when searching for packages and libraries, instead of the directory the files
were copied to. In most circumstances this is the same as the installation
directory chosen before.
Path [/home/shenweiyan/software/ActiveTcl-8.6.9]:

Press return to begin installation
     Installation Directory:  /home/shenweiyan/software/ActiveTcl-8.6.9
     Demos Directory:         /home/shenweiyan/software/ActiveTcl-8.6.9/demos
     Runtime Directory:       See Installation Directory
Cancel => C
Next   => [RET] >>

Installing ActiveTcl ...
        Creating directory /home/shenweiyan/software/ActiveTcl-8.6.9/share ...
        Creating directory /home/shenweiyan/software/ActiveTcl-8.6.9/share/man ...
        ......

Please do not forget to extend your PATH and MANPATH variables to
get access to the applications and manpages distributed with ActiveTcl.

For a csh or compatible perform
    setenv PATH "/home/shenweiyan/software/ActiveTcl-8.6.9/bin:$PATH"

For a sh or similar perform
    PATH="/home/shenweiyan/software/ActiveTcl-8.6.9/bin:$PATH"
    export PATH

Some shells (bash for example) allow
    export PATH="/home/shenweiyan/software/ActiveTcl-8.6.9/bin:$PATH"

Similar changes are required for MANPATH
Finish >>
```

ActiveTcl 安装完成后，需要把 path 添加至环境变量（\~/.bashrc）:
```
export PATH="/home/shenweiyan/software/ActiveTcl-8.6.9/bin:$PATH"
```

## Tcl/Tk

我们也可以直接去 <https://sourceforge.net/projects/tcl/files/Tcl/> 直接通过源码的方式去编译安装 Tcl/Tk，尤其是当你的系统版本比较低，需要低版本的 Tcl/Tk，这种方法会比较合适。

以 tcl8.5.19-src.tar.gz/tk8.5.19-src.tar.gz 为例，下载完成后，直接解压，然后执行常规安装即可。
```
cd tcl8.5.19/unix
./configure
make
make test
make install
```

## Python 重新编译安装

参考：[What’s New In Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) - doc.python.org

> 📢 **注意：**
>
> 1. Python 3.11.x 起（如 Python-3.11.3）中的 `configure` 已经把 `--with-tcltk-includes`和`--with-tcltk-libs`这两个参数移除！并使用 `TCLTK_CFLAGS` 和 `TCLTK_LIBS` 替代！！！
> 2. Python 3.10.x (及以下版本，如 Python-3.9.16) 以及 Python 2.x.x 在 `configure` 中 `--with-tcltk-includes`和`--with-tcltk-libs`都是有的，通过这两个参数可以解决 Tkinter 的问题！！！

### Python 3

这里以 Python-3.11.6 为例，参考 [Python 3.11.0 install doesn’t recognize homebrew Tcl/Tk due to --with-tcltk-libs, --with-tcltk-includes switches being removed from 3.11 - pyenv#2499](https://github.com/pyenv/pyenv/issues/2499)，在编译安装过程中使用 `TCLTK_CFLAGS` 和 `TCLTK_LIBS` 解决 `_tkinter` 缺失的问题。
```
export TCLTK_LIBS="-L/home/shenweiyan/software/ActiveTcl-8.6.9/lib -ltcl8.6 -ltk8.6"  # 8.5.x 版本，需改为 -ltcl8.5 -ltk8.5
export TCLTK_CFLAGS="-I/home/shenweiyan/software/ActiveTcl-8.6.9/include"

cd Python-3.11.6
/configure --prefix=/home/shenweiyan/software/python-3.11.6 ......
make && make install
```

![python3-confiigure-tkinter-yes](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/KGarden/2023/python-3-tkinter.png)

对于 Python 3.10.x (及以下版本，如 Python-3.9.18)，`configure` 中 `--with-tcltk-includes` 和 `--with-tcltk-libs` 的具体使用参考 <https://bugs.python.org/issue21887>：  
   
![tcltk-issue-21887-msg](https://gi.weiyan.tech/2024/10/tcltk-issue-21887-msg.webp)

### Python 2

想要在 Python 2.7 安装 Tkinter，需要在编译过程中通过 `--with-tcltk-includes` 和 `--with-tcltk-libs` 中指定 ActiveTcl 的头文件以及库所在路径。

如果在执行编译安装过程中，出现无法找到 libXss.so.1 共享动态库报错：

```bash
$ tar zvxf Python-2.7.15.tgz
$ cd Python-2.7.15
$ ./configure --prefix=/usr/local/software/python-2.7 --with-tcltk-includes='-I/usr/local/software/ActiveTcl-8.6/include' --with-tcltk-libs='-L/usr/local/software/ActiveTcl-8.6/lib -ltcl8.6 -ltk8.6' --enable-optimizations
$ make

......

warning: building with the bundled copy of libffi is deprecated on this platform.  It will not be distributed with Python 3.7
*** WARNING: renaming "_tkinter" since importing it failed: libXss.so.1: cannot open shared object file: No such file or directory

Python build finished successfully!
The necessary bits to build these optional modules were not found:
_dbm                  _gdbm
To find the necessary bits, look in setup.py in detect_modules() for the module's name.

The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
atexit                pwd                   time

Following modules built successfully but were removed because they could not be imported:
_tkinter

running build_scripts

......
```

CentOS 下请参考以下解决方法：
```
$ sudo yum install libXScrnSaver libXScrnSaver-devel
```

## 调用 Tkinter

Python 2/3 重新编译完后，执行一下下面的命令即可显示 Tk 的 ui 界面，以及相应的 Tcl/Tk 版本。
```
python2 -m Tkinter   # python 2
python3 -m tkinter   # python 3
```
![python2-m-Tkinter](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgBtb14ZgZFZXIRhOdt6efbYz7fd.png)

这时候，我们重新运行开头的 GUI 界面程序，可以看到中文已经正常显示：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqRHUXczPdHrQjFUXNQr_Cg_j2B4.png)

## 参考资料

- Download And Install Tcl: ActiveTcl，<https://www.activestate.com/products/activetcl/downloads/>
- Installing Tk，<https://tkdocs.com/tutorial/install.html>
- Python 下"No module named \_tkinter"问题解决过程分析，<https://www.jianshu.com/p/0baa9657377f>
- Python GUI 编程(Tkinter)文件对话框，<https://my.oschina.net/u/2245781/blog/661533>


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="12"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
