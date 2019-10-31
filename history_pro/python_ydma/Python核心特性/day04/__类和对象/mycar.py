#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 声明一个类

class MyCar:
    # 成员属性
    grand = '宝马' # 品牌
    price = 1500    # 价格
    color = '蓝色'    # 颜色
    persons = '5'   # 座位数

    # 成员方法
    # 运动
    def move(self):
        print('汽车开始运动')


    # 制冷
    def make_cool(self):
        print("汽车空调制冷中")

    # 加热
    def make_hot(self):
        print("汽车空调加热中")

# 将汽车类实例化一个对象

car = MyCar()   # 调用类得到一个对象

print(car)
print(id(MyCar))
print(type(MyCar))

# 用户自己定义的一个类,就是一种数据类型
# 所以python有无数种数据类型
print(MyCar)
print(int)
print(float)
print(tuple)

# 查看对象信息
print(id(car))










'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
