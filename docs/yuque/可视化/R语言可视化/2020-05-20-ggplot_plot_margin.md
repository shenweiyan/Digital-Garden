---
title: ggplot2 调整绘图区域大小
urlname: 2020-05-20-ggplot_plot_margin
author: 章鱼猫先生
date: 2020-05-20
updated: "2021-10-03 08:38:03"
---

熟悉 R 绘图的朋友肯定知道，在普通绘图中，图片的大小可以直接在 `png()`  和 `pdf()`  中指定，而绘图区大小则可以用 `par()`  中的 `mar`  或 `mai`  来指定。

但是在 ggplot2 中，图片大小依然可以在 `png`  和 `pdf`  中设定，但是边界大小， `par`  函数似乎就不奏效了。至今天探索，才发现原来这个参数隐藏在 `theme`  中，其名为 `plot.margin` 。

## 1. 原图

```r
library(ggplot2)
library(ggthemes)
p <- ggplot(mtcars, aes(mpg, wt)) + geom_point(aes(colour=factor(cyl))) + guides(color=F)
p <- p + theme_solarized(light=FALSE) + scale_colour_solarized('blue')
ggsave("test0.png", units="in", dpi=300, width=4, height=4, device="png")
```

![test0.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsVQvwY2GAZJJU8-Uc8wHbB001in.png)

## 2. 第一次调整边界参数

```r
library(ggplot2)
library(ggthemes)
p <- ggplot(mtcars, aes(mpg, wt)) + geom_point(aes(colour=factor(cyl))) + guides(color=F)
p <- p + theme_solarized(light=FALSE) + scale_colour_solarized('blue')
p <- p + theme(plot.margin=unit(rep(1,4),'lines'))
ggsave("test1.png", units="in", dpi=300, width=4, height=4, device="png")
```

![test1.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlT7xm5tQQjc489eE0zd9BaCBR2v.png)

## 3. 第二次调整边界参数

```r
library(ggplot2)
library(ggthemes)
p <- ggplot(mtcars, aes(mpg, wt)) + geom_point(aes(colour=factor(cyl))) + guides(color=F)
p <- p + theme_solarized(light=FALSE) + scale_colour_solarized('blue')
p <- p + theme(plot.margin=unit(rep(3,4),'lines'))
ggsave("test2.png", units="in", dpi=300, width=4, height=4, device="png")
```

![test3.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlHN-gS_YGQorvGsJYBcIPSteTs2.png)

比较上述 3 幅图片，可明显发现，随着边界参数值增大，绘图区与边界的距离不断增大，从而在图片上留出更多空白区域。

此外， `plot.margin`  是否跟 `par(mar=...)`  一样遵循下、左、上、右的控制顺序呢？各位可以敲下代码，稍稍一试。
