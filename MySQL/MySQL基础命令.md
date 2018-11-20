#MySQL : 创建、修改和删除表

###连接数据库:

```python
import pymysql
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
```

###连接数据库的'xxx'表

```python
import pymysql
db = pymysqk.connect(host='localhost', user='root', password='123456', port=3306, db='xxx')
```

###操作数据库命令:

```python
关闭
db.close()

定义光标
cursor = db.cursor()

实行sql语句
cursor.execute(sql)

数据插入
# 执行db对象的commit()方法才可以实现数据插入, 这个方法才是真正将语句提交到数据库执行的方法, 对于数据插入、更新、删除操作, 都需要调用该方法才能生效
db.commit()

数据回滚
# 如果执行失败, 则调用rollback()执行数据回滚, 相当于什么都没有发生过
db.rollback()

获取当前mysql版本
sql = 'SELECT VERSION()'

查看已经存在的数据库
sql = 'SHOW DATABASES'

创建数据库 默认字符集utf8
sql = 'CREATE DATABASE 库名 DEFAULT CHARACTER SET utf8'
# MySQL自动将数据库名的大写字母替换为小写字母

删除数据库
sql = 'DROP DATABASE 库名'
```

### 返回数据命令:

```python

返回单个数据
data = cursor.fetchone()
# 调用一次fetchone()方法, 指针就会指向下一条数据

返回所有数据
data = cursor.fetchall()
# 会将结果以元祖形式全部返回, 如果数据量很大, 那么占用的开销会非常高
# 最好用while循环加fetchone()方法来获取所有数据

```

## 操作表命令:

###1. 创建表的形式:

```python
# 创建表之前有一定要在链接数据库是指定数据库"db='库名'"
第一种方法:直接创建
sql = 'CREATE TABLE 表名 (属性名 数据类型 完整约束条件, 
						属性名 数据类型 完整约束条件, 
  						...
    					属性名 数据类型 完整约束条件)'
第二种方法: 先判断数据空中是否有此表, 如果没有则创建
sql = 'CREATE TABLE IF NOT EXISTS 表名(属性名 数据类型 完整约束条件, 
										属性名 数据类型 完整约束条件, 
  										...
    									属性名 数据类型 完整约束条件)'
```



## 完整性约束条件

```
完整性约束条件
----------------------------------------------------------------------
PRIMARY KEY		标识该属性为该表的"主键", 可以唯一的标识对应的元组
FOREIGN KEY		标识该属性为该表的"外键", 是与之联系某表的主键
NOT NULL		标识该属性"不能为空"
UNIQUE			标识该属性的值是"唯一"的
AUTO_INCREMENT	标识该属性的值是"自动增加", 这是MySQL的SQL语句的特色
DEFAULT			为该属性设置默认值
----------------------------------------------------------------------
```



## 2.设置表的主键

```python
单字段主键格式:
  属性名  数据类型 PRIMARY KEY
  实例:
    # id 为主键
    sql = 'CREATE TABLE 表名(id int PRIMARY KEY, name varchar(20))'
多字段主键格式:
  PRIMARY KEY(属性名1, 属性名2..., 属性名n)
  实例:
    # id, stu_id为主键
    sql = 'CREATE TABLE 表名(id int, stu_id int, name varchar(20), PRIMARY KEY(id, stu_id))'
```



## 3.设置表的外键

```python
格式:
  CONSTRAINT 外键别名 FOREIGN KEY(属性1, 属性2..., 属性n) REFERENCES 表名(属性1, 属性2..., 属性n)
  实例:
    sql = 'CREATE TABLE 表名1 (id int RPIMARY KEY, 
    							stu_id int, 
      							name varchar(20), 	
        						CONSTRAINT 外键别名 FOREIGN KEY(stu_id) REFERENCES 表名2(id)')
	# 创建表1, 将表1的stu_id与表2的id链接
```



## 4.设置表的非空约束

```python
格式:
  # 此属性不能为空, 不填的话会"报错"
  属性名 数据类型 NOT NULL
```



## 5.设置表的唯一性约束

```python
格式:
  # 此属性的值不能重复
  属性名 数据类型 UNIQUE
```



## 6.设置表的属性值自动增加

```python
格式:
  # AUTO_INCREMNT约束的字段可以使任何整数类型(TINYINT, SMALLINT, INT和BIGINT), 在默认的情况下, 该字段是从1开始自增
  属性名 数据类型 AUTO_INCREMNT
```



## 7.设置表的属性的默认值

```python
格式:
  属性名 数据类型 DEFAULT 默认值
```



## *综合示例:

```python
sql = 'CREATE TABLE student (
		id int PRIMARY KEY AUTO_INCREMENT,
  		teacher_id int UNIQUE,
    	name varchar(20) NOT NULL,
      	sex varchar(10) DEFAULT 'male')
# 创建student表, id为主键和自动增加, teacher_id为唯一的, name为非空, sex默认是'male'
```



## *查看表结构

```python
格式:
  DESCRIBE 表名
  # 通过查看表的结构, 就很明确的对表进行解读, 而且可以查看一下自己创建的表有没有错误
```

## 查看表详细结构

```python
格式:
  # 通过这个SQL语句可以查看表的详细定义, 除了字段名, 字段的数据类型, 约束条件外, 还可以查看表的默认存储引擎和字符编码
  SHOW CREATE TABLE 表名
```



## 修改表

```python
1.修改表名:
  格式:
    ALTER TABLE 原表名 RENAME 新表明
    
2.修改字段的数据类型:
  格式:
    ALTER TABLE 表名 MODIFY 属性名 数据类型

3.修改字段名:
  格式:
    ALTER TABLE 表名 CHANGE 原属性名 新属性名 新数据类型

4.增加字段:
  格式:
    ALTER TABLE 表名 ADD 属性名1 数据类型 完整性约束条件 [FIRST | AFTER 属性名2]
    # 其中, "属性名1"参数指需要增加的字段的名称, "FIRST"参数是可选参数, 起作用是将新增字段设置为表的第一个字段, "AFTER"参数也是可选的参数, 其作用是将新增字段添加到已有的"属性名2"字段的后面.

5.删除字段:
  格式:
    ALTER TABLE 表名 DROP 属性名

6.更改表的存储引擎:
  格式:
    ALTER TABLE 表名 ENGINE = 存储引擎名
    
7.删除表的外键约束:
  格式:
    ALTER TABLE 表名 DROP FOREIGN KEY 外键别名
```

## 删除表:

```python
格式:
  # 删除没有被关联的普通表
  DROP TABLE 表名
  # 删除被其他表关联的父表
  1. 先删除子表, 再删除父表
  2. 删除父表的外键约束, 再删该表
```



## 查询表内数据

```python
查询表内所有数据:
  格式:
    SELECT * FROM 表名
    
按条件查找数据:
  格式:
    SELECT * FROM 表名 WHERE 属性名="属性值"
    比较:
      SELECT * FROM 表名 WHERE 属性名 > 属性值
      
      
查看找到的数据的数量
number = cursor.rowcount
```


