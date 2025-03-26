---
title: Windows/Linux 下功能强大的桌面截图软件
urlname: 2021-02-26-flameshot
author: 章鱼猫先生
date: 2021-02-26
updated: "2021-06-25 10:47:00"
---

![SeventeenSolstice_ZH-CN4901756341_1920x1080.jpg](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoeC6XEfbiPhkCNcLhbfNxxTH1Sq.jpeg)
说到桌面截图软件，很多人首先想到的是 QQ 自带的截图，或者更高级功能更强大的 [Snipaste](https://zh.snipaste.com/index.html) 截图工具。

独立版本的 QQ 截图至少我目前没找到官方正式的下载链接，默认需要安装和打开 QQ 才能使用，而且貌似只能在 windows 下使用。功能强悍的 [Snipaste](https://zh.snipaste.com/index.html) 目前主要支持 windows，Mac 版本的正在公测中，不支持其他 Linux 平台的使用。

今天给大家推荐一款开源的功能很强的桌面截图软件：[Flameshot](https://flameshot.org/)，它可以同时支持 Windows 和 Linux 平台。

- 官网：<https://flameshot.org/>
- GitHub：<https://github.com/flameshot-org/flameshot>

![flameshot.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fgt4g16Y5EfpRv7yeDJG9f_XyZxB.png)

## 介绍

Flameshot 是一个 Linux 发行版中完全免费且开源的截图工具。Flameshot 简单易用并有一个 CLI 版本，所以你也可以从命令行来进行截图。

通常 Linux 发行版中会默认自带一个截图工具，但功能有限，往往只能单纯的截图截屏，无法完成对截图的编辑、涂画、标记文本等功能。Flameshot 强大之处在于它不仅能截图，更能对截图进行充分的编辑、涂画、标记、具备的功能更强于 QQ 截图。

**Flameshot 自带一系列非常好的功能，例如：**
\*\*

- 可自定义各个功能对应的键盘快捷方式；
- 可以进行手写；
- 可以划直线；
- 可以画长方形或者圆形框；
- 可以进行长方形区域选择；
- 可以画箭头；
- 可以对要点进行标注；
- 可以添加文本；
- 可以对图片或者文字进行模糊处理；
- 可以展示图片的尺寸大小；
- 在编辑图片是可以进行撤销和重做操作；
- 可以将选择的东西复制到剪贴板；
- 可以保存选区；
- 可以离开截屏；
- 可以选择另一个 app 来打开图片；
- 可以上传图片到 imgur 网站；
- 可以将图片固定到桌面上；

看一下操作的的 GIF 动画效果：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Foic6dCPtIAi9EPi4HAqz8t3RL5a.gif)

## 安装与使用

[Flameshot](https://flameshot.org/) 的官网提供了各个平台下详细的安装说明，感兴趣的可以去看一下。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlexH89LMt__CyXH6CXHN9Sh6stW.png)
对于 Windows 用户，只要把安装包下载下来，解压，即可免安装直接使用。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq8Iu77GUYvXOenLJTbnJkv72_sw.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fii_zW_FFeCAwxbRGwdy93DoYYom.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrV8O0TUjxSY5pSt02clItBwP2qb.png)

## 快捷键

Frameshot 支持快捷键。在 Flameshot 的托盘图标上右击并点击 “配置” 窗口便可以看到在 GUI 模式下所有可用的设置。配置 →Shortcuts，即可看到所有快捷键的设置页面。下面是在 GUI 模式下可用的快捷键清单。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsrS8xsEgOk8h5_ez5bpqjYr9wMh.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpXUjZk1GAlTR-gwUGtzp790WGeh.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn-AAK8ffo1BsM3F25XU1lLctNwq.png)

## 高级用法

Flameshot 还有一些命令行选项，如通过一系列的命令行选项来延时截图和保存图片到自定义的路径；CLI configuration；Linux 对应发行版本高级使用配置，等等。这不一一列举，感兴趣的童鞋可以去官网或者 GitHub 研究折腾一下。

## 一句话

Flameshot 几乎拥有截屏的所有功能：添加注释、编辑图片、模糊处理，或者对要点做高亮等等功能。可以尝试一下它，相信你不会失望的。

## 获取软件

文章最后，小编把截止 2021-02-26（元宵节）前 flameshot 在 Windows 32/64、AppImage 的最新版本免安装包都打包好放在了云盘上，喜欢的童鞋欢迎关注 **"BioIT 爱好者"** 公众号，后台回复\*\* "截图"\*\* 关键字，即可获取。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmv1rwSShbT0qC6EAXj_ImLTuQrz.png)
