#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


class Human:
    # 属性
    sex = 'man'
    age = 1
    name = '张三'
    eye = 2
    skin = 'yellow'

    # 方法

    # 魔术方法 # 重载object内部自带的__new__
    def __del__(self):
        pass
    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法~~~~~~~~')

    def __del__(self):
        print('del方法被触发')

# 实例化一个对象
one = Human()
print("---------------------")
# python作为高级语言,会在运行脚本结束后进行回收
two = one
del two
# 主动删除对象
del one
print('--------------------------')











'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
