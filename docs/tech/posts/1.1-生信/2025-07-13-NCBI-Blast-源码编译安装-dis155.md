---
title: NCBI Blast 源码编译安装
number: 155
slug: discussions-155/
url: https://github.com/shenweiyan/Digital-Garden/discussions/155
date: 2025-07-13
authors: [shenweiyan]
categories: 
  - 生信
tags: ['1.1.6-软件', 'blast']
---

记录一下在老破旧服务器从源码编译安装 NCBI Blast 2.15.0+ 遇到的一些问题。

<!-- more -->

![Basic-Local-Alignment-Search-Tool](https://gi.weiyan.tech/2025/07/ncbi-blast.png)

先说一下，总体的安装步骤。

首先，根据 `ncbi-blast-2.xx.x+-src/c++/src/algo/blast/core/README` 的说明，blast+ 的源码编译安装，直接通过下面命令即可：
```bash
./configure --with-projects=scripts/projects/blast_core_lib.lst \
            --without-debug --with-mt --with-build-root=ReleaseMT
cd ReleaseMT/build
make all_p
```

其实 `configure` 这一步的最后也会有提示：
```bash
$ ./configure --with-projects=scripts/projects/blast_core_lib.lst \
            --without-debug --with-mt --with-build-root=ReleaseMT
===============================================================================
NCBI C++ Toolkit documentation:
  Online:   https://www.ncbi.nlm.nih.gov/toolkit/doc/book/
  Local:    ./doc/public/index.html
For the available configuration flags run:  ./configure --help

CFLAGS   =  -Wall -Wno-format-y2k  -pthread -fopenmp -O2 -fPIC
CXXFLAGS =  -Wall -Wno-format-y2k  -pthread -fopenmp -O2 -fPIC
CPPFLAGS = -DNDEBUG -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE   -D_MT -D_REENTRANT -D_THREAD_SAFE
LDFLAGS  =  -Wl,--enable-new-dtags -Wl,-export-dynamic  -pthread -fopenmp   -O2

LIBRARIES:  build as static by default
FEATURES:   Int8GI GCC MT LFS DLL unix WinMain Linux
PACKAGES:
  enabled:  UUID Iconv Z BZ2 PCRE LocalPCRE MBEDTLS GMP GMP OPENSSL KRB5 CURL MySQL BerkeleyDB BerkeleyDB++ PYTHON PYTHON27 PYTHON3 PERL Boost.Iostreams Boost.Program-Options Boost.Regex Boost.Serialization Boost.Spirit Boost.Test.Included OpenGL GLUT GLEW EXPAT LIBXML LIBXSLT LIBEXSLT SQLITE3 HDF5 JPEG PNG TIFF XPM FreeType LMDB LocalLMDB LIBUV
  disabled: FUSE LIBUNWIND LIBDW BACKWARD_CPP LocalZ LocalBZ2 LZO ZSTD GCRYPT NETTLE GNUTLS Sybase DBLib FreeTDS ODBC PYTHON25 PYTHON26 Boost.Chrono Boost.Filesystem Boost.System Boost.Test Boost.Thread C-Toolkit NCBICRYPT MESA wxWidgets wx2.8 Fast-CGI FASTCGIPP LocalSSS LocalMSGMAIL2 SSSUTILS LocalNCBILS NCBILS2 SSSDB SP ORBacus ICU SABLOT Xerces Xalan Zorba SQLITE3ASYNC VDB NGS OECHEM SGE DRMAA2 MUPARSER GIF UNGIF GL2PS FTGL MAGIC MIMETIC GSOAP AVRO Cereal SASL2 MONGODB MONGODB3 LEVELDB LIBURING ROCKSDB GMOCK LAPACK LIBSSH2 CASSANDRA NGHTTP2 H2O INFLUXDB LIBXLSXWRITER PROTOBUF GRPC MSGSL AWS_SDK CRC32C GOOGLE_CLOUD HIREDIS APACHE_ARROW LIBRDKAFKA CPPKAFKA THRIFT NLohmann_JSON YAML_CPP OPENTRACING JAEGER
PROJECTS:
  enabled:  cgi serial objects dbapi app algo
  disabled: bdb ctools gui gbench

Tools / flags / paths:  /software/src/build/ncbi-blast-2.16.0+-src/c++/ReleaseMT/build/Makefile.mk
Configuration  header:  /software/src/build/ncbi-blast-2.15.0+-src/c++/ReleaseMT/inc/ncbiconf_unix.h

To build everything:  cd /software/src/build/ncbi-blast-2.15.0+-src/c++/ReleaseMT/build && /opt/rh/devtoolset-7/root/usr/bin/make all_r
or simply run /opt/rh/devtoolset-7/root/usr/bin/make in the current directory
To build selected projects (as listed in "scripts/projects/blast_core_lib.lst"):
  cd /software/src/build/ncbi-blast-2.15.0+-src/c++/ReleaseMT/build && /opt/rh/devtoolset-7/root/usr/bin/make all_p

******* CONFIGURATION SUCCESSFUL *******
```

梳理一下它整个步骤，其实就是 **`configure`** → **生成 `Makefile.mk`** → **`make`**。

## Makefile.mk 

很不幸的是，个人在 CentOS 6.5 的老破旧服务器上执行 `configure` 或者 `make` 出现了 `Makefile.mk:682: *** missing separator.  Stop.` 的异常。

对于这个突如其来的错误，本人最开始也想当然的认为这是 `Makefile` 语法的一个BUG，很明显 Makefile 中命令的前缀默认要使用 Tab, 不能使用 4 个空格代替，因此需要在 `Makefile.mk` 682 行开始用 Tab 替换四个空格开头的行。

事实上，这个问题的根本原因并非单纯的 `Makefile` 语法的问题，而是问题出现在 **`configure`** → **生成 `Makefile.mk`** 这一步。经过对 **`configure`** 源码排查了一下发现，问题就出在 `curl-config --static-libs` 的错误输出被直接插入到了 `Makefile` 中，导致 `make` 误解析这些文本（如 `--ca`, `--cc` 等）为 `Makefil`e 规则，从而引发 `missing separator` 和 `ignoring old recipe` 错误。
![blast-curl-config](https://gi.weiyan.tech/2025/07/blast-curl-config.webp)

因此，有几个解决方法。

- 方法1，修改 `Makefile.mk`，确保正确处理 `curl-config` 的输出。例如：
  ```
  # 安全获取静态库链接信息（避免错误输出污染 Makefile）
  CURL_STATIC_LIBS := $(shell curl-config --static-libs 2>/dev/null || echo "-lcurl")
  ```

- 方法2：如果系统支持 `pkg-config`，可以改用更可靠的方式获取 `libcurl` 链接信息。
  ```bash
  CURL_LIBS   := $(shell pkg-config --libs libcurl)
  CURL_STATIC_LIBS := $(shell pkg-config --static --libs libcurl 2>/dev/null || echo "-lcurl")
  ```
- 方法3：在 `configure` 一步中通过 `--without-curl` 来禁用 `libcurl`。

## ZLIB_VER_MAJOR

`make` 过程中出现 `ZLIB_VER_MAJOR` 相关错误：
```bash
$ make all_r
Build session ID: 37264a70-80c7-4bfb-857e-3fcc536c2046
/opt/rh/devtoolset-7/root/usr/bin/make -C corelib   all_r  ||  exit 5
......
/opt/rh/devtoolset-7/root/usr/bin/make[3] (Makefile.compress.lib): Nothing to be done for `flag-stamps'.
/opt/rh/devtoolset-7/root/usr/bin/make -f /software/ncbi-blast-2.16.0+/build/Makefile.lib.tmpl srcdir=/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api TMPL=compress -w all
make[4]: Entering directory '/software/ncbi-blast-2.16.0+/build/util/compress/api'
/opt/rh/devtoolset-7/root/usr/bin/g++  -std=gnu++17 -msse4.2 -c  -Wall -Wno-format-y2k  -pthread -fopenmp -O2 -fPIC   -DNDEBUG -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE   -D_MT -D_REENTRANT -D_THREAD_SAFE -I/software/ncbi-blast-2.16.0+/inc -I/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/include      -DNCBI_BUILD_SESSION_ID=37264a70-80c7-4bfb-857e-3fcc536c2046 /software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp -o zlib.o
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp: In member function ‘virtual ncbi::CVersionInfo ncbi::CZipCompression::GetVersion() const’:
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:25: error: ‘ZLIB_VER_MAJOR’ was not declared in this scope
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                         ^~~~~~~~~~~~~~
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:25: note: suggested alternative: ‘ZLIB_VERSION’
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                         ^~~~~~~~~~~~~~
                         ZLIB_VERSION
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:41: error: ‘ZLIB_VER_MINOR’ was not declared in this scope
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                                         ^~~~~~~~~~~~~~
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:41: note: suggested alternative: ‘ZLIB_VERSION’
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                                         ^~~~~~~~~~~~~~
                                         ZLIB_VERSION
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:57: error: ‘ZLIB_VER_REVISION’ was not declared in this scope
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                                                         ^~~~~~~~~~~~~~~~~
/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/util/compress/api/zlib.cpp:333:57: note: suggested alternative: ‘ZLIB_VERSION’
     return CVersionInfo(ZLIB_VER_MAJOR, ZLIB_VER_MINOR, ZLIB_VER_REVISION, "zlib");
                                                         ^~~~~~~~~~~~~~~~~
                                                         ZLIB_VERSION
make[4]: *** [/software/ncbi-blast-2.16.0+/build/Makefile.rules:103: zlib.o] Error 1
make[4]: Leaving directory '/software/ncbi-blast-2.16.0+/build/util/compress/api'
FAILED: src/util/compress/api/Makefile.compress.lib
make[4]: Entering directory '/software/ncbi-blast-2.16.0+/build/util/compress/api'
/bin/rm -f libxcompress.a .xcompress.dep .libxcompress.a.stamp
/bin/rm -f /software/ncbi-blast-2.16.0+/lib/libxcompress.a /software/ncbi-blast-2.16.0+/status/.xcompress.dep \
    /software/ncbi-blast-2.16.0+/lib/libxcompress-static.a /software/ncbi-blast-2.16.0+/status/.xcompress-static.dep
make[4]: Leaving directory '/software/ncbi-blast-2.16.0+/build/util/compress/api'
make[3]: *** [/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/build-system/Makefile.meta_l:336: all.nonusr] Error 2
make[3]: Leaving directory '/software/ncbi-blast-2.16.0+/build/util/compress/api'
make[2]: *** [/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/build-system/Makefile.meta_r:41: all_r.real] Error 5
make[2]: Leaving directory '/software/ncbi-blast-2.16.0+/build/util/compress'
make[1]: *** [/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/build-system/Makefile.meta_r:41: all_r.real] Error 5
make[1]: Leaving directory '/software/ncbi-blast-2.16.0+/build/util'
make: *** [/software/ncbi-blast-2.16.0+/src/ncbi-blast-2.16.0+-src/c++/src/build-system/Makefile.meta_r:41: all_r.real] Error 5
```

最后，想说的是，以上扒拉扒拉折腾了那么多，到最后还是没能完整安装起来，只好先放弃了，后面有时间再慢慢去 debug 看看吧。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="155"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
