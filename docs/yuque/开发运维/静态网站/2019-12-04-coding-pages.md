---
title: 怎么在 CODING 上部署自己的静态网站
urlname: 2019-12-04-coding-pages
author: 章鱼猫先生
date: 2019-12-04
updated: "2021-08-14 10:48:58"
---

在 cong.net 部署静态博客，跟 github 是不一样的，这里简单记录一下。以谢益辉的  [hugo-xmag](https://github.com/yihui/hugo-xmag)  博客主题为例。

## 1. 创建项目，进入代码浏览

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhBe5Ia8ejpeJbvurVlTS9RwRr3Z.png)

## 2. 在服务器中生成网站，并推送

```bash
shenweiyan@ecs-steven 14:25:22 /home/shenweiyan
$ mkdir shenweiyan.com
$ cd shenweiyan.com
$ mkdir themes
$ cd themes
$ git clone https://github.com/yihui/hugo-xmag.git
Cloning into 'hugo-xmag'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 547 (delta 2), reused 7 (delta 1), pack-reused 535
Receiving objects: 100% (547/547), 339.23 KiB | 53.00 KiB/s, done.
Resolving deltas: 100% (236/236), done.
$ cd /home/shenweiyan/shenweiyan.com
$ cp -r themes/hugo-xmag/exampleSite/* .
$ hugo   # 这一步会默认生成 public 静态博客目录

                   | EN
+------------------+----+
  Pages            | 41
  Paginator pages  |  3
  Non-page files   |  0
  Static files     |  2
  Processed images |  0
  Aliases          | 16
  Sitemaps         |  1
  Cleaned          |  0

Total in 129 ms
$ cd public
$ git init
Initialized empty Git repository in /home/shenweiyan/shenweiyan.com/public/.git/
$ git remote add origin https://username:passwd@e.coding.net/bioit/shenweiyan.com.git
$ git add --all
$ git commit -m "first commit"
$ git push origin master        # 完成 public 目录的所有文件推送
```

## 3. 开始构建静态网站

在导航栏的 “**构建与部署**” 中选择 “**静态网站**”，点击“**直接发布静态网站**”。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmbcgo5jdhd6hO6YtMg8xVNRdKbj.png)

填写网站名称，然后 "**保存**"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fql3_vK9lCUgKCjHRTGg_rxlwdTF.png)

"**保存**" 后，在部署页面点击 "**立即部署**"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn4Nm-LecNF7IcOuDuh97O4_vDqm.png)

部署成功后，通过访问地址可以打开静态的网站。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiMkVKhkOCY1U01IjFaiuVphF4Zu.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqkGIf-oBOD5W9ThS55qh93Rw3K4.png)

## 4. 绑定域名

在项目导航栏 "构建与部署" → "静态网站" 页面，点击右上角的 "设置" 按钮。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq21jVp5Snhf7l5OCvLMEe6kOwDU.png)

在 "设置" 页面，填写需要绑定的域名，并选择强制 https 访问。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlnPUJV1HANAUcFbfNOR1A2QT8_R.png)

在域名解析中添加一条 CNAME 记录。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtnyQ-iVV1l-Z77xyeyJVUXWkl86.png)

域名解析 CNAME 添加后，等待几分钟，直至证书状态为“正常”。如果证书状态失败，检查你的 CNAME 记录，并再尝试多重新申请几次。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fv8SS-gwX48ZRRf8f8w-JKdkDP1v.png)

最后，通过域名访问，一切正常。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlgcTNCIMD5y4GUw7sOT_C8Ea9Dt.png)
