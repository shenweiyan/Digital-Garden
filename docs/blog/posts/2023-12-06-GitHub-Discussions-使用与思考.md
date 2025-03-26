---
title: GitHub Discussions 使用与思考
number: 38
slug: discussions-38/
url: https://github.com/shenweiyan/Digital-Garden/discussions/38
date: 2023-12-06
authors: [shenweiyan]
categories: 
  - 乱弹
labels: ['公众号']
---

从2023年7月起我所有可公开的文档都保存在了 [GitHub Discussions](https://github.com/shenweiyan/Knowledge-Garden/discussions) 上，作为博客、IED 编辑器，以及评论使用，GitHub Discussions 是完全没问题的。

<!-- more -->

## 开源的代名词

开源已成为 GitHub 的代名词。

> 当开发者谈论开源时，通常会想到 GitHub，它不仅仅是一个代码托管平台，更是一个汇聚了全球开发者的社交中心。过去，开发者发布一款软件后，都是在自己的小圈子里默默努力和交流，现在通过 GitHub 平台可以方便地与全球的开发者分享、交流和协作。贡献者在这里展示自己的才华，追随者在这里寻找强者的脚印，等待着被世人认可的时刻。

## 体验与感受

由于 GitHub 是直接 markdown 源码进行书写，正常的导出基本不会有格式错乱的问题，这一点非常好。不像有一些富文本的编辑器，动不动就给你增加几个换行或者空格什么的额外字符。

借助 GitHub GraphQL API + Python + GitHub Actions 进行每天定时导出非常顺滑，导出来的文档可以随意折腾，自由度非常大。

## 专业书籍文档

今天忽然想到的一个问题，即如果作为专业性比较强的系列文档写作，如《[Hello 算法](https://www.hello-algo.com/)》 这样专业性和逻辑性非常明确的专业书籍，使用 GitHub Discussions 写作应该是有点不太合适。

但又仔细想了一下，如果**只是写作**应该是没问题的 —— 我们可以用 sections 或者 categories，甚至是 tags 进行书籍分类，最后在导出的时候借助这些标签把相关的文档整合到一块，再借助 nav 梳理成大纲展现给读者阅读就可以。所以，总的来说可以用于专业书籍**写作(编辑)**，但**不太适合用于专业书籍的呈现和阅读** —— 主要是大纲和逻辑性会变得不明显。

## 目录和分类标签

GitHub Discussions 目前[最多支持 25 个 categories](https://github.com/orgs/community/discussions/7960)，这是一个限制。因此，通过 section+category 我们在 Discussions 上最多只能实现两级的目录结构，所以对于三级和三级以上的目录结构目前暂时无能为力。

因此，想到一个折中的解决方法：使用 labels 来区分第三级目录结构。
```
1.1-生信
  - 1.1.1-算法
  - 1.1.2-数据
  - 1.1.2-软件
```

然后，导出 Discussions 的时候需要在本地先在本地建立一个 `section+category: dictory` 一一对应的字典，最后通过这个字典把不同的讨论 md 归档至对应的目录。
```
1.1-生信:
    1.1.1-算法: docs/cookbook/生物信息/算法
    1.1.2-数据: docs/cookbook/生物信息/数据
    1.1.2-软件: docs/cookbook/生物信息/软件
    ...
```

## GitHub GraphQL API

GitHub Discussions 的 API 操作主要依赖 [GitHub GraphQL API](https://docs.github.com/zh/graphql/overview/about-the-graphql-api)。

> ## 概述
> 
> GraphQL 是一种用于[应用编程接口（API）](https://www.redhat.com/zh/topics/api/what-are-application-programming-interfaces)的查询语言和服务器端运行时，它可以使客户端准确地获得所需的数据，没有任何冗余。
>    
> ## GraphQL 有什么用？    
> GraphQL 旨在让 API 变得快速、灵活并且为开发人员提供便利。它甚至可以部署在名为 [GraphiQL](https://github.com/graphql/graphiql) 的[集成开发环境（IDE）](https://www.redhat.com/zh/topics/middleware/what-is-ide)中。作为 [REST](https://www.redhat.com/zh/topics/integration/whats-the-difference-between-soap-rest) 的替代方案，GraphQL 允许开发人员构建相应的请求，从而通过单个 API 调用从多个数据源中提取数据。
>    
> 此外，GraphQL 还可让 API 维护人员灵活地添加或弃用字段，而不会影响现有查询。开发人员可以使用自己喜欢的方法来构建 API，并且 GraphQL 规范将确保它们以可预测的方式在客户端发挥作用。
>    
> From：《[什么是 GraphQL？核心概念解析](https://www.redhat.com/zh/topics/api/what-is-graphql)》- 红帽

- 中文文档：https://docs.github.com/zh/graphql/guides/introduction-to-graphql
- 在线使用：https://docs.github.com/en/graphql/overview/explorer

### 获取 discussions 主要信息
```
{
  repository(owner: "shenweiyan", name: "Knowledge-Garden") {
    discussions(orderBy: {field: CREATED_AT, direction: DESC}, categoryId: null, first: 5) {
      nodes {
        title
        number
        url
        createdAt
        lastEditedAt
        updatedAt
        body
        bodyText
        bodyHTML
        author {
          login
        }
        category {
          name
        }
        labels(first: 100) {
          nodes {
            name
          }
        }
        comments(first: 10) {
          nodes {
            body
            author {
              login
            }
          }
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```


### 获取 discussions categoryId

参考：《[how to get github discussions categoryId](https://qiita.com/shooter/items/d59fbb43d0f118c95092)》

```
{
  repository(owner: "shenweiyan", name: "Knowledge-Garden") {
    id
    name
    discussionCategories(first: 30) {
      nodes {
        id
        name
      }
    }
  }
}
```

### 其他的一些问题

目前，通过 GitHub GraphQL API 暂时无法获取 Sections 的信息。

## 简单的总结

拥抱 GitHub Discussions 的一个前提是你可以随时登录 GitHub，如果你已经解决了这个问题，也想着像我一样 Using Github discussions as your blog engine，那么你可以参考一下我的 [shenweiyan/Knowledge-Garden](https://github.com/shenweiyan/Knowledge-Garden/) 仓库。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="38"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
