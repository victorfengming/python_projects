#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

class CongHao:
    # 成员属性
    name = '丛浩'
    sex = '男'
    age = 25
    color = 'yellow'
    height = '180cm'
    weight = '160斤'
    house = '130m2'

    # 成员方法

    def talk(self):
        print("我的名字是丛浩",self.name)    # 此处需要使用对象的属性来输出名字,性别等

    def sing(self):
        print("你存在我深深的脑海里")

    def wash(self):
        self.sing()
        # 洗澡的时候唱歌(调用自己的唱歌功能)
        print('洗刷刷洗刷刷')

    # 吃饭
    def eat(zhen):  # 非绑定类的方法
        print('我的体重是',zhen.weight)
        print('我最喜欢吃烤羊腿')

    # 没有self参数的方法
    def smoking():
        print('饭后一支烟,赛过活神仙')

    # 哭
    # self设计为接收次数的参数
    def cry(self):  # 绑定类的方法
        print('我哭了'+self+'次')
#
# # 实例化一个对象
# ch = CongHao()
# ch.talk()
# print(ch)
#
# # 使用对象
#
# # print(CongHao)
#
# # 再次实例化一个对象
# hnr = CongHao()
#
# hnr.talk()
#

'''
# 实例化对象
ch = CongHao()
# 调用洗澡方法
ch.wash()
'''
'''
# 测试使用其他的参数名字能不能好使
ch = CongHao()
# ch = CongHao()
ch.eat()


'''

ch = CongHao()
# ch.smoking()    # 报错,smoking没有形参,但是却给了一个实参
# 无法通过对象调用没有接收对象的方法
# 但是类可以访问灭有接收对象参数的方法
CongHao.smoking()
# 这种方法很少用

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
