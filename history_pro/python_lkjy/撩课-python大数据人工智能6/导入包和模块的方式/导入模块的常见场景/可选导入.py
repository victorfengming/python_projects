#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 本模块的功能:<可选导入>

# 可选导入:
#     概念:
#         两个功能相近的包,根据需求优先选择其中一共导入
#     场景:
#         有两个包A和B都可以实现相同的功能
#     实现:
#


# 我现在想要导入other可选3,还想在other可选3不存在的情况下导入other可选2

import other可选3
# 1
try:
    import other可选3 as o

except ModuleNotFoundError:
    import other可选2 as o


print(o.o1)








'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
