---
title: Mkdocs material 对指定页面隐藏 H1 标题
number: 53
slug: discussions-53/
url: https://github.com/shenweiyan/Digital-Garden/discussions/53
date: 2024-01-19
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

主要记录一下在 Mkdocs material 中对指定页面隐藏标题，尤其是指在 Home 页面把 H1 级别的标题隐藏的一些解决方法。

<!-- more -->

## 背景

对于一些特定的页面，不想显示顶级的标题，尤其是 H1 标题。Mkdocs material 讨论区给出了几个方案：

1. 内联 CSS 的方法，参考 [squidfunk/mkdocs-material#2163](https://github.com/squidfunk/mkdocs-material/issues/2163)。    
   这个方法的确能解决隐藏当前页面的 H1 标题，但**同时会把搜索栏搜索结果的 H1 标题给隐藏了**。有点治标不治本！
2. 自定义页面模板，参考 [squidfunk/mkdocs-material#6185](https://github.com/squidfunk/mkdocs-material/discussions/6185)。
   这个参考的讨论里面没有给出具体的解决方法，本文章来详细介绍一下。

## 创建模板

首先，在 `overrides` 目录下创建一个名为 `home.html` 的文件(文件名可以随意命名)，内容可以参考 [`blog.html`](https://github.com/squidfunk/mkdocs-material/blob/master/material/templates/blog.html) 的内容。
```
{% extends "base.html" %}
{% block htmltitle %}
      {% if page.meta and page.meta.title %}
        <title>{{ page.meta.title }}</title>
      {% elif page.title and not page.is_homepage %}
        <title>{{ page.title | striptags }}</title>
      {% else %}
        <title>{{ config.site_name }}</title>
      {% endif %}
{% endblock %}

{% block container %}
    <div class="md-content" data-md-component="content">
      <article class="md-content__inner md-typeset">
        {% block content %}
          {% include "partials/mycontent.html" %}
        {% endblock %}
      </article>
    </div>
{% endblock %}

{% block extrahead %}
      <!--style>.md-typeset h1,.md-content__button {display:none !important}; </style-->
      <style>.md-header__topic {font-weight:700 !important}</style>
{% endblock %}
```

第二，创建 `overrides/partials/mycontent.html` 文件，内容参考 [`content.html`](https://github.com/squidfunk/mkdocs-material/blob/master/material/templates/partials/content.html) 文件，注意把 h1 的元素注释掉。
```
{#-
  This file was automatically generated - do not edit
-#}
{% if "material/tags" in config.plugins and tags %}
  {% include "partials/tags.html" %}
{% endif %}
{% include "partials/actions.html" %}
{% if "\x3ch1" not in page.content %}
  <!--h1>{{ page.title | d(config.site_name, true)}}</h1-->
{% endif %}
{{ page.content }}
{% include "partials/source-file.html" %}
{% include "partials/feedback.html" %}
{% include "partials/comments.html" %}
```

## 在页面中使用模板

例如，在个人站点的主页文件 `docs/index.md` 中头部，使用 `template` 指定使用的模板。
```
---
title: 维燕的知识花园
template: home.html
---
```

最后，重新启动 mkdocs 就可以看到对应页面 H1 隐藏后的效果。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="53"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
