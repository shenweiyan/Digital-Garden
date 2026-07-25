---
title: SciPy 安装无法识别 BLAS 和 LAPACK
number: 188
slug: discussions-188/
url: https://github.com/shenweiyan/Digital-Garden/discussions/188
date: 2026-04-20
authors: 
  - shenweiyan
categories: 
  - 运维
tags: []
---

这个问题出现在 `import sklearn` 时候，调用 `from scipy.linalg import _flapack`，出现 `undefined symbol: sgeqrt_` 错误。

```python
$ /ifs1/SoftWare/Python-3.10.16/bin/python3
Python 3.10.16 (main, Feb 11 2025, 13:45:26) [GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sklearn
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/sklearn/__init__.py", line 82, in <module>
    from .base import clone
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/sklearn/base.py", line 17, in <module>
    from .utils import _IS_32BIT
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/sklearn/utils/__init__.py", line 29, in <module>
    from .fixes import parse_version, threadpool_info
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/sklearn/utils/fixes.py", line 19, in <module>
    import scipy.stats
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/stats/__init__.py", line 391, in <module>
    from .stats import *
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/stats/stats.py", line 174, in <module>
    from scipy.spatial.distance import cdist
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/spatial/__init__.py", line 101, in <module>
    from ._procrustes import procrustes
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/spatial/_procrustes.py", line 9, in <module>
    from scipy.linalg import orthogonal_procrustes
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/__init__.py", line 195, in <module>
    from .misc import *
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/misc.py", line 4, in <module>
    from .lapack import get_lapack_funcs
  File "/ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/lapack.py", line 808, in <module>
    from scipy.linalg import _flapack
ImportError: /ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/_flapack.cpython-310-x86_64-linux-gnu.so: undefined symbol: sgeqrt_
>>>
```

这个错误的核心原因是：`scipy.linalg._flapack` 在运行时无法找到 `LAPACK` 函数的 `sgeqrt_`。

<!-- more -->

## 问题分析

```python
>>> import scipy
>>> scipy.show_config()
lapack_mkl_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/include', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib']
lapack_opt_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/include', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib']
blas_mkl_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/include', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib']
blas_opt_info:
    libraries = ['mkl_rt', 'pthread']
    library_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['/opt/intel/composer_xe_2011_sp1.6.233/mkl', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/include', '/opt/intel/composer_xe_2011_sp1.6.233/mkl/lib']
Supported SIMD extensions in this NumPy install:
    baseline = SSE,SSE2,SSE3
    found = SSSE3,SSE41,POPCNT,SSE42,AVX,F16C
    not found = FMA3,AVX2,AVX512F,AVX512CD,AVX512_KNL,AVX512_KNM,AVX512_SKX,AVX512_CNL
```

```bash
$ ldd /ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/_flapack.cpython-310-x86_64-linux-gnu.so | grep -iE "lapack|blas|mkl"
        libmkl_rt.so => /opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64/libmkl_rt.so (0x00007fc1db146000)
$ nm -D /opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64/libmkl_rt.so | grep sgeqrt       
$ nm -D /usr/lib64/libopenblas.so.0 | grep sgeqrt
0000000001d86020 T LAPACKE_sgeqrt
0000000001d86170 T LAPACKE_sgeqrt2
0000000001d86270 T LAPACKE_sgeqrt2_work
0000000001d86510 T LAPACKE_sgeqrt3
0000000001d86610 T LAPACKE_sgeqrt3_work
0000000001d868b0 T LAPACKE_sgeqrt_work
0000000001705ba0 T sgeqrt2_
0000000001706230 T sgeqrt3_
00000000017057b0 T sgeqrt_
```       

结合 `scipy.show_config()` 输出，可以明确以下几点。

1. `sgeqrt_` 是 LAPACK 3.3.0+ 引入的 QR 分解函数。
2. 使用的 MKL 版本为 composer_xe_2011_sp1.6.233（约 2011 年发布），该版本未包含此函数；但系统的 libopenblas 是包含 `sgeqrt` 函数的。

## 解决方法

```bash
source /opt/rh/devtoolset-7/enable
export BLAS=/usr/lib64/libopenblas.so
export LAPACK=/usr/lib64/libopenblas.so
export LDFLAGS="-Wl,--no-as-needed -lopenblas"
/ifs1/SoftWare/Python-3.10.10/bin/pip3 install --no-cache-dir --force-reinstall --no-binary :all: scipy==1.7.3
```

这时候看到多了一个 `libopenblas.so.0` 的动态库链接，再 `import sklearn` 也可以正常导入了。
```bash
$ ldd /ifs1/SoftWare/Python-3.10.16/lib/python3.10/site-packages/scipy/linalg/_flapack.cpython-310-x86_64-linux-gnu.so
        linux-vdso.so.1 =>  (0x00007fffa04a7000)
        libopenblas.so.0 => /usr/lib64/libopenblas.so.0 (0x00007f4ae1e79000)
        libmkl_rt.so => /opt/intel/composer_xe_2011_sp1.6.233/mkl/lib/intel64/libmkl_rt.so (0x00007f4ae190f000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f4ae16f2000)
        libgfortran.so.3 => /usr/lib64/libgfortran.so.3 (0x00007f4ae1400000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f4ae117b000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f4ae0f65000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f4ae0bd1000)
        /lib64/ld-linux-x86-64.so.2 (0x0000003636a00000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f4ae09cc000)
```

![py3-sklearn-scipy](https://gi.weiyan.tech/2026/04/py3-sklearn-scipy.png)

## 参考资料

- [Cython compilation error with Cython>=3 and scikit-learn<1.2 - scikit-learn/scikit-learn#26858](https://github.com/scikit-learn/scikit-learn/issues/26858)
- [BLAS and LAPACK — SciPy v1.17.0 Manual](https://docs.scipy.org/doc/scipy/building/blas_lapack.html) 

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="188"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
