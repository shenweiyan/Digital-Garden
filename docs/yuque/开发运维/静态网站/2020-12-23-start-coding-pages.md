---
title: 使用 coding.net 发布你的个人博客
urlname: 2020-12-23-start-coding-pages
author: 章鱼猫先生
date: 2020-12-23
updated: "2021-06-30 09:35:51"
---

很多人喜欢在 github pages / gitee pages 发布自己的个人博客，前者由于服务器位于国外可能会导致国内的访问有时候很慢（你也可以使用 CDN 进行加速），后者如果想要配置自定义域名需要开通 Gitee Pages Pro 付费服务。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnF4yJF0Ehy-3OUoTbho7XWbSbd9.png)
[Gitee Pages Pro 暂时关闭个人用户购买入口](https://gitee.com/help/articles/4228)

这里介绍一下，由腾讯云提供支持的 coding.net 代码托管平台提供的静态网站功能，为免费博客、静态站点提供一个解决方法，以供参考。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn8x1_edIjoQJbZo19vgSkHSEV7s.png)

本文章最后搭建完成的示例静态站点，可以点击这里进行预览：
[Creative - Start Bootstrap Theme](https://coding-pages-bucket-396338-8151423-8649-429346-1251708715.cos-website.ap-guangzhou.myqcloud.com/)

首先，进入你的 coding.net 主页，选择组边导航栏的"项目"，然后"创建项目"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoibxD7td7j-1REdQX_2qrghuh0d.png)
选择“代码托管项目”。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmmTUz72mLQtYeHw7E_Lcvg8u2-y.png)
填写项目基本信息，点击"完成创建"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fs18c5yRt-sZ-NbLaGq52YkNb9wa.png)
第二步，创建完成项目后，进入创建好的项目，在"代码仓库"中"新建代码仓库"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FunGmG7sVE93QYUGEjvLN5Mc4sY1.png)
填写新建代码仓库信息。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuAe2vvCmIgcgKOQVRwyLvM8kRt6.png)
第三步，在创建好的代码仓库中，选择"新建/上传"，或者通过 git 的方式，上传文件或文件夹。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmkJUl-lPxdh7SrM3grhPnS2QK7d.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq1Bx0i4tRY1y8CCCOP3fF54gjll.png)
第四步，开启项目设置中的“持续部署”功能。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnzHKrnW3hoDflDed_BsWfLxrW3H.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjzGhign9AHQuzJLulaSQ3VbeoIY.png)
第五步，构建"静态网站"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiIqxbEmupZJRiIdcRq4oFx_fwl7.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlER5RGikiwwe5BmiLNHPsR6I3Rw.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtjpVfTxGJc_aawM4WVdaacwZXLG.png)
第六步，部署成功，访问站点。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnWQHToby6SH_lmDn2swMeODY-a_.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiD4dRHwKGWLNnLRu1lkQ8oAJK0t.png)
到这里，你在 coding.net 上的静态网站（博客）就已经部署完成，部署完成后 coding.net 会自动生成一个很长的 url，你可以通过这个 URL 访问你的站点。

附上本文章最后搭建完成的示例静态站点：
[Creative - Start Bootstrap Theme](https://coding-pages-bucket-396338-8151423-8649-429346-1251708715.cos-website.ap-guangzhou.myqcloud.com/)

当然，你也可以配置一个更加容易访问的自定义域名，我们在下一篇推文中再详细如何配置，敬请期待。
