#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

'''
相对路径(用的更多)
    文件路径以某个文件作为参考的位置,相对路径
    ./  当前目录中的文件夹       ./ABC
    ../ 当前目录上一层          ../day1/__init__.py
    
绝对路径(不经常用)
    文件路径以某个精确位置作为参考的路径是绝对路径,例如:
    Windows 里面就是从盘符开始,到所找的路径
        e:\\sjkg\\ss\\stri
    Linux   里面就是
        /stc/host
'''


# chdir() 修改当前目录

import os

# res = os.chdir("E:\\PycharmProjects\\python_January\\python10")
res = os.getcwd()

rs = os.listdir("../../python_lkjy")
print(res)
print(rs)

















