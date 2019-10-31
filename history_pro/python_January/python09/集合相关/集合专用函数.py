#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''
集合专用函数

'''


# 添加一个函数
setvar = {1, 2, 3, 34, 5, 66, 7}
# setvar.add(78)
# print(setvar)
# setvar.add(38)
# print(setvar)

# pop()随机删除一个元素
# 集合.pop() 随机删除集合中的元素
# res = setvar.pop()
# print(res)
# print(setvar)
# setvar.pop()
# print(setvar)


# remove() 删除集合中的某个元素
# 如果删除元素不存在报错


# discard()删除的元素不存在,返回

# clear().清空集合
# 格式:
	# 集合.clear()
# 	# 无返回值
# setvar = {1,9,3,4,7,5,6,6,7}
# res = setvar.clear()
# print(setvar)
# print(res)
#
# setvar
#
#
# set1 = {'吴泽','郭海艳','曹阳','于凤明','王子','孔维宇','丁帅','丁建楠','孙浩腾'}
# set2 = {'吴泽','郭海艳','曹阳','王建林','马化腾'}
#
#
# res = set1.intersection(set2)
# print(res)
#
# res = set1.difference(set2)
# print(res)
#
# set1.intersection_update(set2)
# print(set1)
#
# set1.difference_update(set2)
# print(set1)}
# # set2 = {1,2,3,4,5,67,8}
#
#
# res = set1.union(set2)
# print(res)
#
# set1.update(set2)
# print(set1)

# set1 = {7,1,2,3,4

# b = set1.issuperset(set2)
# print(b)
#
# b = set1.issubset(set2)
# print(b)
#
#
# # sett = frozenset()
# #
# # print(sett,type(sett))
# sett = frozenset([2,4,6,7,8,9])
#
# print(sett,type(sett))
# for i in sett:
#     print(i)



set1 = {'吴泽','郭海艳','曹阳','于凤明','王子','孔维宇','丁帅','丁建楠','孙浩腾'}
set2 = {'吴泽','郭海艳','曹阳','王建林','马化腾'}
#
res = set1.symmetric_difference(set2)
print(res)
print(set1)






















