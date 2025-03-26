---
title: 基于 gulp 的 fancybox 源码压缩
urlname: 2019-12-26-gulp-for-fancybox
author: 章鱼猫先生
date: 2019-12-26
updated: "2021-06-25 10:53:12"
---

前不久，处理生信分析网页版自动化报告的时候就使用过 fancybox，今天在优化个人博客，为博文增加图片缩放效果，解决一些滚动条问题时，才从 fancybox 的 Github 源码中接触到 gulp —— 一个基于流的前端自动化构建工具，记录一下学习的过程。

## 1. fancybox 简单介绍

关于 fancybox，其官网的介绍是：JavaScript lightbox library for presenting various types of media. Responsive, touch-enabled and customizable. 翻译过来就是，Fancybox 是一个 JavaScript 库，用于以优雅的方式呈现图像，视频和任何 HTML 内容。它具有您期望的所有功能——触摸启用，响应和完全可定制。我们来看一下 fancybox 官网提供的 demo 效果。
![fancybox-demo-86.gif](https://shub.weiyan.tech/yuque/elog-cookbook-img/lm6qacxnx4eYVOB5vgQoa3nl-ImJ.gif)

## 2. fancybox 的安装使用

我们这里所说的 fancybox，主要指的是它的 3.x 版本（即 fancybox3），网络上还有不少 1.x、2.x 的版本，我们不讨论。fancybox3 的使用很简单，只需要简单的 2 步。

1.  引入 jQuery 和  fancybox 样式文件

```html
<script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js"></script>

<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css"
/>
<script src="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>
```

2.  创建图像链接

```html
<a data-fancybox="gallery" href="big_1.jpg"><img src="small_1.jpg" /></a>
<a data-fancybox="gallery" href="big_2.jpg"><img src="small_2.jpg" /></a>
```

## 3. fancybox 的一些问题

在网上看到部分网友说，fancybox3 在打开或关闭遮罩层的时候，页面会自动返回顶部的 bug，目前我使用的  <fancybox@3.5.7> 暂时没发现这个问题。

我在这里想说一下，关于  fancybox3  隐藏页面滚动条的事情，因为  fancybox3 默认的配置项是 `hideScrollbar: true`，即默认隐藏滚动条。当然，我们可以直接修改样式也可以达到显示和隐藏滚动条的目的；或者可以在 fancybox3 的源码中设置 hideScrollbar 选项为 false，就可以出现滚动条了。

- 直接修改样式

```css
.fancybox-active {
  overflow: hidden;
}
```

- 修改源码设置

fancybox 是基于  GPLv3 进行源码开放的，它的源吗托管在 github 上，我们可以直接在 `fancybox/dist/jquery.fancybox.js`  源码中把 `hideScrollbar: true`，更改成  `hideScrollbar: false`，然后把修改后的  `jquery.fancybox.js`  应用到你的图片页面，以达到显示滚动条的效果。

细心的童鞋可能发现了，fancybox 默认使用的 js 文件是 `jquery.fancybox.min.js` ，相比源码文件 `jquery.fancybox.js`  多了一个 **min**  后缀！所以，我们怎么才能把 `jquery.fancybox.js`  变成 `jquery.fancybox.min.js` ？

## 4. Gulp 简单介绍

Gulp 在官网的 title 是：用自动化构建工具增强你的工作流程，即一款基于流的前端自动化构建工具\*\*。\*\*作为前端的菜鸟，第一次听到这样的描述，是不是跟小编一样满头雾水？那么，下面摘录  segmentfault 前端分享专栏中《[gulp 前端构建工具白话讲解，也包含自己使用的一些心得体](https://segmentfault.com/a/1190000007137199)》的一些回答，让大家直观了解一下。

> ![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlGCZhuxcY6aND9Z8-2iFe2EsYDq.png)
>
> 大家现在看到的这个图片是我使用 gulp 的一个基本的项目结构，而这边的 src 文件就是我们的源文件，dist 是通过 gulp 编译过后的文件（稍后会详细说明每一个文件的作用）。
>
> **现在请大家思考这样一个问题**
>
> 1.  倘若我让线上的网站（不论 PC 还是移动端）使用的 css 文件，JS 文件，images 文件等静态资源，JS 是压缩过的，css 是压缩过的，images（主要针对雪碧图）也是压缩过的，好来减少文件的大小，从而提升一下浏览器的性能，那么应该怎么办？
>
> 2.  如果说我们在项目中使用 LESS，或者 SASS 作为 CSS 的预编译语言（浏览器本身是不支持 LESS，SASS 文件的，难道每次还要使用类似与考拉软件去处理这些吗？）
>
> 3.  如果我想找一个东西帮我去处理上面的这些东西，我写的还是没有压缩的 JS 或者 CSS/less/sass 等，但是在页面上实际上运行（或者等到项目发布的时候替换为压缩过的文件），那么 gulp 就是你很好的选择。

> **那么现在这样说大家有没有明白 gulp 是干嘛的吗？不错，它就是来处理上述这些事情的，而且我们在编辑器里修改的代码都是在 src 的目录下，而 dist 文件目录就是经过上述处理过后的文件目录，江湖人称编译过后的文件目录，而 gulp 就是起到了这个桥梁的作用。**
>
> - package.json 文件。它就是记录了我们使用了什么插件，以及版本号的记录的一个 json 文件。
>
> - gulpfile.js 文件是大家学习 gulp 的重点。它就是告诉了 gulp 我们要将什么文件编译到什么文件下的 XXX 目录里面。例如在我的 src 目录里面存在一个 css 文件夹，里面装了很多 css 或者 LESS 等样式文件，我现在想通过 gulp 将它编译到 dist 目录下面的 css 文件夹里面并且这个 css 文件夹里的样式文件还是压缩过了。那么 gulpfile.js 就是起到了这样的一个作用。

接下来，我们以 fancybox 的源码的为例，简单了解一下 Gulp 的安装和使用。

## 5. Gulp 安装与使用

首先，gulp 是基于 node.js 的工具，所以，在安装 Gulp 前我们需要先安装 node.js 和 npm。node.js 的安装大家可以自行谷歌一下怎么安装，这里不细说。

关于 npm，其实它是一个基于 node.js 的包管理工具，说的通俗一点就是，我们可以通过 npm 这个工具去下载我们想要的包，这些包就是我们在后面需要的各种各样的插件（比如压缩 JS 代码的插件，压缩 CSS 代码的插件），这些都是通过 npm 这样一个工具下载到我们的电脑里面的。说白了，npm 就等同 python 里面的 pip。

第二，我们使用 git 先把 fancybox 的 github 源码先 clone 下来。

```bash
$ git clone https://github.com/fancyapps/fancybox.git
Cloning into 'fancybox'...
remote: Enumerating objects: 2611, done.
remote: Total 2611 (delta 0), reused 0 (delta 0), pack-reused 2611
Receiving objects: 100% (2611/2611), 2.26 MiB | 359.00 KiB/s, done.
Resolving deltas: 100% (1680/1680), done.
```

第三，进入  fancybox 目录，安装 gulp 和其他依赖。

```bash
$ cd fancybox
$ ls
bower.json  dist  docs  gulpfile.js  package.json  README.md  src
$ mv dist dist.raw
$ /usr/local/software/node-v6.12.0/bin/npm install
npm WARN deprecated gulp-header@1.8.12: Removed event-stream from gulp-header
npm WARN deprecated gulp-util@3.0.8: gulp-util is deprecated - replace it, following the guidelines at https://medium.com/gulpjs/gulp-util-ca3b1f9f9ac5
npm WARN deprecated minimatch@2.0.10: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated minimatch@0.2.14: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated graceful-fs@1.2.3: please upgrade to graceful-fs 4 for compatibility with current and future versions of Node.js
npm WARN deprecated natives@1.1.6: This module relies on Node.js's internals and will break at some point. Do not use it, and update to graceful-fs@4.x.
npm WARN deprecated browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
@fancyapps/fancybox@3.5.7 /home/shenweiyan/fancybox
......
```

第四，修改 fancybox 的 `src/js/core.js`  源码。把该文件中的 `hideScrollbar: true`  更改为 `hideScrollbar: false` 。

```bash
$ sed -i 's/hideScrollbar: true/hideScrollbar: false/g' src/js/core.js
```

第五，回到  fancybox 根目录，执行  fancybox 源码压缩。

```bash
$ ls
bower.json  dist.raw  docs  gulpfile.js  node_modules  package.json  README.md  src
$ ./node_modules/gulp/bin/gulp.js
[11:14:32] Using gulpfile ~/fancybox/gulpfile.js
[11:14:32] Starting 'scripts'...
[11:14:32] Starting 'css'...
[11:14:33] Finished 'css' after 624 ms
[11:14:34] Finished 'scripts' after 2.18 s
[11:14:34] Starting 'default'...
[11:14:34] Finished 'default' after 23 μs
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsXa7tQEFSYvduI-37gPCncD900S.png)

最后，把编译后的 `dist/jquery.fancybox.min.js`  文件应用到博客或者其他网站页面，完成最后设置。

## 6. 几点总结

- 正常情况下的 `gulp`  可以使用 `npm install -g gulp`  进行全局安装，或者 `npm install --save-dev gulp`  在当前项目(目录)中安装 `gulp` 。区别是， `-g`  参数会把 `gulp`  安装在 `node`  默认的 `bin`  路径下，即全局安装；而不加 `-g`  参数， 则会把  `gulp`  默认安装到当前目录的 `node_modules/gulp/bin`  下。
- `--save`  会把依赖包名称添加到 `package.json`  文件 `dependencies`  键下；而 `--save-dev`  则添加到 `package.json`  文件 `devDependencies`  键下，譬如：

```json
{
  "dependencies": {
    "vue": "^2.2.1"
  },
  "devDependencies": {
    "babel-core": "^6.0.0",
    "babel-loader": "^6.0.0",
    "babel-preset-latest": "^6.0.0",
    "cross-env": "^3.0.0",
    "css-loader": "^0.25.0",
    "file-loader": "^0.9.0",
    "vue-loader": "^11.1.4",
    "vue-template-compiler": "^2.2.1",
    "webpack": "^2.2.0",
    "webpack-dev-server": "^2.2.0"
  }
}
```

- 它们真正的区别是， `npm`  自己的文档说 `dependencies`  是运行时依赖， `devDependencies`  是开发时的依赖。即 `devDependencies`  下列出的模块，是我们开发时用的，比如我们安装 js 的压缩包 `gulp-uglify`  时，我们采用的是 `npm install –save-dev gulp-uglify`  命令安装，因为我们在发布后用不到它，而只是在我们开发才用到它。 `dependencies`  下的模块，则是我们发布后还需要依赖的模块，譬如像 jQuery 库或者 Angular 框架类似的，我们在开发完后后肯定还要依赖它们，否则就运行不了。
- 对于已经存在 `package.json`  配置文件(定义了这个项目所需要的各种模块，以及项目的配置信息（比如名称、版本、许可证等元数据）)的目录，我们可以直接在当前目录执行 `npm install`  进行安装， `npm install`  命令根据这个配置文件，自动下载所需的模块，也就是配置项目所需的运行和开发环境。

## 7. 参考资料

- panw3i，《[npm --save-dev --save 的区别](https://www.jianshu.com/p/b1b6e5a94b6a)》，简书
- 小丑皇，《[gulp 前端构建工具白话讲解，也包含自己使用的一些心得体会](https://segmentfault.com/a/1190000007137199)》，SegmentFault
- 十年踪迹的博客，《[使用 Gulp 构建网站小白教程](https://www.h5jun.com/post/gulp-build)》，十年踪迹的博客
- bibichuan，《[fancybox3 使用总结](https://bibichuan.github.io/2019/03/19/fancybox3%E4%BD%BF%E7%94%A8%E6%80%BB%E7%BB%93/)》，bibichuan 的底盘 - Github 个人博客
