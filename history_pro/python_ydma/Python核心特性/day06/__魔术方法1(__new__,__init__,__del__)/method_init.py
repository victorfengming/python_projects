#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# __init__ 初始化魔术方法

class Human:
    # 属性
    sex = 'man'
    age = 1
    name = '张三'
    eye = 2
    skin = 'yellow'

    # 方法

    # 魔术方法__init__
    def __init__(self,kid_name): #初始化操作
        print('init立体方法被执行')
        self.sex = 'yao'
        self.age = 1
        self.name = kid_name
        print(self)
    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法~~~~~~~~')


# 实例化一个人的对象

one = Human('小宁')
# 实例化对象的两部:1.制作一个对象 2.为对象初始化操作
print()

print(one.__dict__)












'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
