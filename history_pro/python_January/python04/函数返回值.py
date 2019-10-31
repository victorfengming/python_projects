#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 带有返回值的函数
'''
python中:
    过程式函数:
        不具有返回值,无法对函数内部产生的结果进行更改
    带有返回值的函数:
        可以将函数内部产生的结果,拿到外部使用或更改

    点外卖:
        过程式函数:外卖小哥,把我们的外卖送到了,什么都没拿,走了
        带有返回值的函数:外卖小哥,把我们的外卖送到了,拿着钱走了
            (钱相当于返回值)
    return 语句:
        当函数执行了return语句,函数将结束执行,return语句后面的代码将不会执行
        # 如果return返回多个值,将会以元祖的形式返回给我们

'''
# def sum(a = 5,b = 7):
#     result = a + b
#     # print(result)
#     # 返回值
#     return result
#     # print("适当")
#
# newsum = sum()*10
# print(newsum)
#
# 定义
# def func():
#     print("########")
#     if 3>5:
#         return 1
#     # print("********")
#     else:
#         return 2

# def fun():
#     def fun1():
#         print("***********")
#
#     return
#
# return

def sum():
    result = 1
    return result,1,3


print(sum())










