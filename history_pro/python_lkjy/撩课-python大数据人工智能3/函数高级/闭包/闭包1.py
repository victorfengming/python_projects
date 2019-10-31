#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
闭包的优缺点：

优点：
    1.可以方便的进行函数式编程，组织程序代码
    2.使内部函数和局部变量在外部可以访问

缺点：
    1.闭包操作会导致整个函数的内部环境，被长久保存，占用大量内存。
闭包环境查看：__closure__

用于查询当前闭包操作所使用的环境中的变量和内部函数等信息。
'''

'''
闭包
使用特定或特殊的方式，将局部变量(内部函数)引入到全局环境中使用，这就是闭包操作。

闭包方法1：

def 函数名():
    局部变量...
    def 内部函数名():
        pass
    return (局部变量，内部函数...)
闭包方法2：

def 函数名():
    局部变量
    def 内部函数名():
        pass
    #获取所有需要进行闭包操作的函数和变量
    defall():
        return(局部变量,内部函数...)
    return all

'''

# def func():
#     print()
#     def inner():
#         print()
#         return 1
#     return inner

# 函数的嵌套
# def test(c):
#     # 外部变量
#     a = 4
#     def test2(b):
#         print(a)
#         print(b)
#         print(c)
#         print("xxx")
#         # 定义内部变量
#         b = 666
#     return test2
#
# test(7)(5)

# 根据不同的配置信息,生成不同的分隔线函数
# print("----------abc----------")
# 我现在想实现一个这样的一个功能,就是我这个分隔线啊,中间的内容是可变的,然后我这个线的长度也是可以变化的
# # 自己实现的
# def chang(lennn):
#     def contain(con):
#         for i in range(1,int(lennn/2)):
#             print("-",end="")
#         print(con,end="")
#         for i in range(1,int(lennn/2)):
#             print("-",end="")
#     return contain
#
# chang(14)("acs")
#
# def line_config(content,length):
#
#     print("-"*(length//2)+content+"-"*(length//2))
#
#
# line_config("闭包包包包",40)

# 那我要是想打印好几行咋整
'''
line_config("闭包包包包",40)
line_config("闭包包包包",40)
line_config("闭包包包包",40)
line_config("闭包包包包",40)
line_config("闭包包包包",40)

'''
# 就得这样写


def line_config(content,length):
    def line():

        print("-"*(length//2)+content+"-"*(length//2))
    return line

line1 = line_config("闭包包包包",40)
line1()
line1()
line1()
line2 = line_config("不闭包了",60)
line2()






