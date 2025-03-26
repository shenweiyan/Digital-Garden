---
title: Jekyll 网站添加访问量统计分析
urlname: 2019-06-03-jekyll-add-page-view
author: 章鱼猫先生
date: 2019-06-03
updated: "2021-06-30 09:36:45"
---

## Google Analysis

谷歌分析是谷歌提供的免费网络分析服务，用于跟踪和报告网站流量。将谷歌分析添加到 Jekyll 网站十分简单。登录  [谷歌分析](https://www.google.com/intl/zh-CN/analytics/)  并新建一个媒体资源，以获取网站的跟踪 ID。可在`管理 > 媒体资源 > 跟踪信息 > 跟踪代码`下找到跟踪 ID。

在 Jekyll 网站上部署谷歌分析，首先在`_includes`文件夹新建名为`google-analytics.html`的文件,并写入以下代码：

```javascript
<script>
if(!(window.doNotTrack === "1" || navigator.doNotTrack === "1" || navigator.doNotTrack === "yes" || navigator.msDoNotTrack === "1")) {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', '{{ site.google_analytics }}', 'auto');
  ga('send', 'pageview');
}
</script>
```

上面的 JavaScript 片段是 minima 主题自带的，用于确保跟踪脚本在所有浏览器上异步加载和执行，但它不允许预加载脚本。

下面的代码片段增加了对预加载的支持，在现代浏览器上提供较小的性能提升，但在 IE9 和较旧的移动浏览器上可能会同步加载和执行，因为这些浏览器不识别 async 属性。如果你的网站访客主要使用现代浏览器，请仅使用以下跟踪代码段。

```javascript
<script>
window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
ga('create', '{{ site.google_analytics }}', 'auto');
ga('send', 'pageview');
</script>
<script async src='https://www.google-analytics.com/analytics.js'></script>
```

上面 Liquid 对象`{{ site.google_analytics }}`用于通过`_config.yml`设置跟踪 ID，或者你可以直接把跟踪 ID 置换进去。

然后在`_config.yml`中添加跟踪 ID：

```yaml
# Google Analytics
google_analytics: UA—XXXXXXXX-X
```

最后添加`google-analytics.html`到网页，谷歌建议把跟踪代码放在每个页面的`<head>`中，以确保正确跟踪所有访问。

    {% raw %}{%- if jekyll.environment == 'production' -%}
      {%- include google-analytics.html -%}
    {%- endif -%}
    {% endraw %}

上面代码表示只有在生产环境下，才运行谷歌分析，GitHub Pages 默认设置是生产环境。

问题来了，中国大陆不能正常访问谷歌啊，如果添加了谷歌分析，访客打开网页时，加载跟踪代码会导致网页速度下降。

幸运的是 [jsDelivr CDN works in China](https://www.jsdelivr.com/network#china)，如此一来，我们仅仅添加以下代码即可：

```javascript
<script>
(function(e,t,n,i,s,a,c){e[n]=e[n]||function(){(e[n].q=e[n].q||[]).push(arguments)}
;a=t.createElement(i);c=t.getElementsByTagName(i)[0];a.async=true;a.src=s
;c.parentNode.insertBefore(a,c)
})(window,document,"galite","script","https://cdn.jsdelivr.net/npm/ga-lite@2/dist/ga-lite.min.js");
galite('create', '{{ site.google_analytics }}', 'auto');
galite('send', 'pageview');
</script>
```

[ga-lite](https://github.com/jehna/ga-lite)  不仅解决了谷歌分析跟踪代码在中国大陆影响加载速度的问题，还解决了官方脚本只缓存 2 个小时的问题。

## 不蒜子

官网：<https://busuanzi.ibruce.info/>
网站流量统计分析：<https://www.wumz.me/2018/baidu-analysis.html>
