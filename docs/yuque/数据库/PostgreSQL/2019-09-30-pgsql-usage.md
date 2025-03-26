---
title: PostgreSQL 常用命令
urlname: 2019-09-30-pgsql-usage
author: 章鱼猫先生
date: 2019-09-30
updated: "2023-08-22 11:03:01"
---

关于 PostgreSQL 的基本用法，供初次使用者上手。以下内容基于 CentOS 操作系统，其他操作系统实在没有精力兼顾，但是大部分内容应该普遍适用。

## 1. 数据库登录

- **重启：** /etc/init.d/postgresql restart
- **登陆：** psql -U user -d dbname  （默认的用户和数据库是 postgres）

```
psql -h 172.16.254.21 -p 5432 -U postgres –d databasename     # 访问远程数据库
```

```
\h             // 查看 SQL 命令的解释，比如 \h select。
\?             // 查看 psql 命令列表。
\l             // 列举数据库，相当于 mysql 的 show databases
\c dbname      // 切换数据库，相当于 mysql 的use dbname
\dt            // 查看表结构，相当于 desc tblname,show columns from tbname
\d tblname     // 看数据结构
\di            // 查看索引
\q             // 退出
```

```
create database [数据库名];               // 创建数据库
drop database [数据库名];                 // 删除数据库
alter table [表名A] rename to [表名B];    // 重命名一个表
```

## 2. 用户操作

创建删除用户：postgres 创建除 postgres 本身以外的新用户，需要通过以 postgres 登录命令行的方式进行创建，或者删除。

### 创建新用户

```bash
createuser -P 用户名
```

运行该命令后系统会自动提示输入该用户的密码、是否为超级用户、是否具有创建数据库，或者其他用户的权限。

```
bash-4.1$ createuser -P shenweiyan`
Enter ``password` `for` `new role:`
Enter it again:`
Shall the new role be a superuser? (y/n) n`
Shall the new role be allowed ``to` `create` `databases? (y/n) y`
Shall the new role be allowed ``to` `create` `more new roles? (y/n) n
```

### 为新用户创建新数据库

```bash
createdb 数据库名 -O 用户名
```

```
bash-4.1$ createdb djangodb -O shenweiyan
bash-4.1$ psql`
psql (8.4.20)`
Type "help" for elp.
postgres=# \l
List of databases
Name    |   Owner    | Encoding |  Collation  |    Ctype    |   Access privileges
-----------+------------+----------+-------------+-------------+-----------------------
djangodb  | shenweiyan | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
postgres  | postgres   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
template0 | postgres   | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres
                                                              : postgres=CTc/postgres
template1 | postgres   | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres
                                                              : postgres=CTc/postgres
(4 rows)
bash-4.1$
```

### 删除用户

```bash
dropuser -e 用户名
```

**注意：删除用户，必须先要删除该用户所拥有的数据库，否则无法删除。**

```
bash-4.1$ dropuser -e shenweiyan
DROP ROLE shenweiyan;
dropuser: removal of role "shenweiyan" failed: ERROR:  role "shenweiyan" cannot be dropped because some objects depend on it
DETAIL:  owner of database djangodb
bash-4.1$ dropdb -U postgres -e djangodb
DROP DATABASE djangodb;
bash-4.1$ dropuser -e shenweiyan
DROP ROLE shenweiyan;
```

### 查看数据库用户

```sql
select * from pg_user; （注意分号不能省）
```

```
postgres=# select * from pg_user;
  usename   | usesysid | usecreatedb | usesuper | usecatupd |  passwd  | valuntil | useconfig
------------+----------+-------------+----------+-----------+----------+----------+-----------
 postgres   |       10 | t           | t        | t         | ******** |          |
 shenweiyan |    16408 | t           | f        | f         | ******** |          |
(2 rows)
```

### 修改数据库内某个用户密码

```
postgres=# \password djangoadmin
Enter new password:
Enter it again:
postgres=#
```

## 3. 数据库操作

### 3.1 数据库导入与导出

数据库的导入导出是最常用的功能之一，每种数据库都提供有这方面的工具，例如 Oracle 的 **exp/imp**，Informi 的**dbexp/dbimp**，MySQL 的 **mysqldump**，而 PostgreSQL 提供的对应工具为 **pg_dump** 和 **pg_restore**。

**pg_dump** 是用于备份 PostgreSQL 数据库的工具。它可以在数据库正在使用的时候进行完整一致的备份，并不阻塞其它用户对数据库的访问。

转储格式可以是一个脚本（纯文件）或者归档文件。转储脚本的格式是纯文本，包含许多 SQL 命令，这些 SQL 命令可以用于重建该数据库并将之恢复到保存脚本时的状态。可以使用 **psql** 从这样的脚本中恢复。它们甚至可以用于在其它机器甚至是其它硬件体系的机器上重建数据库，通过对脚本进行一些修改，甚至可以在其它 SQL 数据库产品上重建数据库。

归档文件格式必须和 **pg_restore** 一起使用重建数据库。它们允许 **pg_restore** 对恢复什么东西进行选择，甚至是在恢复之前对需要恢复的条目进行重新排序。归档文件也是可以跨平台移植的。

**最简单的导出命令如下(导出指定数据库)：**

```bash
$ pg_dump db_name > db.sql
$ pg_dump -U postgres -f mydatabase.sql mydatabase
$ pg_dump -h 数据库服务器地址 -U postgres(用户名) (-t 表名) 数据库名(缺省时同用户名) > 路径/文件名.sql
```

**导入数据时，首先创建数据库，再用 psql/pg_restore 导入：**

```
$ createdb newdatabase
$ psql -d newdatabase -U postgres -f mydatabase.sql
$ pg_restore -d newdb db.dump

```

---

### 3.2 修改数据库名

```plsql
ALTER DATABASE "3_8_dev_test" RENAME TO "3_8_dev_demo";
```

## 4. 常用数据库表操作

### 数据表导入与导出

在 postgres 数据库中执行：
```
bash-4.1$ psql
psql (10.18, server 9.6.23)
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 galaxydb  | shenwy   | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/shenwy           +
           |          |          |             |             | shenwy=CTc/shenwy
 plpgsql   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(5 rows)

postgres=# \c plpgsql
psql (10.18, server 9.6.23)
You are now connected to database "plpgsql" as user "postgres".
# 从数据库中把 clustercas_gene 表导出为表格(\t)，且带表头
plpgsql=# \copy clustercas_gene to '/home/shenweiyan/pg/clustercas_gene.txt' with csv header DELIMITER E'\t';
COPY 3
```

在命令行中执行：
```
# 从 galaxydb 数据库中把 galaxy_user 表导出为表格(\t)，默认不带表头
$ echo 'copy "galaxy_user" to stdout' | psql galaxydb > galaxy_user.txt

# 从 galaxydb 数据库中把 galaxy_user 表导出为 sql
$ pg_dump -Upostgres -t galaxy_user -f galaxy_user.sql galaxydb

# 把 galaxy_user.txt 内容导入 galaxy_user 表
galaxydb=# \copy "galaxy_user" from '/home/postgres/galaxy_user.txt';

# 把 galaxy_user.sql 导入 galaxy_user 表
$ psql -U galaxy -d galaxydb -f galaxy_user.sql
```

### 赋予所有权限

```
# 把 galaxydb 数据库的所有权限赋予 shenweiyan 用户
postgres=# grant all on database galaxydb to shenweiyan;
```

### 常用数据表操作命令

```
# 创建 user_table 新表
CREATE TABLE user_table(name VARCHAR(20), signup_date DATE);
# 在 user_table 表中插入数据
INSERT INTO user_table(name, signup_date) VALUES('张三', '2013-12-22');
# 查找 user_table 表记录
SELECT * FROM user_table;
# 更新数据
UPDATE user_table set name = '李四' WHERE name = '张三';
# 删除记录
DELETE FROM user_table WHERE name = '李四' ;
# 添加 email 字段
ALTER TABLE user_table ADD email VARCHAR(40);
# 更新结构
ALTER TABLE user_table ALTER COLUMN signup_date SET NOT NULL;
# 重命名 signup_date 字段
ALTER TABLE user_table RENAME COLUMN signup_date TO signup;
# 删除字段
ALTER TABLE user_table DROP COLUMN email;
# 表重命名
ALTER TABLE user_table RENAME TO user_tbl;
# 删除表
DROP TABLE IF EXISTS user_tbl;
```

## 4. 备份数据库 shell 脚本

```
#!/bin/bash
#PostgreSQL database_backup

#SET VARIABLE-----

DB_NAME="galaxydb"
DB_USER="shenweiyan"
BIN_DIR="/usr/bin/pg_dump"
BACK_DIR="/data/db_backup/galaxy"
LOG_DIR="/root/logs"
DATE="$(date +'%Y%m%d-%H-%M')"
LogFile="${LOG_DIR}/${DB_NAME}-bakup.log"
BackNewFile=${DB_NAME}-$DATE.sql
KEEP_TIME="30"

#BACK_UP----------------------------------------------------

[ ! -d ${BACK_DIR} ] && mkdir -p ${BACK_DIR}

$BIN_DIR -U $DB_USER -Fc $DB_NAME > $BACK_DIR/${BackNewFile}

echo -----------------------"$(date +"%Y-%m-%d %H:%M:%S")"----------------------- >> $LogFile

echo  createFile:"$BackNewFile" >> $LogFile

#BACK_UP_FILE_CLEAN ----------------------------------------

find "${BACK_DIR}" -atime +$KEEP_TIME -type f -name "${DB_NAME}-*.sql" -print > ${LOG_DIR}/${DB_NAME}_del_list

echo -e "delete files:\n" >> $LogFile

cat ${LOG_DIR}/${DB_NAME}_del_list | while read LINE
do
    rm -rf $LINE
    echo $LINE >> $LogFile
done

echo -e "---------------------------------------------------------------\n \n" >> $LogFile
```
