#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
+   将两个元组拼接成1个
*   复制元组内的所有元素

索引
查看
分片
格式:
    变量[:]       获取整个元组的元素
    变量[开始索引:]从元组开始索引截取到末尾的元素
    变量[:结束索引]从开始截取到元素结束索引之前
    变量[开始索引:结束索引]从开始索引截取到元素结束索引之前
    成员 检测
    格式:
        值 in 元组 检测值是否存在于元组中,存在返回True
        值 not in 元组 检测值是否不存在于元组中,不存在返回True
'''
# tuple1 = (1,2,3,4)
# tuple2 = (5,6,7,8)
#
# res = tuple1 + tuple2
# print(res)
#
# tupvar = ("大猩猩","狒狒","够了")
#
# newtup = tupvar * 3
# print(newtup)
#
#
# # 使用tuple() 创建元组
# var = tuple({"大猩猩","狒狒","够了"})
# print(var,type(var))
#
# # 元组
# #           0      1      2
# names = ("吴泽","郭海艳","曹阳","孔维宇","丁帅","于凤明","王子","丁建楠","孙浩腾")
# print(names[:])
# print(names[5:])
# print(names[:5])
# print(names[1:3])
# print(names[:8:2])  #print(names[0:7:2])

# # 成员检测
# names_jsdgj = ("吴泽", "郭海艳", "曹阳", "孔维宇", "丁帅", "于凤明", "王子", "丁建楠", "孙浩腾")
#
# res = "丁帅" not in names_jsdgj
# print(res)
#
# res = "丁帅" in names_jsdgj
# print(res)
'''
# 序列函数
len()
max()
min()

'''
# # 元组相关函数
# tu = (2,)
# # index 获取指定值的索引
# tu.index()
# # count 获取指定值在元组中出现的次数

# names = ("吴泽", "郭海艳", "曹阳", "孔维宇", "丁帅", "郭海艳", "曹阳", "孔维宇", "丁帅", "郭海艳", "曹阳", "孔维宇", "丁帅", "于凤明", "王子", "丁建楠", "孙浩腾")
# res = names.index("郭海艳")
# print(res)
# print()
#
# res = names.count("丁帅")
# print(res)


#
# ## 循环遍历
# names = ("吴泽", "郭海艳", "曹阳", "孔维宇", "丁帅", "于凤明", "王子", "丁建楠", "孙浩腾")
#
# # for in ...
# # while ...
# # 遍历长度相同的多级元组
# # 遍历长度不同的多级元组
#
# # 一维
# for i in names:
#     print(i)
#
# j = 0
# while j < len(names):
#     print(names[j],end="")
#     j += 1
#
# 二维
names = (("skdf","孙尚香","小乔"),("大桥","十几"),("爱上的离开","杀了高科技"))

# # 这个只能是等长度的
# for i in names:
#     for j in i:
#         print(j)
# 这才是正招
for i,j,k in names:
    print("i:",i,type(i))
    print("j:",j,type(j))
    print("k:",k,type(k))

