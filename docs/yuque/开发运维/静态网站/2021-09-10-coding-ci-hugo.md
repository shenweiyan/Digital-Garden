---
title: 使用腾讯 CODING 托管并自动部署 Hugo 网站
urlname: 2021-09-10-coding-ci-hugo
author: 章鱼猫先生
date: 2021-09-10
updated: "2022-11-25 09:51:15"
---

一直以来，个人的很多应用站点，包括博客、[MDX](https://mdx.ncbix.com/)、[BioIT 网址导航](https://nav.bioitee.com/)等，都托管和部署在了 Coding 上，而且用的基本都是网站托管服务中的\*\*"静态网站"\*\*（coding 新建网站没有 hugo 可以勾选）!
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjVWtCmj3d3WXbpDpipsRB_DFoyj.png)

自己平时懒得去管主机的各种服务之类的，主机（尤其是云主机）在部署 Hugo 用的最多的是：

1.  使用 hugo 来生成站点的静态网站文件；
2.  把静态网站文件 push 到 coding，通过 coding 的静态网站服务进行自动部署。

今天，来解锁 coding 上的一个 **"持续集成"** 功能，通过它自动进行托管并部署 Hugo 网站（从此再也不用依赖主机了）。

# CODING 和腾讯云关联

这边要打通两边，做一个关联，详细就不多说了，折腾一下都 OK 的。

# 创建项目

做了上面的事情后，你应该会有一个团队主体，然后用这个团队主体创建一个项目。
![随便选一个都行，我是选的左边那个](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsF7wQieptdwXWCg8HudF80WMsGU.png "随便选一个都行，我是选的左边那个")
![填写项目信息](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrH79T4lvPe5axS6K7RhbTNQfqfw.png "填写项目信息")

# 创建两个仓库

创建项目成功后进入项目。创建两个仓库，一个是存储源代码的文件，一个是放置生成的静态网站文件。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvFrvgpIZ1cd7YDIUdNb5YuyoMxa.png)

# 流程配置

创建完网站后，在左边导航栏选择"持续集成"→"构建计划"，选择自定义构建过程。
![创建构建计划](https://shub.weiyan.tech/yuque/elog-cookbook-img/FulUKaBrExOaVESrmSpGYf5fcawl.png "创建构建计划")
![选择自定义构建过程](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoBKzV74UZ8QFJX2cvW0XN4nCk_L.png "选择自定义构建过程")
![设置自定义构建过程的代码源：CODING](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fl-jUXVMs2wZDvZPDbmmlXw0YueS.png "设置自定义构建过程的代码源：CODING")

在自定义构建过程中点击确定后，进入创建构建计划设置——流程配置。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fi0zTbvYw0lj0nTieZtLi08Amush.png)

## 代码检出

代码检出保持原有的就可以，不用去设置什么。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmXxmg5h2KeGV-x_uGxPLS_WX1A2.png)

## 执行 Hugo 构建

定义 2-1 步骤名称（我这里命名为：执行 Hugo 构建）。
![定义 2-1 步骤名称](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsM9PBVjuKDWUHQvSktMouBBq2Ye.png "定义 2-1 步骤名称")
![设置 2-1 步骤日志消息](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnJ36cZbpMl4UPwtvKLtvUVnxETi.png "设置 2-1 步骤日志消息")
![打印消息后，添加执行 Shell 脚本命令](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpbbjiiKDYj4NTH-krYCmP0xDhun.png "打印消息后，添加执行 Shell 脚本命令")
![配置具体的 Shell 脚本命令](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrOx5v_P1CH9f99Jz6pDJdV0TPTs.png "配置具体的 Shell 脚本命令")

```bash
# 这一步是下载 hugo 的执行程序，我是放在了 coding 的制品里面了；
# 外网下载好像速度有点慢，可以修改成其他版本或下载地址，下面需要对应修改文件名。
curl -fL "https://shenweiyan-generic.pkg.coding.net/btscl/tools/hugo_Linux-64bit.tar.gz?version=0.91.0" -o hugo_Linux-64bit-0.91.0.tar.gz

# 解压
tar -zvxf hugo_Linux-64bit-0.91.0.tar.gz
# 删除压缩包
rm -rf hugo_Linux-64bit-0.91.0.tar.gz

# 列出当前目录的文件
ls -hal

# 移动 hugo 到执行目录
mv hugo /usr/bin/hugo

# 由于前一步我们把代码检出了，所以我们目前是处于源代码目录下的；
# 执行 hugo 命令便可生成静态网站到 public 目录。
hugo -D
```

## 执行代码同步

点击"增加阶段"，增加一个"3-1 执行代码同步阶段"。

![执行代码同步，选择命令→执行 Shell 脚本](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqsOkFAwsFL-ljeLd7YW1xuBd7Ng.png "执行代码同步，选择命令→执行 Shell 脚本")

![执行代码同步，编辑执行的 Shell 脚本](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjoKwRRqJx9mmKcwnWk5bIjdUwOc.png "执行代码同步，编辑执行的 Shell 脚本")

```bash
# 进入到网站目录
cd ./public
# 初始化仓库
git init
# 绑定public仓库，这边是可以用默认变量token来代替认证
git remote add origin https://${CODING_USER}:${CODING_TOKEN}@e.coding.net/shenweiyan/webstack/nav.bioitee.pub.git
git add --all
git commit -m "执行自动更新"
# 强制推送内容
git push --force origin master
```

## 添加环境变量

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsBCf_Z6Uhycl_JKWSHcXuOLC8Sq.png)
**CODING_USER** 和 **CODING_TOKEN** 的环境变量可以通过下面的方法获取（如下截图），也可以直接使用你个人的用户名和密码。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlNz1I8HQlJB8ODp0p6-pTdh5Muh.png)
勾选以下权限：

- **project:depot**，读/写，完整的仓库控制权限；
- **project:file**，读/写，授权读取与操作文件；
- **project:deployment**，读/写，授权用户持续部署；
- **project:ci**，读/写，持续集成；

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtoOfFh7A3uHAdb6a-vlVvG2obuK.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsygEpCg4Bkoje3nsl-baLHdQYEL.png)

## 配置完成

配置完成后，点击保存。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn9EjsSoEzCrfaUTT9Vf_pKnxgLa.png)

# 立即构建

流程配置后立即构建，这个时候就会自动跑一遍这个流程了，基本上就完成了整个自动化构建部署。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fvc1rhb8Iqz2YPdpjfbHUoJZEmb_.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrYequZ3t2nIur7a3qwC5HROnCVF.png)

# 简单总结

最后说几句，这边要注意流程计划的触发规则为当代码源触发时自动执行，这样的话当你源代码仓库有更新时就会执行这个流程更新 public 仓库，而当 public 仓库发生改动时，你可以结合腾讯云的云开发 Webify 触发静态网站自动部署，具体的 Webify 操作可以参考《[腾讯云云开发 Webify 上手体验](https://www.yuque.com/shenweiyan/cookbook/webify-testing?view=doc_embed)》。
