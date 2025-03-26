---
title: Vim 使用的一些小技巧
urlname: 2019-05-18-how-to-use-vim
author: 章鱼猫先生
date: 2019-05-18
updated: "2023-04-26 15:06:00"
---

# vim 常用小技巧

vim 操作中常用的一些小技巧总结。

## tab 分隔文件列对齐

```bash
:%!column -t
```

## vim 字体颜色看不清

```bash
# Ubuntu 中设置(在 /etc/vim/vimrc 中加入）
set background=dark

# CentOS 中设置(在 /etc/vimrc 最后一行加入)
hi Comment ctermfg = blue  //更改vi中注释内容字体颜色，可修改为：white、darkyellow、blue 等
```

修改前：
![ubuntu_vim_1.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj1HL8vk95C0qdSKZn7zuAe1qjl6.png)

修改后：
![ubuntu_vim_2.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvVDq6tpUUD6gjENp_Rxv9SAZv_P.png)

## 撤消 vim 中的更改

vim 会跟踪您在当前会话中所做的所有更改。要撤消 vi 和 vim 中的更改，可以使用  `u`，`:u`  或  `:undo`  命令令：

- 如果当前 vi/vim 处于插入或其他任何模式，可以按  `Esc`  键盘返回到正常模式，也称为命令模式。

- 键入  `u`  撤销上一次更改。在 vim 中，`u`  命令还接受量词。例如，如果要撤消最后 4 个更改，则可以使用  `4u`。
  确保您输入的是小写的  `u`，而不是大写的  `U`  命令，大写的 `U` 会撤消一行中所有的最新更改。

- `undo`  命令用来恢复其他命令所做的更改，例如删除，粘贴，搜索和替换等。

- 在插入模式下工作时，对文本的所有更改都被视为撤消树中的一项。例如，如果你切换到插入模式并输入五行，然后返回普通模式并按 u 撤消更改，则所有五行都将被删除。

## 恢复 vim 中的更改

恢复（重做）功能可撤消撤消操作。恢复（重做）vi 和 vim 中的更改，可以使用  `Ctrl+R`  或  `:redo`：

- 按 `Esc`  键返回到正常模式，即命令行模式。

- 使用 `Ctrl+R`  键（按住 `Ctrl`  键并按 `r`  键）可恢复（重做）上一次更改。在 vim 中，您也可以使用量词。例如，如果要重做最近的 4 个更改，则可以键入 `4+Ctrl+R` 。

- 每个撤消命令都可以由恢复（重做）命令撤消。

# 参考资料

1.  等会再说，《[如何在 Vi/Vim 中进行撤消和重做操作](https://www.jianshu.com/p/6cc7278a6d50)》，简书
