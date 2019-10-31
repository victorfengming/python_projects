#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<__new__玩坏了>
# 仅供娱乐,没事儿别这么玩,真正开发当中没有这种需求,或者说很少有这种玩法


# 猴子类
class Monkey:
    pass


class Human:
    # 重载人类的构造方法 用猴子类来做人的对象
    def __new__(cls):
        # 使用猴子类代替人类创建对象
        # return object.__new__(cls)
        return object.__new__(Monkey)
    pass


# 实例化人类
ren = Human()
print(ren)













'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
