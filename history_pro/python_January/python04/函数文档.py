#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
# 如何来写一个函数文档
def star(hang = 5,lie = 5):
    '''
    参数:hang 控制星星的行数
    参数:lie 控制星星的列数
    功能:打印一个n行n列星星,默认打印5行5列
    :return:打印星星函数
    '''
    var = 0
    while var < hang:
        num = 0
        while num < lie:

            print("☆",end="")
            num += 1
        print()
        var += 1

    return "打印星星函数"



# 查看方式1
# help(star)
# 查看方式2
# print(star.__doc__)
# print(star().__doc__)
#
re = star(3,4)
print(re)















