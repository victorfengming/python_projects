#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<单继承案例>

'''

爷爷类
爸爸类
儿子类

'''

class GrandFather:
    # 成员属性

    skin = '黄色'

    # 成员方法
    def say(self):
        print('爷爷说话中')


#爸爸类
class Father(GrandFather):
    # chengyaunshuxing成员属性
    eye = '水汪汪的大眼睛'

    # 成员方法
    def walk(self):
        print('走走``~~停停中')


# 儿子类
class Son(Father):
    pass


# 实例化儿子对象

erzi = Son()

print(erzi)


# 嗲用方法或者属性

print(erzi.skin)
print(erzi.eye)
















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
