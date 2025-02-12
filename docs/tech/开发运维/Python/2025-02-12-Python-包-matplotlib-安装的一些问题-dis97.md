---
title: Python 包 matplotlib 安装的一些问题
number: 97
slug: discussions-97/
url: https://github.com/shenweiyan/Digital-Garden/discussions/97
date: 2025-02-12
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.5-Python']
---

Python 的 matplotlib 在安装的过程中一直无法解决 freetype2 自动下载的问题，导致始终安装不成功。

<!-- more -->

Python-3.10.16 通过本地（或者是在线）方式安装 matplotlib-3.10.0 的时候，发现对应 `freetype2`、`qhull` 通过对应的 URL 无法正常下载，以至于 `matplotlib` 一直安装不成功，详细信息如下面代码所示。

```bash
$ pip3 install .
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Processing /bioinfo/src/py/matplotlib-3.10.0
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [48 lines of output]
      + meson setup /bioinfo/src/py/matplotlib-3.10.0 /bioinfo/src/py/matplotlib-3.10.0/.mesonpy-smx69lrx -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --native-file=/bioinfo/src/py/matplotlib-3.10.0/.mesonpy-smx69lrx/meson-python-native-file.ini
      The Meson build system
      Version: 1.7.0
      Source dir: /bioinfo/src/py/matplotlib-3.10.0
      Build dir: /bioinfo/src/py/matplotlib-3.10.0/.mesonpy-smx69lrx
      Build type: native build
      Program python3 found: YES (/bioinfo/software/Python-3.10.16/bin/python3)
      Project name: matplotlib
      Project version: 3.10.0
      C compiler for the host machine: cc (gcc 4.4.7 "cc (GCC) 4.4.7 20120313 (Red Hat 4.4.7-4)")
      C linker for the host machine: cc ld.bfd 2.20.51.0.2-5
      C++ compiler for the host machine: c++ (gcc 4.4.7 "c++ (GCC) 4.4.7 20120313 (Red Hat 4.4.7-4)")
      C++ linker for the host machine: c++ ld.bfd 2.20.51.0.2-5
      Host machine cpu family: x86_64
      Host machine cpu: x86_64
      Program python found: YES (/bioinfo/software/Python-3.10.16/bin/python3.10)
      Found pkg-config: YES (/usr/bin/pkg-config) 0.23
      Run-time dependency python found: YES 3.10
      pybind11-config found: YES (/tmp/pip-build-env-gf0psrg8/overlay/bin/pybind11-config) 2.13.6
      Run-time dependency pybind11 found: YES 2.13.6
      Downloading freetype-2.6.1 source from https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://download.savannah.gnu.org/releases/freetype/freetype-old/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      Downloading freetype-2.6.1 source from https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>
      WARNING: failed to download with error: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?. Trying after a delay...
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1007)>

      ../extern/meson.build:18:18: ERROR: could not get https://downloads.sourceforge.net/project/freetype/freetype2/2.6.1/freetype-2.6.1.tar.gz is the internet available?

      A full log can be found at /bioinfo/src/py/matplotlib-3.10.0/.mesonpy-smx69lrx/meson-logs/meson-log.txt
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.

[notice] A new release of pip is available: 23.0.1 -> 25.0.1
[notice] To update, run: pip3 install --upgrade pip
```

对于这种情况，可以：
1. 根据提示给出的 URL 下载好相应的依赖（这个 URL 也可以在 `matplotlib-3.10.0/subprojects/*.wrap` 中找到），并把依赖包保存的服务器任何一个目录下。
   - [freetype-2.6.1.wrap](https://github.com/matplotlib/matplotlib/blob/v3.10.x/subprojects/freetype-2.6.1.wrap)：`/bioinfo/src/py/freetype-2.6.1.tar.gz`；
   - [qhull.wrap](https://github.com/matplotlib/matplotlib/blob/v3.10.x/subprojects/qhull.wrap)：`/bioinfo/src/py/qhull-8.0.2.tar.gz`
   
2. 修改 `matplotlib-3.10.0/subprojects/*.wrap`。
   - freetype-2.6.1.wrap
   ```
   [wrap-file]
   source_url = file:///bioinfo/src/py/freetype-2.6.1.tar.gz
   source_fallback_url = file:///bioinfo/src/py/freetype-2.6.1.tar.gz
   source_filename = freetype-2.6.1.tar.gz
   source_hash = 0a3c7dfbda6da1e8fce29232e8e96d987ababbbf71ebc8c75659e4132c367014

   patch_directory = freetype-2.6.1-meson

   [provide]
   freetype-2.6.1 = freetype_dep
   ```
   
   - qhull.wrap
   ```
   [wrap-file]
   # Also bump the cache key in `.circleci/config.yml`.
   # Also update the docs in `docs/devel/dependencies.rst`.
   directory = qhull-8.0.2
   source_url = file:///bioinfo/src/py/qhull-8.0.2.tar.gz
   source_filename = qhull-8.0.2.tgz
   source_hash = 8774e9a12c70b0180b95d6b0b563c5aa4bea8d5960c15e18ae3b6d2521d64f8b

   patch_directory = qhull-8.0.2
   ```

3. 最后，再次执行安装。
   ```bash
   pip3 install .
   ```
   ![pip3-matplotlib](https://kg.weiyan.cc/2025/02/pip3-matplotlib.png)
   


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="97"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
