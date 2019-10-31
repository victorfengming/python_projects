#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 列表的推导式
'''
简单的列表推导式
格式：[变量 for 变量 in 列表]
结果：遍历列表中的每个值，将每个值获取之后组成新的列表，可以对获取的值进行修改
[变量可以其他操作 for 变量 in 列表]

带有判断条件的列表推导式
格式：[变量 for 变量 in 列表  if 条件表达式]
结果：遍历列表中的每个值，根据判断条件决定是否取出指定的值组成新的列表，可以对获取的值进行修改

多个列表的同时循环的列表推导式
格式：[变量1+变量2  for 变量1 in 列表1  for 变量2  in 列表2]
结果：同时遍历列表1和列表2中的每个值，将列表1中的每个值和列表2中的每个值进行运算得到新的列表
     新的列表中元素个数=列表1中元素个数 * 列表2中的元素个数
变量1和变量2可以进行其他操作，不一定非要+ 这只是demo

'''


# 格式:
# [变量 for 变量 in 列表]
# [变量表达式 for 变量 in 列表]
# [变量 for 变量 in 列表 if 判断条件]
# [变量表达式 for 变量 in 列表 if 判断条件]
# [变量1变量2表达式 for 变量1 in 列表1 for 变量2 in 列表2 if 判断条件]
# 结果: 同时循环遍历出列表1和列表2的每个元素,将列表1的每个元素与列表2进行运算,得到一个新的值作为新列表中的元素,新列表中的元素个数等于 列表1元素个数 * 列表2元素个数

# xing = ["吕","赵","孙","丁"]
# ming = ["步","景云","婉儿","尚香"]
# sum = []

# for i in xing:
#     for j in ming:
#         sum[0:0] = [i+j]
# print(sum)
# for i in xing:
#     for j in ming:
#         sum.append(i+j)
# print(sum)

#
# sum = [i+j for i in xing for j in ming]
# print(sum)
#
# result = [i+j for i in xing for j in ming]
# result = result[::5]
# print(result)

# l = [12,3,14,26,47,53,24,9,45]
#
# res = [i*2 for i in l if i<30 ]
# print(res)


xing = ["吕","赵","孙","丁"]
ming = ["步","景云","婉儿","尚香"]
sum = [i+j for i in xing for j in ming if xing.index(i)==ming.index(j)]
print(sum)







