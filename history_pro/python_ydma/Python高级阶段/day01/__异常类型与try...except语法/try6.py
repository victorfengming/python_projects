#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 实际工作中往往这些异常要把他们写到日志里面,方便程序员的调试
a = 66
try:
    # a = 99
    print(a)

except NameError:
    print('变量异常')

except IndexError:
    print('索引错误')

except:
    print('程序异常')

else:
    print('程序执行成功,恭喜您!')














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
