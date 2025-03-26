---
title: 苹果字体 PingFang SC 的一些踩坑记录
number: 49
slug: discussions-49/
url: https://github.com/shenweiyan/Digital-Garden/discussions/49
date: 2024-01-09
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['公众号', '1.3.10-Windows']
---

曾经在 《[为 Windows 系统替换优雅的苹果字体](https://www.weiyan.cc/cookbook/%E5%BC%80%E5%8F%91%E8%BF%90%E7%BB%B4/windows/2021-02-19-win-font/)》中提到可在 Windows 中使用苹方字体替代默认的微软雅黑，这里就有一个问题即需要在 Wondows 下安装苹方字体 —— 如果你的字体安装错误，很有可能导致你的浏览器或其他应用出现乱码。

## 浏览器乱码

出现这个的原因主要是站点使用了 `PingFang SC` 的字体设置。
```
body {
    font-family: PingFang SC,microsoft yahei,sans-serif;
}
```

我们可以看到使用 F12 检查源码模式把 `font-family` 中的 `PingFang SC` 去掉后即可显示正常。

## 字体安装后不起作用

这里就涉及一个 **萍方** vs **苹方** vs **PingFang** 区别的一个问题。

> 猛地看上去，萍方/苹方/PingFang 应该是同一个字体。但是，实际上的效果，却并不相同。那么，到底谁是真正的 pingfang sc呢？    
>     
> 这里以能否**以 PingFang SC 为名称识别出来，作为标准**。为什么这么说呢？因为网页里面的 font-family，写的都是 pingfang sc，也许萍方/苹方都是差不多的字体，但是不能在网页里面自动识别出来。所以，就等于零。
> 
> ```
> body {
>    font-family: PingFang SC,microsoft yahei,sans-serif;
> }
> ```
> 比如，上述 css 定义，就来自于腾讯云主页。在实际的应用过程中，只有安装好的 pingfang sc 系列字体才能被识别【如下图中的右侧字体】。    
> **注意：萍方/苹方，在安装的时候，文件名也都是 pingfang-sc 之类的文件名。但是，安装完成的真正成品，可不是这个拼音名字。进而导致字体不能识别。**
> ![pingfang sc 区别](https://shub.weiyan.tech/kgarden/2024/01/fingfang-sc.png)
>     
> From 《[由 pingfang sc 字体缺失，所暴露的字体加载顺序的潜规则](https://newsn.net/say/css-font-family-pingfang.html)》

## 解决方案

参考 《[由 pingfang sc 字体缺失，所暴露的字体加载顺序的潜规则](https://newsn.net/say/css-font-family-pingfang.html)》 一文的方案。

### 安装 PingFang SC

名称为 **PingFang SC** (英文) 的字体找了很久才在 GitHub 翻到一个(以防丢失，个人 Fork 了过来)：[shenweiyan/PingFangSC-Fonts](https://github.com/shenweiyan/PingFangSC-Fonts)，如有需要可以直接下载安装。

> 国内大多数网页，在定义网页字体的时候，都是先定义 PingFang SC，然后定义微软雅黑。那么：    
>    
> - 正常来说，win 系统是不会安装 PingFang SC 字体的，所以，显示微软雅黑，页面正常。    
> - 但是，一旦单独安装了 PingFang SC Light，页面就会识别出这个 Light 字体，页面不正常。    
> - 解决方案是：再安装一个 PingFang SC Regular，页面会在 Light 之前优先识别 Regular，页面正常。    

>    
> 如果您非要在 win 下面安装 pingfang sc 字体，可能要三思而后安装了。李鬼似乎有点多...

>    
> ![PingFang SC Regular](https://shub.weiyan.tech/kgarden/2024/01/pingfang-sc-regular.png)

### 删除 PingFang SC

个人用的就是这一个方法，但是在 `C:\Windows\Fonts` 中删除的时候会提示 **该字体正在使用无法删除！所以，必须要关闭使用苹方字体的程序。**

因此，我们需要：

参考：《[电脑安装新字体，浏览器字体全变了，如何删除正在使用的苹方字体](https://www.bilibili.com/video/BV1nc411575s/)》 - 哔哩哔哩

- 在 Windows 任务管理的进程中把浏览器相关的全部结束掉，如 360 浏览器相关的进程、Microsoft edge、Google Chrome 等等，全部选择结束任务。    
- 把其他可能使用苹方字体的，如 OneNote、WPS、微信、... 这些的进程也全部结束掉。    

最后，回到 `C:\Windows\Fonts` 中再次删除相应的苹方字体，发现即可成功删除。删除了这些苹方字体，浏览器上的字体显示也就恢复正常了。

## 参考资料

1. 苏南大叔，《[由 pingfang sc 字体缺失，所暴露的字体加载顺序的潜规则](https://newsn.net/say/css-font-family-pingfang.html)》
2. 科技猎手2023，《[电脑安装新字体，浏览器字体全变了，如何删除正在使用的苹方字体](https://www.bilibili.com/video/BV1nc411575s/)》 - 哔哩哔哩

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="49"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
