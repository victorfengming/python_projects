#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# # 定义两个功能函数
#
# def fss():
#     print("发说说")
#     pass
#
# def ftp():
#     print("发图片")
#     pass
#
#
# # 相关的逻辑代码
# # 将 功能函数和逻辑代码分开
# btnIndex = 1
# if btnIndex == 1:
#     fss()
# else:
#     ftp()

# 发说说,和发图片 必须得有一个前提,就是用户必须登录后才能进行操作
# 登录验证操作

# -------方式1-------------
# 定义两个功能函数
#
# def fss():
#     print("发说说")
#     pass
#
# def ftp():
#     print("发图片")
#     pass
#
# def check_login():
#     print("登录验证")
# # 相关的逻辑代码
# # 将 功能函数和逻辑代码分开
#
# btnIndex = 1
# if btnIndex == 1:
#     check_login()
#     fss()
# else:
#     check_login()
#     ftp()

# 这个业务逻辑代码其变化是非常多的,
# 所以造成了每一份逻辑代码在调用功能函数之前都要进行验证
# 代码的维护性差,代码过于冗余
#
# # -------方式2-------------
# # 定义两个功能函数,功能函数的代码重用性比较高
#
# def fss():
#     check_login()
#     print("发说说")
#     pass
#
# def ftp():
#     check_login()
#     print("发图片")
#     pass
#
# def check_login():
#     print("登录验证----------")
#     pass
#
# def ywlj():
#     btnIndex = 1
#     if btnIndex == 1:
#         fss()
#     else:
#         ftp()
#
# # 这样写,违背了开放封闭原则
# # 还违背了单一职责,不能在已经写好的代码中加其他功能

# # -------方式3-------------
# # 定义两个功能函数,功能函数的代码重用性比较高
#
# def fss():
#     print("发说说")
#     pass
#
# def ftp():
#     print("发图片")
#     pass
#
# def check_login1():
#     print("登录验证----------")
#     fss()
#     pass
# def check_login2():
#     print("登录验证----------")
#     ftp()
#     pass
#
# def ywlj():
#     btnIndex = 1
#     if btnIndex == 1:
#         fss()
#     else:
#         ftp()
# 还是冗余
#
# # -------方式4-------------
# # 定义两个功能函数,功能函数的代码重用性比较高
#
# def fss():
#     print("发说说")
#     pass
#
# def ftp():
#     print("发图片")
#     pass
#
# def check_login(func):
#     print("登录验证----------")
#     func()
#     pass
#
# def ywlj():
#     btnIndex = 1
#     if btnIndex == 1:
#         check_login(fss)
#     else:
#         check_login(ftp)
#
# # 还是麻烦
# # ywlj的调用发生了改变
# ywlj()

# # -------方式5-------------
# # 定义两个功能函数,功能函数的代码重用性比较高
#
# def check_login(func):
#     def inner():
#         print("登录验证----------")
#         func()
#         pass
#     return inner
#
# def fss():
#     print("发说说")
#     pass
#
# def ftp():
#     print("发图片")
#     pass
# fss = check_login(fss)
# ftp = check_login(ftp)
# def ywlj():
#     btnIndex = 1
#     if btnIndex == 1:
#         fss()
#         # check_login(fss)
#     else:
#         check_login(ftp)
#
# # 还是麻烦
# # ywlj的调用发生了改变
# ywlj()


# -------方式6-------------
# 定义两个功能函数,功能函数的代码重用性比较高

def check_login(func):
    def inner():
        print("登录验证----------")
        func()
        pass
    return inner

# python 的语法糖

@check_login
def fss():
    print("发说说")
    pass
@check_login
def ftp():
    print("发图片")
    pass

def ywlj():
    btnIndex = 0
    if btnIndex == 1:
        fss()
    else:
        ftp()

ywlj()
# 调用函数体没有改变,并且增加了额外的功能
#
















