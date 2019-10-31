#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''



# 定义一个方法
def outer():
    # 定义一个变量
    var = 11

    # 定义一个内部函数
    def inner():
        # nonlocal 声明var 变量 var是inner函数的外部变量
        nonlocal var # nonlocal 关键字声明 ,既不是全局变量,也不是局部变量
        # 在内部函数中使用外部函数声明的变量
        var = var + 56
        print(var)
    inner()

outer()

'''

'''
# 在python2中利用列表的穿透性 搞定的'
# 这个作为了解,不是重点
# 定义一个方法
def outer():
    # 定义一个变量
    var = [11]

    # 定义一个内部函数
    def inner():
        # 利用列表的穿透性
        var[0] = var[0] + 56
        print(var[0])
    inner()

outer()
'''

# def outer():
#     var = 46
#     def inner():
#         nonlocal var
#         var = var + 8
#         print(var)
#     inner()
#
# outer()
#
#












