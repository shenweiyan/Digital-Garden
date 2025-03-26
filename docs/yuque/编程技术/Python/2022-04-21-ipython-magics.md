---
title: IPython 内置魔法命令
urlname: 2022-04-21-ipython-magics
author: 章鱼猫先生
date: 2022-04-21
updated: "2023-09-06 11:09:50"
---

> **IPython 中有一些特有的魔法命令，如果能合理的利用这些魔法命令，会省去很多不必要的操作，为编程带来很大程度的便利，下面基于 IPytthon 官方的《[Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)》安利一下这些命令。**

> 本文档涵盖 IPython 6.0 及更高版本。 从 6.0 版开始，IPython 停止支持与低于 3.3 的 Python 版本的兼容性，包括所有 Python 2.7 版本。
> 如果您正在寻找与 Python 2.7 兼容的 IPython 版本，请使用 IPython 5.x LTS 版本并参考其文档（LTS 是长期支持版本）。


## 基础知识

### ? 和 ??

**例：%matplotlib?、%matplotlib??**
后缀为 ? 可以获取一个对象的相关信息，比如描述一个方法该怎么用；后缀为 ?? 可以获取该对象更加详细的信息，比如源码。这个对象可以是 IPython 中自带的、也可以是导入的、也可以是自己定义的。

### % 和 %%

**例：%time、%%time**
前缀为 % 被称作行魔法命令（line magics），只能在单个输入行上运行；前缀为 %% 被称作单元格魔法命令（cell magics），可以在多个输入行上运行。

更新中。。。

## 参考资料

1. 佚名，《[12 个常用的 IPython 魔法命令](https://developer.51cto.com/article/620863.html?pc)》，51CTO.COM
