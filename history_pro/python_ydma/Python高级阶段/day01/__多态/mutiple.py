#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 设定抽象类 定义动物规则

import abc

class Animal(metaclass = abc.ABCMeta):

    # 设定抽象方法 叫
    @abc.abstractmethod
    def say(self):
        pass

    # 设定抽象方法 跑
    @abc.abstractmethod
    def run(self):
        pass
    pass


# 声明小狗的类
class Dog(Animal):
    # 设定抽象方法 叫
    def say(self):
        print('小狗,旺旺旺```')

    # 设定抽象方法 跑
    def run(self):
        print('小狗四条腿跑``')

    # 狗的类实现了Animal的所有方法

# 声明小猫的类
class Cat(Animal):
    # 设定抽象方法 叫
    def say(self):
        print('小猫喵喵喵```')

    # 设定抽象方法 跑
    def run(self):
        print('小猫撒腿就跑')


    # 猫的类实现了Animal的所有方法
    #

class Chick(Animal):
    # 设定抽象方法 叫
    def say(self):
        print('小鸡咯咯咯```')

    # 设定抽象方法 跑
    def run(self):
        print('小鸡拔腿就跑')

    # 鸡的类实现了Animal的所有方法



# 实例化小狗,小猫和小鸡的对象
xiaohei = Dog()
xiaohua = Cat()
xiaofei = Chick()

# 声明行为类

class Action:
    # 初始化方法
    def __init__(self,animal):
        # 将接受的动物保存到当前对象中
        self.animal = animal

        pass
    # 叫的方法
    def jiao(self):
        # 调用动物叫的方法
        self.animal.say()
        # 连续访问,是可以的

        pass

    # 跑的方法
    def pao(self):
        self.animal.run()

        pass


# 实例化行为类的对象
action = Action(xiaohei)

# 调用行为对象的方法
action.jiao()
action.pao()

# 修改传入动物
action.animal = xiaofei


# 调用行为对象的方法
action.jiao()
action.pao()
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
