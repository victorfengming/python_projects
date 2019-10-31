#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


try:
    result = 9 / 0  # 出现异常
    #           0       1      2       3
    girls = ['貂蝉', '西施', '杨玉环', '王昭君']
    print(girls[20])

except IndexError:  # 仅仅接收IndexError
    print('索引异常``')

except NameError:   # 仅仅接收NameError
    print('变量异常``')

# except 这块代码一定要写在最后的一个except那块儿
except: # 表示接受所有异常
    print('程序出席那了异常')















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
