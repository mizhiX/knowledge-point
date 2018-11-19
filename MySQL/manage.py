from hello import *
from MySQL_using import *


def main():
    while 1:
        hello()
        while 1:
            try:
                option = int(input(': '))

                if option > 0 and option < 6:
                    break
                else:
                    print('请输入正确信息!')
            except:
                print('请输入正确信息!')

        if option == 1:
            # 添加数据
            while 1:
                insert_option = insert_options()
                if insert_option == 1:
                    # 新建表
                    while 1:
                        try:
                            table_name = input('请输入表名: ')
                            if table_name in query_table(switch=1):
                                print('%s表已存在!' % table_name)
                                break
                            else:
                                create_table(table_name)
                                break
                        except:
                            print('请从新输入!')

                elif insert_option == 2:
                    # 添加人物
                    while 1:
                        table_list = query_table()
                        table_option = input('请选择要添加人物的表号,如不更改按q返回\n:')
                        try:
                            if table_option == 'q':
                                break
                            elif int(table_option) > len(table_list):
                                print('超出总表数,请从新选择。')
                                pass
                            else:
                                table_name = table_list[int(table_option) - 1]
                                print('进入%s表' % table_name)
                                id_title = 'id: '
                                id = input_id(id_title)
                                judge = query_id(table_name, id=id)
                                while 1:
                                    i = 1
                                    if judge == 1:
                                        select_option = input('此id已存在:\n1.更新此id数据\n2.输入新id\n3.上一级\n: ')
                                        if select_option == '1':
                                            break
                                        elif select_option == '2':
                                            while 1:
                                                try:
                                                    id = int(input('id: '))
                                                    break
                                                except:
                                                    print('请输入正确信息!')
                                            break
                                        elif select_option == '3':
                                            i = 0
                                            break

                                        else:
                                            print('请输入正确信息!')
                                    else:
                                        break
                                if i == 1:
                                    name = input('name: ')
                                    age_title = 'age: '
                                    age = input_age(age_title)
                                    insert_into(table_name, id, name, age)

                        except:
                            print('请输入正确信息')

                elif insert_option == 3:
                    break

        elif option == 2:
            # 查询数据
            while 1:
                query_header()
                query_list = query_table()
                query_option = input('请选择要查询人物的表号,如不查询按q返回\n: ')
                try:
                    if query_option == 'q':
                        break
                    elif int(query_option) > len(query_list):
                        print('超出总表数,请从新选择。')
                        pass
                    else:
                        while 1:
                            table_name = query_list[int(query_option) - 1]
                            print('进入%s表' % table_name)
                            select_option = input('1.id查找\n2.name查找\n3.age查找\n4.展示所有\nq.返回\n')

                            if select_option == '1':
                                id_title = '请输入需要查询的id\n: '
                                id = input_id(id_title)
                                query_data(table_name, id=id)
                                option_quit = input('按任意键返回')
                                break

                            elif select_option == '2':
                                name = input('请输入需要查询的name\n: ')
                                query_data(table_name, name=name)
                                option_quit = input('按任意键返回')
                                break

                            elif select_option == '3':
                                big_age_title = '请输入需要查询的最大age\n: '
                                big_age = input_age(big_age_title)
                                small_age_title = '请输入需要查询的最小age\n: '
                                small_age = input_age(small_age_title)
                                query_data(table_name, big_age=big_age, small_age=small_age)
                                option_quit = input('按任意键返回')
                                break

                            elif select_option == '4':
                                query_data(table_name)
                                option_quit = input('按任意键返回')
                                break

                            elif select_option == 'q':
                                break

                            else:
                                print('请输入正确信息!')

                            # 跳出本次循环
                            continue
                except:
                    print('请输入正确信息!')

        elif option == 3:
            # 更改数据
            while 1:
                updata_option = updata_options()
                if updata_option == 1:
                    query_list = query_table()
                    while 1:
                        table_name = input('请输入要更改的表名\n: ')
                        if table_name not in query_list:
                            print('%s表不存在, 请从新输入\n: ' % table_name)
                        else:
                            break
                    while 1:
                        new_table_name = input('请输入新的表名\n: ')
                        if table_name in query_list:
                            print('%s表已存在, 请从新输入\n: ' % new_table_name)
                        else:
                            break
                    new_table_name = input('请输入新的表名\n: ')
                    rename_table(table_name, new_table_name)

                elif updata_option == 2:
                    while 1:
                        table_list = query_table()
                        table_option = input('请选择要更新人物的表号,如不查询按q返回\n: ')
                        try:
                            if table_option == 'q':
                                break
                            elif int(table_option) > len(table_list):
                                print('超出总表数,请从新选择。')
                                pass
                            else:
                                while 1:
                                    table_name = table_list[int(table_option) - 1]
                                    print('进入%s表' % table_name)
                                    id_title = '请输入要更新的id: '
                                    id = input_id(id_title)
                                    judge = query_id(table_name, id)
                                    i = 1

                                    if judge != 1:
                                        while 1:
                                            judge_option = input('id%s未在%s中!\n1.添加新人物\n2.返回\n: ' % (id, table_name))
                                            if judge_option == '1':
                                                i = 1
                                                break
                                            elif judge_option == '2':
                                                i = 0
                                                break
                                            else:
                                                print('请输入正确信息!')

                                    if i == 1:
                                        name = input('请输入此id更新的name: ')
                                        age_title = '请输入此id更新的age: '
                                        age = input_age(age_title)
                                        insert_or_update(table_name, id, name, age)
                                    break
                        except:
                            print('请输入正确信息!')

                elif updata_option == 3:
                    # 返回上一级
                    break
                continue

        elif option == 4:
            # 删除数据
            while 1:
                delete_option = delete_options()
                if delete_option == 1:
                    # 删除表
                    table_list = query_table()
                    table_option = input('请选择要删除的表号,如不删除按q返回\n: ')
                    try:
                        if table_option == 'q':
                            break
                        elif int(table_option) > len(table_list):
                            print('超出总表数,请从新选择。')
                            pass
                        else:
                            table_name = table_list[int(table_option) - 1]
                            delete_table(table_name)
                    except:
                        print('请输入有效信息!')

                elif delete_option == 2:
                    # 删除人物
                    table_list = query_table()
                    delete_table_option = input('请选择要删除人物的表号,如不删除按q返回\n: ')
                    try:
                        if delete_table_option == 'q':
                            break
                        elif int(delete_table_option) > len(table_list):
                            print('超出总表数,请从新选择。')
                        else:
                            while 1:
                                table_name = table_list[int(delete_table_option) - 1]
                                query_data(table_name)
                                delete_id = input('请输入要删除的id, 如不删除按q返回\n: ')
                                try:
                                    if delete_id == 'q':
                                        break
                                    elif int(delete_id):
                                        delete_id = int(delete_id)
                                        judge = query_id(table_name, id=delete_id)
                                        if judge == 1:
                                            delete_field(table_name, delete_id)
                                        else:
                                            print('id:%s 不存在!' % delete_id)

                                    else:
                                        print('请输入有效信息!')
                                except:
                                    print('请输入有效信息!')


                    except:
                        print('请输入有效信息!')


                elif delete_option == 3:
                    # 返回上一级
                    break

        elif option == 5:
            # 退出程序
            print('系统退出成功')
            db_close()
            break


if __name__ == '__main__':
    main()