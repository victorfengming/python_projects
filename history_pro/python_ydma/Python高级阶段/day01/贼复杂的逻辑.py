#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        # f()
        fs.append(f)
    return fs
# [返回i的函数,返回i的函数,返回i的函数]
for q in count():
    print(q())
















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
