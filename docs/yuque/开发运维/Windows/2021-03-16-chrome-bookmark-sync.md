---
title: 使用码云同步谷歌 Chrome 浏览器书签
urlname: 2021-03-16-chrome-bookmark-sync
author: 章鱼猫先生
date: 2021-03-16
updated: "2021-10-31 10:40:20"
---

由于东方的神秘力量，国内正常情况下是连不上 Google 账号的，所以平时使用 Chrome 经常会头疼书签同步问题。  由于魔法力量的不稳定，有时候不同步，有时还会同步错乱导致书签丢失。

针对这个问题，这两天尝试了一下微软最新版本的 Edge，不得不说 Edge 很多地方的确很符合国人的使用习惯，尤其无需梯子即可进行书签同步，真心香！但唯一有点坑的地方是对 Windows 7 的支持还不够友好。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq-j4BEB4RvNG-9M6KhQwbrader1.png)

虽然现在的 Edge 提供了 Windows 7 版本，但是安装过程中需要把 IE 升级到最新的 IE11，就算你好不容易把 IE11 升级好的，Edge 在获取更新说不定还会遇到其他更加难搞的事情。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FutF2Q-w_xQA6Rgqrg9l_8pOx5_l.png)

回到 Chrome，介绍一下这个偶然发现的插件：书签同步码云。这个工具可以把谷歌浏览器书签同步至码云
在国内码云平台是访问速度比较快的，平时用着也比较方便。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlGw7B1ONgoPE5Am-6qGduoZwf6H.png)

## 1. 安装插件

如果有条件用谷歌商店的可以直接去谷歌商店中搜索安装，当然也有同步在 Github 中的插件，也是类似，应用商店也可以找到。

如果无法使用谷歌商店，我上传到天翼云盘，有需要的可以关注\*\* "BioIT 爱好者\*\*" 公众号后台回复  **"码云书签"**  关键字，即可获取下载链接。
![BioIT爱好者-关注我们.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fv-cZ0ZzOktyc4yEFX5ZbF4bmuDu.png)
下载解压后，把里面 .crx 文件直接拖到浏览器，应该就可以加载，如果提示无效或者错误的话，可以把后缀名改成 .zip 或者 .rar，然后找个目录解压了，在打开开发者模式：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fhc01HNHYd1St5Pa9ygXSl33MZTe.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fjnuzft4rv7qokjehW_Wki4tRSIn.png)
然后点击加载已解压的扩展程序，选择你解压的目录，注意是目录，不是具体的文件，点击确定就可以，应该就可以见扩展程序页面的插件了，如下：

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvMmi6jN9_d4lUV-YNNiv7PsD1Tt.png)

插件打开长这样子：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fqx7H53yyGiOi4owahG3Jw5uDRuG.png)

## 2. 添加码云仓库使用

### 2.1 新建仓库

打开码云，新建仓库。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq_E6L7ye55ATBRaibFJxMKF-vbG.png)

### 2.2 填写插件信息

#### access_token

首先，在码云中点击设置：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvbKxQ7_fIo6JEGMqtZ5cdj92ntr.png)
第二，进去之后，点击  \*\*私人令牌 -> 生成新令牌  \*\*：![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjNLbebmjWmefwwMVJ4vJwfOn21b.png)
点击生成令牌之后，在页面中填写 **私人令牌描述**，下面权限要全选：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtDWM8LIZmn_yvxXuDreFPAUKR1v.png)
然后点击提交，会验证当前账户密码，验证之后会弹出令牌页面。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrZgi5FNlY2kLVAexyCTmcvSFUbx.png)

**注意：这个令牌只显示一次，建议复制保存到本地记事本或者其他地方之后再确认关闭！！！**
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrfA3dC9fhmWqUOCSXepC4ddRrom.png)
然后再将该该令牌复制到 插件的 access_token 位置就好。

#### owner

回到我们刚才创建的仓库，例如 <https://gitee.com/shenweiyan/bookmarks>，owner 就是 **shenweiyan**，把这个信息复制到插件的 owner 位置就好。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhEosdSBIm7aHJ6pGDWRoA6g_04C.png)

#### repo

以我们刚才创建的 <https://gitee.com/shenweiyan/bookmarks> 仓库为例，repo 就是 **bookmarks**，把这个信息复制到插件的 repo 位置就好。

#### path

注意，这里写的是相对 repo 仓库的 path 信息，如果你想直接把文件保存的仓库根目录，path 就可以写 chrome.html 或者 chrome.json，名称可以随便写，以 html/json 作为格式后缀即可。

#### branch

分支(通常是写 master)。

以 <https://gitee.com/shenweiyan/bookmarks> 仓库为例的最终插件信息如下：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpJgSdZUuC3VnMcn_LP1_gKgyghs.png)

## 3. 使用事项

注意，如果是第一次添加使用，在填写完信息之后，需要先在仓库中创建一个 path 的文件（例如，这里的 chrome.json，需要先创建）。

然后，直接点 Upload 把当前浏览器的书签上传到 gitee 仓库中。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjVMibJM6oV3_jjVc17oldMdwchp.png)
最后，就可以通过点击 Download 把云端（即仓库）的书签信息同步到其他电脑的当前浏览器。

:::success
**注意，注意，注意！！！**
如果是两个电脑用这个同步，建议先把当前浏览器的书签线导出到本地，因为这个 Download 会用云端（即仓库）的书签把当前浏览器（即本地）的书签**覆盖。如果直接把当前浏览器（即本地）的书签 Upload，则会把云端（即仓库）的书签覆盖。**
:::

我就是这么操作之后才知道，不过还好本地覆盖云端还有救，因为码云可以看历史版本，恢复一下就好了。

正常操作应该是：

1）先将当前浏览器书签导出到本地电脑。
2）然后点击 Download 把云端仓库的书签信息同步到当前浏览器。
3）然后再将本地书签导入到当前浏览器，再自己将书签整理下，把当前浏览器的书签和云端仓库的书签整合。
4）整理完毕再上传（Upload）就 OK。

## 3. 参考资料

1.  [谷歌浏览器书签同步工具 - 知乎](https://zhuanlan.zhihu.com/p/158026344)
