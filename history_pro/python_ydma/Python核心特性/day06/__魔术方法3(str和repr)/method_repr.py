#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


class Human:

    #成员属性
    color = 'pick'
    age = 19
    name = '鞠红安'

    # 成员方法
    # __repr__ 魔术方法
    def __repr__(self):
        print('repr被触发')
        return 'reprfanhui d 返回的数据'
    # 所有类默认都存在一个等式
    # __str__ = __repr__
    # 将repr的方法赋值给str方法完全一样
    # 重新定义str魔术方法
    def __str__(self):
        return 'str返回数据'
    def eat(self):
        print('烤肉真好吃')

    def drink(self):
        print('白酒真好喝``')


# 实例化对象
jh = Human()

# 默认是str打印
print(jh)

#使用repr打印
print(repr(jh))
'''
# repr的应用
mysong = "我\n稀罕\t你"
# 正常打印字符串(打印字符串对象)
print(mysong)
print(str(mysong))  #没卵用


# 使用repr函数转换 并打印

print(repr(mysong))
'''

mylist = [1,2,8,9,21,4,45,6,7]

print(str(mylist))
print(repr(mylist))




