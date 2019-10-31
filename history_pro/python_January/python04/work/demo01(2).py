#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# for in 循环
# 循环遍历容器类数据 字符串
#
# lists = ["出租车","滴滴快车","首期约车","优享快车","共享单车","助力车"]

# print(lists[0])
# print(lists[0])
#
# i = len(lists)
# while i >=0:
#     i -= 1
#     print(lists[i])
#
# 由于集合是没有索引的,就要引入for in 循环

# jihe = {"出租车","滴滴快车","首期约车","优享快车","共享单车","助力车"}
# for i in jihe:
#     print(i)
'''
for in 循环的基本格式:
    for 自定义变量 in 容器:
        循环代码
'''

# 字典的遍历
# dicts = {"A":"出租车","B":"滴滴快车","C":"首汽约车","D":"优享单车","E":"共享单车"}
# for i in dicts:
#     print(i)
# # 打印的是字典的键,默认打印字典中的所有键
# # 如何打印字典中的值呢,这里面我们用一个values方法
# for i in dicts.values():
#     print(i)

# 如何打印字典中的键呢,这里面我们用一个values方法
# for i in dicts.keys():
#     print(i)
#
# 打印键和值
# for i,j in dicts.items():
#     print(i,j)

# else区间
# 在循环结束后才能执行
#
# lists = ["出租车","滴滴快车","首期约车","优享快车","共享单车","助力车"]
#
# for i in lists:
#     print(i)
#
# else:
#     print("else内的for结束")
#
# # 元祖也行
# z = (1,4,6,7,8)
# for i in z:
#     print(i)

# print(help(print()))
#-----------------------------------------------------

# 二级容器
# var = [["A","baidu","sad"],["b","alibaba","ew"],["C","tengxun","jk"],["e","guge","uyi"]]
#
# for k,v,i in var:
#     print(k,v,i)
#
# #
# for i in var:
#     print(i)
# # 两次循环搞定 遍历出所有不等长的列表的内容
# for i in var:
#     for j in i:     #遍历内部列表
#         print(j)    #打印内部列表的内部变量
#     # print(i)

# 讲一下range函数
# range(开始值,结束值,步长)
# for i in range(1,10):
#     print(i,end = " ")
#
# for i in range(0,-10,-1):
#     print(i,end=" ")