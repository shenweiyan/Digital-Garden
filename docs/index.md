---
hide:
  - navigation
  - feedback
  - toc
title: 维燕的数字花园
template: home.html
---

<style>
  @media (min-width: 900px) {
    main > div > div.md-content {
      max-width: 75%;
      margin: auto;
    }
  }
</style>

<!--center><font  color= #518FC1 size=6 class="ml3">循此苦旅，以达星辰</font></center-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>

<!--p align="center">
    <img src="https://kg.weiyan.tech/0000/img/kg-readme-cover.gif" alt='readme-cover' style="border-radius: 2%;"><br>
</p-->


本知识库基于 [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/) 进行部署，有一部分文章来源于个人的 [**语雀知识库**](https://www.yuque.com/shenweiyan)，是作者关于生物信息学、互联网 IT、运维开发、软件测评使用等相关文章汇总。

<div id="rcorners">
    <body>
      <font color="#4351AF">
        <p class="p1" style="font-weight:bold;"></p>
<script defer>
    //格式：2020年04月12日 10:20:00 星期二
    function format(newDate) {
        var day = newDate.getDay();
        var y = newDate.getFullYear();
        var m =
            newDate.getMonth() + 1 < 10
                ? "0" + (newDate.getMonth() + 1)
                : newDate.getMonth() + 1;
        var d =
            newDate.getDate() < 10 ? "0" + newDate.getDate() : newDate.getDate();
        var h =
            newDate.getHours() < 10 ? "0" + newDate.getHours() : newDate.getHours();
        var min =
            newDate.getMinutes() < 10
                ? "0" + newDate.getMinutes()
                : newDate.getMinutes();
        var s =
            newDate.getSeconds() < 10
                ? "0" + newDate.getSeconds()
                : newDate.getSeconds();
        var dict = {
            1: "一",
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            0: "天",
        };
        //var week=["日","一","二","三","四","五","六"]
        return (
            y +
            "年" +
            m +
            "月" +
            d +
            "日" +
            " " +
            h +
            ":" +
            min +
            ":" +
            s +
            " 星期" +
            dict[day]
        );
    }
    var timerId = setInterval(function () {
        var newDate = new Date();
        var p1 = document.querySelector(".p1");
        if (p1) {
            p1.textContent = format(newDate);
        }
    }, 1000);
</script>
      </font>
    </body>
  </div>

<!--p>以下两个地址都可以访问本站点：     

- [weiyan.cc](https://www.weiyan.cc)：基于 [Netlify](https://app.netlify.com/)，国内访问相对快一些；     
- [gh-pages.weiyan.cc](https://gh-pages.weiyan.cc)：基于 [GitHub Pages](https://pages.github.com/)，国内访问可能有一定延迟。
</p-->

!!! abstract "希望所有读到此博客文章的读者都有所收获"

    愿上帝赐予我平静，让我能接纳我无法改变的事。

    愿上帝赐予我勇气，让我能改变我可以改变的事。

    并赐予我智慧，让我能分辨这两者的不同。
    
    用心生活每一天；用灵魂享受每个时刻。
    
    承受磨难，因为它是通向安宁的必经之路。

    效法耶稣，看清这个罪恶的世界。

    接受它原本的样子，而不是我所期盼的样子。
 
    相信只要服从神的旨意，神就能庇佑一切。

    这样，这一生我就有理由得到快乐，并在天堂与您一起得到极乐。

## 特别说明

很长一段时间以来，一直都在使用 [语雀](https://www.yuque.com/shenweiyan) 来记录个人工作、生活的各种知识。

从 2023 年下半年起出于某些原因，开始考虑数据多平台使用+备份+搜索的一些使用场景，几经考虑于是决定开始 All in GitHub 的一些探索，把语雀的一些文章记录同步到这里。同时开始探索 Issues + Discussions 来替换语雀小记，并最终选择了 All in [GitHub Discussions](https://github.com/shenweiyan/Digital-Garden/discussions)。

我希望这是我**最后一次**折腾个人的站点（博客），作为从为知笔记、[博客园](https://www.cnblogs.com/shenweiyan/)、[蚂蚁笔记](https://leanote.com/)、Jekyll、Hexo、Hugo ... 一路过来的人，曾经把太多的时间和精力都花费到 Themes/Html/CSS 的装潢上面了。内容才是核心，老老实实回归最简单的 Issues 或者 Discussions 对我来说已经足够了，另外，需要知道的是，博客其实就是写给自己看的，什么 SEO 流量、关注度、知名度，只需要保持一颗随缘的心态就好。

<p align="center">
    <img src="https://kg.weiyan.tech/0000/img/kg-readme-cover.gif" alt='readme-cover' style="border-radius: 2%;"><br>
</p>

至于为什么选择 Mkdocs，尤其是 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)，主要基于下面几点考虑：

1. 这是一个基于 Python 的静态站点生成器，生成专业的技术文档。
2. 支持 Markdown 语法。
3. 支持全文搜索。
4. 丰富插件支持和高度可定制化。
5. 可以直接托管在 GitHub、Netlify、Cloudflare 等平台。
6. 认可与赞赏 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 包括 [Insiders](https://squidfunk.github.io/mkdocs-material/insiders/) 在内的一些理念。
7. Material for MkDocs 的社区活跃，很多问题在 [Discussions](https://github.com/squidfunk/mkdocs-material/discussions) 都能得到及时友好的解决。

## 如何搜索

1. 使用点本站自带的搜索（推荐方法）。
2. 使用 [必应](https://cn.bing.com/)/[谷歌](https://www.google.com/) 进行搜索，如 `关键字(例如：生信) site:weiyan.cc` 。
<p align="center">
    <img style="max-width:600" src="https://kg.weiyan.cc/0000/img/google-weiyan-cc.png" alt="keywords-search"><br>
</p>

## 致谢

感谢 [Openbiox](https://openbiox.org/) 的 [《生信爱好者周刊》](https://github.com/openbiox/weekly)，它让我第一次知道并认识了 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)。

感谢 [LetTTGACO](https://github.com/LetTTGACO) 提供的 [Elog](https://elog.1874.cool/) 工具，提供了一个可以从语雀到本平台的优雅同步方案。

<br>
