---
title: LEfSe 分析软件安装小记
urlname: 2019-05-18-kefse-install
author: 章鱼猫先生
date: 2019-05-18
updated: "2021-10-31 10:37:47"
---

## 问题

源码下载的 LEfSe，或者使用 `conda install -c bioconda lefse` 安装完成后，执行分析出现报错：

```bash
$ lefse-format_input.py hmp_aerobiosis_small.txt hmp_aerobiosis_small.in -c 1 -s 2 -u 3 -o 1000000

$ run_lefse.py hmp_aerobiosis_small.in hmp_aerobiosis_small.res
Number of significantly discriminative features: 51 ( 131 ) before internal wilcoxon
Number of discriminative features with abs LDA score > 2.0 : 51

$ lefse-plot_res.py hmp_aerobiosis_small.res hmp_aerobiosis_small.png
Traceback (most recent call last):
  File "/Bio/home/shenweiyan/software/Anaconda2/bin/lefse-plot_res.py", line 177, in <module>
    else: plot_histo_hor(params['output_file'],params,data,len(data['cls']) == 2,params['report_features'])
  File "/Bio/home/shenweiyan/software/Anaconda2/bin/lefse-plot_res.py", line 70, in plot_histo_hor
    ax = fig.add_subplot(111,frame_on=False,axis_bgcolor=params['back_color'])
  File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/matplotlib/figure.py", line 1239, in add_subplot
    a = subplot_class_factory(projection_class)(self, *args, **kwargs)
  File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/matplotlib/axes/_subplots.py", line 77, in __init__
    self._axes_class.__init__(self, fig, self.figbox, **kwargs)
  File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/matplotlib/axes/_base.py", line 539, in __init__
    self.update(kwargs)
  File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/matplotlib/artist.py", line 888, in update
    for k, v in props.items()]
  File "/Bio/home/shenweiyan/software/Anaconda2/lib/python2.7/site-packages/matplotlib/artist.py", line 881, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property axis_bgcolor
```

## 原因

出现报错主要原因是 matplotlib==2.2.0 起把部分功能函数移除了，我们需要回退 matplotlib 版本。

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsFXTJemjeJR4BJp87MySIjsQ4JN.png)

    $ python
    Python 2.7.15 |Anaconda custom (64-bit)| (default, May  1 2018, 23:32:55)
    [GCC 7.2.0] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import matplotlib
    >>> matplotlib.__version__
    '2.2.2'
    >>>

## 解决

```shell
$ pip install matplotlib==1.5  #注意不要用conda, 以免发生环境conflicts
```

## 重新测试

    $ wget http://huttenhower.sph.harvard.edu/webfm_send/129 -O hmp_aerobiosis_small.txt

    $ format_input.py hmp_aerobiosis_small.txt hmp_aerobiosis_small.in -c 1 -s 2 -u 3 -o 1000000

    $ run_lefse.py hmp_aerobiosis_small.in hmp_aerobiosis_small.res

    $ plot_res.py hmp_aerobiosis_small.res hmp_aerobiosis_small.png

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqsG3Z4pUugvj6p3BDyw1vPL3G8T.png)

问题解决！
