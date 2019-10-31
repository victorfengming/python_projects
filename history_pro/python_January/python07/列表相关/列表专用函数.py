#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''

列表专用函数
append()

功能：向列表的末尾添加新的元素
格式：列表.append(值)
返回值：None
注意：新添加的值在列表的末尾，该函数直接操作原有列表
clear()

功能：清空列表中所有元素
格式：列表.clear()
返回值:None
copy()

功能：复制列表
格式：列表.copy()
返回值：新的列表
count()

功能：计算某个元素出现的次数
格式：列表.count(值)
返回值：整数
extend()

功能：将一个列列表继承另一个列表
格式：列表.extend(序列)
返回值：None
注意：直接改变原有列表
index()

功能：获取某个值在列表中的索引
格式：列表.index(值)
返回值：整数
注意：值不存在与列表时抛出异常错误！
insert()

功能：在指定位置之前插入元素
格式：列表.insert(索引,值)
返回值:None
注意：直接改变原有列表
pop()

功能：在列表中移除一个元素
格式：列表.pop([索引])
返回值：无
注意：没有指定索引，默认移除最后一个元素
remove()

功能：移除指定的值
格式：列表.remove(值)
返回值：无
注意：如果有索引的清空下推荐使用POP移除，效率比remove高
reverse()

功能：列表反转操作
格式：列表.reverse()
返回值：None
sort()

功能：列表排序

格式：列表.sort()                      按照从小到大排序（数字）
格式：列表.sort(reverse=True)          按照从大到小排序（数字）
格式：列表.sort(key=函数)               对值进行指定的函数处理之后在从小到大排序
格式：列表.sort(key=函数，reverse=True)  对值进行指定的函数处理之后在从大到小排序

返回值：None
注意：直接改变原有列表


'''

# sort永久排序
lis = [63,45,31,26,17,2,8,78,56,7,13,3,9,12]

# print(lis)
# lis.sort()
# print(lis)
# lis.sort(reverse=True)
# print(lis)
# lis.reverse()
# print(lis)
# lis.reverse()
# print(lis)
# lis.remove(8)
# print(lis)
# lis.pop()
# print(lis)
# lis.pop(3)
# print(lis)

lista = [6,3,5,76,3,7,3,52,14,67,23,89,17]
listb = []
listc = []
listb.extend(lista)
listc = listb.copy()
print(lista)
print(listb)
print(listc)
listc.append(99)
print(listc)










