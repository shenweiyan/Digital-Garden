---
title: Galaxy Project 的 Sphinx 文档部署
number: 46
slug: discussions-46/
url: https://github.com/shenweiyan/Digital-Garden/discussions/46
date: 2024-01-05
authors: [shenweiyan]
categories: 
  - 3.1-Galaxy
labels: ['公众号', '3.1.x-GalaxyOther']
---

<https://docs.galaxyproject.org/> 是 Galaxy Project 官方的文档地址链接，这是一个基于 [Sphinx](https://www.sphinx-doc.org/) + [Read the Docs](https://readthedocs.org/) 的文档站点。如果我们也想要创建一个这样一模一样的 Galaxy 文档需要怎么操作呢？

<!-- more -->

虽然 [Galaxy 官方文档](https://docs.galaxyproject.org/en/master/#building-this-documentation) 也给出了关于构建该文档的一些说明，但没有太多细节。

> If you have your own copy of the Galaxy source code, you can also generate your own version of this documentation. Run the following command from the Galaxy’s root:
> ```
> $ make docs
> ```
> The generated documentation will be in `doc/build/html/` and can be viewed with a web browser. Note that you will need to install Sphinx and other module dependencies which are listed in the Makefile in the Galaxy root folder.

下面我们来详细分解一下 `make docs` 这个命令具体执行的构建步骤。

首先，在 Galaxy 根目录的执行 `make docs`，主要是执行了该目录下 [Makefile](https://github.com/galaxyproject/galaxy/blob/dev/Makefile) 中的这几句命令：
```
docs: ## Generate HTML documentation.
# Run following commands to setup the Python portion of the requirements:
#   $ ./scripts/common_startup.sh
#   $ . .venv/bin/activate
#   $ pip install -r requirements.txt -r lib/galaxy/dependencies/dev-requirements.txt
	$(IN_VENV) $(MAKE) -C doc clean
	$(IN_VENV) $(MAKE) -C doc html
```
- `$(MAKE)`就是预设的 `make` 这个命令的名称（或者路径）。    
- `-C`：到指定目录下读取 Makefile 文件并执行（给出指定的目录的路径）。     

第二步，读取 `doc` 目录下的 [Makefile](https://github.com/galaxyproject/galaxy/blob/dev/doc/Makefile) 文件，并执行 `make html`。
```
html: $(GENERATED_RST)
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
```

结合其中的一些参数，其实最终就是执行了下面这个命令完成最终的构建。
```bash
sphinx-build -b html -d build/doctrees source build/html
```

- sphinx-build [OPTIONS] SOURCEDIR OUTPUTDIR [FILENAMES...]
- sourcedir：path to documentation source files
- outputdir：path to output directory
- `-b`：BUILDER，builder to use (default: html)

了解了以上几个步骤后，我们就可以把 Galaxy 根目录的 doc 目录单独拎出来，通过 Sphinx 的命令实现独立构建部署。

## 1. 安装必须依赖

主要包括三个依赖。
```
pip3 install Sphinx sphinx_rtd_theme myst_parser
```

## 2. 修改配置

由于 `sphinx-build` 会读取 `source/conf.py` 并执行，但这个文件调用了 [`galaxy.version`](https://github.com/galaxyproject/galaxy/blob/dev/lib/galaxy/version.py) 模块：
![No module named 'galaxy'](https://shub.weiyan.tech/kgarden/2024/01/no-galaxy-version.png)

所以，如果我们想要把 `galaxy/doc` 和 Galaxy 独立开来进行部署，就需要修改一下 `source/conf.py`：
```python
# The short X.Y version.
#from galaxy.version import (
#    VERSION,
#    VERSION_MAJOR,
#)

VERSION_MAJOR = "23.1"
VERSION_MINOR = "5.dev0"
VERSION = VERSION_MAJOR + (f".{VERSION_MINOR}" if VERSION_MINOR else "")
```

## 3. 执行构建
```bash
$ sphinx-build -b html -d build/doctrees   source build/html
Running Sphinx v7.2.6
making output directory... done
myst v2.0.0: MdParserConfig(commonmark_only=False, gfm_only=False, enable_extensions={'deflist', 'attrs_block', 'substitution'}, disable_syntax=[], all_links_external=False, url_schemes=('http', 'https', 'mailto', 'ftp'), ref_domains=None, fence_as_directive=set(), number_code_blocks=[], title_to_header=False, heading_anchors=5, heading_slug_func=<function make_id at 0x7f46201a6a60>, html_meta={}, footnote_transition=True, words_per_minute=200, substitutions={}, linkify_fuzzy_links=True, dmath_allow_labels=True, dmath_allow_space=True, dmath_allow_digits=True, dmath_double_inline=False, update_mathjax=True, mathjax_classes='tex2jax_process|mathjax_process|math|output_area', enable_checkboxes=False, suppress_warnings=[], highlight_code_blocks=True)
loading intersphinx inventory from https://docs.python.org/3/objects.inv...
loading intersphinx inventory from https://requests.readthedocs.io/en/master/objects.inv...
intersphinx inventory has moved: https://requests.readthedocs.io/en/master/objects.inv -> https://requests.readthedocs.io/en/latest/objects.inv
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 332 source files that are out of date
updating environment: [new config] 332 added, 0 changed, 0 removed
reading sources... [100%] ts_api_doc

...

generating indices... genindex done
highlighting module code... 
writing additional pages... search done
copying images... [100%] releases/images/23.1-hdf5.png
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 1223 warnings.

The HTML pages are in build/html.
```

最后生成的静态文件都保存在了 `build/html` 目录，我们可以借助 NGINX 或者其他 Pages 就可以直接看到一个一模一样对应当前 Repo 版本的 Galaxy Project 文档了。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="46"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
