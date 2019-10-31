#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<99乘法表>

res = [str(j)+"x"+str(i)+"="+str(i*j) for i in range(1,10) for j in range(1,i+1)]

for i in range(0,45):
    print(res[i],end=" ")
    if res[i][0] == res[i][2]:
        print()















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
