---
title: 聊一聊 Python 安装中的 --enable-shared
urlname: 2019-05-18-python-enable-shared
author: 章鱼猫先生
date: 2019-05-18
updated: "2021-06-25 10:44:50"
---

今天在 CentOS 7.4 使用源码编译安装 Python-2.7.15 的时候，发现了一个非常奇怪的问题：

```bash
$ ./configure --prefix=/home/steven/python-2.7 --enable-shared
$ make
$ make install
```

安装完成，进入 /home/steven/python-2.7/bin/python 命令行，发现 Python 变成了 2.7.5。安装过程中既没有报错，也没有其他任何的 warnning 信息。重装过程中甚至使用 make test 进行了检测，Tests result: SUCCESS！问题依然无法解决。

    $ /home/steven/python-2.7/bin/python
    Python 2.7.5 (default, Aug  4 2017, 00:39:18)
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

开始怀疑是个人 home 目录或者系统 env 的影响，但检查了很多遍，甚至清空了所有的 env，更换其他用户，更换 Python-2.7.14 安装，结果都一样。毫无头绪之下，调整编译尝试最简安装：

    $ ./configure --prefix=/home/steven/python-2.7
    $ make
    $ make install

这次，/home/steven/python-2.7/bin/python 居然变成了 2.7.15，一切都正常了！很明显 `--enable-shared` 是整个问题的关键。对此 Python 官方给出了解释：

> The problem is, that on most Unix systems (with the notable exception of Mac OS X), the path to shared libraries is not an absolute path.  So, if you install Python in a non-standard location, which is the right thing to do so as not to interfere with a system Python of the same version, you will need to configure in the path to the shared library or supply it via an environment variable at run time, like LD_LIBRARY_PATH.  You may be better off avoiding --enable-shared; it's easy to run into problems like this with it.
>
> From Python Issue27685, <https://bugs.python.org/issue27685>

即是说，在大多数 Unix 系统上（除了 Mac OS X 之外），共享库的路径不是绝对路径。 因此，如果我们在非标准位置安装 Python，为了不和相同版本的系统 Python 产生干扰，我们需要配置非标准位置安装的 Python 共享库的路径，或者通过设置运行时的环境变量，如 LD_LIBRARY_PATH。 为了避免这个问题，我们最好避免使用 `--enable-shared`。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu3mNt-6GcKZPAlp-GyEH2qfCVOm.png)

或者我们也可以使用以下预编译命令，以避免开启 `--enable-shared` 时，默认只有一个版本的 python：

```bash
./configure --enable-shared --prefix=/opt/python LDFLAGS=-Wl,-rpath=/opt/python/lib
```
