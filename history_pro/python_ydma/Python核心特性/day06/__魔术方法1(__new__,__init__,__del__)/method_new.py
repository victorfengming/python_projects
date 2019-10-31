#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# __new__ 构造方法


class Human:
    # 属性
    sex = 'man'
    age = 1
    name = '张三'
    eye = 2
    skin = 'yellow'

    # 方法

    # 魔术方法 # 重载object内部自带的__new__
    def __new__(cls, sex):
        # cls是class的缩写
        print('cls是',cls)
        # 用于管理控制对象的生成过程
        # print('new魔术方法被触发~`')
        # 自己控制对象的生成过程(女的生,男的不生)
        # print(sex)
        # 结果能够控制生成还是不生成,但是要是想控制生成的过程,那不行
        if sex == '女':
            # 生成对象并且返回
            # return object.__new__(Human)
            return object.__new__(cls)
            pass
        else:
            # 不生成对象
            pass
        # return 2
        pass
    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法~~~~~~~~')


# 实例化一个人的对象

one = Human('男')
# 实例化对象的两部:1.制作一个对象 2.为对象初始化操作
print()

# print(one)
# Human.__new__()
print(one)

















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
