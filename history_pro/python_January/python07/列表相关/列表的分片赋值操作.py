#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


# 列表的分片赋值操作
#           0         1     2     3       4     5       6
listvar = ["黑龙江","辽宁","吉林","山东","北京","河南","福建"]
#           -7        -6    -5    -4      -3    -2      -1

# # 如何增加列表中的内容
# # listvar[3:3] = "天津" # 这个样子不行,字符串一个字符为一个元素了
# # 在选中的位置的前面添加元素
# listvar[3:3] = ["天津","甘肃","云南"]
# # listvar[3:5] = ["天津","甘肃","云南"]
# # 一样的
# print(listvar)

# # 删除列表中的内容
# # listvar[2:3] = []
# listvar[3:5] = []
# # 让他变成空的,就是删除了
# print(listvar)


# 修改列表中的内容
# #
# # listvar[4:5] = ["云南省"]
# # print(listvar)
# listvar[0:3] = ["东三省"]
# # listvar[0:3] = ["东北黑龙","东北吉林","东北辽宁"]
# print(listvar)


# 使用间隔符删除或更改列表(不可以使用间隔符)
listvar [3:5:2] = []
# 步长不能加到删除操作中
print(listvar)







