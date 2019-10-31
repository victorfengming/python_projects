#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 声明一个类
class Car:
    # 成员属性
    color = '黑色'
    weight = '1.3T'
    grand = 'BMW'
    circle = ['左前轮','右前轮','左后轮','右后轮','备胎']

    # 成员方法

    def __len__(self):
        # print('len方法被触发')
        # 返回轮子个数
        res = len(self.circle)
        return res

    def paly_music(self):
        print('是谁的心啊,孤单的留下,她还好吗,我多想他')

    def move(self):
        print('请注意,您已经超速')

    pass



# shilu实例化对象
mycar = Car()

# 可以使用len函数检测对象

print(len(mycar))

# len方法的存在,就可以使用len()函数来检测

'''
列表也是list类,我们定义的列表不就是list类的一个对象?
确确实实

'''








'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
