---
title: UpSetR 关联的 venneuler 包安装笔记
urlname: 2020-03-05-venneuler-installation
author: 章鱼猫先生
date: 2020-03-05
updated: "2023-07-10 16:32:15"
---

> 本文章已经设置了最低额度的付费阅读，如果您觉得文章对您有用，且手头宽裕，欢迎请作者喝杯热茶。本文章付费部分内容并不影响您对文章的理解，只是作者对付费阅读的一次尝试和态度，感谢支持。

## 背景

R 语言中的  [venneuler](https://cran.r-project.org/web/packages/venneuler/index.html)  是一个用于计算并显示韦恩图和欧拉图的包，这个包在 CRAN 上的最后一个版本是 1.1.0，发布于  2011-08-10，它是一个基于 rJava 依赖的 R 包。

```r
vd <- venneuler(c(A=0.3, B=0.3, C=1.1, "A&B"=0.1, "A&C"=0.2, "B&C"=0.1 ,"A&B&C"=0.1))
plot(vd)

# same as c(A=1, `A&B&C`=1, C=1)
m <- data.frame(elements=c("1","2","2","2","3"), sets=c("A","A","B","C","C"))
v <- venneuler(m)
plot(v)

m <- as.matrix(data.frame(A=c(1.5, 0.2, 0.4, 0, 0),
                          B=c(0 , 0.2, 0 , 1, 0),
                          C=c(0 , 0 , 0.3, 0, 1)))
# without weights
v <- venneuler(m > 0)
plot(v)

# with weights
v <- venneuler(m)
plot(v)
```

在  [venneuler](https://cran.r-project.org/web/packages/venneuler/index.html)  包，作者引入了一个的用于描述集合交集的向量，这一点后来也被 `UpSetR`  所借鉴，即 `UpSetR`  中的 `fromExpression` 。 `UpSetR`  接受三种类型的数据输入：

- 表格数据，即 R 语言里面的数据框。行表示元素，列表示数据集分配和额外信息。

- 元素名的集合( `fromList` )。
- `venneuler`  包引入的用于描述集合交集的向量 ( `fromExpression`）。

早在 18 年 6 月的时候，我公众号上写过一篇关于 `UpSetR`  的学习笔记《[UpSetR：多数据集绘图可视化处理利器](https://mp.weixin.qq.com/s/SOOcQxQrj23GqYaO-lTCig)》，提到过一下 `venneuler` ，当时也没怎么留意，直到前不久有个读者在使用 `UpSetR`  的时候给我了一个截图。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpnAmeZVOJhekLD4ZVlh4Wb1-6tR.png)

- 其实，这个截图中的 `fromExpression`  拼写错了，如果 `UpSetR`  安装好，又把 `fromExpression`  拼对，就可以解决导入集合交集向量数据的问题。
- `rJava` 、 `venneuler`  包的安装并没有想象中的那么好安装，尤其是 `venneuler` 。

## 问题

使用 `conda install r-venneuler`  安装完 `venneuler`  包后， `library(venneuler)`  加载时出现动态库异常。

```r
> library(venneuler)
Loading required package: rJava
Error occurred during initialization of VM
Unable to load native library: /usr/local/software/miniconda3/libjava.so: cannot open shared object file: No such file or directory
```

```r
$ R CMD javareconf
Java interpreter : /usr/local/software/miniconda3/bin/java
Java version     : 1.8.0_192
Java home path   : /usr/local/software/miniconda3/jre
Java compiler    : /usr/local/software/miniconda3/bin/javac
Java headers gen.: /usr/local/software/miniconda3/bin/javah
Java archive tool: /usr/local/software/miniconda3/bin/jar

trying to compile and link a JNI program
detected JNI cpp flags    : -I$(JAVA_HOME)/../include -I$(JAVA_HOME)/../include/linux
detected JNI linker flags : -L$(JAVA_HOME)/lib/amd64/server -ljvm
x86_64-conda_cos6-linux-gnu-cc -I"/usr/local/software/miniconda3/lib/R/include" -DNDEBUG -I/usr/local/software/miniconda3/jre/../include -I/usr/local/software/miniconda3/jre/../include/linux  -DNDEBUG -D_FORTIFY_SOURCE=2 -O2 -isystem /usr/local/software/miniconda3/include -I/usr/local/software/miniconda3/include -Wl,-rpath-link,/usr/local/software/miniconda3/lib  -fpic  -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /usr/local/software/miniconda3/include -fdebug-prefix-map=/home/conda/feedstock_root/build_artifacts/r-base_1576190804673/work=/usr/local/src/conda/r-base-3.6.2 -fdebug-prefix-map=/usr/local/software/miniconda3=/usr/local/src/conda-prefix  -c conftest.c -o conftest.o
x86_64-conda_cos6-linux-gnu-cc -shared -L/usr/local/software/miniconda3/lib/R/lib -Wl,-O2 -Wl,--sort-common -Wl,--as-needed -Wl,-z,relro -Wl,-z,now -Wl,--disable-new-dtags -Wl,--gc-sections -Wl,-rpath,/usr/local/software/miniconda3/lib -Wl,-rpath-link,/usr/local/software/miniconda3/lib -L/usr/local/software/miniconda3/lib -Wl,-rpath-link,/usr/local/software/miniconda3/lib -o conftest.so conftest.o -L/usr/local/software/miniconda3/jre/lib/amd64/server -ljvm -L/usr/local/software/miniconda3/lib/R/lib -lR


JAVA_HOME        : /usr/local/software/miniconda3/jre
Java library path: $(JAVA_HOME)/lib/amd64/server
JNI cpp flags    : -I$(JAVA_HOME)/../include -I$(JAVA_HOME)/../include/linux
JNI linker flags : -L$(JAVA_HOME)/lib/amd64/server -ljvm
Updating Java configuration in /usr/local/software/miniconda3/lib/R
Done.

$ cd /usr/local/software/miniconda3
$ find ./ -name libjava.so
./pkgs/openjdk-8.0.192-h516909a_1004/jre/lib/amd64/libjava.so
./jre/lib/amd64/libjava.s
```

即使使用 `LD_LIBRARY_PATH` 添加完目标动态库后，依然无法避免 "**java/lang/NoClassDefFoundError:  java/lang/Object**" 的异常。

```r
$ export LD_LIBRARY_PATH=/usr/local/software/miniconda3/jre/lib/amd64:$LD_LIBRARY_PATH
$ R

R version 3.6.2 (2019-12-12) -- "Dark and Stormy Night"
Copyright (C) 2019 The R Foundation for Statistical Computing
Platform: x86_64-conda_cos6-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> library(venneuler)
Loading required package: rJava
Error occurred during initialization of VM
java/lang/NoClassDefFoundError: java/lang/Object
```

使用 `conda create -n r-3.6.2 r-base=3.6.2`  创建的新环境中发现， `conda install -r r-venneuler`  会同时执行 `openjdk` 、 `r-rjava` 、 `r-venneuler`  三个包的安装，并解决相关的依赖，但即使安装过程没有任何问题，在使用 `library(venneuler)`  后上面提到的问题依然会出现。

`conda`  环境中  `openjdk` 、 `r-rjava` 、 `r-venneuler`  都可以安装成功，但就是用不了，这是我当前遇到的问题，暂时没找到解决方法。

## 解决

抛弃了 conda 后，用最原始的方法，终于可以解决这个问题，下面是记录。

### 1. 安装二进制的 java

在  <http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html>  下载  [jdk-7u80-linux-x64.tar.gz](https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html#license-lightbox)，解压缩。

```bash
$ tar zvxf jdk-7u80-linux-x64.tar.gz
$ mv jdk1.7.0_80 /usr/local/software
```

### 2. Java 环境配置

把下面的内容添加到 `~/.bashrc`  最后， `source ~/.bashrc`  执行环境变量更新。

```bash
export PATH=/usr/local/software/jdk1.7.0_80/bin:$PATH
export JAVA_HOME=/usr/local/software/jdk1.7.0_80
export JRE_HOME=/usr/local/software/jdk1.7.0_80/jre
export LD_LIBRARY_PATH=/usr/local/software/jdk1.7.0_80/lib/amd64:/usr/local/software/jdk1.7.0_80/jre/lib/amd64:$LD_LIBRARY_PATH
```

### 3. 更新 R 的 java 配置

如果没有更新 R 语言的 `java`  支持配置，直接执行 ` isntall.packages(rJava)`  可能会引发以下问题：

```bash
checking whether JNI programs run... configure: error: Unable to run a simple JNI program.
Make sure you have configured R with Java support (see R documentation) and check config.log for failure reason.
```

所以，请使用下面的命令更新 R 语言的 java 支持配置：

```bash
$ /usr/local/software/miniconda3/bin/R CMD javareconf
Java interpreter : /usr/local/software/jdk1.7.0_80/jre/bin/java
Java version     : 1.7.0_80
Java home path   : /usr/local/software/jdk1.7.0_80
Java compiler    : /usr/local/software/jdk1.7.0_80/bin/javac
Java headers gen.: /usr/local/software/jdk1.7.0_80/bin/javah
Java archive tool: /usr/local/software/jdk1.7.0_80/bin/jar

trying to compile and link a JNI program
detected JNI cpp flags    : -I$(JAVA_HOME)/include -I$(JAVA_HOME)/include/linux
detected JNI linker flags : -L$(JAVA_HOME)/jre/lib/amd64/server -ljvm
x86_64-conda_cos6-linux-gnu-cc -I"/usr/local/software/miniconda3/lib/R/include" -DNDEBUG -I/usr/local/software/jdk1.7.0_80/include -I/usr/local/software/jdk1.7.0_80/include/linux  -DNDEBUG -D_FORTIFY_SOURCE=2 -O2 -isystem /usr/local/software/miniconda3/include -I/usr/local/software/miniconda3/include -Wl,-rpath-link,/usr/local/software/miniconda3/lib  -fpic  -march=nocona -mtune=haswell -ftree-vectorize -fPIC -fstack-protector-strong -fno-plt -O2 -ffunction-sections -pipe -isystem /usr/local/software/miniconda3/include -fdebug-prefix-map=/home/conda/feedstock_root/build_artifacts/r-base_1576190804673/work=/usr/local/src/conda/r-base-3.6.2 -fdebug-prefix-map=/usr/local/software/miniconda3=/usr/local/src/conda-prefix  -c conftest.c -o conftest.o
x86_64-conda_cos6-linux-gnu-cc -shared -L/usr/local/software/miniconda3/lib/R/lib -Wl,-O2 -Wl,--sort-common -Wl,--as-needed -Wl,-z,relro -Wl,-z,now -Wl,--disable-new-dtags -Wl,--gc-sections -Wl,-rpath,/usr/local/software/miniconda3/lib -Wl,-rpath-link,/usr/local/software/miniconda3/lib -L/usr/local/software/miniconda3/lib -Wl,-rpath-link,/usr/local/software/miniconda3/lib -o conftest.so conftest.o -L/usr/local/software/jdk1.7.0_80/jre/lib/amd64/server -ljvm -L/usr/local/software/miniconda3/lib/R/lib -lR


JAVA_HOME        : /usr/local/software/jdk1.7.0_80
Java library path: $(JAVA_HOME)/jre/lib/amd64/server
JNI cpp flags    : -I$(JAVA_HOME)/include -I$(JAVA_HOME)/include/linux
JNI linker flags : -L$(JAVA_HOME)/jre/lib/amd64/server -ljvm
Updating Java configuration in /usr/local/software/miniconda3/lib/R
Done.
```

### 4. 安装 rJava 和  venneuler

上面的步骤完成后，在 R 中使用 `install.packages("rJava")`  和 `install.packages("venneuler")` ，发现一切正常。

## 后话

这篇文章与其是说在填坑，其实就是 `venneuler`  安装的一个记录，也是对在 `conda`  中对不再更新的旧版本 R 包的一次安装经历，希望这篇文章对 JAVA 不是很了解，但又想要安装与之相关的一些 R 包的人有所启发。或者你有更好的解决方法，也欢迎留言交流。

## 资料

1.  [venneuler: Venn and Euler Diagrams](https://cran.r-project.org/web/packages/venneuler/index.html)
2.  [UpSetR - Basic ](https://cran.r-project.org/web/packages/UpSetR/vignettes/basic.usage.html)
3.  [UpSetR：多数据集绘图可视化处理利器](https://mp.weixin.qq.com/s/SOOcQxQrj23GqYaO-lTCig)

![comment.gif](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlMO8jnjfaW7QalT7nyPkxQ4d37w.gif)
