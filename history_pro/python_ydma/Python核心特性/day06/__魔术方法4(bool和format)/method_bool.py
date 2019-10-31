#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 声明一个类
class Man:
    # 属性
    color = '黄色'
    age = 18
    sex = '男'
    married = '已婚'


    # 犯法

    #添加一个魔术方法
    #yongyu用于检测一个人是否单身
    def __bool__(self):
        print('bool方法被触发')
        # 这里来做判断,根据某些数据返回不同的布尔值,
        # 实现布尔转换对象的作用
        if self.married == '已婚':
            return True
        else:
            return False
    def smoking(self):
        print('多数男人会抽烟')

    def say(self):
        print('男人就会甜言蜜语``')


# 实例化对象
mr = Man()

print(mr)

# 转换对象 用于检测男人对象是否已婚
res = bool(mr)  # 一般情况下 对象转换的结果默认的结果就是True
print(res)














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
