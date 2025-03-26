---
title: 博客 | hugo 博客添加 disqus 评论系统
urlname: 2019-08-28-disqus-for-hugo
author: 章鱼猫先生
date: 2019-08-28
updated: "2021-06-30 09:36:31"
---

打开 diqus 官网：[http://disqus.com](http://disqus.com/)，点击 "GET STARTED" 进入注册页面：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fm0Nvud2wM-Qmbfob3ehCL_rdOmd.png)

选择 "I want to install Disqus on my site"，进入"Create" 创建页面：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fiq4H0QXlYmvbO60hCDMeEUbNEUe.png)

在创建页面填写网站信息：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvB1DauKhovYmXFfiwPY6HosIROR.png)

在 "Choose a plan" 页面，拉到最下面，选择免费的 "Basic" 版本，点击 "Subscribe Now"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmxqzjzaHNEoBu_uoO05DIwPGTX7.png)

在 "Choose a platform" 选择博客的平台类型，对于 hugo 我们选择页面最下面的 "Universal Code"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqIXNu0hV9zS8tceXMCAmm9eCAtB.png)

把 "Install instructions for Universal Code - Disqus Admin" 页面的代码拷贝到 hugo 博客的  layouts/partials/disqus.html 文件：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjM1YaY7MfIwDdKxFCW-wTocPfrb.png)

```html
<div id="disqus_thread"></div>
<script>
  /**
   *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
   *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
  /*
var disqus_config = function () {
this.page.url = "{{ .Permalink }}";  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = "{{ .Permalink }}"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
  (function () {
    // DON'T EDIT BELOW THIS LINE
    var d = document,
      s = d.createElement("script");
    s.src = "https://shen-hugo-blog.disqus.com/embed.js";
    s.setAttribute("data-timestamp", +new Date());
    (d.head || d.body).appendChild(s);
  })();
</script>
<noscript
  >Please enable JavaScript to view the
  <a href="https://disqus.com/?ref_noscript"
    >comments powered by Disqus.</a
  ></noscript
>
```

最后，在 "Install instructions for Universal Code - Disqus Admin" 页面拉到最下面，点击 "Configure"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvW6lksIeO95ArDtIzT1_oFVQ-dl.png)

在 "Configure" 页面填写完善网站的相关信息，点击 "Complete Setup" 完成设置。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjPQ-fQXnTEvXv8NwQnSVpkakm23.png)

在 hugo 博客的  config.toml 配置文件中增加 `disqusShortname`  参数：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FptzgYP-5erH5oeiMS-se8b7g7nU.png)

在 hugo 博客  layouts 目录下的模板中引入 `disqus.html`  模板：

```go
{{ partial "disqus.html" . }}
```

最后，执行 hugo，重新渲染生成所有的静态博客文件，push 到 github pages，完成所有操作。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgU5Coq-uy53JF_ELjI7JedghJOd.png)
