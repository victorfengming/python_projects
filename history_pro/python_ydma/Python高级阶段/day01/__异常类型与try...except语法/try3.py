#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>



try:
    #           0    1      2       3
    girls = ['貂蝉', '西施', '杨玉环', '王昭君']

    print(girls[20])
except IndexError as err:
    # err 是一个对象,而不是一个字符串
    # 但是这个对象里面自带魔术方法__call__,所以打印的时候能够打印出对应的内容
    print('索引出现了错误')
    print(err)
    print(IndexError.__dict__)
    print(type(err))

print('程序继续执行')















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
