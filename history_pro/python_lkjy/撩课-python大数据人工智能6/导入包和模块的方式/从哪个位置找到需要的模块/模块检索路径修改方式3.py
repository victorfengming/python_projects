#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<创建.pth文件>


# 添加.pth文件,(配置文件)


import site

res = site.getsitepackages()
print(res)  # ['D:\\Python37', 'D:\\Python37\\lib\\site-packages']

# 这两个路径都可以存放.pth文件
# 环境变量干掉
import demo
# '''
# D:\\Python37中的37.pth 中的内容
#
# c:\
# C:\Users\Administrator\Desktop\my_directory1
#
#
# '''

import site

res = site.getsitepackages()
print(res)  # ['D:\\Python37', 'D:\\Python37\\lib\\site-packages']





'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
