---
title: Linux 中多终端同步 history 记录
urlname: 2020-09-04-history-command
author: 章鱼猫先生
date: 2020-09-04
updated: "2021-06-25 10:54:31"
---

## 基本认识

Linux 默认配置是当打开一个 shell 终端后，执行的所有命令均不会写入到 `~/.bash_history`  文件中，只有当前用户退出后才会写入，这期间发生的所有命令其它终端是感知不到的。

## 问题场景

在网络上看到 2 个问题，有点意思：

假若之前 `history`  命令记录为 c0，用户先打开了 shell 终端 a，执行了一部分命令 c1，又打开了一个 shell 终端 b，又执行了一部分命令 c2。

- \*\*问题 1：\*\*终端 a 执行的这部分命令终端 b 上看不到。
- \*\*问题 2：\*\*终端 a 正常退出，相关命令会写入到 `~/.bash_history`  文件中（c1 命令也会写入，即 c0+c1），等到终端 b 正常退出后，相关命令也会写入到 `~/.bash_history`  文件中，注意这个时候终端 b 写入的内容为 c0+c2，也即 c1 记录会丢失！！！

问题 1 的确会出现！

但是问题 2 貌似不会出现，个人在 CentOS 7 中测试了一下，发现终端 a 正常退出，相关命令的确会写入到 `~/.bash_history`  文件中，即 c0+c1；但终端 b 也正常退出后，终端 b 的相关命令是会自动追加到 `~/.bash_history`  文件，这时候 `~/.bash_history`  的文件内容 = c0 + c1 + c2！造成这样的原因，刚开始以为是受 `/etc/bashrc`  的这一段配置的影响，后来把这两句注释，重新测试发现问题 2 貌似也不会出现。

```bash
# Turn on parallel history
shopt -s histappend
history -a
```

如果在多个打开的终端中实时同步 history（例如，如果我 ls 在一个终端中，切换到另一个已经运行的终端，然后按向上， `ls`  出现）的确也是有一定的使用需求，但真正的需求个人觉得更应该是这样的：

> **我可以看到多终端实时同步 history 的优点，但是就我个人而言，我会讨厌它。我通常在终端中打开 3 或 4 个选项卡以用于非常特定的用途：一个用于运行 “make”，一个用于 vi，一个用于运行东西，等等。因此，当我编译时，我转到选项卡 1，单击并显示 “make”。依此类推。这对我非常有帮助。因此，如果突然我进入我的 “make” 选项卡并点击弹出，并且出现一些随机的 grep 命令，我会很生气！**

所以，我们增加一个问题 3：当打开一个 shell 终端后，不管是正常退出还是非正常退出，执行的所有命令均实时追加到 `~/.bash_history`  文件中，但当前终端不会实时同步其他终端的 history，除非我重新开启了一个新终端。

## 解决方案

\*\*问题一：\*\*实时同步多个终端的 history 记录。

```bash
# Avoid duplicates
export HISTCONTROL=ignoredups:erasedups
# When the shell exits, append to the history file instead of overwriting it
shopt -s histappend

# After each command, append to the history file and reread it
export PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND$'\n'}history -a; history -c; history -r"
```

\*\*
\*\*问题二：\*\*多个终端执行的所有命令均实时追加到 `~/.bash_history`  文件中。

```bash
shopt -s histappend
PROMPT_COMMAND="history -a"
```

## 参数解析

贴上一些 history 的参数解析。
![linux-history.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsHkJsSu2sLuB8lqAkDbw2wP8IF2.png)

```
history [n]
history -c
history -d offset
history -anrw [filename]
history -p arg [arg ...]
history -s arg [arg ...]
       With no options, display the command history list with line numbers.  Lines listed with  a  *
       have  been  modified.   An  argument of n lists only the last n lines.  If the shell variable
       HISTTIMEFORMAT is set and not null, it is used as a format string for strftime(3) to  display
       the time stamp associated with each displayed history entry.  No intervening blank is printed
       between the formatted time stamp and the history line.  If filename is supplied, it  is  used
       as  the  name  of  the history file; if not, the value of HISTFILE is used.  Options, if sup‐
       plied, have the following meanings:
       -c     Clear the history list by deleting all the entries.
       -d offset
              Delete the history entry at position offset.
       -a     Append the ``new'' history lines (history lines entered since  the  beginning  of  the
              current bash session) to the history file.
       -n     Read the history lines not already read from the history file into the current history
              list.  These are lines appended to the history file since the beginning of the current
              bash session.
       -r     Read the contents of the history file and use them as the current history.
       -w     Write  the  current  history  to the history file, overwriting the history file's con‐
              tents.
       -p     Perform history substitution on the following args and display the result on the stan‐
              dard output.  Does not store the results in the history list.  Each arg must be quoted
              to disable normal history expansion.
       -s     Store the args in the history list as a single entry.  The last command in the history
              list is removed before the args are added.

       If  the  HISTTIMEFORMAT variable is set, the time stamp information associated with each his‐
       tory entry is written to the history file, marked with the history comment  character.   When
       the history file is read, lines beginning with the history comment character followed immedi‐
       ately by a digit are interpreted as timestamps for the previous  history  line.   The  return
       value  is 0 unless an invalid option is encountered, an error occurs while reading or writing
       the history file, an invalid offset is supplied as an argument to -d, or the  history  expan‐       sion supplied as an argument to -p fails.

```

## 常用配置

### 1. 设置历史记录的时间

```bash
export HISTTIMEFORMAT='%F %T '     # 注意有个空格, 这样在显示时日期与命令之间会有空格分隔
```

HISTTIMEFORMAT %F %T 代表意义：

- %F – expands to full date same, as %Y-%m-%d (year-month-date).
- %T – expands to time; same as %H:%M:%S (hour:minute:seconds).

### 2. 控制历史命令记录的总个数

```bash
export HISTSIZE=1000         # 设置内存中的history命令的个数
export HISTFILESIZE=1000     # 设置文件中的history命令的个数
```

简单说明：

- HISTFILESIZE：定义了在 `.bash_history`  中保存命令的记录总数，可以理解为 `.bash_history`  文件中最多只有 HISTFILESIZE 行。默认值是 500。
- HISTSIZE：定义了 `history`  命令输出的记录数，即输出 `.bash_history`  文件中的最后 HISTSIZE 行。默认值是 500。

\*\*
\*\*

### 3. 更换历史命令的存储位置

一般情况下，历史命令会被存储在 `~/.bash_history`  文件中。如果不想存储在这个文件中，而想存储在其他文件中，那么可以通过下面的方式来更改：

```bash
export HISTFILE=~/history.log
```

### 4. 其他个性化的配置

```bash
export HISTCONTROL=erasedups    # 清除整个命令历史中的重复条目
export HISTCONTROL=ignoredups   # 忽略记录命令历史中连续重复的命令
export HISTCONTROL=ignorespace  # 忽略记录空格开始的命令
export HISTCONTROL=ignoreboth   # 等价于ignoredups和ignorespace
```

## 尊重重要命令的隐私

以下内容节选自：编程帮《[history 命令 Linux history 命令：查看和执行历史命令](http://c.biancheng.net/linux/history.html)》。

> 试想一下，我们操作 Linux 系统，如果把所有的命令都记录到 .bash_history 中，会不会有风险呢？
>
> 当然有风险啦，如果哪一天我们不幸中招，黑客攻入了我们的系统，他只要查看一下 history 就能知道我们的很多秘密，比如一些登录密码。为了避免该类事情的发生，我们希望 history 不要显示含有隐私信息的历史命令，只显示不含有隐私信息的命令。这个需求太个性化，但 history 仍然能够实现，下面我们就为大家介绍两种行之有效的解决方案。
>
> 第一种靠谱的解决方案：
>
> - 第 1 步：设置 HISTCONTROL 环境变量：export HISTCONTROL=ignorespace。
> - 第 2 步：输入重要命令时，记得在输入命令前加上空格。
> - 第 3 步：执行 history，可以看到刚输入的重要命令没有出现在 history 中。
>
> 通过设置 HISTCONTROL=ignorespace，可以让 history 不记录你的特殊输入（命令前加空格），这样可以在一定程度上有效地保护我们的系统。
>
> 第二种靠谱的解决方案：
>
> - 第 1 步：设置 HISTIGNORE 环境变量 export HISTIGNORE=\*。
> - 第 2 步：输入重要命令，比如 mysql-uroot-p123。
> - 第 3 步：查看你的 history，可以看到刚输入的 mysql 命令没有记录在 history 中。
> - 第 4 步：恢复命令的记录 export HISTIGNORE=。
> - 第 4 步后，系统又恢复正常，输入的命令又能被正常记录了。
>
> 这个方法虽然略显烦琐，需要你每次在输入重要命令时都要先设置 HISTIGNORE=\*，执行完命令后再设置 HISTIGNORE=，但是，这种方法能规避由于你的粗心大意（忘记命令前加空格）带来的巨大安全隐患，确保机密信息不会被泄露出去。

## 参考资料

1.  脚本小娃子，《[linux 的 history 命令设置](https://www.cnblogs.com/shengulong/p/9034821.html)》，博客园
2.  toy，《[增强 Bash 的功能](https://linuxtoy.org/archives/bash_tricks.html)》，LINUXTOY 个人博客
3.  toy，《[History（历史）命令用法 15 例](https://linuxtoy.org/archives/history-command-usage-examples.html)》，LINUXTOY 个人博客
4.  明月 Alioo，《[Linux 多个会话同时执行命令后 history 记录不全的解决方案](https://blog.csdn.net/hl_java/article/details/80847488)》，CSDN
5.  whatday，《[linux shell 日志环境变量 HISTFILESIZE 和 HISTSIZE 的区别](https://blog.csdn.net/whatday/article/details/103537044)》，CSDN
6.  Unix & Linux，《[在多个终端窗口中保留 bash 历史记录](https://qastack.cn/unix/1288/preserve-bash-history-in-multiple-terminal-windows)》，QA Stack
7.  Tsung，《[Bash history 加上 日期和時間](https://blog.longwin.com.tw/2017/05/linux-bash-history-date-time-display-2017/)》，WordPress 个人博客
