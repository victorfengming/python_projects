#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<用于测试继承相关>

# 父类

class Father:
    # 成员属性

    family_name = '王'  # 姓氏
    first_name = '强'  # 名字
    sex = 'man'  # 性别
    age = 27  # 年龄
    color = '黄色'  # 肤色
    # 对媳妇进行私有化操作
    __wife = ('甘夫人', '糜夫人', '孙尚香')

    # 成员方法

    # 吃饭
    def eat(self):
        print('甜甜圈,咖啡,面包,方便面~')

    # 跑
    def run(self):
        print('霸气退就跑')

    # 做鞋
    def makeshoes(self):
        print('做草鞋')


# dayikn打印Father类的成员
# print(Father.__dict__)


# 声明一个类
class Son(Father):
    # 父类私有化之后,子类肚子添加的成员
    first_name = '禅'
    # 添加子类独有的成员
    height = '179cm'

    # 做鞋功能父类已经具有
    # 重新定义 # 这个操作称为方法重载
    def makeshoes(self):
        print('做皮鞋,不是人造革,是真的皮')

    # 跑路的重载(重载父类的操作 -> 再覆盖的同时加点儿功能)
    def run(self):
        # 这个不太一样了
        print('穿上鞋子')
        # print('霸气退就跑~') # 这行代码重复
        # 嗲用父类的跑路方法(方法1)
        super().run()   # 咱叔暂时可以认为super表示寻找父类



        # 用
        # 添加一个操作
        print('好汉饶命')
    pass


# # 打印子类的成员
# print(Son.__dict__)

ls = Son()

# 子对象里面没有找类要,类也没有找父类要

# print(ls.family_name)
# print(ls.sex)
# print(ls.age)
# ls.run()

# 继承关系带来的好处
#
# 私有成员仅仅运行原有类和原有类的对象访问,子类也不可以继承或者访问
# print(ls.wife)

# 访问子类独有的成员
# print(ls.height)
#
#
# # 访问做鞋功能
#
# ls.makeshoes()

ls.run()
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
