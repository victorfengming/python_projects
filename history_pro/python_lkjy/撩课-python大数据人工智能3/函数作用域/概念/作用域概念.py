#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''


# python是静态作用域
'''
L - Local 函数内的命名空间 作用范围:当前整个函数体范围
E - Enclosing function locals 外部嵌套函数的命名空间 作用范围:闭包函数
G - Global 全局命名空间 作用范围:当前模块(文件)
B - Builtin 内建模块命名空间 作用范围:所有模块(文件)

'''
b = 12
def test():
    b = 13
    a = 1
    print(a)
    print(b)
    def test2():
        print(a)
        c = 111




# print(a)
# 在外界访问不了

test()
# import os
#
# os.remove()
#
# xxx.remove()

print(b)











