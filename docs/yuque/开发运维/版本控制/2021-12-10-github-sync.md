---
title: GitHub 代码实时同步至国内 GIT 站点
urlname: 2021-12-10-github-sync
author: 章鱼猫先生
date: 2021-12-10
updated: "2024-01-15 16:12:07"
---

GitHub 是一个神奇而强大的社区，它作为全世界最大的代码集中地，在上面，我们可以随意地下载或者参与各种著名开源项目和开源开发框架。

**使用 GitHub 至少有以下几个好处：**

1. 获取最新最热门最实用的开源组件，有助于开发公司项目；
2. 获取最流行的技术相关源代码，有助于参考学习借鉴；
3. 参与感兴趣的开源项目，增强与他人协作开发的能力；
4. 创建属于自己的开源项目，提升编程能力，打造个人名片。

但由于一些大家都知道的原因，国内访问 GitHub 有时候会不太稳定，这就可能导致你在安装 GitHub 上的一些软件（或者拉取代码）的时候，由于网络问题而失败。这时候你就想：

1. 把代码同步一份到 gitee/coding/gitcode 等托管平台，从这些托管平台进行拉取下载；
2. 把代码同步一份到 gitee，使用 gitee 的网站托管/自动构建功能，实时部署你的站点应用。

虽然，gitee/coding/gitcode 等平台都提供了从 GitHub 导入项目和强制更新的选项（coding 还提供了可以**通过触发时间来自动同步**），但都比较繁琐，在这里介绍一种通过 GitHub Actions 的方法是一步实现 GitHub 代码实时同步 gitee/coding/gitcode 等。

## 使用秘钥的方式

**本方法主要基于 <https://github.com/Yikun/hub-mirror-action> 提供的 Actions 实现。**

### 1. 基于 SSH 配置公钥和私钥

这一步可以参考或网上N多资料，如《[生成/添加SSH公钥 -Gitee](https://help.gitee.com/enterprise/code-manage/%E6%9D%83%E9%99%90%E4%B8%8E%E8%AE%BE%E7%BD%AE/%E9%83%A8%E7%BD%B2%E5%85%AC%E9%92%A5%E7%AE%A1%E7%90%86/%E7%94%9F%E6%88%90%E6%88%96%E6%B7%BB%E5%8A%A0SSH%E5%85%AC%E9%92%A5)》。      
![ssh-keygen-ed25519](https://shub.weiyan.tech/kgarden/2024/01/ssh-keygen-ed25519.png)

### 2. 将私钥传到 GitHub 仓库

通过 "**Settings → Secrets and variables → Actions → New repository secret**"，创建一个 `GITEE_PRIVATE_KEY` 变量，将私钥(`~/.ssh/id_ed25519`)内容拷贝到值区域。     
![GITEE_PRIVATE_KEY](https://shub.weiyan.tech/kgarden/2024/01/gitee_private_key.png)

### 3. 将公钥传到 Gitee

我们只需要把公钥 `~/.ssh/id_ed25519.pub` 的内容，粘贴到 Gitee 即可。

这样一来，就可以实现 GitHub 和 Gitee 之间的通信。而对于不同的公钥配置，Github 可以在[这里](https://github.com/settings/keys)配置，Gitee 可以在[这里](https://gitee.com/profile/sshkeys)配置，对于 GitHub → Giee 我们只需要配置 Giee 上配置公钥即可。    
![ssh-pub-key](https://shub.weiyan.tech/kgarden/2024/01/ssh-pub-key.png)

### 4. 在 Gitee 上创建一个私人令牌

这个 token 记得保存，因为它只会出现一次。     
![gitee-token](https://shub.weiyan.tech/kgarden/2024/01/gitee-token.png)

### 5. GitHub 目标仓库粘贴 Gitee 私人令牌

类似第 2 步，我们在想要同步到 Gitee 的 GitHub 源仓库中创建一个 `GITEE_TOKEN` 变量，将第 4 步生成的私人令牌作为值粘贴进去。     
![add-gitee-token](https://shub.weiyan.tech/kgarden/2024/01/add-gitee-token.png)

### 6. 修改配置文件中的源和目标设置

最后，我们将配置文件中的源和目标设置为你自己的账号即可。
```
src: github/<这里改成自己的GitHub名字>
dst: gitee/<这里改成自己的Gitee名字>
```

这样配置就完成了。提交你的修改，GitHub Action 就会开始启动并工作了。

> **注意**：     
> [**Hub Mirror Action**](https://github.com/Yikun/hub-mirror-action) 默认会同步你个人账号(或者组织) 下的全部仓库，如果你只想同步当前一个仓库，可以参考 [**黑/白名单**](https://github.com/Yikun/hub-mirror-action?tab=readme-ov-file#%E9%BB%91%E7%99%BD%E5%90%8D%E5%8D%95) 和 [**静态名单（可用于单一仓库同步）**](https://github.com/Yikun/hub-mirror-action?tab=readme-ov-file#%E9%9D%99%E6%80%81%E5%90%8D%E5%8D%95%E5%8F%AF%E7%94%A8%E4%BA%8E%E5%8D%95%E4%B8%80%E4%BB%93%E5%BA%93%E5%90%8C%E6%AD%A5) 的配置。

## 使用账号密码的方式

这个方法参考的是 [@abersheeran](https://github.com/abersheeran) 的 [push-to-mirror ](https://github.com/abersheeran/index.py/blob/a9ef1e2dca0c975108b942657679ec47908c7bcc/.github/workflows/setup.yml#L55-L82)方法，可以同步到 gitee 以及任何一个支持 git 的平台，其原理很简单，就拉取然后推送。

从 2024-01 起，发现通过这种方法同步到 gitee，会提示 `Connection timed out`，但是同步 GitCode.com 是正常的，目前暂时没找到解决方法。     
![sync-gitee Connection timed out](https://shub.weiyan.tech/kgarden/2024/01/sync-gitee-time-out.png)


### 配置账号密码

首先，在 GitHub 项目的「**Settings** -> **Secrets** → **New repository secret**」路径下配置好你需要同步的 coding 和 gitee 账号密码（命名可以随便，只要求跟下面 **sync.yml** 的变量名称一致即可）。其中：

- **GITEE_USERNAME** 存放 **Gitee 的账号**；
- **GITEE_PASSWORD** 存放 **Gitee** **帐号的密码**；
- **CODING_USERNAME** 存放 **Coding 的账号**；
- **CODING_PASSWORD** 存放 **Coding** **帐号的密码**；

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsW8HjkaxCtwI0YVC4DHrFPceXmD.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrllDsG6dnVD9N553JIP4a1GVOZA.png)

### 创建 workflow

在你的 GitHub 项目 **.github/workflows/** 文件夹下创建一个 `.yml` 文件，如 **sync.yml**，内容如下：

```yaml
name: Sync-To-Gitee-and-Coding

on:
  push:
    branches:
      - main

jobs:
  push-to-mirror:
    runs-on: ubuntu-latest
    steps:
      - name: Clone
        run: |
          git init
          git remote add origin https://github.com/${GITHUB_REPOSITORY}.git
          git fetch --all
          for branch in `git branch -a | grep remotes | grep -v HEAD`; do
            git branch --track ${branch##*/} $branch
          done
        env:
          GITHUB_REPOSITORY: shenweiyan/GitHub-SYNC

      - name: Push to Coding
        run: |
          remote_repo="https://${CODING_USERNAME}:${CODING_PASSWORD}@e.coding.net/${CODING_REPOSITORY}.git"

          git remote add coding "${remote_repo}"
          git show-ref # useful for debugging
          git branch --verbose

          # publish all
          git push --all --force coding
          git push --tags --force coding
        env:
          CODING_REPOSITORY: shenweiyan/devs/GitHub-SYNC
          CODING_USERNAME: ${{ secrets.CODING_USERNAME }}
          CODING_PASSWORD: ${{ secrets.CODING_PASSWORD }}

      - name: Push to Gitee
        run: |
          remote_repo="https://${GITEE_USERNAME}:${GITEE_PASSWORD}@gitee.com/${GITEE_REPOSITORY}.git"

          git remote add gitee "${remote_repo}"
          git show-ref # useful for debugging
          git branch --verbose

          # publish all
          git push --all --force gitee
          git push --tags --force gitee
        env:
          GITEE_REPOSITORY: shenweiyan/GitHub-SYNC
          GITEE_USERNAME: ${{ secrets.GITEE_USERNAME }}
          GITEE_PASSWORD: ${{ secrets.GITEE_PASSWORD }}
```

### 执行同步

最后，修改代码（如修改 README），提交，成功触发同步！
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnPI_f183sRTBRgB6Gh5bVbzJE7b.png)

![同步 workflows 执行成功！](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn7B-rFuN_RYsSuuraS0H7YpBx-f.png "同步 workflows 执行成功！")

![GitHub 代码同步 Coding 成功！](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqGnfZCiqR_Jd1EiWghqmztpcfe2.png "GitHub 代码同步 Coding 成功！")

![GitHub 代码同步 Gitee 成功！](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlfUfgGFbwojp08rLox4EwsFVP4d.png "GitHub 代码同步 Gitee 成功！")

## 总结

文章中参考前人的一些成果成功把 GitHub 的代码同步到了 gitee 和 coding，可能还有可以改进的地方，但不管怎么说，基本满足了个人的需求。

最后，GitHub 是一个非常棒的平台，希望大家拥抱开源，多多分享。
