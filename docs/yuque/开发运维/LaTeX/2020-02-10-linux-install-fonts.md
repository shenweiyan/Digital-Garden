---
title: Linux 字体安装
urlname: 2020-02-10-linux-install-fonts
author: 章鱼猫先生
date: 2020-02-10
updated: "2021-06-30 09:38:15"
---

在使用 LaTeX 进行中文字体编译排版过程中，发现 CentOS 6.5 中缺乏很大一部分中文字体，以至于在编译过程中频繁抛出缺乏字体的错误。现在基于 windows 的 ttf 字体，以 **“微软雅黑”** 体为例，简单记录一下 Linux 下如何安装 windows 字体。

1. 首先获得一套”微软雅黑”字体库( Google 去下载，或者去 `C:\Windows\Fonts` 下直接复制)，包含两个文件 msyh.ttf （普通）、 msyhbd.ttf （加粗）；

2. 在 `/usr/share/fonts` 目录下建立一个子目录，例如 `win` ，命令如下：

```bash
$ mkdir /usr/share/fonts/win
```

3. 将 `msyh.ttf` 和 `msyhbd.ttf` 复制到该目录下，例如这两个文件放在 `/home/shenweiyan` 下，使用命令：

```bash
$ cd /home/shenweiyan
$ cp msyh.ttf msyhbd.ttf  /usr/share/fonts/win/
```

4. 建立字体索引信息，更新字体缓存：

```bash
$ cd /usr/share/fonts/win
$ mkfontscale
$ mkfontdir
$ fc-cache
```

至此，字体已经安装完毕！如果想要查看本机器所安装的中文字体，可通过 `fc-list`  命令查看：

```bash
shenweiyan@localhost 14:23:19 ~
$ fc-list :lang=zh-cn
AR PL UMing TW:style=Light
AR PL UMing HK:style=Light
AR PL UMing CN:style=Light
Microsoft YaHei,微软雅黑:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
Microsoft YaHei UI,Microsoft YaHei UI Light:style=Light,Regular
AR PL UKai TW MBE:style=Book
AR PL UKai CN:style=Book
AR PL UKai HK:style=Book
AR PL UKai TW:style=Book
Microsoft YaHei UI:style=Regular,Normal,obyčejné,Standard,Κανονικά,Normaali,Normál,Normale,Standaard,Normalny,Обычный,Normálne,Navadno,Arrunta
Microsoft YaHei,微软雅黑,Microsoft YaHei Light,微软雅黑 Light:style=Light,Regular
WenQuanYi Zen Hei,文泉驛正黑,文泉驿正黑:style=Regular
Microsoft YaHei UI:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
Microsoft YaHei,微软雅黑:style=Bold,Negreta,tučné,fed,Fett,Έντονα,Negrita,Lihavoitu,Gras,Félkövér,Grassetto,Vet,Halvfet,Pogrubiony,Negrito,Полужирный,Fet,Kalın,Krepko,Lodia
WenQuanYi Zen Hei Mono,文泉驛等寬正黑,文泉驿等宽正黑:style=Regular
AR PL UMing TW MBE:style=Light
WenQuanYi Zen Hei Sharp,文泉驛點陣正黑,文泉驿点阵正黑:style=Regular
```
