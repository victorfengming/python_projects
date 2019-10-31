#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<菱形继承bug解决>
# 将菱形结构转变为单继承的结构
'''
A类(动物)

B类(人类)

C类(鸟类)

D类(鸟人类)

'''

# 动物类
class Animal:
    # 发生的方法
    def say(self):
        print('动物类开始发音')
        print('动物类发音结束')
    pass


# 人类
class Human(Animal):
    # 人类的发音方法
    def say(self):
        print('人类准备开始发音')
        # 调用父类中的发音功能
        super().say()
        print('人类准备发音结束')
    pass


# 鸟类
class Bird(Animal):
    # 发音方法
    def say(self):
        print('鸟类准备开始发音')
        # 调用父类的发音功能
        super().say()
        print('鸟类准备发音结束')
    pass


# 鸟人类
class BirdMan(Human,Bird):
    # 发音方法
    def say(self):
        # 自己要发音,毫无疑问
        print('鸟人类开始发音')
        # 调用人类的发音
        super().say()
        # 调用鸟类的发音
        super().say()
        print('鸟人类发音结束')
    pass




# 实例化鸟人对象

bm = BirdMan()

# 调用说话方法
bm.say()

'''
鸟人类开始发音
人类准备开始发音
动物类开始发音
动物类发音结束
人类准备发音结束
鸟类准备开始发音
动物类开始发音
动物类发音结束
鸟类准备发音结束
鸟人类发音结束
'''

# 动物类执行了两次
# 菱形继承中的BUG所在,某个方法在继承中被多次调用!
# (如果该方法具有唯一或者计时类方法,bug产生)


print(super)





'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

