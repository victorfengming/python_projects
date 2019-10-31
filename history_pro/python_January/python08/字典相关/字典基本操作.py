#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''
格式:
    访问字典中的元素:
        变量[键]
    添加字典中的元素:
        变量[新的键] = 值
    修改字典中的元素
        变量[已经有的键] = 值
    删除字典中的元素
        del 变量[已经有的键]

'''
#
# dictvar = {"辽宁":"沈阳","吉林":"长春","四川":"成都","云南":"昆明"}
#
# print(dictvar["辽宁"])
# # 只能用键来访问他的值,没办法用值,访问键
#
#
# dictvar["甘肃"] = "兰州"
# print(dictvar)
#
# # 看到的是末尾的,但是字典他就是无序的
#
# dictvar["四川"] = "重庆"
# print(dictvar)
#
# del dictvar["吉林"]
# print(dictvar)
#

# 序列操作
'''
成员检测:
    值 in 字典 
        检测一个值时候在字典的键中
    值 not in 字典
        检测一个值不在在字典的键中
'''
#
# dictvar = {"辽宁":"沈阳","吉林":"长春","四川":"成都","云南":"昆明"}
# res = "吉林" in dictvar
# print(res)

# 无法用值来查找,只能用键查找
'''
字典中的序列函数
len 获取字典的长度
max 获取字典中最大的键
min 获取字典中最小的键

'''

# dictvar = {1:"F",2:"T",3:"R",4:"P",5:"W"}
#
# res = len(dictvar)
# print(res)
# res = max(dictvar)
# print(res)
#
# res = min(dictvar)
# print(res)

# 要是字符串的话,那就用ASCII码表比较
a = "a"
z = "z"

# print(int(a))
# print(int(z))
#
print(chr(48))
print(ord("A"))
# chr() 输入ascii码 输出对应字符
# ord() 输入字符 输出对应的ASCII码