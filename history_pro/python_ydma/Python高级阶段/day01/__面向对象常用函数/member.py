#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<内置成员>

# 声明一个类
class Animal:
    pass
class Action:
    pass
class Human(Animal,Action):
    '''
    这是类的问道
    成员   信息
    成员   信息
    成员   信息
    成员   信息
    '''
    # 成员属性
    sex = 1
    age = 18
    color = 'yellow'

    # 成员方法

    def smile(self):
        print('hhhhhh')

    def cry(self):
        print('555555``')


# 实例化对象
ren = Human()

# # __dict__
# print(Human.__dict__)
# print(ren.__dict__)
#
# # __doc__
# print(Human.__doc__)
# print(ren.__doc__)

# __name__

print(Human.__name__)

# __module__

print(Human.__module__)

# __bases__

print(Human.__bases__)













'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
