#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


class Human:
    # 添加成员属性
    def __init__(self):
        self.name = '东方不败'
        self.sex = 'man'
        self.age = 18

    # 添加成员方法
    # 魔术方法
    def __getattr__(self, item):
        print('getattr方法被触发')
        print('第二个参数',item)
        # 根据访问的内容的不同,可以进行一些判断
        if 'name' in item:
            return self.name
        # 这样就进行一些容错信息
        # return '西方不败'
    def eat(self):
        print('一天三顿小烧烤')

    def drink(self):
        print('喝啤酒`')




# 实例化对象
df = Human()
print(df)


# 访问对象成员
print(df.name2)


# getattr 这个魔术方法就是在 谁都没有






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
