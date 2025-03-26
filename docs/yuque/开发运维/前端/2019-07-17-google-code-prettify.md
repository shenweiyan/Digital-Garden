---
title: Google Code Prettify 代码高亮使用教程
urlname: 2019-07-17-google-code-prettify
author: 章鱼猫先生
date: 2019-07-17
updated: "2021-06-25 10:53:27"
---

Google Code Prettify 是 Google 的一款代码高亮插件，它由 js 代码和 css 代码构成，用来高亮显示 HTML 页面中的源代码。

Google Code Prettify 支持的语言数量比较多、比较全，支持自动识别代码语言，不需要手动指定，渲染效果也不错。最重要的是，非常轻巧，加载速度远比 SyntaxHighlighter 快得多，而且可以直接使用 Markdown 的语法写代码。

GitHub 地址：<https://github.com/google/code-prettify>

# **1、主题**

google-code-prettify 提供了 5 个 css 主题可供选择，而且支持自定义 style。相关的 demo 及 style 文件参见：<https://rawgit.com/google/code-prettify/master/styles/index.html>。

# **2、文件**

google-code-prettify 需要两个文件，prettify.js 和 prettify.css，去官网下载。把这两个放到 head 模板中，如下：

```html
<link
  href="http://alfred-sun.github.io/assets/google-code-prettify/prettify.css"
  rel="stylesheet"
  type="text/css"
  media="all"
/>
<script
  type="text/javascript"
  src="http://alfred-sun.github.io/assets/google-code-prettify/prettify.js"
></script>
```

# **3、使用**

考虑到加载速度，最好 js 写到文档末尾，body 闭合标签之前，css 写到头部之后，还需要在合适位置（如：$(document).ready）添加如下代码，用于识别并高亮代码块，这个需要使用 jQuery：

```javascript
$(function () {
  window.prettyPrint && prettyPrint();
});
```

到这里，我们就可以使用 `<pre></pre>` 标签进行高亮了。

## 3.1. 基本用法

Google 的高亮插件使用比较方便，只需要在  `<pre>`  的标签上加入 `prettyprint`  即可。

```html
<pre class="prettyPrint">
    // code here
</pre>
```

## 3.2. 行号设置

google-code-prettify 默认每五行显示一次行号，如果想要显示所有的行号，我们只需要在 google-code-prettify 对应主题的 css 文件中找到下面一样把它注释掉即可：

```html
li.L0,li.L1,li.L2,li.L3,li.L5,li.L6,li.L7,li.L8 { list-style-type: none }
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk8fPWIL8yWxeBJCxFjzJ001cJ2h.png)

## 3.3. Markdown

如果用 Markdown 来生成 HTML 的话，需事先给相关的标签追加必要的 class；Markdown 产生的代码块必然含义 `<pre>`  元素，那么可以用 jQuery 在 Prettyprinter 运行前处理下 HTML 样式：

```javascript
$(function () {
  $("pre").addClass("prettyprint linenums").attr("style", "overflow:auto");
});
```

这样就没有问题了，可以直接用 markdown 的前置 4 空格来写代码了。其中 `addClass('prettyprint linenums')`  的 linenums 是添加行号的意思。默认只显示第 5、10、15... 行，可以在 css 文件中 li 的格式添加 `list-style-type: decimal;` ，以显示全部行号。

## 3.4. Bootstrap 代码框滚动

如果博客中有用 Bootstrap，其中对 pre 有如下几句：

```css
white-space: pre;
white-space: pre-wrap;
word-break: break-all;
word-wrap: break-word;
```

这会使得 pre 中的代码自动换行，而不是溢出形成滚动条。如果不希望如此，可以注释掉。看个人喜好。

如果是滚动条，默认的滚动太难看而且还有个 Bug（stripe 的高亮背景色无法固定，随着滚动条位置改变而改变，可以考虑去掉 stripe，或者禁用横向滚动条），可以修改一下样式，看一下：[CSS 自定义浏览器滚动条样式](http://ju.outofmemory.cn/entry/149458)。

# **4、Leanote 博客**

这里主要讲一下如何在 leanote 博客中使用 Google Code Prettify，并实现代码框左右滚动的效果。

## 4.1. bootstrap 文件

由于 leanote 应用了 bootstrap 的样式，其内置的 pre 代码会自动换行，而不是溢出形成滚动条，因此我们需要自定义样式（以下为完整 customHilight.css 文件内容）：

    /*自定义 ol 列表数字距离*/
    code.prettyprint ol.linenums, pre.prettyprint ol.linenums{
        padding: 0 0 0 25px !important;
    }

    /*代码框左右滚动*/
    pre.prettyprint {
        white-space: pre !important;
    	word-wrap: break-word !important;
    	overflow:auto !important;
    }
    pre{
        word-break: unset !important;
        word-wrap:unset !important;
        white-space:unset !important;
    }
    pre code{
        white-space:unset !important;
    }
    code.prettyprint .linenums, pre.prettyprint .linenums{
        white-space: pre;
    	word-wrap: break-word;
    	overflow:auto;
    }

最后，清空浏览器缓存，就可以看到 [leanote 博客](http://blog.leanote.com/shenweiyan)代码框左右滚动的效果。

# 5. 参考资料

- [Jekyll 中用 Google Code Prettify](http://ju.outofmemory.cn/entry/149451)，Vermillion Phoinix by Alfred Sun，2014-12-15
