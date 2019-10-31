#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<主程序>

'''
用于实现循环的程序

'''


# 本模块的功能:<主要的功能>


from card_tools import *


while True:
    # 欢迎界面
    menu_display()
    choice = input("请选择操作功能:")
    print("您选择的操作是:%s" % choice)
    # 根据用户的选择,做相对应的判断操作.
    if choice in ['1','2','3']:
        if choice == "1":
            new_card()
        elif choice == "2":
            all_card()
        elif choice == "3":
            search_card()
        pass
    elif choice == "0":
        print('[欢迎再次使用名片管理系统]')
        break
    else:
        print("[输入错误,请重新输入!]")
        pass
    pass














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
