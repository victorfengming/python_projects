#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
#
# 列表相关操作
# 列表:就是一组序列组合,列表中的数据可以修改
#
# 如何定义一个列表
# 空列表

# lists = []
# print(lists)
#
# # 列表函数声明一个空列表
# lists = list()
# print(lists,type(lists))

# 如何声明一个带有数据的列表:
'''
变量名 = [值,值,值,值]
变量名 = list(其他容器类数据)
'''

# 定义一个带有数据的列表
# lists = ["春天","夏天","秋天","冬天"]
# print(list,type(list))
#
#
# lists = list(("春天","夏天","秋天","冬天"))

# 列表相关操作
'''
+   列表的拼接操作
*   列表的数据复制操作

'''
# 声明列表
# listvar = ["刘备","张飞","赵云","关羽"]
# listvar2 = ["小乔","大乔","孙尚香"]
#
# result = listvar + listvar2
# print(result,type(result))
#
# lists = ["张飞","刘备","关羽"]
# result = lists * 3
# print(result)
#
# 列表的索引
# lists = ["苹果","橘子","香蕉","榴莲","西瓜","葵花籽"]
#
# # 查看列表中的内容
# print(lists[2])
#
# # 修改列表中的数据
# lists[-1] = "柚子"
# print(lists)

# # 删除列表中的值
# lists = ["苹果","橘子","香蕉","榴莲","西瓜","葵花籽"]
# # 删除葵花籽
#
# del lists[5]
# print(lists)

# 添加一个元素
lists = ["苹果","橘子","香蕉","榴莲","西瓜","葵花籽"]


# 如何删除列表本身
print(lists)
del lists
print(lists)
