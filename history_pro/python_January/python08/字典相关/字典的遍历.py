#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''
for 变量 in 字典
    遍历字典中所有的键

for 变量 in 字典.keys()
    遍历字典中所有的键

for 变量 in 子弹.values()
    遍历字典中的值

for 变量1,变量2 in 字典.items()
    遍历字典中的键和值


'''


dictvar = {"黑旋风":"李逵","浪里白条":"䎠小二","大刀":"关胜","股上调":"时迁"}

for i in dictvar:
    print(i)

for i in dictvar.keys():
    print(i)

for i in dictvar.values():
    print(i)

for i,j in dictvar.items():
    print(i,j)


print("2343","876",sep=" ")
# print()sep 连接符














