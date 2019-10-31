#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
普通集合推导式
变量 = {变量 for 变量 in 集合}

'''
#
# setvar = {1,2,3,4,5}
#
# res = {i for i in setvar}
# print(res,type(res))

setvar1 = {1,2,3,4,5}
setvar2 = {6,2,3,4,5}

res = {i*j for i in setvar1 for j in setvar2 if i == j}
print(res,type(res))


