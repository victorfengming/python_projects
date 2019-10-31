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
    # 可以在当用户修改成员的时候进行一些限制
    def __setattr__(self, key, value):  # 相当于重载object中的__setattr__方法
        print('setattr被触发')
        # 禁止修改性别
        if key == 'sex':
            # self.sex = '男'
            # 添加也是修改的一环,这里会出现递归调用bug
            pass
        else:
            # 解决办法
            object.__setattr__(self,key,value)
        # 修改名称的时候,最多使用三个字符,多余舍去
        # object.__setattr__(self,key,value)
        pass
    def eat(self):
        print('一天三顿小烧烤')

    def drink(self):
        print('喝啤酒`')



df = Human()

# print(df.name)
# 修改对象成员
df.name = '西门吹雪'

# print(df.name)
print(df.__dict__)

# 访问性别
print(df.age)

# 修改性别
# df.sex = 'nv'

# print(df.sex)











'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
