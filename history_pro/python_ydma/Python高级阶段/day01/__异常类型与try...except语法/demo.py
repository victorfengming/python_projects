#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<用于测试异常>


#AssertError        断言语句(assert)失败
# assert 5>10

# AttributeError       尝试访问未知的对象属性
class Person:
    pass

# print(Person.sex)

# ImportError       导入模块失败的时候

# import mother
# IndexError
girls = ['小美','小丽','马冬梅']

# print(girls[3])

# KeyError      字典中查找一个不存在的关键字

hero = {'one':'刘备','two':'关羽','three':'张飞'}

# print(hero['twoo'])

# KeyboardInterrupt     用户输入中断键(ctrl+C)
for i in range(0,10000):
    print(i)


res = input('sdf')








'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
