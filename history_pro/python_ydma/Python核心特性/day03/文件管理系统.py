#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<文件夹管理功能>

import os

def creat_file():
    name = input("请输入创建的文件名:")
    open(name,'w')
    print("恭喜你,创建文件成功")
    pass

def change_file():
    name = input("请输入要更改的文件路径:")
    with open(name,'r+',encoding='utf-8') as f:
        print("该文件内容如下:")
        print(f.read())
        after_con = input("请输入修改后的内容:")
        f.write(after_con)
        print("恭喜你,文件写入成功")
        print("新的文件内容为:")
        print(f.read())
    pass

def del_file():
    lj = input("请输入要删除的文件路径:")
    os.remove(lj)
    print("恭喜你,删除文件成功")
    pass

print(os.listdir())
while True:
    print('''
    1.创建文件
    2.修改文件
    3.删除文件
    4.退出程序
    ''')

    choice = input('请选择你要的操作:')
    if choice in ['1','2','3']:
        if choice == '1':
            creat_file()
        elif choice == '2':
            change_file()
        else:
            del_file()
        pass
    elif choice == '4':
        print("欢迎下次使用!!!")
        break
    else:
        print("输入有误,请重新输入.")

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
