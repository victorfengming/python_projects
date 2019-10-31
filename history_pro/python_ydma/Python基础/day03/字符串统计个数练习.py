#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

char = input('请输入一串字符:')
zimu = 0
shuzi = 0
kong = 0
other = 0
for i in char:
    if i.isspace():
        kong += 1
    elif i.isalpha():
        zimu += 1
    elif i.isdigit():
        shuzi += 1
    else:
        other += 1
print("字母个数:",zimu)
print("数字个数:",shuzi)
print("空格个数:",kong)
print("其他字符个数:",other)















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
