---
title: NCBI Blast 源码编译安装方法
urlname: 2022-12-01-build-blast-from-src
author: 章鱼猫先生
date: 2022-12-01
updated: 2024-08-30
---

CentOS 6.5 的老服务器没法直接使用官方提供的二进制版本，其中最要命的提示就是 Glibc 的版本太低，且非 root 用户手动升级 glibc 基本是个无解的难题。于是考虑从官方提供的 Blast+ 源码进行手动编译安装。

虽然 Blast 官网的帮助文档中没有提到如何从源代码编译出 Blast，但是却在 `ncbi-blast-2.xx.x+-src/c++/src/algo/blast/core/README` 里面交代了在各个平台下编译 Blast 的方式。这里就直接把它的内容转发如下，以作补充：

### 获取源代码

Download the source distribution of BLAST+:

- <https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/>

### 安装与构建说明

Unpack the source archive in its installation directory and change working directory to ncbi-blast-VERSION+-src/c++.

**UNIX**
To build these source files into a library without the rest of the NCBI BLAST+ applications/libraries, one should use the following commands:

```bash
./configure --with-projects=scripts/projects/blast_core_lib.lst \
            --without-debug --with-mt --with-build-root=ReleaseMT
cd ReleaseMT/build
make all_p
```

make 编译 blast 非常耗时间，大概 2 个小时后编译结束，在 `./ReleaseMT/bin` 下会生成各种二进制可执行文件。把这个目录加入到 `PATH` 中，你就可以使用 Blast 的各种工具了。

This will configure and build an optimized library called blast, which can then be referenced in makefiles as follows:

```python
NCBI_HOME=<installation directory of the NCBI C++ toolkit>
-I$NCBI_HOME/c++/ReleaseMT/inc -I$NCBI_HOME/c++/include
-L $NCBI_HOME/c++/ReleaseMT/lib
```

**Windows**

1. Open the ncbi_cpp.sln project/solution file c++/compilers/msvc800_prj/static/build/ncbi_cpp.sln.
2. Right click on the -CONFIGURE-DIALOG- project on the Solution Explorer and select **"Build"** from the context menu, which will bring up a window titled **"Project Tree Builder"**.
3. In the "Project Tree Builder" window's first text box, enter scripts\projects\blast_core_lib.lst, click OK, and on the subsequent window click "Reload".
4. After the environment reloads, right click on blast.lib and select **"Build"**.

The blast.lib library file will be found in c++\compilers\msvc800_prj\static\lib\CONF\blast.lib, where CONF represents the appropriate configuration (e.g.: debugdll, debugmt, releasedll, or releasemt), and the headers will be found in c++\compilers\msvc800_prj\static\inc and c++\include.

### 安装与说明

#### 指定安装路径

在 **`configure`** 一步，我们可以使用 `--with-build-root` 指定 blast 的安装路径：

- `--with-build-root=ReleaseMT`，将会安装到当前目录的 ReleaseMT 目录下；      
  ![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoG_RuZNkxg3zk0ce5iDaQaYUYbr.png)

- `--with-build-root=/usr/local/shenweiyan/ncbi-blast-2.13.0+`，将会安装到该指定的路径中。

#### GCC 版本与环境配置

ncbi-blast-2.13.0+ 的源码编译安装要求 **GCC 7.1 or newer**：

```bash
configure: error: Please upgrade to a compiler supporting C++ '17, such as GCC 7.1 or newer.
```

GCC 的手动编译安装还是挺简单的，参考：《[非 root 用户手动编译安装 GCC](https://www.yuque.com/shenweiyan/cookbook/linux-gcc-install?view=doc_embed)》

GCC 安装完以后需要执行以下两步：

1. 把可执行程序添加到 PATH 环境：**`export PATH=/Path/To/gcc-7.3.0/bin:$PATH`**。
2. 解决 **`libstdc++.so.6: version `GLIBCXX_3.4.22' not found`**

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpcXY1qyhMM4EIGgd5lx2ashEm8-.png)

```bash
export LD_LIBRARY_PATH=/Path/To/gcc-7.3.0/lib:/Path/To/gcc-7.3.0/lib64:$LD_LIBRARY_PATH
```
