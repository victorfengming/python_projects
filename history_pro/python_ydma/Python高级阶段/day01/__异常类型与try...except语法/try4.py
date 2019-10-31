#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


# 注意:如果try中出现了异常
try:
    #           0    1      2       3
    # girls = ['貂蝉', '西施', '杨玉环', '王昭君']
    # print(girls[20])    # 制造索引错误
    # 我们的错误一旦抛出 就不会往下执行 不会执行下面的代码了
    print(a)        # 制造NameError
except IndexError as err:
    print('索引出现了问题',err)
    # print(girls[-1]) # 索引超出范围,自动设置最大索引
except NameError as err:
    print('变量不存在',err)
    pass













'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
