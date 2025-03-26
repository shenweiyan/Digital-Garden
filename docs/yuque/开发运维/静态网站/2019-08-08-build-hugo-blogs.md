---
title: 博客 | Hugo 博客折腾的一些记录
urlname: 2019-08-08-build-hugo-blogs
author: 章鱼猫先生
date: 2019-08-08
updated: "2023-01-05 11:16:14"
---

模仿 R 语言大神谢益辉，搭建了一个 Hugo+Blogdown 的博客：<https://www.shumlab.com>

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FofWGzhVVKFkuXNKeP0e3a932SWw.png)

主要记录：

- `.Site.BaseURL`  不起作用， `relURL` 、 `absURL`  也不起作用时，可参考使用 `params`  方法解决。
- 修复原博客 url 的一些 bug，shen.bioinit.com 部分链接被直接写死，想要复用的需要重新定义。

---

### CentOS 7 安装 Go

```bash
$ wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
$ tar zvxf go1.12.7.linux-amd64.tar.gz
$ mv go go-1.12.7

$ vi ~/.bashrc
# 在文件最后一行加入以下内容
export GOPATH=/ifs1/go-projects                #这个是你自己开发的GO代码位置，以后开发可以放这个目录下
export GOROOT=/usr/local/software/go-1.12.7    #这个就是我们安装的位置了。
export PATH=$PATH:$GOROOT/bin                  #go语言一些常用的命令引入PATH环境变量

$ go env 		# 查看 Go 的一些环境配置
```

### CentOS 7 安装 Hugo

```bash
$ wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.tar.gz
$ tar zvxf hugo_0.54.0_Linux-64bit.tar.gz -C /usr/local/software/hugo-0.54.0
$ echo "export PATH=/usr/local/software/hugo-0.54.0:\$PATH" >>~/.bashrc
$ source ~/.bashrc
```

### 启动 hugo 博客服务

```bash
shenweiyan@ecs-steven 15:04:06 ~/shenweiyan/home
$ hugo		# 渲染生成静态站点文件

                   | ZH
+------------------+-----+
  Pages            | 159
  Paginator pages  |   0
  Non-page files   |   2
  Static files     |  44
  Processed images |   0
  Aliases          |   0
  Sitemaps         |   1
  Cleaned          |   0

Total in 203 ms

$ hugo server --baseUrl=120.77.xx.xx --bind=0.0.0.0		# 启动本地预览服务
```

> **🏷️Hugo 小知识 - 草案、未来和过期内容**

> Hugo 允许您在网站内容的前言设定中设置文档的`draft`，`publishdate`甚至`expirydate`字段。默认情况下，Hugo 不会发布下面内容：
>
> 1.  `publishdate` 发布日期值设定在未来的内容；
> 2.  `draft:true` 草案状态设置为真的内容；
> 3.  `expirydate` 过期日期值设置为过去某事件的内容。
>
> 这三个可以在本地开发和部署编译时通过对`hugo`和`hugo server`分别添加如下参数来重新设定，或者在配置文件中设定对应(不包含`--`)域的 boolean 值：
>
> 1.  \-F, --buildFuture include content with publishdate in the future
> 2.  \-D, --buildDrafts include content marked as draft
> 3.  \-E, --buildExpired include expired content

### 一些问题

**问题：**
hugo-ivy 主题在 0.55 后版本的 Hugo 中 RSS 无法使用，并且在编译时会有如下警告：

```bash
Building sites …
WARN 2019/08/13 09:03:08 Page's .URL is deprecated and will be removed in a future release. Use .Permalink or .RelPermalink. If what you want is the front matter URL value, use .Params.url.
WARN 2019/08/13 09:03:08 Page's .RSSLink is deprecated and will be removed in a future release. Use the Output Format's link, e.g. something like:
    {{ with .OutputFormats.Get "RSS" }}{{ .RelPermalink }}{{ end }}.
```

**方法：**

1.  网络部分关于将  `.URL`  相关的文件中  `.URL`  改成 `.Permalink`  以解决 `.URL`  的上述报错的做法（参考：《[LeaveIt 以支持最新版 Hugo](https://blog.hgtweb.com/2019/%E4%BF%AE%E5%A4%8Dleaveit%E4%BB%A5%E6%94%AF%E6%8C%81%E6%9C%80%E6%96%B0%E7%89%88hugo/)》），经测试如果针对 Menu 级别的 html 模板会引发其他错误；而且虽然 hugo 更新到了 0.56.3，但官方文档示例还在使用 `.URL` ，参考  <https://github.com/gohugoio/hugo/issues/5835>。

2.  修改包含 `.RSSLink`  相关的文件，如下：

```go
<!-- 修改前 -->
{{ if .RSSLink }}
    <link href="{{ .RSSLink | relURL }}" rel="alternate" type="application/rss+xml" title="{{ .Site.Title }}" />
{{ end }}

<!-- 修改后 -->
{{ with .OutputFormats.Get "RSS" }}
    <link href="{{ .RelPermalink | relURL }}" rel="alternate" type="application/rss+xml" title="{{ $.Title }}" />
{{ end }}
```

### 一些资料

记录一下，搭建部署过程中参考的一些资料：

- 钟浩光，《[用 R 语言的 blogdown+hugo+netlify+github 建博客](https://cosx.org/2018/01/build-blog-with-blogdown-hugo-netlify-github/)》，统计之都
- Hash_Borgir, rdwatters, etc.《[What should be used for the value of .Site.BaseURL?](https://discourse.gohugo.io/t/solved-what-should-be-used-for-the-value-of-site-baseurl/5896)》，Hugo forums
- chaomifan，《[Hugo+GitHub 静态博客折腾笔记](https://www.jianshu.com/p/076279c9ceea)》，简书
- Mogeko，《[链接为 Hugo 添加谈笑风生区 (Gitalk)](https://mogeko.me/2018/024/)》，Mogeko\`s Blog
- ByQiu，《[为博客添加 Gitalk 评论插件](https://www.jianshu.com/p/78c64d07124d)》，简书
- Parsia，《[Archive Page in Hugo](https://parsiya.net/blog/2016-02-14-archive-page-in-hugo/)》，Hackerman's Hacking Tutorials
- olOwOlo desu，《[Hugo 从入门到会用](https://blog.olowolo.com/post/hugo-quick-start/)》，olOwOlo's Blog
- 小龙虾，《[用 hugo 创建自己的博客](https://cray.vip/post/blog/)》，小龙虾的博客
- Hugo 的作品集主题页：[_https://themes.gohugo.io/tags/portfolio/_](https://themes.gohugo.io/tags/portfolio/)
