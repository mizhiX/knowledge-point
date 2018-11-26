import pymysql
# 链接mysql  db='Once_Upon_a_Time'库
db = pymysql.connect(host='localhost', user='root', password='yao120', port=3306, db='Once_Upon_a_Time')
# 创建光标
cursor = db.cursor()


# TODO 1.创建表
def create_table(table_name):
    """
    CREATE TABLE IF NOT EXISTS students  如果students库不存在则创建该库
    VARCHAR(255) 可变长字符串 最长255
    INT 整数类型
    NOT NULL 非空约束
    PRIMARY KEY (id)  设置主键为id
    """

    create_sql = 'CREATE TABLE IF NOT EXISTS %s (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    # 执行sql语句
    try:
        cursor.execute(create_sql % table_name)
        print('%s创建成功!' % table_name)
    except:
        print('%s表已存在' % table_name)


# TODO 查询所有的表名
def query_table(switch=0):
    query_sql = 'select table_name from information_schema.tables where table_schema="Once_Upon_a_Time" and table_type="base table"'
    try:
        cursor.execute(query_sql)
        # 表的总数
        count = cursor.rowcount
        if switch == 0:
            print('共有%d个表' % count)
        row = cursor.fetchone()
        rows = []
        while row:
            rows += row
            row = cursor.fetchone()
        table_count = len(rows)
        if switch == 0:
            for i in range(table_count):
                count = i + 1
                print(str(count) + '.' + rows[i])
        return rows
    except:
        db.rollback()


# TODO 2.插入数据(增)
def insert_into(table_name, id, name, age):
    """
    insert into hero 向hero表添加数据
    """

    insert_sql = 'INSERT INTO %s(id, name, age) values(%s, "%s", %s)'
    # print(insert_sql)
    try:
        cursor.execute(insert_sql % (table_name, id, name, age))
        # commit() 提交
        db.commit()
        print('数据添加成功!')

    except:
        '''
        注意: 如果执行失败, 则调用rollback()执行数据回滚, 相当于什么都没有发生过.
        rollback_commit.TXT有深入讲解
        '''
        db.rollback()
        # 更新数据
        insert_or_update(table_name, id, name, age)



# TODO 3.更新数据(改)
""" 没有第二种方法强大
def update(name, age):
    '''
    uodate 更新在hero集name为Emma的age属性
    '''
    ''' 第一种方法:基础的更新数据'''
    update_sql = 'UPDATE hero SET age = %s WHERE name = %s'
    try:
        cursor.execute(update_sql, (age, name))
        db.commit()
    except:
        db.rollback()
        print('Failed')
"""


# TODO 更新表数据
def insert_or_update(table_name, id, name, age):
    """第二种方法: 判断id是否存在 如果存在则更新数据, 如果不存在则插入数据"""
    table_name = tuple([table_name])
    data = id, name, age

    sql = 'INSERT INTO %s(id, name, age) values (%s, "%s", %s) ON DUPLICATE KEY UPDATE id = %s, name = "%s", age = %s'
    try:
        cursor.execute(sql % (table_name + data * 2))
        db.commit()
        print('数据更新成功!')
    except:
        db.rollback()
        print('Failed')


# 更新表名
def rename_table(table_name, new_table_name):
    rename_sql = 'alter table %s rename as %s'
    try:
        cursor.execute(rename_sql %(table_name, new_table_name))
        print('%s表成功更改为%s表' % (table_name, new_table_name))
        db.commit()
    except:
        db.rollback()
        print('Failed')


# TODO 4.删除数据(删)
def delete_field(table_name, del_id):
    # 删除一条数据
    '''
    delete 删除
    from 从哪里
    where 删除的数据信息
    '''
    delete_sql = 'DELETE FROM %s where %s="%s"'
    try:

        cursor.execute(delete_sql % (table_name, 'id', del_id))
        db.commit()
        print('id:%s 删除成功!' % del_id)
    except:
        db.rollback()
        print('delete Failed')


def delete_table(table_name):
    delete_sql = 'DROP TABLE %s'
    try:
        cursor.execute(delete_sql % table_name)
        db.commit()
        print('%s表删除成功!' % table_name)

    except:
        db.rollback()
        print('delete table Failed')


# TODO 5.查询数据(查)
def query_data(table_name, id=None, name=None, big_age=None, small_age=None):
    """
    """
    if id:
        try:
            id = int(id)
            query_sql = 'SELECT * FROM %s WHERE id = %s' % (table_name, id)
            pass
        except:
            pass
    elif name:
        query_sql = 'SELECT * FROM %s WHERE name = "%s"' % (table_name, name)
    elif big_age:
        print(small_age)
        print(big_age)
        query_sql = 'SELECT * FROM %s WHERE age >= %s and age <= %s' % (table_name, small_age, big_age)
    else:
        query_sql = 'SELECT * FROM %s' % (table_name)
    try:
        cursor.execute(query_sql)
        # 返回查找到的总数
        count = cursor.rowcount
        print('%s共有%d条数据' % (table_name, count))
        row = cursor.fetchone()
        while row:
            row_list = list(row)
            print('id: %s, name: %s, age: %s' % (row_list[0], row_list[1], row_list[2]))
            row = cursor.fetchone()
    except:
        print('Failed')


# 添加新id时, 查看id是否重复
def query_id(table_name, id):
    query_sql = 'SELECT * FROM %s WHERE id = %s' % (table_name, id)
    try:
        cursor.execute(query_sql)
        count = cursor.rowcount
        if count > 0:
            return 1
        else:
            pass
    except:
        print('Failed')


def db_close():
    db.close()


def main():
    table_name = 'Once_Upon_a_Time'
    create_table(table_name)
    # 关闭
    db.close()


if __name__ == '__main__':
    main()
