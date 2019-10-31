#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


# 创建一个类
class Human:
    # 成员属性
    color = 'yellow'
    sex = '女'
    age = 18
    name = '史珍香'

    # 成员方法
    # __str__ 魔术方法 ,用于控制打印这个对象的内容的时候输出啥

    def __str__(self):  # 重载魔术方法__str__(继承自object类的)
        print('str方法被触发啦`````````')
        return '我不能告诉你我的内容````'
        pass

    def eat(self):
        print('真香``````')

    def smile(self):
        print('唔哈哈哈`````')



#实例化对象
szx = Human()

# 打印对象

print(szx)
# 触发__str__第二个时机
# 类型转换
str(szx)
'''
我打印列表(list类对象)? 给我真正列表内容
我打印字符串(str对象)? 给我sajdlkjg
'''














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
