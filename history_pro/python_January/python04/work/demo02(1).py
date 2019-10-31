#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 飞摩那切数列

dic = {"黑旋风":"李逵","小李广":"华荣","及时雨":"松江","智多星":"吴用"}

for name in dic:
    print(name)

for name in dic.keys():
    print(name)

for name in dic.values():
    print(name)

for name,name1 in dic.items():
    print(name,name1)

#--------------------------------------------------
# for in 循环
#     基本格式
#     for 自定义变量 in 容器:
#         循环内容
    # 遍历字典时,默认打印字典中的键
    # else 区间 ,在循环结束后执行 ,总之就是没啥用

    # 循环遍历容器类数据 字符串 列表 元祖 集合 字典

    lists = ["出租车","滴滴快车","首汽约车","优享单车","助理车"]
num = 0
while num <= 4:
    print(lists[num])
    num += 1

集合 = {"出租车","滴滴快车","首汽约车","优享单车","助理车"}

for car in 集合:
    print(car)


















