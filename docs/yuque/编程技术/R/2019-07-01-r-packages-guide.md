---
title: R 包初学者指南
urlname: 2019-07-01-r-packages-guide
author: 章鱼猫先生
date: 2019-07-01
updated: "2022-09-15 10:02:19"
---

> **本文以 Adolfo Álvarez 的《**[**R Packages: A Beginner's Tutorial**](https://www.datacamp.com/community/tutorials/r-packages-guide)\*\* 》中文版本为基础，对部分内容进行了扩展和部分调整，致力于为 R 初学者形成一个更加系统化完善化的 R 软件安装配置与学习使用指南!\*\*

基于 11 个最常见的用户问题介绍 R 软件包。

R 包是由社区开发（developed by the community）的功能（functions）和数据集（data sets）的集合。 它们通过改进现有的基本 R 功能或通过添加新功能来提升 R 的效率。 例如，如果您经常使用数据框，可能您会听说 dplyr 或 data.table 这两个最流行的 R 包。

但是想象一下，您想要对韩文的文本进行一些自然语言处理，从网络中提取天气数据，甚至使用地表能量平衡模型（land surface energy balance models）估算实际蒸散量，R 包都可以帮到您！ 截止最近，R 的官方存储库（CRAN）已经发布的包就接近了 10,000 个，除此以外还有更多通过互联网公开发布的其他 R 包。

如果您刚开始使用 R，今天的文章将介绍 R 软件包的基础知识以及如何使用它们。 您将涵盖以下主题和 11 个常见问题用户问题：

- R 软件包的基础知识：什么是软件包，为什么要将它们用于您的 R 体验？ 你在哪里可以找到包裹？
- 安装和使用：如何从 CRAN，CRAN 镜像，Bioconductor 或 Github 安装软件包？ 有哪些与 install.packages() 相关的函数以及可用于更新，删除,......包的函数？ 如何使用用户界面安装软件包？ 你如何加载 R 包？ R 中的包和库有什么区别？ 如何同时加载多个包？ 如何卸载 R 包？
- 文档：除了 DESCRIPTION 文件之外，是否还有其他文档来源以及如何使用它们？
- 在 R 包之间进行选择：您如何找到适合您的分析的包？

如果您是一位经验丰富的用户，您可以随时学习新内容（例如我在前一段中提到的三个软件包的名称）。 无论如何，欢迎阅读 R 包的介绍以及如何使用它们！

# 1. 什么是包

让我们从一些定义开始。 包是用于组织您自己工作的一种合适方式（a suitable way），如果您愿意，也可以与他人分享。 通常，包将包含代码（不仅仅 是 R 代码！），包及内部函数相关的文档，一些以检查一切是否正常工作的测试（some tests to check everything works as it should），以及数据集。

[DESCRIPTION 文件](https://cran.r-project.org/doc/manuals/r-release/R-exts.html#The-DESCRIPTION-file) 提供了有关包的基本信息，您可以在其中找到包的功能，作者是谁，文档所属的版本，日期，使用的许可类型以及包依赖性。

请注意，您也可以单击 [此处](https://stat.ethz.ch/R-manual/R-devel/library/stats/DESCRIPTION) 查看 DESCRIPTION 文件。

除了查找诸如 [cran.r-project.org](http://cran.r-project.org) 或 [stat.ethz.ch](http://stat.ethz.ch) 之类的 DESCRIPTION 文件之外，您还可以使用命令 `packageDescription("package")` 通过包帮助文档访问 R 中的描述文件 `help(package = "package")`，或在线访问存储库（repository）中 R 包。

例如，对于 "stats" 包，这些方法将是：

```r
packageDescription("stats")
help(package = "stats")
```

# 2. 什么是存储库

存储库（repository）是包所在的位置，因此您可以从存储库中安装 R 包。 虽然您或您的组织可能拥有本地存储库，但通常它们是在线并且可供所有人访问的。 R 软件包最受欢迎的三个存储库是：

- [CRAN](https://cran.r-project.org/)：官方存储库，它是一个由全球 R 社区维护的 ftp 和 Web 服务器网络。 它是由 R 基金会协调的，对于要在此发布的包，它需要通过几个测试，以确保包遵循 CRAN 策略。 你可以在 [这里](https://cran.r-project.org/web/packages/policies.html) 找到更多细节。
- [Bioconductor](https://www.bioconductor.org/)：这是一个专题库，用于生物信息学的开源软件。 作为 CRAN，它有自己的 [提交和审核流程](https://www.bioconductor.org/developers/package-submission/)，其社区非常活跃，每年举行多次会议。
- [Github](https://github.com/)：虽然这不是 R 特有的，但 github 可能是开源项目中最受欢迎的存储库。 它的受欢迎程度来自于开源的无限空间，与 git 的集成，版本控制软件以及与其他人共享和协作的便利性。 但请注意，没有与之相关的审核流程。

# 3. 如何安装 R 包

## 从 CRAN 安装

如何安装软件包取决于它的位置。 因此，对于公开可用的包，这意味着它属于哪个存储库。 最常见的方法是使用 CRAN 存储库，然后只需要包的名称并使用命令 `install.packages（"package"）`。

例如，y 已经在 CRAN 中发布，并且仍然在线并正在更新的最早的软件包是来自 Daniel Adler 的 `vioplot` 软件包。

你能找到它的发布日期吗？ 线索：在包装说明中。

要从 CRAN 安装它，您只需要使用：

```r
install.packages("vioplot")
```

运行上面的命令后，您将在屏幕上收到一些消息。 它们将取决于您使用的操作系统，依赖性以及是否成功安装了包。

让我们深入了解一下 vioplot 安装的输出，你可能得到的一些消息是：

```r
Installing package into ‘/home/username/R/x86_64-pc-linux-gnu-library/3.3’
(as ‘lib’ is unspecified)
```

这表示您的计算机上安装了软件包的位置，您可以使用 lib 参数提供不同的文件夹位置。

```r
trying URL 'https://cran.rstudio.com/src/contrib/vioplot_0.2.tar.gz'
Content type 'application/x-gzip' length 3801 bytes
==================================================
downloaded 3801 bytes
```

在这里，您将收到有关包裹的来源和大小的信息。 这取决于您选择的 CRAN 镜像。

您也可以更改它，但稍后您将在本文中阅读更多相关内容。

```r
* installing *source* package ‘vioplot’ ...
** R
** preparing package for lazy loading
** help
*** installing help indices
** building package indices
** testing if installed package can be loaded
* DONE (vioplot)
```

这些是安装本身的消息，源代码，帮助，一些测试，最后是一切顺利的消息，并且包已成功安装。 根据您的平台，这些消息可能有所不同。

```r
The downloaded source packages are in
    ‘/tmp/RtmpqfWbYL/downloaded_packages’
```

最后一条信息告诉您下载后包的原始文件位于何处。 它们不是使用包所必需的，因此通常它们是被复制到了临时文件夹位置。

最后，要一次安装多个包，只需在 `install.packages()`函数的第一个参数中将它们写为字符向量：

```r
install.packages(c("vioplot", "MASS"))
```

## 从 CRAN 镜像中安装

请记住，CRAN 是一个服务器网络（每个服务器称为"镜像（mirror）"），因此您可以指定要使用的服务器。 如果您通过 RGui 接口使用 R，则可以通过从使用 `install.packages()`命令后出现的列表中选择它来完成。 在 RStudio 上，默认情况下已选择镜像。

您还可以使用 `chooseCRANmirror()`选择镜像，或使用 `repo` 参数直接在 `install.packages()`函数内选择镜像。 您可以使用`getCRANmirrors()`或直接在此 [链接](https://cran.r-project.org/mirrors.html) 上查看可用镜像列表。

示例：要使用 Ghent University Library 镜像（比利时）安装 vioplot 软件包，您可以运行以下命令：

```r
install.packages("vioplot", repo = "https://lib.ugent.be/CRAN/")
```

示例：使用清华大学镜像安装`**vioplot**`包：

```r
options("repos"=c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
install.packages('vioplot')
```

## 安装 Bioconductor 包

> Bioconductor 是和 R 版本绑定的，这是为了确保用户不把包安装在错误的版本上。Bioconductor 发行版每年更新两次，它在任何时候都有一个发行版本（release version），对应于 R 的发行版本。此外，Bioconductor 还有一个开发版本（development version），它对应于 R 的开发版本。
>
> R 每年（通常是 4 月中旬）在 'x.y.z' 中发布一个 '.y' 版本，但 Bioconductor 每 6 个月（4 月中旬和 10 月中旬）发布一个 '.y' 版本。
>
> Bioconductor 与 R 各自对应的版本如下：（参考：[Bioconductor releases](https://bioconductor.org/about/release-announcements/)）
> ![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkXS0_Pc5QLBO1v0i83uWMVnnkF3.png)

```r
BiocManager::version()
## '3.8'
```

### Bioconductor <= 3.7

对于 Bioconductor，在 R-3.5（Bioconductor-3.7） 前安装包的标准方法是首先执行以下脚本：

```r
source("https://bioconductor.org/biocLite.R")
```

这将安装安装 bioconductor 包所需的一些基本功能，例如 `biocLite()`函数。 如果你想安装 Bioconductor 的核心软件包，只需输入它而不需要进一步的参数：

```r
biocLite()
```

但是，如果您只对此存储库中的一些特定包感兴趣，则可以直接键入它们的名称作为字符向量：

```r
biocLite(c("GenomicFeatures", "AnnotationDbi"))
```

### Bioconductor >= 3.8

从 R-3.5（Bioconductor-3.8）起，Bioconductor 更改了 R 包的安装方式：它们通过发布在 CRAN 的 `[BiocManager](https://cran.r-project.org/web/packages/BiocManager/index.html)` 包来对 Bioconductor 的包进行安装和管理——通过 CRAN 安装 `BiocManager`，再通过这个包来安装 Bioconductor 的包。

```r
#设置 Bioconductor 镜像
options(BioC_mirror="https://mirrors.tuna.tsinghua.edu.cn/bioconductor")

# 安装 Bioconductor 的 R 包
BiocManager::install(c("GenomicRanges", "Organism.dplyr"))
```

## 通过 devtools 安装

如上所述，每个存储库都有自己的方法安装各自对应的包，因此，如果您经常使用来自不同来源的包，这可能会有点令人沮丧。 更有效的方法可能是使用 devtools 包来简化此过程，因为它包含了每个存储库的特定功能，包括 CRAN。

您可以像往常一样使用 `install.packages("devtools")` 安装 `devtools`，但您可能还需要在 Windows 上安装 Rtools，在 Mac 上安装 Xcode 命令行工具，或在 Linux 上安装 `r-base-dev` 和 `r-devel`。 [这里](https://www.rstudio.com/products/rpackages/devtools/) 有关于 devtools 和安装的更多细节。

安装 devtools 后，您将能够使用实用程序功能来安装另一个软件包。 选项是：

- `install_bioc()` from [Bioconductor](https://www.bioconductor.org/)
- `install_bitbucket()` from [Bitbucket](https://bitbucket.org/),
- `install_cran()` from [CRAN](https://cran.r-project.org/index.html),
- `install_git()` from a [git](https://git-scm.com/) repository,
- `install_github()` from [GitHub](https://github.com/),
- `install_local()` from a local file,
- `install_svn()` from a [SVN repository](https://subversion.apache.org/),
- `install_url()` from a URL, and
- `install_version()` from a specific version of a CRAN package.

例如，要从其 GitHub 存储库安装 [babynames ](https://github.com/hadley/babynames)包，您可以使用：

```r
# From github
devtools::install_github("hadley/babynames")

# From local
devtools::install_local("babynames.zip")
```

# 4. 如何更新，删除和检查已安装的软件包

在你花费更多时间使用 R 之后，你每周甚至每天都会使用`install.packages()` 几次是正常的，考虑到 R 软件包的开发速度，你可能需要更新或者更换你心爱的 R 包。 在本节中，您将找到一些可以帮助您管理集合的功能。

- 要检查计算机上已经安装的 R 软件包，您可以使用：

```r
installed.packages()
```

- 使用 `remove.packages()` 函数卸载软件包非常简单：

```r
remove.packages("vioplot")
```

- 您可以通过调用函数来检查需要更新的软件包：

```r
old.packages()
```

- 您可以使用以下命令更新所有包：

```r
update.packages()
```

- 对于特定的包，只需再次使用 `install.packages()` 即可升级：

```r
install.packages("vioplot")
```

# 5. 是否有用于安装包的用户界面

如果您更喜欢图形用户界面来安装包，则 RStudio 和 RGui 都包含它们。 在 RStudio 中，您可以在"工具" -> "安装包"中找到它，然后您将在弹出窗口中键入要安装的包：
![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/content_rstudio1.png/bioinit#id=jTQdU&originHeight=354&originWidth=485&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

在 RGui 中，您将在"包（Packages）"菜单下找到实用程序。
![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/content_rgui1.png/bioinit#id=h2fxg&originHeight=195&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

# 6. 如何加载程序包

安装软件包后，您就可以使用其功能了。 如果您只需要在包中偶尔使用一些函数或数据，则可以使用符号 `packagename::functionname()` 来访问它们。 例如，由于您已安装 `babynames` 包，因此可以浏览其中一个数据集。

您还记得如何查看包中包含哪些功能和数据的概述？是的，`help(package = "babynames")` 可以告诉你这个。

要访问 `babynames` 包中的 `births` 数据集，只需键入：

```r
> babynames::births
# A tibble: 119 x 2
year  births
<int>   <int>
1  1909 2718000
2  1910 2777000
3  1911 2809000
4  1912 2840000
5  1913 2869000
6  1914 2966000
7  1915 2965000
8  1916 2964000
9  1917 2944000
10  1918 2948000
# ... with 109 more rows
```

如果您将更密集地使用该软件包，那么可能值得将其加载到内存中。 最简单的方法是使用 `library()` 命令。

请注意，`install.packages()`的输入是一个字符向量，并且要求名称在引号中，而 `library()` 接受字符或名称，这使您可以编写没有引号的包名称。

在此之后，您不再需要 `package::function()` 表示法，并且您可以像其他任何 R 基本函数或数据一样直接访问其功能：

```r
> library(babynames)
> births
# A tibble: 119 x 2
year  births
<int>   <int>
1  1909 2718000
2  1910 2777000
3  1911 2809000
4  1912 2840000
5  1913 2869000
6  1914 2966000
7  1915 2965000
8  1916 2964000
9  1917 2944000
10  1918 2948000
# ... with 109 more rows
```

您可能已经听说过 `require()` 函数：确实可以使用此函数加载包，但区别在于如果未安装包，它不会引发错误。所以请仔细使用此功能！

提示：[这里](https://yihui.name/en/2014/07/library-vs-require/) 强烈推荐一篇关于此主题的文章。

# 7. Package 和 Library 的区别

说到 `library()` 函数，有时候包和库之间会有混淆，有时候你可以返现人们会把库（libraries）也叫成包（packages）。

请不要混淆：`library()` 是用于加载包的命令，它指的是包含包的位置，通常是计算机上的文件夹，而包（package）是方便地捆绑的函数的集合。

也许可以引用来自 RStudio 的首席数据科学家 Hadley Wickham 以及 "Writing functions in R" DataCamp 课程讲师的对话说明一下：

> **@ijlyttle a package is a like a book, a library is like a library; you use library() to check a package out of the library #rsats**

> **— Hadley Wickham (@hadleywickham) December 8, 2014**

关于这两者之间的区别，一个更好的例子是运行不带参数的 `library()`。它将为您提供计算机上不同库中安装的软件包列表：

```r
library()
```

# 8. 如何一次加载多个包

虽然您可以在 `install.packages()` 函数中输入一组名称向量来同时安装多个包，但在 `library()` 函数的情况下，这是不可能的。 您可以一次加载一组软件包，或者如果您愿意，可以使用 R 用户开发的众多解决方法之一。

您可以在 [this Stack Overflow discussion](https://stackoverflow.com/questions/8175912/load-multiple-packages-at-once)，[this R package](https://cran.r-project.org/web/packages/easypackages/README.html) 和 [this GitHub repository](https://gist.github.com/stevenworthington/3178163) 中找到示例。

# 9. 如何卸除已加载的包

要卸除已加载的包，可以使用 `detach()` 函数。

```r
detach("package:babynames", unload=TRUE)
```

# 10. 有什么文档和帮助的替代来源

正如您在上面的部分中所读到的那样，DESCRIPTION 文件包含有关包的基本信息，即使该信息非常有用，也无法帮助您使用此包进行分析。 然后，您将需要另外两个文档源：帮助文件和小品文（vignettes）。

## Help Files

与基础的 R 一样，命令 `?()` 和 `help()`是开始使用软件包时的第一个文档源。 你可能记得你可以使用 `help(package = "packagename") 来获得包的一般概述，但是如果尚未加载包得情况下，每个函数都可以通过`help("name of the function")`或`help(function, package = "package")\` 来单独探讨，您通常会在其中找到函数及其参数的描述以及应用程序示例。

例如，您可能记得要从 `vioplot` 包中获取 `vioplot` 命令的帮助文件，您可以键入：

```r
help(vioplot, package = "vioplot")
```

\*\*提示：\*\*您还可以使用其他方式查看已加载包中的内容。 如使用 `ls()` 命令：

```r
> library(babynames)
> ls("package:babynames")
[1] "applicants" "babynames"  "births"     "lifetables"
```

## Vignettes

大多数软件包中包含的另一个非常有用的帮助来源是小品文（Vignettes），这些小文件是作者以更详细的方式显示其软件包的一些功能的文档。跟随着小品文是一个可以让你手把手去熟悉 R 包常见用途的好方法，所以在做您自己的分析之前，这是一个开始使用它的完美方法。

您可能还记得，给定包中包含的 vignettes 信息也可以在本地或在线的 DOCUMENTATION 文件中找到，但您也可以使用函数 `browseVignettes()` 获取已安装包中包含的所有 vignettes 列表。对于想要获取某一个特定 package 的 vignettes，我们只需要输入一个该包的名称作为参数即可：\`browseVignettes(package ="packagename")。上面的这两种情况下，都会打开一个浏览器窗口，以便您可以轻松地浏览或者点击您喜欢的 vignette 进去查看。

如果您希望留在命令行中，则可以使用 `vignette()` 命令显示所有的 vignettes 列表，`vignette(package = "packagename")` 命令可以查看某一个指定包中包含的 vignettes 内容。找到所需的内容后探索，只需使用\`vignette("vignettename") 命令，即可查看该 vignettename 的详细信息 。

例如，ggplot2 是最受欢迎的可视化包之一。您可能已经在计算机上安装了它，但如果没有，这是您实现它并测试新的 `install.packages()` 技能的机会。

假设您已经安装了 ggplot2，您可以检查其中包含的插图：

```r
> vignette(package = "ggplot2")

Vignettes in package ‘ggplot2’:

ggplot2-specs           Aesthetic specifications (source, html)
extending-ggplot2       Extending ggplot2 (source, html)

(END)
```

ggplot2 有两个 vignettes："ggplot2-specs" 和 "extends-ggplot2"。 您可以通过以下方式检查第一个：

```r
vignette("ggplot2-specs")
```

在 RStudio 上，这将显示在右侧的 "帮助" 选项卡上，而在 RGui 或命令行中，这将打开带有 vignette 的浏览器窗口。

在 [此链接](https://www.r-project.org/help.html) 上，您可以找到更多有关从 R 获得帮助的选项。

# 11. 如何选择合适的 R 包

此时，你应该可以安装并从你的 R 包中获得最大的收益，但仍然有一个最后的问题：你在哪里找到你需要的软件包？

发现包的典型方法是通过学习 R，在许多教程和课程中，通常会提到最流行的包。 DataCamp 课程在这里就是一个很好的例子："[Cleaning Data in R](https://www.datacamp.com/courses/cleaning-data-in-r)" 教授了所有关于 'tidyr' 包的使用知识，"[Data Analysis in R, the data.table Way](https://www.datacamp.com/courses/data-table-data-manipulation-r-tutorial)" 讲述如何使用 `data.table` 包进行数据处理，等等。

对于您想要通过 R 中去解决的每个主题，您可以找到一个有趣的包。但是如果你有一个特定的问题并且你不知道从哪里开始怎么办，例如，正如我在这篇文章的介绍中所说的那样，如果你有兴趣分析一些韩文的文本怎么办？或者如果你想收集一些天气数据怎么办？ 或估计蒸发蒸腾量？

您已经查看了几个存储库，是的，您也知道在这里可以查看 CRAN 包列表，但是有超过 10000 个选项，很容易你就迷失方向了。

让我们来看看一些替代方案！

由于 CRAN 具有任务视图，一种替代方案可以是浏览 CRAN 包的类别。 那就对了！ CRAN 官方存储库，还为您提供浏览包的选项。 任务视图基本上是基于其功能对包进行分组的主题或类别。

如您所见，所有与遗传有关的包都将在 "遗传学（Genetics）" 任务视图中进行分类：
![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/cran_task_views.png/bioinit#id=ZeMUq&originHeight=355&originWidth=643&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

以韩语文本为例，您可以通过导航到自然语言处理任务视图轻松找到所需的包。 在那里，您可以阅读文本以查找可以处理文本的包，或者您可以执行简单的 `CTRL + F` 并键入您要查找的关键字。保证，您可以立即获得正确的包！

查找软件包的另一种方法可以是 RDocumentation，它是来自 CRAN，BioConductor 和 GitHub 的 R 软件包的帮助文档聚合器，它直接在主页面上为我们提供了搜索框。

你可能还不知道这第二种选择，所以让我们深入挖掘一下！让我们从韩语文本开始，RDocumentation 的一个有趣特性是快速搜索，所以当你输入一点点关键字时会就出现第一与之匹配的结果：
![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/rdocumentation.png/bioinit#id=SbJFx&originHeight=506&originWidth=943&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

但是，如果您输入关键词 "korean" 并单击"搜索"，我们将进行完整搜索，您将获得两列结果：左侧的包，右侧的功能。

关注 packages 列，我们可以在每个结果中获取到包的名称，包含更详细信息的链接，作者姓名，也可链接以查看来自同一作者的其他包，以及带有搜索关键字高亮显示的包的一些描述，以及有关包的流行度的信息。
![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/rdocumentation_korean.png/bioinit#id=PNBTn&originHeight=550&originWidth=1317&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

谈到流行度，这是紧密相关的，因为搜索将首先对下载次数最多的包进行排名，以提高结果的准确性。 如果您想了解有关 RDocumentatio n 的搜索实现的更多详细信息，在 [此处](https://www.datacamp.com/community/blog/rdocumentation-ranking-scoring) 提供了非常详细的帖子。

因此，似乎 `KoNLP` 软件包可以满足您的需求，点击其名称后，您将获得以下信息：

- 一个包含了程序包名称、作者、版本、选择旧版本的选项、下载数量以及指向其 RDocumentation 页面的链接的表头。
- 包的说明。
- 包中包含的函数列表，其中每个函数都是可单击的，因此您可以获得有关函数使用的更多详细信息。
- 基于下载次数的变化的曲线图。
- 来源于 DESCRIPTION 文件的包详细信息。
- 最后，是一个包含在包的 README 文件中，指向 RDocumentation 链接的 badge 标记。

RDocumentation 不仅是一个搜索引擎，它还为您提供了一些更好的选择来发现和了解 R 包和函数：

- 就像 CRAN 任务视图一样，RDocumentation 也提供了 [任务视图](https://www.rdocumentation.org/taskviews#Bayesian)：正如你上面读到的那样，它是按主题探索 R 包的另一种方式。 例如，您可以获得与 Graphics，Finance 或 Time Series 相关的包列表。
- [排行榜（Leaderboard）](https://www.rdocumentation.org/trends)。此模式提供关于以下内容的一个概览：最受欢迎的软件包和开发人员，最新的软件包和更新，以及关于下载分布（Downloads distribution）、最常用关键词（Most used keywords）、Top packages dependency graph 相关的 3 个图形，您可以在其中查看最受欢迎的软件包相互之间的关联性，你也可以找到不同分组的包（用不同的颜色标识）。
  ![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/rdocumentation_trends.png/bioinit#id=bYcMV&originHeight=548&originWidth=644&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)
- [RDocumentation package](https://github.com/datacamp/Rdocumentation)。 `RDocumentation` 不仅是一个网站，也是一个 R 包。 它会覆盖帮助功能，因此您可以将 `RDocumentation` 的功能整合到您的工作流程中。 加载此包后，`help()` 函数将打开一个浏览器窗口或带有 `RDocumentation` 访问权限的 RStudio 帮助面板。

---

直接在 R 或 RStudio 面板上使用 RDocumentation 比网站使用提供了一些优势：

- 检查已安装的软件包版本。 程序包的帮助窗格将为您提供与网页相同的信息（下载，说明，功能列表，详细信息），以及有关已安装的程序包版本的信息。例如，检查先前安装的 vioplot 软件包：

```r
install.packages("RDocumentation")
library(RDocumentation)
help(package = "vioplot")
```

- 能够直接从帮助面板安装或更新软件包。 我知道现在你是安装软件包的专家，但是你可以通过点击 RDocumentation 提供的帮助面板上的一个按钮来实现它。

```r
remove.packages("vioplot")
help(package = "vioplot")
```

![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/rdocumentation_help_install.png/bioinit#id=yMaUz&originHeight=198&originWidth=522&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

- 运行并提出示例。 包中函数的帮助窗格将为您提供仅通过单击按钮就可以再次运行示例的选项。 您还可以提出可以合并到帮助页面并由其他 R 用户测试的示例。

```r
install.packages("vioplot")
help(vioplot)
```

![](https://note-db.oss-cn-shenzhen.aliyuncs.com/2018/09/29-Sat/topics_vioplot.png/bioinit#id=zuE8s&originHeight=1053&originWidth=1175&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=)

- [RDocumentation API](https://www.rdocumentation.org/docs/)。最后，RDocumentation 不仅是一个网站和一个 R 包，还是一个 API。 对于需要更多灵活性的更高级用户，[RDocumentation.org](http://RDocumentation.org) 提供了具有其网页功能的 JSON API。

# 总结

本文章涵盖了广泛的通过使用包来从 R 中获得最大收益的相关技术（techniques）和功能（functions）。 像往常一样，在 R 中执行某项任务的方法不止一种，管理包也不例外。

我希望今天您已经学习了最常用的和一些替代方法来发现，安装，加载，更新，获取帮助或删除软件包。

我知道这篇文章没有详细介绍有关包的内部结构或如何创建自己的包。 请继续关注 DataCamp 的博客以及这些和其他主题相关的课程，但与此同时，您可以在 [这里](http://r-pkgs.had.co.nz/) 找到一本很好的 "R packages" 参考书。

我差点忘了，如果你通过搜索 RDocumentation 还没有发现什么东西，我可以告诉你，使用 [weatherData](https://www.rdocumentation.org/packages/weatherData) 你可以从互联网上提取天气数据，如果你对蒸发蒸腾感兴趣，也许你应该看看 [Evapotranspiration](https://www.rdocumentation.org/packages/Evapotranspiration/versions/1.10)， [water](https://www.rdocumentation.org/packages/water/versions/0.5) 或 [SPEI](https://www.rdocumentation.org/packages/SPEI/versions/1.6) 包。
