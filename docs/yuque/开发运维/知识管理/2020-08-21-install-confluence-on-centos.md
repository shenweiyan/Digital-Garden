---
title: 一个小清新的知识管理和问题讨论平台
urlname: 2020-08-21-install-confluence-on-centos
author: 章鱼猫先生
date: 2020-08-21
updated: "2021-06-25 10:45:31"
---

[一个小清新的知识管理和问题讨论平台](https://mp.weixin.qq.com/s/fL7CaYo2xvuleihlY8XDIA)

在《[一个小团队使用的知识管理方案与工具](https://www.yuque.com/shenweiyan/cookbook/zwtn5w?view=doc_embed)》中我们介绍了一些 Confluence 的基本特性，今天我们来看看这个工具的一些安装部署问题。

## 1. Java 与 PostgreSQL 安装配置

### 1.1 Oracle Java JDK 8

<https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html>
注册一个 oracle 账号就行，需要的文件：jdk-8u251-linux-x64.tar.gz

1.  创建目录，解压。

```bash
mkdir /usr/java
tar zvxf jdk-8u251-linux-x64.tar.gz -C /usr/java
```

2.  环境配置，修改 \~/.bashrc（或者 /etc/profile）文件。

```bash
vim ~/.bashrc
```

3.  添加以下内容。

```bash
export JAVA_HOME=/usr/java/jdk1.8.0_251
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```

4.  使环境变量生效。

```bash
source ~/.bashrc
```

5.  检查配置是否成功。

```bash
$ java -version
java version "1.8.0_251"
Java(TM) SE Runtime Environment (build 1.8.0_251-b08)
Java HotSpot(TM) 64-Bit Server VM (build 25.251-b08, mixed mode)
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjwONGM3a7lpYeCuLlFZL3vVyn7b.png)

### 1.2 PostgreSQL

PostgreSQL 是 Atlassian 官方推荐用于 Confluence 的数据库，接下来我们需要安装 PostgreSQL，并执行一些必要的设置。

#### 1. 安装

Linux 下 PostgreSQL 数据库的安装请参考《[Linux 下 PostgreSQL 源码编译安装](https://www.yuque.com/bioitee/mp/linux-postgresql-install?view=doc_embed)》一文，这里不赘述。

#### 2. 配置

创建用于 Confluence 的数据库。详细可以参考《[How to install Confluence on Centos7 with PostgreSQ](https://comtronic.com.au/how-to-install-confluence-on-centos7-with-postgresql/)》。

```bash
$ sudo -u postgres -i
$ psql
psql (10.13)
Type "help" for help.

postgres=# CREATE USER confluencedbuser PASSWORD 'confluencedbpassword';
postgres=# CREATE DATABASE confluencedb WITH ENCODING 'UNICODE' LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0;
postgres=# GRANT ALL PRIVILEGES ON DATABASE confluencedb to confluencedbuser;
\q
-bash-4.2$ exit
```

## 2. 下载安装 Confluence

### 2.1 下载

```bash
$ mkdir /data/apps/atlassian
$ cd /data/apps/atlassian
$ wget https://product-downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-7.2.1-x64.bin
```

### 2.2 安装

给 atlassian-confluence-7.2.1-x64.bin 添加可执行权限后进行安装。
![mkdir-atlassian-dir.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj5c6ROzhtwANVRThs3shInSS1la.png)

然后，执行 ./atlassian-confluence-7.2.1-x64.bin 安装，注意安装完成后先不要急着启动！！！
![atlassian-confluence-install.jpg](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpkP20zD5fnEtYmakle0O1eyUj5W.jpeg)

### 2.3 破解

由于 Confluence 本身是一个收费的软件，想要免费安装，可以使用 pengzhile 提供的在 GitHub 上开源了对 Atlassian 家所有产品（包括插件市场所有收费插件）的破解方法。

- [Gitee: pengzhile/atlassian-agent](https://gitee.com/pengzhile/atlassian-agent)
- [GitHub: pengzhile/atlassian-agent](https://github.com/pengzhile) (DMCA takedown)
- [**编译好的包**](https://pan.baidu.com/s/1AucTmTNPSG85hhWF7mkIcQ)，提取码：`n4ug`

具体做法如下。

1.  将 atlassian-agent.jar 放在一个你不会随便删除的位置（你服务器上的所有 Atlassian 服务可共享同一个 atlassian-agent.jar）

```bash
tar zvxf atlassian-agent-v1.2.3.tar.gz -C /data/apps/atlassian
```

2.  非常重要！！！需要设置环境变量 JAVA_OPTS，避免开机失效。在 [atlassian-agent](https://gitee.com/pengzhile/atlassian-agent) 的说明中提供了 3 个建议，大家可以根据自己需要去设置，这里我们选择第二种方法：把 JAVA_OPTS 环境放到服务安装所在 bin 目录下的 setenv.sh 或 setenv.bat 中。

```bash
# vim /data/apps/atlassian/confluence/bin/setenv.sh

CATALINA_OPTS="-javaagent:/data/apps/atlassian/atlassian-agent-v1.2.3/atlassian-agent.jar ${JAVA_OPTS}"
```

![cinfluence-setenv.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhczP92LnsJhUTq9TRHjeAYkKYmd.png)

3.  准备就绪后，我们就要开启 Configuration 了，找到启动脚本并启动 start-confluence.sh，启动完成后我们可以通过浏览器进行访问。

![start_confluence.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrtpIUcif5V1K8gXtSpHXUgGcox3.png)

### 2.4 配置

在浏览器中打开 **<http://localhost:8090>** 或者 \*\*http\://<你服务器的公网 IP>:8090 \*\*，打开 Confluence 的配置页面。

选择中文，产品安装。
![01-产品安装.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoM2tysNankGbPYt-UXdDofwoWzM.png)

获取应用。
![02-获取应用.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnD_VyxXgzhtQyPO4r1hN5zeWF9k.png)

获得服务器 ID 及授权码提示。
![03-授权码.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvuroXP_Z_y0p-g1ogMihijfFIvO.png)

### **2.5 授权码**

当我们在后台服务器通过命令行执行 java -jar /atlassian-agent.jar 时应该可以看到输出的 KeyGen 参数帮助。

- 破解 Confluence 时，选择 conf 即可，具体命令如下：

```bash
# 将server ID复制（-m 邮箱 -n 用户名 -o 公司名 -s SERVER ID）
java -jar atlassian-agent.jar -p conf -m ishenweiyan@foxmail.com -n shenweiyan -o wiki-test -s B7DP-BX09-325B-DJLP
```

- 破解团队日程表时，选择 tc 即可，具体命令如下：

```bash
# 将server ID复制（-m 邮箱 -n 用户名 -o 公司名 -s SERVER ID）
java -jar atlassian-agent.jar -p tc -m ishenweiyan@foxmail.com -n shenweiyan -o wiki-test -s B7DP-BX09-325B-DJLP
```

- 破解 Confluence Questions 时，选择 questions 即可，具体命令如下：

```bash
# 将server ID复制（-m 邮箱 -n 用户名 -o 公司名 -s SERVER ID）
java -jar atlassian-agent.jar -p question -m ishenweiyan@foxmail.com -n shenweiyan -o wiki-test -s B7DP-BX09-325B-DJLP
```

将生成的授权码粘贴，下一步。
![04-授权码.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fknwnui-bJqhlI1_p0_AIJrKQ0dn.png)

设置数据库，生产环境建议独立的数据。
![05-设置数据库.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtFvK_Y2DnZYLOrwqRIKNbu2ZqWN.png)

选择 PostgreSQL 数据库，填写数据库信息，测试数据库连通性。
![06-设置-测试数据库.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpHJirbRRQJ8of-Ux0FMQhnFJJv-.png)

过一会你就可以看到这个页面了，安装成功了。

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrcZbpu_e3ocfXaYWWrhWM3Hdkbb.png)

## 3. 使用与管理

### 3.1 使用

#### 1. 选择站点

如果是全新的站点，那就选择空白站点，如果只是升级或者备份恢复，那就选择从备份还原站点。这里我们选择"示范站点"。
![07-示范站点.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj8hcocs17OiXr15ezpiQF3iz7k6.png)

#### 2. 配置用户管理

配置用户，如果有 Jira 环境的话 ，可以集成 Jira 的用户管理，也可以使用 confluence 自己的用户，那就选择“在 confluence 中管理用户和组”。
![08-配置用户管理.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrchRIEbAooYjOV1ivdssHCvwWZc.png)
![09-设置系统管理员.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmo9iwK9BBYjXpybhYjfDk55QE-n.png)
![10-设置成功.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjBV9AbjCPH11B78hK4rzpvADQd4.png)

#### 3. 创建空间

![创建空间.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fl0U4NJLPFs63Q6_ChC2pIelmMiJ.png)
空间创建完成后，就会自动进入已经创建好的空间，接下来，enjoy！
![进入空间.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmIY9RLRaNgWYpGJZERUSDKxdz6c.png)

### 3.2 站点管理

点击右上角，可以进行站点管理，常用的如 **"一般配置"**：
![一般配置.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq8BjZIlWxpR-t3yBveaLSnaNRu6.png)
点击一般配置，授权管理，可以查看到授权情况：
![授权信息.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FixsCBHkKdY68UCDhcgK_LLMAqGB.png)
当然本文介绍的方式仅用于学习体验，有能力的还是建议支持正版！！！

## 4. 备份恢复

Confluence 本身会有每日的备份管理，就是定时备份任务（“一般配置”→“每日备份管理”）。
![每日备份管理.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqaJjQUmnAajkkEC2rwEepNKoloa.png)
由于一些其他原因需要新建一个 Confluence 环境，然后还原的，可以点下面的\*\*“备份与还原”\*\*。

- 如果您的导出文件很小(小于 25 MB)，请直接在浏览器“备份与还原”页面直接进行上传。
- 而较大的文件需要从主目录导入。需要提前将备份的文件放到 **/path/to/application-data/confluence/restore** 下。

具体备份与还原，可以参考 **“一般配置”** → \*\*“备份与还原” \*\*页面的详细介绍。
![备份与还原-Confluence.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk-UdPQjXEgm7xLDdE-6Qh9rRb53.png)

## 5. 参考资料

1.  武培轩，《[CentOS 7 安装 JAVA 环境（JDK 1.8）](https://www.cnblogs.com/wupeixuan/p/11433922.html)》，博客园
2.  王良付，《[CentOS 7.6 安装 Confluence 7.2](https://liangfu.wang/2020/01/22/CentOS-7-6-%E5%AE%89%E8%A3%85-Confluence-7-2/)》，良付の博客
3.  胖哥叨逼叨，《[Atlassian Confluence 部署-confluence 安装](https://www.pangshare.com/1919.htm)》，WordPress
4.  Agile Project Management \* DIY Electronics，《[How to install Confluence on Centos7 with PostgreSQL](https://comtronic.com.au/how-to-install-confluence-on-centos7-with-postgresql/)》，Comtronic Blog
