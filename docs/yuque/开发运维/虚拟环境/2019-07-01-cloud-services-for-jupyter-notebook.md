---
title: 基于云的六大 Jupyter Notebook 平台测评
urlname: 2019-07-01-cloud-services-for-jupyter-notebook
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-30 09:38:08"
---

**作\*\*\*\*者：**[Kevin Markham](https://twitter.com/justmarkham)
\*\*编译：\*\*Steven Shen
**原文：**<https://www.dataschool.io/cloud-services-for-jupyter-notebook/>

![1_oj36TMqOkHmi6u3kCSsr7Q.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmI-XQJskzKJrjXg9rD0pZPaF0g0.png)

有许多方法可以与其他人共享静态 Jupyter 笔记本，例如把它发布在 GitHub 上或通过 nbviewer 链接进行分享。 但是，如果接收人已经安装了 Jupyter Notebook 环境，那么他们只能通过笔记本文件进行交互。

但是，如果您想分享一个不需要安装任何东西的全交互式 Jupyter 笔记，该怎么办？ 或者，您只想要创建一个自己的 Jupyter 笔记但又不想在本地计算机上安装任何东西？

在这篇文章中，我将回顾六种可以用来在云端轻松运行 Jupyter 笔记的服务。所有这些服务都具有以下特征：

- 它们不需要在你的本地计算机上安装任何东西。
- 它们都是完全免费的（或者它们有自己的免费计划）。
- 它们都可以让你访问 Jupyter Notebook 环境（或类似 Jupyter 的环境）。
- 它们都持 Python 语言（并且大多数支持其他语言）。

由于所有的这些都是基于云的服务，如果您仅限于使用内部部署的数据，则它们都不适合您。

## 比较标准

以下是我对六种服务进行比较的标准：

- **支持的语言：**  此服务是否支持除 Python 以外的其他编程语言？
- **安装软件包：**  除了已安装的软件包，此服务是否允许您安装其他软件包（或特定版本的软件包）？
- **界面相似性：**  如果服务提供的是 "Jupyter-like" 界面（而不是原生的 Jupyter 界面），它与 Jupyter 的界面有多相似？ （这会使地已有的 Jupyter 用户更容易转换到该服务。）
- **键盘快捷键：**  此服务是否使用了与 Jupyter Notebook 相同的键盘快捷键？
- **缺少的功能：**  在 Jupyter Notebook 中可以执行的操作，在此服务不支持？
- **新增的功能：** Jupyter Notebook 中不支持的操作，此服务可以实现支持吗？
- **数据集易用性：**  此服务可以轻松地使用您自己的数据集吗？
- **网络访问：**  此服务是否允许您从 Notebook 中访问 Internet，以便在必要时可以从 URL 读取数据？
- **保证工作私密性：**  这项服务是否能允许保持你工作的私密性？
- **公开分享：**  此服务是否能为您提供公开分享作品的方式？
- **协作能力：**  此服务是否允许您邀请某人在笔记本上进行协作，并且协作是否可以实时进行？
- **免费计划的性能表现：**  该服务提供哪些计算资源（RAM 和 CPU）？ 它是否允许您访问 GPU（这对深度学习很有用）？ 包含多少磁盘空间？ 会话可以运行多长时间？
- **性能升级：**  您是否可以为此服务付费以获取更多计算资源？
- **文档和技术支持：**  该服务是否有详细记录？ 如果遇到问题，你可以与某人取得联系吗？

## 1. Binder

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FglCc-7KKOQBnabvlJeE2wwrSFbg.png)

[Binde](https://mybinder.org/)r 是 Binder 项目提供的服务，它是 Project Jupyter 开源生态系统的一员。它允许您输入任何公共 Git 存储库的 URL，它将在本机的 Jupyter Notebook 界面中打开该存储库。您可以在存储库中运行任何笔记本，但您所做的任何更改都不会保存回存储库。您不必使用 Binder 创建帐户，也不需要是存储库的所有者，但你所使用的存储库必须包含指定其软件包要求的配置文件。

**支持的语言：**
支持  Python (2 and 3), R, Julia，以及  [Jupyter 支持的其他任何语言](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)。

**安装软件包：**
您可以使用[配置文件](https://mybinder.readthedocs.io/en/latest/config_files.html)（例如 environment.yml 或 requirements.txt）指定特定的包要求。

**界面相似度：** Binder 使用原生的 Jupyter Notebook 界面。

**键盘快捷键：** Binder 使用与 Jupyter 相同的所有键盘快捷键。

\*\*缺少的功能：\*\*无。

\*\*新增的功能：\*\*无。

**数据集易用性：**
如果您的数据集位于同一个 Git 存储库中，那么它将自动在 Binder 中可用。如果您的数据集不在该存储库中，但可以在任何公共 URL 上使用，那么您可以向存储库添加一个[特殊文件](https://github.com/binder-examples/getting-data)，告知 Binder 下载您的数据集。但是，Binder 不支持访问私有数据集。

\*\*网络访问：\*\*支持。

**保证工作私密性：**  不，因为它只适用于公共 Git 存储库。

**公开分享：**
支持。您可以分享直接连接到你个人 Binder 的  [URL](https://mybinder.org/v2/gh/justmarkham/pycon-2018-tutorial/master?filepath=tutorial.ipynb)，其他人也可以使用 Binder 网站运行您的笔记本（只要他们知道您的 Git 存储库的 URL）。

**协作能力：**
不支持。如果您想与同一个笔记本上的某个人合作，而您的存储库托管在 GitHub 上，那么您可以使用普通的拉取请求工作流程的方式进行协作。

**免费计划的性能表现：**
您最多可以使用 2GB 的 RAM。虽然它们要求您不要包含 "非常大的文件"（超过几百兆字节），但磁盘空间量没有特定限制。Binder 的[启动速度很慢](https://mybinder.readthedocs.io/en/latest/faq.html#what-factors-influence-how-long-it-takes-a-binder-session-to-start)，尤其是当它在最近更新的存储库上运行时。会话将在 20 分钟不活动后关闭，但它们可以运行 12 小时或更长时间。Binder 还有其他使用指南，包括对任何给定了存储库的 100 个并发用户的限制等。

**性能升级：**
不支持。但是，您可以选择设置自己的  [BinderHub](https://binderhub.readthedocs.io/en/latest/)  部署，它可以提供与 Binder 相同的功能，同时允许您自定义环境（例如增加计算资源或允许私有文件）。

**文档和技术支持：** 
Binder 有大量[文档](https://mybinder.readthedocs.io/en/latest/)。它通过  [Gitter](https://gitter.im/jupyterhub/binder)  聊天和  [Discourse](https://discourse.jupyter.org/)  论坛提供社区支持，并在  [GitHub](https://github.com/jupyterhub/binderhub/issues)  上跟踪产品问题。

**结论：**
如果您的笔记本已经存储在公共 GitHub 中，Binder 是让其他人与它们进行交互的最简单方法。用户不必创建帐户，如果他们已经知道如何使用 Jupyter Notebook，他们会感到宾至如归。但是，您需要牢记 Binder 的性能限制和用户限制！

## 2. Kaggle Kernels

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiByayBnDfsViNwGuiruJCfJuotz.png)

[Kaggle](https://www.kaggle.com/)  是最着名的数据科学竞赛平台。但是，他们还提供可以独立于竞争对手使用，名为  [Kernels](https://www.kaggle.com/kernels)  的免费服务。创建 Kaggle 帐户（或使用 Google 或 Facebook 登录）后，您可以创建一个使用笔记本或脚本界面的内核，但我更专注于下面提到的的笔记本界面信息。

\*\*支持的语言：\*\*只支持 Python3 和 R。

**安装软件包：**
Kaggle\*\* \*\*预先安装了数百个软件包，您可以使用 pip 或通过指定软件包的 GitHub 存储库来安装其他软件包。但是，您安装的任何其他软件包都需要在每个会话开始时重新安装。或者，您可以要求 Kaggle 在其默认安装中包含其他软件包。

**界面相似度：** 
在视觉上，Kernels 界面看起来与 Jupyter 界面完全不同。 屏幕顶部没有菜单栏或工具栏，右侧有可折叠的侧边栏，用于调整设置，并且笔记本下方有一个控制台。然而，在 Kernels 笔记本中工作实际上与在 Jupyter 笔记本中工作非常相似，特别是如果你对 Jupyter 的键盘快捷键感到满意的话。此外，请注意，[重新设计的界面](https://www.kaggle.com/product-feedback/83336)（如上面的屏幕截图所示）将很快发布，这更类似于 Jupyter 界面，并包含一个简单的菜单栏。

**键盘快捷键：**  内核使用了与 Jupyter 相同的所有键盘快捷键。

**缺少的功能：**

- 由于内核尚未包含菜单栏或工具栏，因此许多操作只能使用键盘快捷键或命令调色板完成。
- 您无法将笔记本下载为其他有用的格式，如 Python 脚本，HTML 网页或 Markdown 文件。

**新增的功能：**

- 内核包括了一个轻量级的版本控制系统。每次要保存工作时，都会有一个 "提交" 按钮，从上到下运行整个笔记本，并为历史记录添加新版本。（您可以在此过程中继续工作，这对于长时间运行的笔记本来说非常重要。）虽然您无法命名版本，但您可以在任何两个版本之间显示"差异"。
- 内核允许您有选择地隐藏任何代码单元的输入和/或输出，这样可以轻松自定义笔记本的演示文稿。

**数据集易用性：**  
您可以从本地计算机，URL 或  [GitHub 存储库](https://www.kaggle.com/product-feedback/77211)将数据集上传到 Kaggle，它将由另一个名为  [Datasets](https://www.kaggle.com/datasets)  的 Kaggle 服务免费托管。您可以将上传的数据集设为私有或公共。您上传的任何数据集以及其他 Kaggle 用户上传的任何公共数据集都可以被你的任何一个内核访问。每个数据集的最大大小为 20 GB，单个内核可以访问多个数据集。

**网络访问：**  允许。

\*\*保证工作私密性：\*\*支持。

**公开分享：** 
支持。如果您选择[公开您的内核](https://www.kaggle.com/justmarkham/tutorial)，则任何人都可以在不创建 Kaggle 帐户的情况下访问它，任何拥有 Kaggle 帐户的人都可以对您的内核发表评论或将其复制到自己的帐户。此外，Kaggle 还为您提供了一个[公共的  profile page](https://www.kaggle.com/justmarkham)，其中显示了所有公共内核和数据集。

**协作能力：** 
支持。您可以保持内核私有，但可以邀请特定的 Kaggle 用户查看或编辑它。没有实时协作：它更像是在单独的内核副本上工作，除了所有提交都添加到相同的版本历史记录中。

**免费计划的性能表现：** 
您可以使用具有 17GB RAM 的 4 核 CPU，或具有 14GB RAM 和 GPU 的 2 核 CPU。虽然数据集使用的任何磁盘空间都不计入这些数字，但您将拥有 5 GB 的 "已保存" 磁盘空间和 17 GB 的 "临时" 磁盘空间。会话将在 60 分钟不活动后关闭，但它们可以运行长达 9 个小时。

\*\*性能升级：\*\*支持。

**文档和技术支持：** Kaggle 内核有大量丰富的[文档](https://www.kaggle.com/docs/kernels)。用户可通过[表格的联系方式](https://www.kaggle.com/contact)和[论坛](https://www.kaggle.com/product-feedback)获得支持。

**结论：**
只要您对稍微混乱的界面（在重新设计中已得到改进）感到满意，您就可以访问高性能环境，在该环境中可以轻松使用数据集并公开分享您的工作 （或保持私密）。Kaggle 包含的版本控制和协作功能也是很好的功能补充，但两者都不是功能很齐全。

## 3. Google Colaboratory (Colab)

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fi9errwbCxeyVLKqqSmQ8oPAGdbm.png)

[Google Colaboratory](https://colab.research.google.com/)，通常称为"Google Colab"，适用于拥有 Google 帐户的任何人。只要您已登录 Google，就可以快速开始创建空笔记本，上传现有笔记本或从任何公共 GitHub 存储库导入笔记本。您的 Colab 笔记本会自动保存 在 Google 云端硬盘中的特殊文件夹中，您甚至可以直接从云端硬盘创建新笔记本。

**支持的语言：** 
支持 Python（2 和 3）和 Swift（2019 年 1 月添加）。也可以为其他语言安装内核，但安装过程因语言而异，并且没有详细记录。

**安装软件包：**
已预先安装了数百个软件包，您可以使用  `pip`  安装其他软件包。但是，您安装的任何其他软件包都需要在每个会话开始时重新安装。

**界面相似度：** 
在视觉上，Colab 界面看起来非常类似于 Jupyter 界面。然而，在 Colab 工作实际上感觉与在 Jupyter Notebook 中工作非常不同：

- 大多数菜单项都不同。
- Colab 改变了一些标准术语（"kernel" 被替换成了 "runtime"，"markdown cell" 被替换成了 "text cell"，等）。
- Colab 发明了一些我们必须了解的新概念，例如 "playground mode"。
- Colab 中的命令模式和编辑模式与 Jupyter 中的工作方式不同。

**键盘快捷键：** 
虽然 Colab 允许您自定义快捷方式，但在 Colab 中，Jupyter 使用的大多数单字母键盘快捷键（例如使用 "a" 快捷键实现 "insert cell above"）都已经更改为多步骤的组合键（"Ctrl + m" 后跟 "a"）。

**缺少的功能：**

- 由于 Colab 菜单栏缺少某些条目，且工具栏保持非常简单，因此某些操作只能使用键盘快捷键完成。
- 您无法将笔记本下载为其他有用的格式，例如 HTML 网页或 Markdown 文件（虽然您可以将其下载为 Python 脚本）。

**新增的功能：**

- Colab 包括了一个轻量级版本控制系统。它经常用于保存笔记本的当前状态，您可以浏览修订历史记录。但是，您无法在版本之间显示"差异"，这意味着各个版本之间的任何比较您都必须手动进行操作。
- Colab 允许您将[表单字段](https://colab.research.google.com/notebooks/forms.ipynb)添加到笔记本中，这使您能够以交互的方式参数化代码。但是，这些字段仅适用于 Colab。
- 当您在笔记本中创建一个章节标题时，Colab 会使每个章节都可折叠，并在侧边栏中自动创建"目录"，这使得大型笔记本更容易导航。

**数据集易用性：** 
您可以上传数据集以在 Colab 笔记本中使用，但一旦结束会话，它将自动删除。或者，您可以允许 Colab 从您的 Google 云端硬盘读取文件，虽然它比较[复杂](https://colab.research.google.com/notebooks/snippets/drive.ipynb)。 Colab 还包括其他 Google 服务的连接器，例如 Google 表格和 Google 云端存储。

**网络访问：**  支持。

**保证工作私密性的能力：**  支持。

**公开分享的能力：**
支持。如果您选择公开您的笔记本并分享链接，则任何人都可以在不创建 Google 帐户的情况下访问该笔记本，并且拥有 Google 帐户的任何人都可以将其复制到他们自己的帐户。此外，您可以授权 Colab 将 笔记本的副本保存到 GitHub 或 Gist，然后从那里共享。

**协作能力：**
支持。您可以将笔记本设置为私密，但可以邀请特定人员查看或编辑它（使用 Google 熟悉的共享界面）。您和您的协作者可以同时编辑笔记本并查看彼此的更改，并为彼此添加注释（类似于 Google 文档），尽管在您在执行更改和合作者看到它们之间有 30 秒的延迟。此外，您实际上并未与协作者共享您的环境（意味着没有同步运行的代码），这极大地限制了近实时协作的有用性。

**免费计划的性能表现：**
Colab 可以让您访问  [GPU](https://colab.research.google.com/notebooks/gpu.ipynb)  或  [TPU](https://colab.research.google.com/notebooks/tpu.ipynb)。然而，Google 不会为其环境提供任何规范。如果您将 Colab 连接到 Google 云端硬盘，那么您将获得最多 15 GB 的磁盘空间来存储数据集。Colab  会话将在 60 分钟不活动后关闭，但它们可以运行长达 12 小时。

**性能升级：** 
不允许。但是，您可以选择连接到  [a local runtime](https://research.google.com/colaboratory/local-runtimes.html)，这允许您在本地硬件上执行代码并访问本地文件系统。

**文档和技术支持：**
Colab 拥有很少的文档，这些文档都包含在  [FAQ 页面](https://research.google.com/colaboratory/faq.html)和各种[示例笔记本](https://colab.research.google.com/notebooks/welcome.ipynb)中。用户可通过  [GitHub issues](https://github.com/googlecolab/colabtools/issues)，或者  [Stack Overflow](https://stackoverflow.com/questions/tagged/google-colaboratory)  社区获取支持。

**结论：**
Colab 的最大优势在于它易于上手，因为大多数人已经拥有 Google 帐户，并且共享笔记本很容易，因为共享功能与 Google Docs 相同。然而，繁琐的键盘快捷键和使用数据集的困难是显著的缺点。在同一笔记本上进行协作的能力很有用，但由于您没有共享环境，因此协作能力的作用也会有所降低。

## 4. Microsoft Azure Notebooks

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Frcw6uwHZy_6OvfeZR2Zk0QFI5aI.png)

要开始使用  [Azure 笔记本](https://notebooks.azure.com/)，请先使用 Microsoft 或 Outlook 帐户登录（或创建一个帐户）。然后是创建一个 "项目"，其结构与 GitHub 存储库相同：它可以包含一个或多个笔记本、Markdown 文件、数据集以及您要创建或上传的任何其他文件，所有这些都可以组织到文件夹中。与 GitHub 一样，您可以使用 README 文件初始化项目，该文件将自动显示在项目页面上。如果您的工作已存储在 GitHub 上，则可以将整个存储库直接导入到项目中。

**支持的语言：** Python (2 and 3), R, and F#.

**安装软件包：**
预先安装了数百个软件包，您可以使用  `pip`  或  `conda` [安装其他软件包](https://docs.microsoft.com/en-us/azure/notebooks/install-packages-jupyter-notebook)，并且可以使用[配置文件](https://docs.microsoft.com/en-us/azure/notebooks/quickstart-create-jupyter-notebook-project-environment)（例如  `environment.yml`  或  `requirements.txt` ）指定明确的软件包要求。

**界面相似度：**
Azure 使用原生的 Jupyter Notebook 界面。

**键盘快捷键：**
Azure 使用与 Jupyter 相同的所有键盘快捷键。

\*\*缺少的功能：\*\*无。

**新增的功能：**

- 已预先安装  [RISE](https://rise.readthedocs.io/)  扩展程序，可让您立即将笔记本显示为基于 live.js 的幻灯片。
- 已预先安装  [jupyter_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/)  包，可让您轻松访问 50 多个 Jupyter Notebook 扩展的集合，以增强笔记本界面。

**数据集易用性：**
您可以从本地计算机或 URL 将数据集上传到项目中，并且项目中的任何笔记本都可以访问该数据集。Azure 还包括其他 Azure 服务的[连接器](https://docs.microsoft.com/en-us/azure/notebooks/access-data-resources-jupyter-notebooks)，例如 Azure 存储和各种 Azure 数据库。

**网络访问：**  支持。

\*\*保证工作私密性的能力：\*\*支持。

**公开分享的能力：**
支持。如果您选择[公开您的项目](https://notebooks.azure.com/justmarkham/projects/pycon-2018-tutorial)，则任何人都可以在不创建 Microsoft 帐户的情况下访问它，任何拥有 Microsoft 帐户的人都可以将其复制到自己的帐户。此外，Azure 还为您提供了一个[公共配置文件页面](https://notebooks.azure.com/justmarkham)（非常类似于 GitHub 配置文件），它显示了所有公共项目。

\*\*协作能力：\*\*暂不支持，虽然这是一个[计划中的功能](https://github.com/Microsoft/AzureNotebooks/issues/6)。

**免费计划的性能表现：**
您可以访问 4 GB 的 RAM 和 1 GB 的磁盘空间（每个项目）。会话将在 60 分钟不活动后关闭，但它们可以运行 8 小时或更长时间。

**性能升级：** 
支持。您可以为  [Azure 订阅付费](https://azure.microsoft.com/en-us/free/)，但[设置过程](https://docs.microsoft.com/en-us/azure/notebooks/configure-manage-azure-notebooks-projects)非常琐细且[价格计算](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/)很复杂。

**文档和技术支持：** 
Azure 提供了大量的[文档](https://docs.microsoft.com/en-us/azure/notebooks/)。用户也可通过  [GitHub issues](https://github.com/microsoft/AzureNotebooks/issues)  获得支持。

**结论：**
Azure Notebooks 的最大优势在于它的易用性：项目结构（从 GitHub 借用）使得使用多个笔记本和数据集变得简单，并且使用原生 Jupyter 界面意味着现有的 Jupyter 用户将拥有一个简单的过渡。但是，RAM 和磁盘空间并不是特别慷慨，缺乏协作是功能上的一个巨大差距。

## 5. CoCalc

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgYugeMt0L6WDKav-ZUCKhz-MozM.png)

[CoCalc](https://cocalc.com/)，是 "collaborative calculation" 的缩写，是用于 Python，R，Julia 和许多其他语言计算的在线工作空间。 它允许您创建和编辑 Jupyter 笔记本，Sage 工作表和 LaTeX 文档。创建 CoCalc 帐户后，第一步是创建一个 "项目"，其中可以包含一个或多个笔记本、Markdown 文件、数据集以及您要创建或上传的任何其他文件，并且所有这些文件都可以组织到文件夹中。项目界面起初有点让人应接不暇，但是一旦你创建或打开笔记本，它看起来就会更加熟悉。

\*\*支持的语言：\*\*Python (2 and 3), R, Julia, 以及其他的语言。

**安装软件包：**
CoCalc  预先安装了数百个包。您可以使用  `pip`  安装其他软件包，但在使用免费套餐时无法使用这个功能。或者，您可以要求 CoCalc 在其默认安装中包含其他软件包。

**界面相似度：**
虽然 CoCalc 没有使用原生的 Jupyter Notebook 界面（他们使用 React.js 重写了它），但界面与 Jupyter 非常相似，只有少许修改。您实际上可以从 CoCalc 中[切换](https://doc.cocalc.com/jupyter.html#classical-versus-cocalc)到使用原生的 Jupyter Notebook，但不建议这样做，因为您将无法访问最有价值的 CoCalc 功能（"time travel"  和实时协作，这将在下面讨论）。

**键盘快捷键：** 
CoCalc 几乎使用与 Jupyter 相同的所有键盘快捷键。

**缺少的功能：**
CoCalc [目前不支持](https://github.com/sagemathinc/cocalc/issues/1930)交互式小部件。

**新增的功能：**

- CoCalc 包含一个称为[时间旅行](https://cocalc.com/doc/jupyter-notebook.html#a-timetravel)的强大版本控制功能，可以精确记录笔记本中的所有更改，并允许您使用直观的滑块控件浏览这些更改。
- CoCalc 每隔几分钟就会保存所有项目文件的备份，这意味着您可以根据需要恢复旧版本的文件。
- CoCalc 包括[教学的一些其他功能](https://doc.cocalc.com/teaching-instructors.html)，例如分发和评分作业的能力，以及在学生工作和与学生分交流享任务时观察学生的能力。

**数据集易用性：**
您可以从本地计算机将数据集上传到项目中，并且项目中的任何笔记本都可以访问该数据集。

\*\*网络访问：\*\*不，使用免费计划时无法使用此功能。

\*\*保证工作私密性的能力：\*\*允许。

**公开分享的能力：**
允许。如果您选择公开您的笔记本并分享链接，则任何人都可以在不创建 CoCalc 帐户的情况下访问该笔记本，并且拥有 CoCalc 帐户的任何人都可以将其复制到自己的帐户。

**协作能力：**
允许。您可以将笔记本保密，但可以邀请特定人员进行编辑。您和您的协作者可以同时编辑笔记本，并实时查看彼此的更改（和游标），以及在笔记本旁边的窗口中聊天（使用文本或视频）。所有计算的状态和结果也是同步的，这意味着所涉及的每个人都将以相同的方式体验笔记本。

**免费计划的性能表现：**
您将可以使用具有 1 GB 共享 RAM 和 3 GB 磁盘空间（每个项目）的 1 核共享 CPU。会话将在 30 分钟不活动后关闭，但它们可以运行长达 24 小时。

**性能升级：**
支持。您可以为 CoCalc 支付[订阅费用](https://cocalc.com/policies/pricing.html)，起价为每月 14 美元。或者，您可以在自己的计算机上安装  [CoCalc Docker 镜像](https://github.com/sagemathinc/cocalc-docker)，这样您就可以免费运行多个私有用户的 CoCalc 服务器。

**文档和技术支持：**
CoCalc 拥有[大量文档](https://doc.cocalc.com/)。用户可通过电子邮件和联系列表获得支持，并在  [GitHub](https://github.com/sagemathinc/cocalc/issues?q=is%3Aopen+is%3Aissue+label%3AA-jupyter)  上跟踪产品问题。

**结论：**
使用 CoCalc 的最有吸引力是它的实时协作和  "time travel"  版本控制功能，以及课程管理功能（如果您是教练）。 虽然界面有点混乱，但现有的 Jupyter 用户可以相对轻松地过渡到 CoCalc。但是，免费计划确实存在一些重要的限制（无法安装其他软件包或访问 Internet），另外，免费计划的性能也不高。

## 6. Datalore

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqarRqe6A--JlmBCX2nycwxA6gzK.png)

[Datalore](https://datalore.io/)  是由 JetBrains，一个制作 PyCharm（一种流行的 Python IDE）的公司创建的。它的入门就像创建帐户或使用 Google 或 JetBrains 帐户登录一样简单。您可以创建新的 Datalore "工作簿(workbook)" 或上传现有的 Jupyter Notebook。 Datalore 工作簿以专有格式存储，但它支持导入和导出标准  `.ipynb`  文件格式。

\*\*支持的语言：\*\*只支持 Python 3。

**安装软件包：**
Datalore  预安装了数百个软件包，您可以使用  `pip`  或  `conda`  安装其他软件包，也可以通过指定软件包的 GitHub 存储库来安装。

**界面相似度：**
当你打开 Datalore 时，界面确实类似于 Jupyter 笔记本，因为有代码和 Markdown 单元格以及在这些单元格下方的输出。但是，Datalore 和 Jupyter 界面之间存在一些重要差异：

- 单元格（Datalore 称之为 "blocks"）不会被编号，因为单元格已经被强制性进行了排序。 换句话说，所有代码都必须按照最终希望它运行的顺序编写。
- 笔记本（Datalore 称之为 "workbook"）可以有多个工作表，类似于 Google 表 格，这是将长工作簿分解为逻辑部分的便捷方式。如果在工作簿中创建多个工作表，则所有工作表共享相同的环境。因为单元格顺序在 Datalore 中很重要，所以第二个工作表中的单元格被视为在第一个工作表中的单元格之后，第三个工作表在第二个工作表之后，依此类推。
- 还有许多其他界面差异，这些差异在 "add features" 部分中进行了解释。

**键盘快捷键：**
键盘快捷键可用于 Datalore 中的大多数操作，但快捷方式与 Jupyter 使用的快捷方式截然不同。

**缺少的功能：**

- Datalore 不使用 IPython 内核，因此 IPython 魔术函数和 shell 命令不可用。（但是，对 IPython 内核的可选访问的功能已经在计划中。）
- 由于 Datalore 菜单栏保持非常简单并且没有工具栏，因此许多操作只能使用键盘快捷键完成。
- 您无法将工作簿下载为其他有用的格式，例如 Python 脚本，HTML 网页或 Markdown 文件。
- Datalore 不支持其 Markdown 单元格中所有常用的 Markdown 功能。（但是，改进的 Markdown 支持功能已经在计划中。）
- Datalore 不支持交互式小部件。
- Datalore 不包括多主机支持。

**新增的功能：**

- 单元格在您编写时自动运行，Datalore 称之为 "实时计算"。这实际上使您在编写代码时更容易调试代码，因为您可以立即查看代码的结果。（可以禁用实时计算，在这种情况下，您可以手动触发要运行的单元格。）
- 由于单元格将始终按其排列顺序运行，因此 Datalor e 可以跟踪单元格依赖性。这意味着当编辑给定单元格时，Datalore 将确定其下面的哪些单元可能受到影响，并将立即重新运行这些单元格（假设启用了实时计算）。如果编辑在从属单元格中导致错误，则会立即标记这些错误。
- Datalore 允许您按顺序显示单元格输入和输出（就像在 Jupyter 中一样）或 "拆分视图(split view)"，在这种情况下，输入和输出位于两个单独的窗格中。使用顺序视图时，Datalore 还可以轻松隐藏所有输入或隐藏所有输出。
- 在代码完成中，Datalore 包含比 Jupyter 更多的"智能"。
- 在编写代码时，Datalore 会为您可能想要采取的操作提供上下文感知建议（称为"意图(intentions)"）。例如，在键入 DataFrame 的名称之后，意图可能包括 "drop string columns"、"histogram" 和 "train test split"。当您单击意图时，Datalore 实际上会为您生成代码，这可能是学习某些任务背后的代码的有用方法。
- Datalore 包括一个精心设计的版本控制系统。它常用于保存工作簿的当前状态，您可以快速浏览当前版本和任何过去版本之间的差异。您还可以选择在保存工作簿时添加消息，然后可以在版本列表筛选仅包含带消息的那些版本。
- 通过 Datalore，您可以访问名为  `datalore.plot`  的绘图库，它与 R 的  `ggplot2`  非常相似，但您只能在 Datalore 中使用它。

**数据集易用性：**
您可以从本地计算机或 URL 将数据集上传到工作簿，但只能由该特定工作簿访问。如果您在许多工作簿中使用相同的数据集，这将是一个大的烦恼。（但是，在工作簿之间共享数据集是一项计划的功能。）

\*\*网络访问：\*\*支持。

\*\*保证工作私密性的能力：\*\*支持。

\*\*公开分享的能力：\*\*不支持。

**协作能力：**
支持。您可以将工作簿保密，但可以邀请特定人员查看或编辑它。您和您的协作者可以同时编辑笔记本，并实时查看彼此的更改（和游标）。所有计算的状态和结果也是同步的，这意味着所涉及的每个人都将以相同的方式体验笔记本。

**免费计划的性能表现：**
您可以访问具有 4 GB RAM 和 10 GB 磁盘空间的 2 核 CPU。会话将在 60 分 钟不活动后关闭，但对各个会话的长度没有特定限制。您可以每月使用该服务长达 120 小时。

**性能升级：**
暂不支持，虽然很快就会有一个付费计划，它提供更多的磁盘空间和更强大的 CPU（或 GPU）。

**文档和技术支持：** 
Datalore 具有比较少的文档，包含在示例工作簿中。用户可通过  [Discourse 论坛](https://forum.datalore.io/)获得支持。

**结论：**
Datalore 不再是对 Jupyter 笔记本的改编，而是更像是对笔记本的重塑。它包括一个创新的功能集，包括实时计算，依赖关系跟踪，实时协作和内置版本控制。但是，现有的 Jupyter 用户可能难以过渡到 Datalore，特别是因为强制执行单元格排序并且所有键盘快捷方式都完全不同。同样，Datalore 目前还包含一些值得注意的限制，即工作簿无法公开共享，上传的数据集无法在工作簿之间共享等。

## 如何选择合适的服务

在提出的六个选项中，没有一个明确的"赢家"。相反，正确的选择将取决于您的优先事项。以下是我根据您的特殊需求选择的建议。（注意：您也可以点击  [comparison table](https://docs.google.com/spreadsheets/d/12thaaXg1Idr3iWST8QyASNDs08sjdPd6m9mbCGtHFn0/edit?usp=sharing)  进行查看 。）

**您使用 Python 以外的语言：**
Binder 和 CoCalc 都支持大量语言。Azure 支持 Python，R 和 F＃，Kernel 支持 Python 和 R，Colab 支持 Python 和 Swift，Datalore 仅支持 Python。

**您需要使用 Python 2：**
Binder，Colab，Azure 和 CoCalc 都支持 Python 2 和 3，而 Kernel 和 Datalore 仅支持 Python 3。

**您使用非标准软件包：**
Binder 和 Azure 允许您使用配置文件指定确切的软件包要求。CoCalc 和 Datalore 允许您安装其他软件包，这些软件包将在会话期间保持不变，尽管这不适用于 CoCalc 的免费计划。Kernels 和 Colab 还允许您安装其他软件包，但它们不会跨会话持续存在。Kernels  和 CoCalc 可以接受哪一些包应包含在其默认安装中的用户请求。

**您喜欢现有的 Jupyter Notebook 界面：**
Binder 和 Azure 使用原生的 Jupyter Notebook 界面，而 CoCalc 使用了几乎相同的界面。Kernels  在视觉上与 Jupyter 不同，但效果与此类似，而 Colab 在视觉上类似于 Jupyter，但不像它那样工作。Datalore 离现有的 Jupyter Notebook 相差最远。

**您是键盘快捷键的重度用户：**
Binder，Kernels 和 Azure 使用与 Jupyter 相同的键盘快捷键，而 CoCalc 几乎使用了所有相同的快捷键。Datalore 使用完全不同的键盘快捷键，Colab 使用繁琐的多步键盘快捷键（尽管可以自定义）。

**您更喜欢点击式界面：**
Binder，Azure 和 CoCalc 允许您通过指向和单击执行所有操作，而 Kernels，Colab 和 Datalore 要求您使用键盘快捷键执行某些操作。

**您需要集成版本控制系统：**
CoCalc 和 Datalore 为 版本控制提供了最佳接口。Kaggle 的版本控制系统有限，Colab 的系统的有限程度更大。 Binder 和 Azure 则不提供版本控制系统。

**您需要使用大量数据集：**
Kernels 与 Kaggle Datasets 无缝协作，Kaggle Datasets 是一个功能齐全（免费）的服务，用于托管每个最多 20 GB 的数据集。CoCalc 为每个项目提供 3 GB 的磁盘空间，您上传的任何数据集都可以被项目中的任何笔记本访问。Azure 具有类似的功能，但每个项目提供 1 GB 的磁盘空间。尽管您上传的每个数据集都必须链接到特定的工作簿，但 Datalore 提供 10 GB 的总磁盘空间。除非您将 Colab 链接到 Google 云端硬盘，否则 Colab 会丢弃您在会话结束时上传的所有数据集。Binder 最适用于存储在 Git 存储库中或位于公共 URL 的小型数据集。

**您的项目已经托管在 GitHub 上：**
Binder 可以直接从 GitHub 运行您的笔记本，Azure 将允许您导入整个 GitHub 存储库，Colab 可以从 GitHub 导入一个笔记本。Kernels、CoCalc 和 Datalore 不提供任何类似的功能。

**您需要将您的工作保密：** 除了 Binder 以外，其他的都支持私有选项。

**您需要将数据保留在本地：**
这些基于云的服务都不允许您将数据保留在本地。但是，您可以在自己的服务器上设置 Binder 或 CoCalc，因为 BinderHub 和 CoCalc Docker 镜像都是开源的，这样您就可以将数据保存在本地。

**您希望公开分享您的工作：**
在共享时  Binder  创建的步骤最少，因为人们无需创建帐户即可查看和运行您的笔记本。Kernels、Colab、Azure 和 CoCalc 允许您共享 URL 以进行只读访问，同时要求用户在想要运行笔记本时创建帐户。通过为您提供公共个人资料页面，Kernels  和 Azure 可以更轻松地进行共享。Datalore 不允许公开共享。

**您需要与其他人协作：**
CoCalc 和 Datalore 支持实时协作。Colab 支持在同一个文档上进行协作，虽然它不是很实时，而且你没有共享相同的环境。Kernels  支持一种您可以在其中共享版本历史记录协作形式。Binder 和 Azure 不包含任何协作功能，但使用 Binder 可以通过正常的 GitHub 拉取请求的工作流轻松实现。

**您需要高性能环境：**
Kernels  提供最强大的环境（4 核 CPU 和 17 GB RAM），其次是 Datalore（2 核 CPU 和 4 GB RAM），Azure（4  GB RAM），Binder（最多 2 GB RAM）和 CoCalc（1 核 CPU 和 1 GB RAM）。Colab 不提供其环境规范。

**您需要访问 GPU：**
Kernels 和 Colab 都可以免费访问 GPU。 Azure 访问和（很快）Datalore 的付费客户也可以使用 GPU 访问。Binder 或 CoCalc 无法访问 GPU。

\*\*您更喜欢使用非商业工具：\*\*Binder 是由非商业实体管理的唯一选项。

## 其他类似的服务

以下服务与上述六个选项类似，但未包括在我的比较中：

- 我没有包含任何只提供 JupyterLab 访问权限的服务，例如  [Notebooks AI](https://notebooks.ai/)，[Kyso](http://kyso.io/)  和  [CyVerse](http://learning.cyverse.org/projects/vice/en/latest/getting_started/about.html)。（请注意，如果您愿意，Binder，Azure 和 CoCalc 都允许您使用 JupyterLab 而不是 Jupyter Notebook。）
- 我没有包含  [IBM Watson Studio Cloud](https://www.ibm.com/cloud/watson-studio)，因为入门过程繁琐，界面过于复杂，免费计划有很多限制，在测试期间有很多错误消息。
- 我没有包括  [Gryd](https://gryd.us/)，因为免费计划需要一个学术性的电子邮件地址，而且我没有包含  [Code Ocean](https://codeocean.com/)，因为没有学术电子邮件地址，免费计划受到严格限制。
- 我没有包含  [ZEPL](https://www.zepl.com/)，因为它不允许您使用标准的  `.ipynb`  格式导出笔记本。
- 我没有包括任何付费服务，例如  [Saturn Cloud](https://www.saturncloud.io/)， [Crestle.ai](https://www.crestle.ai/)，[Paperspace](https://www.paperspace.com/)  和  [Salamander](https://salamander.ai/)。

## 我真实的核查过程

本文是 50 多个小时的研究，测试和写作的结果。 此外，我在 2019 年 3 月与 Binder，Kaggle，Google，Microsoft，CoCalc 和 Datalore 的相关团队分享了本文的草稿。我收到了来自所有六家公司/组织的详细反馈（谢谢！），我将其纳入 发表之前的文章。

话虽如此，这些服务也在不断变化，而且未来可能会有一些信息过时。如果您认为本文中的内容不再正确，请在下面留言，我很乐意考虑更新该文章。
