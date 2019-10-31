#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

info = []

# 欢迎界面的函数
def menu_display():
    '''
    功能:显示菜单
    :return:无
    '''
    print('╔'+"".ljust(31, "═")+'╗')
    print("║", "欢迎使用名片管理系统v3.8.1c".center(21, " "), "║")
    print('╠═══════════════════════════════╣')
    print("║", "1：新建一个名片".ljust(23, " "), "║")
    print("║", "2：显示全部名片".ljust(23, " "), "║")
    print("║", "3：查询对应名片".ljust(23, " "), "║")
    # print("║", "4：修改一个名片".ljust(23, " "), "║")
    # print("║", "5：删除一个名片".ljust(23, " "), "║")
    print("║", "0：退出名片系统".ljust(23, " "), "║")
    print('╚'+"".ljust(31, "═")+'╝')
    pass

def ini():
    name = input("请输入名字:")
    QQ = input("请输入QQ号码:")
    phone = input("请输入手机号:")
    email = input("请输入邮箱:")
    curr = {'name': name, 'QQ': QQ, 'phone': phone, 'email': email}
    return curr


# 新建名片
def new_card():
    '''
    功能:新建名片
    :return:
    '''
    info.append(ini())
    pass


# 显示全部名片
def all_card():
    '''
    显示全部名片
    :return:
    '''
    print('╔═════════════════════════════╗')
    for con in info:
        for i, j in con.items():
            print("║", i.ljust(6, " "), ":", j.ljust(18, " "), "║")
        pass

    print('╚═════════════════════════════╝')


# 查找名片
def search_card():
    '''
    功能:查询名片
    :return:
    '''
    global info

    def sini(method):
        while True:
            curr = input("请输入要查询的%s:" % method)
            for i in info:
                if i[method] == curr:
                    print("您查询的信息如下:")
                    print(i)
                    return i
            else:
                print("您查询的信息不存在,请重新输入")

        pass

    # 修改名片
    def change(card):
        while True:
            print('''您可以修改以下内容:
                    1.姓名
                    2.QQ号码
                    3.电话号码
                    4.邮箱
                    0.修改完毕
                    ''')
            choice = input("请选择操作")
            if choice in ['1', '2', '3', '4']:
                value = input("请输入新的内容")
                if choice == '1':
                    card['name'] = value
                    pass
                elif choice == '2':
                    card['QQ'] = value
                    pass
                elif choice == '3':
                    card['phone'] = value
                    pass
                else:
                    card['email'] = value
                    pass
                pass
            elif choice == '0':
                return card
            else:
                print("输入不正确,请重新输入")
            pass

    # def 删除名片
    def dell():
        pass

    while True:
        print('''您可以通过以下方式查询:
        1.姓名
        2.QQ号码
        3.电话号码
        4.邮箱
        0.退出
        ''')
        way = input("请选择查询方式:")
        if way in ['1', '2', '3', '4']:
            if way == '1':
                curr_card = sini('name')
            elif way == '2':
                curr_card = sini('QQ')
            elif way == '3':
                curr_card = sini('phone')
            elif way == '4':
                curr_card = sini('email')
            pass
            while True:
                print("您还可以进行:")
                print('''
                1.修改该名片
                2.删除该名片
                0.退出当前操作
                ''')
                action = input("请选择操作:")
                if action in ['1', '2']:
                    if action == '1':
                        info.remove(curr_card)
                        info.append(change(curr_card))
                        print("修改成功!")
                    elif action == '2':
                        info.remove(curr_card)
                        print("删除成功!")
                        break
                    else:
                        pass
                    pass
                elif action == '0':
                    break
                    pass
                else:
                    print("输入有误,请重新输入")

        elif way == '0':
            break
        else:
            print("输入不正确,请重新输入")
    pass


'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
