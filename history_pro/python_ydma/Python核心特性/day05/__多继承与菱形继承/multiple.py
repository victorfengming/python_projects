#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<多继承>
'''
音乐老师类
体育老师类
爸爸类
妈妈类
'''

class MusicTeacher:
    # 成员属性
    cloth = '晚礼服'
    # 成员方法
    def sing(self):
        print('门前大桥下,路过一群鸭,快来数一数,24678')


#体育老师类
class SportTeacher:
    # 成员方法
    def run(self):
        print('跑步功能')

    def jump(self):
        print('you jump I jump')


# 爸爸类
class Father:
    # 方法
    def smoking(self):
        print('抽烟中~~~')

class Mother:
    # 方法

    def clear(self):
        print('打扫房间')


# 我的类 # 多继承
class Me(Mother,Father,SportTeacher,MusicTeacher):
    # 继承的父类没有顺序关系


    pass

# 实例化成员
i = Me()

# 调用成员

print(i.cloth)
i.sing()
i.jump()
i.run()
i.smoking()
i.clear()










