#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

class Human:
    # 成员方法

    # 吃方法 改造成对象方法
    def eat(self):
        print('这是一个对象方法')
        pass
    # 喝方法 _> 类方法
    @classmethod
    def drink(cls):
        print(cls)
        print('这是一个类方法')
        pass
    # 玩方法 -> 绑定类的方法
    def play(): # 不需要传入任何东西
        # 但是要是有其他参数,还得给
        print('绑定类的方法')
        pass

    # 乐方法 -> 静态方法
    # 静态方法就是跟类和对象没关系
    @staticmethod   # 申明担当起方法为静态方法
    def happy():
        pass




# 实例化对象
ren = Human()

ren.eat()
print()

ren.drink()

Human.play()

# 调用静态方法
Human.happy()

ren.happy()






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
