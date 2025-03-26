---
title: 又爱又恨的 Microsoft Edge！
urlname: 2021-04-21-microsoft-edge
author: 章鱼猫先生
date: 2021-04-21
updated: "2021-06-25 10:46:47"
---

早在《[使用码云同步谷歌 Chrome 浏览器书签 · 语雀](https://www.yuque.com/shenweiyan/cookbook/chrome-bookmark-sync)》中就吐槽过 win7 下安装 Microsoft Edge 一大堆错误代码的问题，一直都折腾不出个所以然。然而公司的 PC 一直都是 Windowns 7，又不想重装 Windows 10。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgOzpaaBeNVDx6t5iibxFZ33IdOo.png)
既然和 Google Chrome 一样基于 Chroumium 内核，Google Chrome 可以有便携版本，Microsoft Edge 应该也可以有。于是，开始各种谷歌+百度搜索，终于发现 <https://shuax.com/project/edge/> 这个可爱曲线救国的项目。

# 使用

1.  把下载下来的 MicrosoftEdge_X64_90.0.818.39_shuax.com.7z 解压后运行 App/msedge.exe 即可。
2.  由于是便携版，不会和其它版本冲突，不想用了可以直接删掉整个文件夹。

# 更新

1.  升级先把老版本 App 重命名为 App2。（程序放在 App 目录，数据放在 Data 目录）
2.  然后把新下载/安装的所有文件覆盖到老文件夹内。
    1.  如果在 win7 中安装最新的 Microsoft Edge，如 90.818.42，安装后在更新中提示错误代码。
    2.  把最新安装的 Microsoft Edge 的 Application 整个目录拷贝到当前目录，重命名为 App。
    3.  把 App2 旧目录内的 version.dll 拷贝到 App 内。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fkiv5jhaClVSKo72vrGS-JgrL_xe.png)

3.  运行测试正常后可以安全删除 App2 老版本。
4.  建议保留上个版本压缩包以便出问题时还原。
5.  最后，双击 mesedge.exe，发现已经移除更新错误警告（因为是绿色版没有自动更新功能）。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqTj3JRSbg5N-06rJG_5YqWvUkNN.png)

最后说一下，Microsoft Edge 虽然比较符合国人使用习惯，也不需要搭梯子，要是折腾成本太高，Google Chrome 也是很香的。
