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
    print("║", "欢迎使用名片管理系统v3.8.1c".center(21, " "),"║")
    print('╠═══════════════════════════════║')
    print("║", "1：新建一个名片".ljust(23, " "),"║")
    print("║", "2：显示全部名片".ljust(23, " "),"║")
    print("║", "3：查询对应名片".ljust(23, " "),"║")
    print("║", "4：修改一个名片".ljust(23, " "),"║")
    print("║", "5：删除一个名片".ljust(23, " "),"║")
    print("║", "0：退出名片系统".ljust(23, " "),"║")
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
    if info == []:
        print('╔═══════════════════════════════╗')
        print("║","无任何名片记录".center(23))
        print('╚═══════════════════════════════╝')
        return
    print('╔═══════════════════╦═══════════════════╦═══════════════════╦═══════════════════╗')
    print("║", "name".ljust(18, " ")+"║","QQ".ljust(18, " ")+"║","phone".ljust(18, " ")+"║","email".ljust(18, " ")+"║")
    print('╠═══════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣')
    for con in info:
        for j in con.values():
            print("║", j.ljust(18, " "), end="")
        print("║")
        pass
        # print()
    # print()
    print('╚═══════════════════╩═══════════════════╩═══════════════════╩═══════════════════╝')


# 查找名片
def search_card(fun):
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
                    print('╔═══════════════════════════════╗')
                    # print('╠═══════════════════════════════╣')
                    for a,b in i.items():
                        print("║", a.ljust(6, " "), ":", b.ljust(20, " "), "║")
                    pass
                    print('╚═══════════════════════════════╝')
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
            choice = input("请选择需要的操作:")
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

    while True:
        if fun == 0:
            print('您可以通过以下方式查询:')
        elif fun == 1:
            print('您可以通过以下方式选择修改对象:')
        else:
            print('您可以通过以下方式选择删除对象:')
        print('''1.姓名\n2.QQ号码\n3.电话号码\n4.邮箱\n0.退出查询''')

        way = input("请选择需要的操作:")
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
            action = str(fun)
            # if action in ['1', '2']:
            if action == '1':
                info.remove(curr_card)
                info.append(change(curr_card))
                print("修改成功!")
                break
            elif action == '2':
                info.remove(curr_card)
                print("删除成功!")
                break



        elif way == '0':
            break
        else:
            print("输入不正确,请重新输入")
    pass


'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
