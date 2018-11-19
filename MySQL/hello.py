def hello():
    print('=============================='
          '\n==                          =='
          '\n==      欢迎使用本系统      =='
          '\n==                          =='
          '\n==      请选择所需功能      =='
          '\n==                          =='
          '\n==     +  1.添加数据  +     =='
          '\n==     +  2.查询数据  +     =='
          '\n==     +  3.更改数据  +     =='
          '\n==     +  4.删除数据  +     =='
          '\n==     +  5.退出程序  +     =='
          '\n==                          =='
          '\n==============================')


def insert_options():
    i = 1
    while i == 1:
        try:
            i = 0
            return int(input('=============================='
                             '\n==     +   1.新建表   +     =='
                             '\n==     +  2.添加人物  +     =='
                             '\n==     +   3.上一级   +     =='
                             '\n=============================='
                             '\n: '))
        except:
            print('请输入正确信息!')


def query_header():
    print('=============================='
          '\n==         查询数据         =='
          '\n==============================')


def updata_options():
    i = 1
    while i == 1:
        try:
            i = 0
            return int(input('=============================='
                             '\n==    +   1.更改表名   +    =='
                             '\n==     +  2.更新人物  +     =='
                             '\n==     +   3.上一级   +     =='
                             '\n=============================='
                             '\n: '))
        except:
            print('请输入正确信息!')


def delete_options():
    i = 1
    while i == 1:
        try:
            i = 0
            return int(input('=============================='
                             '\n==     +   1.删除表   +     =='
                             '\n==     +  2.删除人物  +     =='
                             '\n==     +   3.上一级   +     =='
                             '\n=============================='
                             '\n: '))
        except:
            print('请输入正确信息!')


def input_id(title):
    # 判断id的类型正确
    while 1:
        try:
            id = int(input(title))
            break
        except:
            print('请输入正确信息!')
    return id


def input_age(title):
    # 判断age的类型正确
    while 1:
        try:
            age = int(input(title))
            break
        except:
            print('请输入正确信息!')
    return age