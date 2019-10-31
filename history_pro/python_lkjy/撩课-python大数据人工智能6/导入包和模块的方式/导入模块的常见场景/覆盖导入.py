#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<解决覆盖导入的问题>
'''
覆盖导入:
    场景1
        自定义模块和非内置的标准模块重名:
            -根据前者储存位置,有可能前者会覆盖后者
        结论:
            自定义模块命名不要与python的标准模块重名
    场景2:
        自定义模块和内置模块重名 内置模块
        pass



'''

import sys

res = sys.path

print(res)

# import macpath
# re = macpath.defpath
# print(re)

# 内置的模块优先级彩色最高的
# 但是现在我就想用我自己定义的和内置模块重名的模块
# 在python3.7版本中,即使我不创建__init__.py 文件,他也认为我这是一个python包
from 测试 import sys

print(sys.name)

# 虽然这样可以解决这个问题,但是还是不建议你这样去弄

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
