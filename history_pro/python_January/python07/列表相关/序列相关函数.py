#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


# 序列相关函数

# len() 查看容器内部元素的长度

# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# # 计数变量
# i = 0
# while i < len(fruit):
#     print(fruit[i])
#     i += 1
#     pass
# leng = len(fruit)
# print(leng)

# # max() 查看 列表 中数值的最大的元素
# num = [5,6,4,8,3,9,23,56,34,78,23,76,43,14]
#
# print(max(num))
#
# # min() 查看列表中的最小值
# print(min(num))

# 列表相关的函数(方法)
# # append()  在列表的尾部添加一个数据
#
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# fruit.append("荔枝")
# fruit.append("胡萝卜")
# fruit.append("凤梨")
# print(fruit)

# insert() 在指定元素之前插入一个元素
'''
格式:
列表.insert(索引值,元素值)
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# print(fruit)
# fruit.insert(3)

# pop() 删除
'''
格式:
    列表.pop(索引) 删除列表中的指定元素,默认删除最后一个元素
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# print(fruit)
# fruit.pop(2)
# print(fruit)
# fruit.pop()
# print(fruit)

# remove() 通过指定的值删除列表中的元素
'''
格式:
    列表.remove(删除的内容)
如果有索引,推荐使用pop方法删除元素,因为pop的效率要高,remove还要找    
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
#
# fruit.remove("香蕉")
# print(fruit)


# copy() 复制
'''
格式:
    列表.copy
    返回值:新的列表
'''

# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# newfruit = fruit.copy()
# print(newfruit)

# count() 计算列表中指定的元素出现的次数
'''
格式:
    列表.count(指定值)
    返回值:元素出现的次数
'''
# num = [1,1,1,1,1,3,3,3,4,3,8,5,5,3,3,6,6,6,6,6,6,7]
#
# result = num.count(1)
# print(result)

# clear()   清除
'''
格式:
    列表.clear() 清空列表成为一个空列表
    无返回
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# print(fruit)
# fruit.clear()
# print(fruit)


# insert() 在指定的元素插入新元素
'''
格式:
    列表.insert(索引,值)
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
#
# fruit.insert(0,"香槟")
# print(fruit)


# extend() 将一个列表继承给一个新的列表
'''
格式:
    列表.extend(序列)   会将这个序列添加到列表的末尾
    无返回
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# fruit.extend(["三打两建","盛大开国际"])
# print(fruit)


# index() 通过指定元素,查看元素的索引值
'''
格式:
    列表.index(元素内容)
    返回索引值
'''
# fruit = ["西瓜","樱桃","水蜜桃","香蕉","香水梨","冻梨"]
# res = fruit.index("香蕉")
# print(res)

# reverse() 翻转
'''
格式:
    列表.reverse()
    无返回值
'''
# lists = [1,2,3,4,5,5,6,7,8]
# print(lists)
# lists.reverse()
# print(lists)

# sort() 将列表中的元素排序
'''
格式:
    列表.sort() 默认值                       从小到大排序
    列表.sort(reverse = True) 默认值         从大到小排序
    列表.sort(key = 自定义函数)              自定义从小到大
    列表.sort(key = 自定义函数,reverse=True) 自定义从小到大
'''
# lists = [2,45,764,242,786,35,648,345,876,345,765,12]
# print(lists)
# lists.sort()
# print(lists)
#
# lists.sort(reverse=True)
# print(lists)


lists = [2,45,764,242,786,35,648,345,876,345,765,12]
def func(num):
    return num%10
    pass

lists.sort(key =  func)
print(lists)

lists.sort(key =  func,reverse = True)
print(lists)



