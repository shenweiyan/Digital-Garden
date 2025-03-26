---
title: Python 源码编译安装
urlname: 2019-05-18-install-python-from-source
author: 章鱼猫先生
date: 2019-05-18
updated: "2023-06-01 16:38:47"
---

编程，作为生物信息学的一个基础性技能，是任何一个生信工程师都无法绕开话题。也许有些人还在纠结 Perl 和 Python 到底应该学习哪一个，但作为目前最火最流行的编程语言 Python 还是非常值得尝试的。它不但可以进行文本处理，在统计、网站、游戏、爬虫、数据可视化等方面也有非常强大的应用，比起曾经的 Perl 真的强大和全面很多，且比 Perl 更容易入手。不管从长远发展，还是短期需要，学会 Python，看懂 Perl (或者先学 Python，后学 Perl) 应该是每一个生信工程必备的基础技能之一。

工欲善其事，必先利其器。关于 Python 安装教程在网上一搜一大把，但总感觉不够全面，尤其对于中间出现的一些问题的解决方法不尽如人意。鉴于此，本文基于  CentOS/Ubuntu Linux 对 Python 的源码编译安装进行了一下简单的总结，记录如下。

- **2024-01-25：** 在 CentOS 7.7.1908 安装 Python-3.11.6 成功！
- **2021-12-21：** 在 Ubuntu 20.04 LTS 安装 Python-3.10.1 成功！
- **2021-09-15：** 在 Red Hat Enterprise 6.5 安装 Python-3.9.5 成功！

## RHEL/CentOS

以下的内容中，我们以安装 Python-3.7.3 为例进行说明。

### 安装环境

Red Hat 6.5 + GCC 4.4.7（GCC-4.8.5/5.3.1）。GCC 高级版本手动/yum 安装参考以下文章。

- [SCL+Devtoolset 安装与使用笔记 · 语雀](https://www.yuque.com/shenweiyan/cookbook/scl-devtoolset-note)
- [非 root 用户手动编译安装 GCC · 语雀](https://www.yuque.com/shenweiyan/cookbook/linux-gcc-install)

```bash
$ lsb_release -a
LSB Version:    :base-4.0-amd64:base-4.0-noarch:core-4.0-amd64:core-4.0-noarch:graphics-4.0-amd64:graphics-4.0-noarch:printing-4.0-amd64:printing-4.0-noarch
Distributor ID: RedHatEnterpriseServer
Description:    Red Hat Enterprise Linux Server release 6.5 (Santiago)
Release:        6.5
Codename:       Santiago

$ gcc --version
gcc (GCC) 4.4.7 20120313 (Red Hat 4.4.7-4)
Copyright (C) 2010 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### 解决依赖

如果您拥有 root 权限，请执以下依赖安装：

```bash
yum install zlib
yum install zlib-devel
yum install openssl
yum install openssl-devel
yum install libffi
yum install libffi-devel
yum install readline readline-devel sqlite sqlite-devel tk-devel
```

| 缺少库名称 | 安装命令                                              |
| ---------- | ----------------------------------------------------- |
| \_uuid     | yum install libuuid-devel                             |
| readline   | yum install readline-devel                            |
| \_tkinter  | yum install tk-devel                                  |
| \_ffi      | yum install libffi-devel                              |
| \_curses   | yum install ncurses-libs                              |
| \_sqlite   | yum install sqlite-devel                              |
| \_bz2      | yum isntall bzip2-devel                               |
| \_ssl      | yum install openssl-devel                             |
| \_gdbm     | yum install gdbm-devel                                |
| \_dbi      | yum install libdbi-devel                              |
| \_zlib     | yum install zlib-devel                                |
| lzma       | yum install xz-develyum install python-backports-lzma |

如果您没有 root 权限，可以参考《[手把手教你在 Linux 源码安装最新版本的 R](https://www.yuque.com/shenweiyan/cookbook/install-latest-r-from-source)》一文，手动一个个去解决以上的依赖。

#### _sqlite3

执行 **make** 过程中提示 **\_sqlite3 not found**，如下：

```bash
$ make
......
Python build finished successfully!
The necessary bits to build these optional modules were not found:
_sqlite3              _ssl
To find the necessary bits, look in setup.py in detect_modules() for the module's name.

The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  atexit                pwd
time
```

如果执行 **rpm -qa|grep sqlite** 看到 sqlite 和 sqlite-devel 都已经安装（libsqlite3.so 默认保存在 /usr/lib64 下； sqlite3.h 默认保存在 /usr/include 下）。

```bash
$ sqlite3 -version
3.6.20

$ ll /usr/lib64/libsqlite3.so
lrwxrwxrwx 1 root root 19 Apr 23  2015 /usr/lib64/libsqlite3.so -> libsqlite3.so.0.8.6

$ ll /usr/include/sqlite3.h
-rw-r--r-- 1 root root 263K Nov 25  2009 /usr/include/sqlite3.h
```

但是，执行 make 依然出现以上报错，参考下面的方法《[python build from source: cannot build optional module sqlite3 - Stack Overflow](https://stackoverflow.com/questions/32779768/python-build-from-source-cannot-build-optional-module-sqlite3)》。

1.    手动安装 sqlite3。

```bash
$ wget https://www.sqlite.org/2021/sqlite-autoconf-3360000.tar.gz --no-check-certificate
$ tar zvxf sqlite-autoconf-3360000.tar.gz
$ cd sqlite-autoconf-3360000
$ ./configure --prefix=/home/shenweiyan/software/sqlite-3.36.0
$ make
$ make install
```

2. 找到 **sqlite3.h** 文件的保存目录。
3. 修改 **setup.py** 文件，在 `sqlite_inc_paths` 中加上 `sqlite3.h` 的文件路径。

```bash
sqlite_inc_paths = [ '/home/shenweiyan/software/sqlite-3.36.0/include',
                     '/usr/include',
                     '/usr/include/sqlite',
                     '/usr/include/sqlite3',
                     '/usr/local/include',
                     '/usr/local/include/sqlite',
                     '/usr/local/include/sqlite3',
                   ]
```

4. 配置环境。

```bash
$ export LD_LIBRARY_PATH=/home/shenweiyan/software/sqlite-3.36.0/lib:$LD_LIBRARY_PATH
```

#### _ssl

Python3 需要引用 `openssl`  模块，但是 python3.7+ 在 CentOS 中要求的 openssl 版本最低为 1.0.2，而 CentOS 默认的为 1.0.1（CentOS-6.x 通过 `yum`  源安装的 openssl 的最高版本是 1.0.1），所以需要手动更新 openssl。

对于 openssl 版本的选择，建议至少选择 1.1.1+ 版本：

1. urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168
2. **Python requires an OpenSSL 1.0.2 or 1.1 compatible libssl with X509_VERIFY_PARAM_set1_host().**

```bash
# 下载
wget http://www.openssl.org/source/openssl-1.1.1.tar.gz

# 解压缩
tar -zxvf openssl-1.1.1.tar.gz

# 进入目录安装
cd openssl-1.1.1

# 进行配置下，自定义
./config --prefix=/home/shenweiyan/software/openssl-1.1.1 shared zlib

# 编译并安装
make && make install

# 配置到用户环境变量，随处使用
echo "export LD_LIBRARY_PATH=/home/shenweiyan/software/openssl-1.1.1/lib:$LD_LIBRARY_PATH" >> $HOME/.bashrc

# 是环境变量配置生效
source $HOME/.bashrc
```

**请注意：**

1. **openssl** 编译（config）的时候 **必须要加上 shared  参数**，否者源码安装 Python 即使添加了 `--with-openssl`  的自定义路径，依然会导致 `Could not build the ssl module!`  报错！
2. 从 <https://www.openssl.org/source/> 下载的源码 openssl-1.0.2s、openssl-1.0.2m，包括  CentOS-7.5 使用 `yum`  安装的最高版本的 openssl-1.0.2k 目前发现依然会导致 `Could not build the ssl module` ，建议从 <https://www.openssl.org/source/old/> 下载 1.1.1 的源码编译安装。

#### _lzma

正常情况下，下面的方法可以解决该问题（如果您有 root 权限的话）。

```bash
# For ubuntu:
$ sudo apt-get install liblzma-dev

# For centos:
$ yum install xz-devel
```

普通用户可以手动安装解决：

```bash
$ wget https://tukaani.org/xz/xz-5.2.5.tar.gz --no-check-certificat
$ tar zvxf xz-5.2.5.tar.gz
$ cd xz-5.2.5
$ ./configure --prefix=/home/shenweiyan/software/xz-5.2.5
$ make
$ make install
```

最后，配置环境：

```bash
$ export LD_LIBRARY_PATH=/home/shenweiyan/software/xz-5.2.5/lib:$LD_LIBRARY_PATH
```

#### _ctypes

在 CentOS 6.x 安装 `libffi-devel`  的时候出现以下问题：

```bash
$ yum install libffi-devel
Loaded plugins: product-id, refresh-packagekit, search-disabled-repos, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Setting up Install Process
cdrom                                                                                                                                         | 4.1 kB     00:00 ...
No package libffi-devel available.
Error: Nothing to do
```

可以使用下面的方法安装：
```shell
[root@log01 ~]# rpm -ivh http://mirror.centos.org/centos/6/os/x86_64/Packages/libffi-devel-3.0.5-3.2.el6.x86_64.rpm
Retrieving http://mirror.centos.org/centos/6/os/x86_64/Packages/libffi-devel-3.0.5-3.2.el6.x86_64.rpm
warning: /var/tmp/rpm-tmp.V9ihbu: Header V3 RSA/SHA256 Signature, key ID c105b9de: NOKEY
Preparing...                ########################################### [100%]
   1:libffi-devel           ########################################### [100%]
[root@log01 ~]# rpm -qa|grep libffi
libffi-3.0.5-3.2.el6.x86_64
libffi-devel-3.0.5-3.2.el6.x86_64
```

手动的源码方法安装如下：
```bash
$ wget ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
$ tar zvxf libffi-3.2.1.tar.gz
$ ./configure --prefix=/home/shenweiyan/software/libffi-3.2.1
$ make
$ make install
```

#### pygraphviz (可选)

如果你不需要使用 pygraphviz，可以不用管这个依赖。

> PyGraphviz is a Python interface to the Graphviz graph layout and visualization package. With PyGraphviz you can create, edit, read, write, and draw graphs using Python to access the Graphviz graph data structure and layout algorithms.

> PyGraphviz 是 Graphviz 图形布局和可视化包的 Python 接口。 借助 PyGraphviz，您可以使用 Python 创建、编辑、读取、写入和绘制图形，以访问 Graphviz 图形数据结构和布局算法。

```bash
$ /home/shenweiyan/software/Python-3.7.3/bin/pip3 install pygraphviz
Collecting pygraphviz
  Using cached https://files.pythonhosted.org/packages/7e/b1/d6d849ddaf6f11036f9980d433f383d4c13d1ebcfc3cd09bc845bda7e433/pygraphviz-1.5.zip
Installing collected packages: pygraphviz
  Running setup.py install for pygraphviz ... error
    Complete output from command /home/shenweiyan/software/Python-3.7.3/bin/python3.7 -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-_zdjdg0j/pygraphviz/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-g0mz7lrq/install-record.txt --single-version-externally-managed --compile:
    running install
    Trying dpkg
    Failed to find dpkg
    Trying pkg-config
    Package libcgraph was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libcgraph.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libcgraph' found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-_zdjdg0j/pygraphviz/setup.py", line 93, in <module>
        tests_require=['nose>=1.3.7', 'doctest-ignore-unicode>=0.1.2', 'mock>=2.0.0'],
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/site-packages/setuptools/__init__.py", line 145, in setup
        return distutils.core.setup(**attrs)
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/distutils/dist.py", line 966, in run_commands
        self.run_command(cmd)
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/distutils/dist.py", line 985, in run_command
        cmd_obj.run()
      File "/tmp/pip-install-_zdjdg0j/pygraphviz/setup_commands.py", line 44, in modified_run
        self.include_path, self.library_path = get_graphviz_dirs()
      File "/tmp/pip-install-_zdjdg0j/pygraphviz/setup_extra.py", line 162, in get_graphviz_dirs
        include_dirs, library_dirs = _try_configure(include_dirs, library_dirs, _pkg_config)
      File "/tmp/pip-install-_zdjdg0j/pygraphviz/setup_extra.py", line 117, in _try_configure
        i, l = try_function()
      File "/tmp/pip-install-_zdjdg0j/pygraphviz/setup_extra.py", line 72, in _pkg_config
        output = S.check_output(['pkg-config', '--libs-only-L', 'libcgraph'])
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/subprocess.py", line 395, in check_output
        **kwargs).stdout
      File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/subprocess.py", line 487, in run
        output=stdout, stderr=stderr)
    subprocess.CalledProcessError: Command '['pkg-config', '--libs-only-L', 'libcgraph']' returned non-zero exit status 1.

    ----------------------------------------
Command "/home/shenweiyan/software/Python-3.7.3/bin/python3.7 -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-_zdjdg0j/pygraphviz/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-g0mz7lrq/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-install-_zdjdg0j/pygraphviz/

```

参考：《[Installation:fatal error: 'graphviz/cgraph.h' file not found](https://github.com/pygraphviz/pygraphviz/issues/11)》

```bash
$ wget https://graphviz.gitlab.io/pub/graphviz/stable/SOURCES/graphviz.tar.gz
$ tar zvxf graphviz.tar.gz
$ cd graphviz-2.40.1
$ ./configure --prefix=/home/shenweiyan/software/graphviz-2.40.1
$ make && make install
```

推荐把安装好的 graphviz 添加到环境变量，这样可以避免运行过程中出现：**"pygraphviz/graphviz_wrap.c:2987:29: fatal error: graphviz/cgraph.h: No such file or directory"** 无法找到头文件的异常。

```bash
export PKG_CONFIG_PATH=/home/shenweiyan/software/graphviz-2.40.1/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=/home/shenweiyan/software/graphviz-2.40.1/lib:$LD_LIBRARY_PATH
export C_INCLUDE_PATH=/home/shenweiyan/software/graphviz-2.40.1/include:$C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH=/home/shenweiyan/software/graphviz-2.40.1/include:$CPLUS_INCLUDE_PATH
```

如果 graphviz 添加到环境变量， `pygraphviz`  的 python 包可以参考下面的方法安装：

```bash
$ /home/shenweiyan/software/Python-3.7.3/bin/pip3 install --global-option=build_ext --global-option="-I/home/shenweiyan/software/graphviz-2.40.1/include" --global-option="-L/home/shenweiyan/software/graphviz-2.40.1/lib" pygraphviz
/home/shenweiyan/software/Python-3.7.3/lib/python3.7/site-packages/pip/_internal/commands/install.py:207: UserWarning: Disabling all use of wheels due to the use of --build-options / --global-options / --install-options.
  cmdoptions.check_install_build_global(options)
Collecting pygraphviz
  Using cached https://files.pythonhosted.org/packages/7e/b1/d6d849ddaf6f11036f9980d433f383d4c13d1ebcfc3cd09bc845bda7e433/pygraphviz-1.5.zip
Installing collected packages: pygraphviz
  Running setup.py install for pygraphviz ... done
Successfully installed pygraphviz-1.5
```

### 编译安装

第一，下载 Python 源码，解压。

```bash
# 官网下载地址 https://www.python.org/downloads
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz

# 解压到指定目录
tar zvxf Python-3.7.3.tgz -C /usr/local/src
```

第二，进入解压的源码路径，编译 Python 源码。

```bash
$ soft=/home/shenweiyan/software
$ export PKG_CONFIG_PATH=$soft/libffi-3.2.1/lib/pkgconfig:$PKG_CONFIG_PATH
$ export PKG_CONFIG_PATH=$soft/graphviz-2.40.1/lib/pkgconfig:$PKG_CONFIG_PATH
$ export LD_LIBRARY_PATH=$soft/libffi-3.2.1/lib64:$LD_LIBRARY_PATH
$ export LD_LIBRARY_PATH=$soft/graphviz-2.40.1/lib:$LD_LIBRARY_PATH
$ export LD_LIBRARY_PATH=$soft/openssl-1.1.1/lib:$LD_LIBRARY_PATH
$ export LD_LIBRARY_PATH=$soft/sqlite-3.36.0/lib:$LD_LIBRARY_PATH

$ ./configure \
--enable-optimizations \
--prefix=/home/shenweiyan/software/Python-3.7.3 \
--with-openssl=$libs/openssl-1.1.1 \
CC=/home/shenweiyan/software/gcc-4.8.5/bin/gcc \
CXX=/home/shenweiyan/software/gcc-4.8.5/bin/c++ \
LDFLAGS="-L/home/shenweiyan/software/libffi-3.2.1/lib64 \
         -L/home/shenweiyan/software/graphviz-2.40.1/lib" \
CPPFLAGS="-I/home/shenweiyan/software/graphviz-2.40.1/include" \
PKG_CONFIG_PATH="/home/shenweiyan/software/libffi-3.2.1/lib/pkgconfig: \
                 /home/shenweiyan/software/graphviz-2.40.1/lib/pkgconfig"
```

- `--enable-optimizations`  是优化选项（LTO，PGO  等）加上这个  flag  编译后，性能有  10%  左右的优化，但是这会明显的增加编译时间。建议使用这个参数；
- `--prefix`  声明安装路径；
- 安装多个 python 的版本，如果不开启`--enable-shared`，指定不同路径即可。当开启`--enable-shared` 时，默认只有一个版本的 python。
- Python 3 编译可以使用`--with-openssl=DIR`  指定 OpenSSL 安装路径进行编译的方式解决 OpenSSL 依赖，否则 `make`  过程可能出错。

```shell
$ make
......
The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  atexit                pwd
time


Failed to build these modules:
_ctypes               _hashlib              _ssl


Could not build the ssl module!
Python requires an OpenSSL 1.0.2 or 1.1 compatible libssl with X509_VERIFY_PARAM_set1_host().
LibreSSL 2.6.4 and earlier do not provide the necessary APIs, https://github.com/libressl-portable/portable/issues/381

......
```

- `make` 过程如果出现 `ModuleNotFoundError: No module named '_ctypes'` 或者 `INFO: Could not locate ffi libs and/or headers` 参考：<https://groups.google.com/forum/#!topic/comp.lang.python/npv-wzmytzo>

!![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmK7bCeEeGjfbl1UVdvHyw3Jg8Zj.png)

- 如果指定 `--with-openssl=DIR` 依然无法解决 ssl 模块的问题，可以参考修改 Modules/Setup.dist 文件（默认这块是注释的，放开注释即可。这块功能是开启 SSL 模块，不然会出现安装完毕后，提示找不到 ssl 模块的错误）再执行 configure，修改内容如下：

```bash
# Socket module helper for SSL support; you must comment out the other
# socket line above, and possibly edit the SSL variable:
SSL=/usr/local/ssl
_ssl _ssl.c \
    -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
    -L$(SSL)/lib -lssl -lcrypto
```

第三，Makefile 生后依次在当前路径执行编译和安装命令。

```bash
make && make install
```

第四，安装完成。以上命令执行完毕，且无报错的情况下，我们将默认 python 换将切换至 3.7.3（一般不建议替换，个人建议把自定义安装的 Python bin 路径添加到 PATH 环境变量即可）：

```bash
# 替换系统自带的 python（不建议）
mv /usr/bin/python /usr/bin/python2
ln -s /home/shenweiyan/software/Python-3.7.3/bin/python3 /usr/bin/python

# 添加新 Python 到 PATH 环境变量（建议）
echo "export PATH=/home/shenweiyan/software/Python-3.7.3/bin:$PATH" >>~/.bashrc
source ~/.bashrc
```

运行命令 `python -V` ，查看是否出现 3.7.3  的版本，出现即为安装成功。

### 安装 pip+setuptools

**说明：** Python >= 3.10 在安装时候，默认会同时安装 **pip3**！如果你的 python < 3.10，可以参考下面的方法安装 pip。

```bash
# 下载 setuptools 和 pip 安装程序
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

至此，CentOS Linux release 6.5 下的 python-3.7.3  全部安装完成。如果在安装过程中出现其他的报错，建议把 error 关键信息直接复制到 Google 进行检索，参考其他人的解决方法。

### 其他异常与解决

#### _bz2

- 系统：CentOS Linux release 7.7.1908 (Core)
- GCC：gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-39)

在 CentOS 7 中安装 Python-3.6.9 中发现 make 过程中一直提示：“**ModuleNotFoundError: No module named '\_bz2'**”，尽管 `sudo yum install bzip2 bzip2-devel`  已经安装了 bzip2 的依赖，问题还是不得其解。最后参考 stackoverflow 上的《Correctly building local python3, with bz2 support》，终于解决问题，下面记录一下。
[Correctly building local python3, with bz2 support](https://stackoverflow.com/questions/51149227/correctly-building-local-python3-with-bz2-support)

**手动安装 bzip2：**

```bash
wget https://nchc.dl.sourceforge.net/project/bzip2/bzip2-1.0.6.tar.gz
tar zvxf bzip2-1.0.6.tar.gz
cd bzip2-1.0.6
make -f Makefile_libbz2_so  # 这一步是生成 libbz2.so.1.0.6 的动态库文件
make
make install PREFIX=/usr/local/software/bzip2-1.0.6
cp libbz2.so.1.0.6 /usr/local/software/bzip2-1.0.6/lib/
```

**几点说明：**

- bzip2 的官网  <http://www.bzip.org/>  已经把 bzip2 的源码下载链接放到了  SourceForge，网络上一些从  <http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz>  下载的做法已经失效。
- [SourceForge](https://sourceforge.net/projects/bzip2/files/) 上 bzip2 的最新版本还是 1.0.6（Last modified 2018-11-3），更高级版本的 bzip2 我也不知道是否存在，也不知道能不能用。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvgxGWlVJSxOCvgXFo9BPOa3ODm5.png)

**编译安装 Python-3.6.9：**

```bash
$ wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
$ tar zvxf Python-3.6.9.tgz
$ cd Python-3.6.9
$ ./configure --enable-optimizations --prefix=/usr/local/software/python-3.6 CFLAGS="-I/usr/local/software/bzip2-1.0.6/include" LDFLAGS="-L/usr/local/software/bzip2-1.0.6/lib"
$ make
$ make install
```

- Python-3.6.9 中的 `./configure --help` 中没有 `--with-openssl` 参数！有点神奇，我也不知道原因。
- 安装完成可以用 `from _bz2 import BZ2Compressor, BZ2Decompressor` 测试一下 `_bz2`  是否可用。

#### init_import_site

如果在 `make` 过程中提示 `init_import_site: Failed to import the site module`：

```bash
Fatal Python error: init_import_site: Failed to import the site module
Python runtime state: initialized
Traceback (most recent call last):
  File "/home/shenweiyan/src/Python-3.11.6/Lib/site.py", line 73, in <module>
    import os
  File "/home/shenweiyan/src/Python-3.11.6/Lib/os.py", line 29, in <module>
    from _collections_abc import _check_methods
SystemError: <built-in function compile> returned NULL without setting an exception
make[1]: *** [Python/frozen_modules/abc.h] Error 1
make[1]: Leaving directory `/home/shenweiyan/src/Python-3.11.6'
make: *** [profile-opt] Error 2
```

个人在 CentOS 7.7.1908 + GCC 4.8.5 安装 Python 3.11.6 就遇到了这个问题，最后在 [这里](https://www.linuxquestions.org/questions/centos-111/build-python-3-11-from-source-on-centos-7-a-4175719297/) 找到了原因 —— GCC 版本太低了，因此我们只需要升级一下 GCC 的版本就可以。

## Ubuntu/Debian

### 安装环境

Ubuntu 20.04 + GCC 9.3.0。

```bash
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

### 解决依赖

| 缺少库名称 | 安装命令                         |
| ---------- | -------------------------------- |
| \_uuid     | apt install uuid-dev             |
| readline   | apt install libreadline-dev      |
| \_tkinter  | apt install python3-tk tk tk-dev |
| \_ffi      | apt install libffi-dev           |
| \_curses   | apt install libncurses5-dev      |
| \_sqlite   | apt install libsqlite3-dev       |
| \_bz2      | apt install libbz2-dev           |
| \_ssl      | apt install libssl-dev           |
| \_gdbm     | apt install libgdbm-compat-dev   |
| \_dbi      |                                  |
| \_zlib     | apt install zlib1g-dev           |
| \_lzma     | apt install lzma-dev liblzma-dev |
| \_ctypes   | apt install libffi-dev           |

### 编译安装

Ubuntu/Debian 下 Python 编译安装的命令跟 CentOS/RedHat 是一样的，具体参考 **编译安装** 一节的内容。

## 参考资料

1. 行者无疆-ITer,《[python2.7 源码编译安装](https://www.cnblogs.com/ITer-jack/p/8305912.html)》, 博客园
2. Scott Frazer,《[How do I compile Python 3.4 with custom OpenSSL?](https://stackoverflow.com/questions/23548188/how-do-i-compile-python-3-4-with-custom-openssl)》, Stack Overflow
