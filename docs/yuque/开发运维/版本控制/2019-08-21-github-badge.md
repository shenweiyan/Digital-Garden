---
title: GitHub 的项目徽章
urlname: 2019-08-21-github-badge
author: 章鱼猫先生
date: 2019-08-21
updated: "2021-06-30 09:37:19"
---

GitHub 项目的 README.md 中可以添加徽章（Badge）对项目进行标记和说明，这些好看的小图标不仅简洁美观，而且还包含了清晰易读的信息。

GitHub 徽标的官方网站是  <http://shields.io/>，我们可以在官网预览绝大部分的徽标样式，然后选择自己喜欢的（当然首先需要适用于自己的目标项目）徽标，添加到自己的项目文档中去。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp90EVTf0C6how5YdnxSq6FdE2Qt.png)

### 生成已有的标签

- 打开  GitHub 徽标的官方网站  <http://shields.io/>，输入你在 Github 的 repo URL，即可看到 issues、forks、stars 相关的图标及代码。

![galaxy-badges.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtCvMnaB2Vwt1haUBIcAkQp41Jxe.png)

- 点击图标或者代码，即可进入设置页，设置图标的颜色、样式等属性，最后选择你想要的 markdown 或者 URL 代码到 README.md 或者项目的文档页面即可。

![galaxy-star.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqG2PLtNfOGR8dk7YVlS5_g5XeJs.png)

- 一些常见比较好玩的  Badges

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Ft3Ua1_WNpygDdZc6mTfaq7BAeNb.png)

### 生成自定义徽章标签

如果我们想要生成的徽章字样和颜色  [shields.io](http://shields.io/)  上面没有怎么办?例如我们想生成一个类似的徽章我们应该怎么做呢?

首先，我们进去  <https://shields.io/> ，在 shields 网站拉到最后，也就是 "You Badge" 部分填写自定义的 label、message、color 信息。
![bioitee-badge.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsoGHVozIF9cUOC8UX_ZMTzEYMEh.png)

然后，点击 "Make Badge" 按钮就可以生成我们想要的任何徽章了！
![bioitee-badge-img.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgN94NqR2gZKLgWwvcX5PeaFzd6h.png)

- 如果我们在写 markdown 的时候想为我们的徽章或者进度条添加点击跳转的超链接，可以使用超链接和图片的语法嵌套来写，具体可以参照 markdown 标准语法。
- 自定义徽章和进度条由于参数是写死的，不会根据网络的数据自动变化上面的文字，所以，这些标签是静态的，修改的时候需要我们手动更改 URL。
