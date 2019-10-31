#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 列表的切片
'''
格式:
开始索引包含,结束索引不包含,python中都是这么整的
    变量[开始索引:结束索引]
    变量[开始索引:]
    变量[:结束索引]
    变量[开始索引:结束索引:间隔符]

'''
# 列表的分片

var = ["曹操","孙权","赵云","黄忠","关凤","孙尚香","祝融符"]

result = var[2:4]
print(result)

result = var[3:]
print(result)

result = var[:5]
print(result)

result = var[1::2]
print(result)

result = var[0:3:2]
print(result)

result = var[0:4:2]
print(result)

















