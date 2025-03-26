---
title: RedHat 6.5 下安装 PyQt4 详细步骤
urlname: 2019-05-18-redhat-install-pyqt-4
author: 章鱼猫先生
date: 2019-05-18
updated: "2021-06-25 10:45:05"
---

**目的：** RedHat 6.5 HPC 环境下安装生物信息 [STAMP](http://kiwi.cs.dal.ca/Software/Quick_installation_instructions_for_STAMP) 软件。

## 服务器环境

    系统：
    Red Hat Enterprise 6.5
    gcc version 4.8.5 (GCC)

    Anaconda 2.5：
    conda 4.4.4
    x86_64-conda_cos6-linux-gnu-gcc：gcc version 7.2.0
    x86_64-conda_cos6-linux-gnu-c++：gcc version 7.2.0

## 安装步骤

### 1、使用 conda 直接安装

    $ conda install STAMP

    $ which STAMP
    /Bio/home/shenweiyan/software/Anaconda2/bin/STAMP

    $ STAMP
    Traceback (most recent call last):
      File "/Bio/home/shenweiyan/software/Anaconda2/bin/STAMP", line 32, in <module>
        from stamp import STAMP
      File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/stamp/STAMP.py", line 38, in <module>
        from stamp.GUI.plotDlg import PlotDlg  # forward reference so py2app recognizes this file is required
      File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/stamp/GUI/plotDlg.py", line 24, in <module>
        from PyQt4 import QtGui, QtCore
    ImportError: No module named PyQt4

### 2、安装 PyQt4

    $ wget https://nchc.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz
    $ tar zvxf PyQt4_gpl_x11-4.12.1
    $ cd PyQt4_gpl_x11-4.12.1
    $ python configure.py
    Error: This version of PyQt requires SIP v4.19.1 or later

### 3、安装依赖一：SIP

虽然在 PyPI 可以找到 sip-4.19.8，但是安装的时候却会提示版本错误：

    $ pip install SIP
    Collecting SIP
      Could not find a version that satisfies the requirement SIP (from versions: )
    No matching distribution found for SIP
    You are using pip version 9.0.3, however version 10.0.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.

因此只能通过源码下载，安装 sip：

```bash
# Home Page：https://www.riverbankcomputing.com/software/sip/intro
$ wget https://nchc.dl.sourceforge.net/project/pyqt/sip/sip-4.19.6/sip-4.19.6.tar.gz
# https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.12/sip-4.19.12.tar.gz

# 由于使用 /Bio/home/shenweiyan/software/Anaconda2/bin/python 为默认 python
# 因此通过源码，默认安装到 /Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages
$ tar zvxf sip-4.19.12.tar.gz
$ cd sip-4.19.12
$ python configure.py
$ make
$ make install
```

最后，在 python 中 `import sip` 查看是否安装成功。

### 4、第二次安装 PyQt4

    $ cd PyQt4_gpl_x11-4.12.1
    $ python configure.py --verbose
    Determining the layout of your Qt installation...
    /Bio/home/shenweiyan/software/Anaconda2/bin/qmake -o qtdirs.mk qtdirs.pro
    make -f qtdirs.mk
    g++ -c -pipe -O2 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_CORE_LIB -I. -I../../../Anaconda2/include/qt -I../../../Anaconda2/include/qt/QtCore -I. -I../../../Anaconda2/mkspecs/linux-g++ -o qtdirs.o qtdirs.cpp
    g++ -Wl,-O1 -Wl,-rpath,/Bio/home/shenweiyan/software/Anaconda2/lib -o qtdirs qtdirs.o   -L/Bio/home/shenweiyan/software/Anaconda2/lib -lQt5Core -lpthread
    /Bio/home/shenweiyan/software/Anaconda2/lib/libQt5Core.so: undefined reference to `__cxa_throw_bad_array_new_length@CXXABI_1.3.8'
    /Bio/home/shenweiyan/software/Anaconda2/lib/libQt5Core.so: undefined reference to `operator delete[](void*, unsigned long)@CXXABI_1.3.9'
    /Bio/home/shenweiyan/software/Anaconda2/lib/libQt5Core.so: undefined reference to `operator delete(void*, unsigned long)@CXXABI_1.3.9'
    collect2: error: ld returned 1 exit status
    make: *** [qtdirs] Error 1
    Error: Failed to determine the layout of your Qt installation. Try again using
    the --verbose flag to see more detail about the problem.

### 5、安装依赖二：QT

使用 conda 安装的 qt >= 5.6.2：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fm2cbO_hsVvL_WajxcYc7SP2K8x7.png)

下面是通过源码安装 qt-4.8.x 的一些记录（使用 conda 应该也可以安装 qt-4.8.x，感兴趣的童鞋可以尝试一下）：

    $ wget http://mirrors.ustc.edu.cn/qtproject/archive/qt/4.8/4.8.3/qt-everywhere-opensource-src-4.8.3.tar.gz
    $ tar zvxf qt-everywhere-opensource-src-4.8.3.tar.gz
    $ cd qt-everywhere-opensource-src-4.8.3
    $ ./configure -prefix /Bio/home/shenweiyan/software/Qt-4.8.3
    $ make   # 很耗时；也可以根据 configure 后的提示使用 gmake
    $ make install

    # 安装 phonon 框架
    $ cd qt-everywhere-opensource-src-4.8.3/src/phonon
    $ make
    $ make install

**注意：**

① 源码安装 Qt-5.x.x 版本，configure 过程会出现 libxcb 相关库缺失，在实际安装过程中即使使用 `yum install xcb* libxcb`，依然无法解决问题。在安装中强烈推荐使用 Qt-4.x.x，如 4.8.3，通过版本解决 libxcb 的问题。

    $ ./configure -prefix /Bio/home/shenweiyan/software/Qt-5.6.0  # 报错信息如截图所示

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu7r9S18lVtBbSIEe8HG4gRQgZ1I.png)

② 在 Qt 4.8 中实现多媒体播放图形界面主要依赖于 phonon 框架，通常情况下，**Qt 基本库已经安装好，默认 phonon 是没有被安装的**，我们需要 configure 后加好参数，然后单独进入 phonon 的文件夹进行编译。

### 6、第三次安装 PyQt4

    $ python configure.py -q /Bio/home/shenweiyan/software/Qt-4.8.3/bin/qmake
    Determining the layout of your Qt installation...
    This is the GPL version of PyQt 4.9.5 (licensed under the GNU General Public
    License) for Python 2.7.3 on linux2.

    Type '2' to view the GPL v2 license.
    Type '3' to view the GPL v3 license.
    Type 'yes' to accept the terms of the license.
    Type 'no' to decline the terms of the license.

    Do you accept the terms of the license? yes

**注意：**
1、在 configure 的时候，指定了 qmake 的路径。
2、成功之后，然后再执行：

    make (要等一段时间)
    make install

如果在执行 make 过程，出现 `abstractaudiooutput.sip:28:33: fatal error: abstractaudiooutput.h` 报错，请参考第 5 步（安装 phonon 框架）进行解决。

3、成功运行命令后，PYQT 安装成功.你可以在 python 解析器下，运行`import PyQt4` 来检测是否安装成功。

## 总结

Qt 是一个跨平台的 C++ 图形用户界面应用程序框架。它提供给应用程序开发者建立艺术级的图形用户界面所需的所用功能。PyQt 是一个创建 GUI 应用程序的工具包（PyQt 的实现被视作 Python 的一个模块），它是 Python 编程语言和 Qt 库的成功融合，由 300 多个类和接近 6000 个函数与方法构成。

PyQt4 在 Linux 下安装，尤其是源码编译安装，需要特别注意：

1、要解决 `xcb*`、`libxcb`必须库依赖。
2、确保满足 sip 依赖。
3、确保 QT 安装，QT 安装过程中确保 phonon 库被编译安装。
4、PyQt4 在执行 configure 过程中可以通过指定 qmake，从而选择 Qt 版本。

## 参考资料

- 博客园. 叶念西风.《[Qt 学习笔记-安装 phonon 模块](http://www.cnblogs.com/ynxf/p/6394801.html)》. 2017-02-13
- 一号门博客.轻舞肥羊《[在 centos 6.2,python2.7 下安装 QT 4.8.3,pyqt 4.9.5 详细步骤](http://yihaomen.com/article/linux/313.htm)》. 2012-11-22
