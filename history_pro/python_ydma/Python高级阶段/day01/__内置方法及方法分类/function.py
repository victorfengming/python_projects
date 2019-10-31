#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<用于测试面向对象相关函数>
#
# # issubclass
#
# class Father:
#     pass
#
# class Son(Father):
#     pass
#
# res = issubclass(Son,Father)
# print(res)
# print(issubclass(Son,object))
# # 不仅仅父子关系型,太太太爷爷也行
#
# #-----------------------------
# class Monkey:
#     pass
#
# class Human:
#     pass
#
# ren = Human()
#
# result = isinstance(ren,Human)
#
# print(result)
#
# result = isinstance(ren,(Human,Monkey))
#
# print(result)
# #----------------------------------------------
#
# class Human:
#     age = 1
#     sex = 'man'
#
#     def cry(self):
#         print('555555555555``')
#
#
# # 对类进行成员检测
# result = hasattr(Human,'smile')
# print(result)
#
# # 实例化对象
# ren = Human()
# result = hasattr(ren,'age')
#
# print(result)
# # #----------------------------------------------
#
# class Monkey:
#     # 属性
#     age = 9
#     sex = '熊'
#     color = 'golden'
#
#     #方法
#     def say(self):
#         print('叽叽叽叽````')
#
#
# # 实例化对象
# houzi = Monkey()
#
# # 获取猴子颜色
#
# print(houzi.color)
#
# result = getattr(houzi,'color')
# print(result)
# # 这样写有什么好处呢,
# # 可以获取不存在的成员,如果前者方法若成员不存在则要报错
# result = getattr(houzi,'name','小猴子')
# print(result)
#
# # 如果没有就输出默认值
#----------------------------------------------

# # setattr()
#
# class Monkey:
#     # 属性
#     age = 9
#     sex = '熊'
#     color = 'golden'
#
#     #方法
#     def say(self):
#         print('叽叽叽叽````')
#
# # 实例化对象
# houzi = Monkey()
# print(houzi.__dict__)
#
# # 设置对象成员
#
# # 语法方式
# houzi.name = '小悟空'
# houzi.color = '黑色'
#
# # 函数方式
# setattr(houzi,'weight','89斤')
# # 跟语法方式没什么区别
# # 函数方式更加的灵活,因为其中的参数名是一个字符串变量,可以动态调整
# print(houzi.__dict__)
# ##----------------------------------------------

# delattr()

class Monkey:
    # 属性
    age = 9
    sex = '熊'
    color = 'golden'


    #方法
    def __init__(self):
        self.name = 'xwk'
        self.height = 100
    def say(self):
        print('叽叽叽叽````')

# 实例化对象
houzi = Monkey()
print(houzi.__dict__)
# 语法方式
del houzi.name
# 函数方式
delattr(houzi,'height')
print(houzi.__dict__)









'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
