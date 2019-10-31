#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''

以键值对的形式存在的无序序列
创建字典:
    空字典:
        1变量 = {}
        2变量 = dict()
    带有值的字典:
        1变量 = {键:值}
        2变量 = dict(键 = 值,键 = 值)
        3变量 = dict({键:值,键:值})
        4变量 = dict([])二级容器内部,序列需满足有序
        5变量 = dict(zip(键,键,键,键,键)(值,值,值,值,值))
'''

dictvar = {}
print(dictvar,type(dictvar))

# 创建多个元素的字典
# 1
dictvar = {"xm":"小明","Xh":"小红","xs":"小帅","xyz":"小燕子"}

print(dictvar,type(dictvar))
# 2 以参数的形式传入,不可以数字作为键,必须符合变量规则
dictvar = dict(xm = "小明",xs = "小帅",xyz = "小燕子",xh = "小红")

print(dictvar)

# 3
dictvar = dict({"xm":"小明","Xh":"小红","xs":"小帅","xyz":"小燕子"})
print(dictvar)

# 4
dictvar = dict([["xm","小明"],["Xh","小红"],["xs","小帅"],["xyz","小燕子"]])
print(dictvar)
# 5
dictvar = dict(zip(("A","b"),("2","6")))
print(dictvar)