import re

import pymysql
# connect()链接
db = pymysql.connect(host='localhost', user='root', password='yao120', port=3306)
# cursor()光标
cursor = db.cursor()
# execute()实行 # select version() 选择版本
# 获取当前版本
cursor.execute('SELECT VERSION()')
# fetchone() 返回单个元组
data = cursor.fetchone()
print('Database version:', data)

cursor.execute('SHOW DATABASES;')
tables = [cursor.fetchall()]
# print(tables)
table_list = re.findall("\('(.*?)',\)", str(tables))
# print(table_list)
base_name = 'spiders'
# 判断数据库base_name是否存在, 如果不存在则创建数据库base_name
if base_name not in table_list:
    # create dataase创建数据库 spiders(数据库名字) default character set utf8 默认字符集utf8
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
else:
    print('已存在数据库' + base_name)
# close()关闭
db.close()