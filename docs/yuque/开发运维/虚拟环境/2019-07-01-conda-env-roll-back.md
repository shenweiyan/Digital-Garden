---
title: 让你的 conda 回滚 到以前版本的环境
urlname: 2019-07-01-conda-env-roll-back
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 10:38:44"
---

我现在使用 Anaconda 作为我的主要 Python 发行版，同样，我们公司也将它用于所有开发人员机器以及他们的服务器。然而，前几天我在浏览一些论坛技术文章时遇到了一个我以前从未知道的 conda 精彩功能——conda 版本回滚！在这里给大家分享一下。

举一个最简单的例子。如果我们运行 `conda list --revisions` ，我们会得到这样的输出：

```shell
$ conda list --revisions
2018-04-03 09:26:14  (rev 0)
    +_ipyw_jlab_nb_ext_conf-0.1.0
    +alabaster-0.7.10
    +anaconda-5.1.0
    +anaconda-client-1.6.9
     ...
2018-04-03 09:30:48  (rev 1)
     anaconda  {5.1.0 -> custom}
     ca-certificates  {2017.08.26 -> 2018.03.07}
     cairo  {1.14.12 -> 1.12.18}
     fontconfig  {2.12.4 -> 2.11.1}
     freetype  {2.8 -> 2.5.5}
     harfbuzz  {1.7.4 -> 0.9.39}
     icu  {58.2 -> 54.1}
     ...

...

2019-02-14 11:48:21  (rev 36)
     _r-mutex  {1.0.0 -> 1.0.0}
     blas  {1.1 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge) -> 1.0 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main)}
     cairo  {1.14.12 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main) -> 1.14.12 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main)}
     conda  {4.5.11 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge) -> 4.6.3 (https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge)}
     ...
```

在上面的输出中，我们可以看到我的 conda 环境的许多特定版本（或修订版），以及它们的创建日期/时间以及差异（已安装的软件包显示为 `+` ，已卸载的显示为 `-`  和升级的显示为 `->` ）。 如果要恢复到以前的版本，只需运行 `conda install --revision N` （其中 N 是修订号）即可。 这将要求你确认相关的软件包卸载/安装，并让您回到原来的位置！

所以，我认为这非常棒！如果你搞砸了，想要回到以前的工作环境，真的很方便。

首先，如果你“恢复”到之前的修订版，那么你会发现创建了一个“逆”修订版，只是做了与之前修订版相反的版本。例如，如果您的修订列表如下所示：

```shell
2019-01-14 21:12:34  (rev 1)
    +mkl-11.3.3
    +numpy-1.11.0
    +pandas-0.18.1
    +python-dateutil-2.5.3
    +pytz-2016.4
    +six-1.10.0

2019-01-14 21:13:08  (rev 2)
    +cycler-0.10.0
    +freetype-2.6.3
    +libpng-1.6.22
    +matplotlib-1.5.1
    +pyparsing-2.1.4
```

接着，通过运行 `conda install --revision 1`  恢复到修订版 1，然后再次运行 `conda list --revisions` ，你会得到：

```shell
2019-01-14 21:13:08 (rev 2)
    +cycler-0.10.0
    +freetype-2.6.3
    +libpng-1.6.22
    +matplotlib-1.5.1
    +pyparsing-2.1.4

2019-01-14 21:15:45 (rev 3)
    -cycler-0.10.0
    -freetype-2.6.3
    -libpng-1.6.22
    -matplotlib-1.5.1
    -pyparsing-2.1.4
```

我们可以看到修订版 3 的更改只是修订版 2 的反转。

还有一点是我发现所有这些数据都存储在环境的 conda-meta 目录中的历史文件中（默认环境对应于  `CONDA_ROOT/conda-meta` ；其他环境对应于  `CONDA_ROOT/envs/ENV_NAME/conda-meta`）。你不想知道为什么我去搜索这个文件（这是一个长篇故事，涉及我的一些愚蠢），但它有一些非常有用的内容：

```shell
$ less /usr/local/software/anaconda3/conda-meta/history
==> 2018-04-10 16:15:45 <==
# cmd: /usr/local/software/anaconda3/bin/conda install netcdf4
+defaults::hdf4-4.2.13-h3ca952b_2
+defaults::libnetcdf-4.4.1.1-h816af47_8
+defaults::netcdf4-1.3.1-py36hfd655bd_2
# update specs: ['netcdf4']
==> 2018-04-11 11:50:02 <==
# cmd: /usr/local/software/anaconda3/bin/conda install r-cairo
+defaults::r-cairo-1.5_9-r342hbf22089_0
# update specs: ['r-cairo']
==> 2018-04-11 13:41:09 <==
# cmd: /usr/local/software/anaconda3/bin/conda remove R
-defaults::r-3.4.2-h65d9972_0
# remove specs: ['r']
......
```

具体来说，它不仅仅提供已安装，卸载或升级的列表，它还为您提供了运行的命令！ 如果需要，可以使用一些命令行魔法来提取这些命令：

```shell
# 获取历史文件的内容，搜索以#cm开头的所有行，然后按空格分割行并从第3组开始提取所有内容
$ cat /usr/local/software/anaconda3/conda-meta/history | grep '# cmd' | cut -d" " -f3-

/usr/local/software/anaconda3/bin/conda update -n base conda
/usr/local/software/anaconda3/bin/conda install -c bioconda r-plotrix --only-deps
/usr/local/software/anaconda3/bin/conda install r=3.4.2
/usr/local/software/anaconda3/bin/conda install gcc_linux-64
/usr/local/software/anaconda3/bin/conda install -c conda-forge ggplot --no-deps
/usr/local/software/anaconda3/bin/conda install -c r r-essentials
/usr/local/software/anaconda3/bin/conda install netcdf4
/usr/local/software/anaconda3/bin/conda install r-cairo
/usr/local/software/anaconda3/bin/conda remove R
/usr/local/software/anaconda3/bin/conda remove -c r r-essentials
/usr/local/software/anaconda3/bin/conda install altair --channel conda-forge
/usr/local/software/anaconda3/bin/conda install r-essentials
/usr/local/software/anaconda3/bin/conda install -c r r-essentials
......
```

最后，我发现 environment.yml 文件有时会有点痛苦（它们并不总是跨平台兼容 - 请参阅 [anaconda-issues: 546](https://github.com/ContinuumIO/anaconda-issues/issues/546)）， 所以通过 `conda install --revision N`   实现 conda 回滚非常有用，因为它实际上给了我运行创建环境的命令。
