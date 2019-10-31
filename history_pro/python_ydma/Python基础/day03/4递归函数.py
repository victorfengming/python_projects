#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 递归函数

# 在函数本事自己掉用自己本身就是递归
# def digui(num):
#     print(num)
#     if num > 0:
#         digui(num-1)
#
#     # 第二次打印 num
#     print(num)
#
# # 调用递归函数
# digui(5)

# 局部变量:每次变量的值,只对当前调用有效

# 用递归函数求斐波那契额数列
# def fbnq(i):
#     if i == 0:
#         return 0
#     elif i ==1:
#         return 1
#     else:
#         return fbnq(i-1)+fbnq(i-2)
#
# print(fbnq(20))

# 用递归函数求阶乘

# def jc(i):
#     if i == 1:
#         return 1
#     elif i == 2:
#         return 2
#     else:
#         return jc(i-1) * i
#
# print(jc(5))

# 递归升级版
def digui(num):
    print(num)
    if num > 0:
        digui(num-1)
    if num == 0:
        print("--------------------")
    print(num)

# 调用递归函数
digui(3)









