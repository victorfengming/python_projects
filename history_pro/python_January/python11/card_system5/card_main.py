#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<主程序>

'''
用于实现循环的程序

'''
# 本模块的功能:<主要的功能>
# from card_tools import *
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
    print("║", "card manage system v3.8.1c".center(29, " "),"║")
    print('╠═══════════════════════════════╣ ')
    print("║", "1: new a card".ljust(29, " "),"║")
    print("║", "2: display all cards".ljust(29, " "),"║")
    print("║", "3: search a card".ljust(29, " "),"║")
    print("║", "4: change a card".ljust(29, " "),"║")
    print("║", "5: delete a card".ljust(29, " "),"║")
    print("║", "0: exit the system".ljust(29, " "),"║")
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
        print("║","Record is empty".center(30)+"║")
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




while True:
    # 欢迎界面
    menu_display()
    choice = input("请选择操作功能:")
    print("您选择的操作是:%s" % choice)
    # 根据用户的选择,做相对应的判断操作.
    if choice in ['1','2','3','4','5']:
        if choice == "1":
            new_card()
        elif choice == "2":
            all_card()
        elif choice == "3":
            search_card(0)
        elif choice == "4":
            search_card(1)
        elif choice == "5":
            search_card(2)
        pass
    elif choice == "0":
        print('[欢迎再次使用名片管理系统]')
        break
    else:
        print("[输入错误,请重新输入!]")
        pass
    pass

