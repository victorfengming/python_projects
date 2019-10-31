#!/usr/bin/env python.
# -*- coding:utf-8 -*-
# coding by xiaoming

# 本模块的功能:<解决循环导入问题>

t1 = "1324klsdj"
t2 = "132sdj"

import other2
print(other2.o1)
print(other2.o2)

# 第一:
#     打印重复了一遍
#         1324klsdj
#         132sdj
#         ooo1
#         ooo2
#         1324klsdj
#         132sdj

# 如何避免
# 直接将两个模块 变成其他的模块 即可解决这个问题










'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
