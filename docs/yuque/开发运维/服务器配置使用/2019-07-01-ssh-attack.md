---
title: 一次 SSH 攻击与处理记录
urlname: 2019-07-01-ssh-attack
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 11:05:52"
---

这是我在简书看到的一个作者经历，结合小编自己的一些实践，抛砖引玉，给大家分享一下。

有段时间发现集群异常卡顿。担心的事情终于发生了，使用命令 `lastb` 查看了一下，我的天呢，好多未知的 IP，我随便复制粘贴了一个到百度查询了一下，我日，美国的。后来还在网上的 IP 黑名单中发现了攻击我们服务器的 IP。下面是从发现到解决的一个过程。

# 一、查看记录错误登录的日志

**/var/log/btmp** 文件是记录错误登录的日志，就是说有很多人试图使用密码字典登录 ssh 服务，此日志需要使用 lastb 程序打开。

`lastb` 查看的是 /var/log/btmp 中的内容，而 /var/log/btmp 是一个二进制的文件；
`last` 查看的是 /var/log/wtmp 中的内容，而  /var/log/wtmp 也是一个二进制的文件；
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FheZchvExI1ORbh4j8LVpue1Kv0X.png)

东北大学收集的发动 SSH 攻击的 IP 地址列表：<http://antivirus.neu.edu.cn/scan/ssh.php>

我们可以简单统计 ip 出现的次数，然后针对这些 ip 进行处理：
`blastb | awk '{print $3}' |sort |uniq -c |sort -k 1 -n -r |head -20`

# 二、处理 /var/log/secure

**/var/log/secure** 一般用来记录安全相关的信息，记录最多的是哪些用户登录服务器的相关日志，如果该文件很大，说明有人在破解你的 root 密码。

# 三、处理 SSH 攻击的基本流程

**首先，查看我们的服务器是否存在 SSH 攻击。**

- 步骤一：使用命令 lastb -20 查看，如果有大量的未知 IP, 加上时间分析。极短时间内出现多次，则可以确定受到 SSH 攻击。
- 步骤二：查看登陆失败的用户 IP，读取 /var/log/secure，查找关键字 Failed，如果是 SSH 攻击，会有很多的 IP 被列出来。

```bash
cat /var/log/secure | grep 'Failed password'
```

**其次，对目标 IP 进行黑白名单处理。**

在上面步骤一、步骤二的基础上我们开始编写脚本，检测多次尝试错误登陆的 IP，将那些有问题 IP 存放到 hosts.deny 黑名单下，并通过 crontab 来每分钟定时执行执行。

- **/etc/hosts.allow**，这个文件是存放允许访问服务器的所有 IP 的内容，可以简单理解为白名单；
- **/etc/hosts.deny**，这个文件存放的是不允许访问服务器的 IP 内容，简单理解为黑名单。

① 创建存放实施攻击的 ip 的文本，命名为：denyhosts.txt（`/root/denyhosts/denyhosts.txt`）。
② 创建定时脚本文件，命名为：denyhosts.sh（`/root/denyhosts/denyhosts.sh`）。

```bash
#!/bin/bash

cat /var/log/secure|awk '/Failed/{print $(NF-3)}'|sort|uniq -c|awk '{print $2"=" $1;}' >/root/denyhosts/denyhosts.txt

DEFINE="5"

for i in `cat /root/denyhosts/denyhosts.txt`
do
	  IP=`echo $i|awk -F '=' '{print $1}'`
    NUM=`echo $i|awk -F '=' '{print $2}'`
    if [ $NUM -gt $DEFINE ];then
				ipExists=`grep $IP /etc/hosts.deny |grep -v grep |wc -l`
        if [ $ipExists -lt 1 ];then
            echo "sshd:$IP" >> /etc/hosts.deny
        fi
    fi
done
```

③ 脚本创建好之后，将脚本的权限更改为可执行权限： `chmod a+x denyhosts.sh` 。
④ SSH 攻击是每时每刻都在发动攻击的，所以我们需要将脚本添加到定时任务中，定时的执行：

```bash
cat /etc/crontab # 这个文本是存放定时脚本的文本
```

⑤ 将脚本添加到定时任务：

```bash
crontab -e

# 每分钟执行一次，执行用户是 root 执行的脚本是 /root/denyhosts/denyhosts.sh
* * * * * root /root/denyhosts/denyhosts.sh
```

⑥ 查看是否将脚本添加到定时任务：**crontab -l**，如果出现我们的定时执行任务，则添加成功；后期如果需要删除此定时任务的话，通过：**crontab -r** 取消。

⑦ 使用命令  **lastb -20** (查看尝试登录我们服务器，但是登陆失败的 IP)，成功的看到，那些之前一秒钟发动几十次攻击的 IP 不存在了。

- 原因一是：脚本对 IP 进行筛选之后，将识别为攻击者 IP 的，都放入了黑名单中；
- 原因二是：如果攻击者尝试用别的新的 IP ，也就是没有被写入到黑名单的 IP， 我们的脚本再次检测，将这些新的攻击 IP 也写入黑名单。这样，攻击者的 IP 会越来越少。

除此之外，简单的办法就是改端口，ssh 攻击大部分都是批量扫 22 的，改了端口再改个不常用用户名和密码基本就没问题了，不知道大神还有没有更好的方式了！

**原文**：昵称又重复，《SSH 攻击》，<https://www.jianshu.com/p/84d38d396629>，简书
