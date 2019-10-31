#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# global 作用 把局部变量提升为全局变量

'''
全局变量: 全身麻醉

局部变量: 局部麻醉
'''
# 声明一个函数
#
# def func():
#     # 将局部变量提升为全局变量
#     global mazuiji
#     # 定义一个局部变量
#     mazuiji = "局部麻醉剂"
#     print("在嘴里拔牙是时候使用",mazuiji)
#     pass
#
# func()
#
# print("在手上使用",mazuiji)



mazuiji = 10

# 声明一个函数
def func():
    # 在函数中只能查看全局变量,但是是不能更改的
    # 所以这个全局变量,不是一个完全的全局变量
    global mazuiji
    mazuiji += 10
    print("在嘴里拔牙是时候使用",mazuiji)
    pass

func()

print("在手上使用",mazuiji)
















