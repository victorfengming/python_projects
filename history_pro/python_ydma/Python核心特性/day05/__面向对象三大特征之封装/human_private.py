#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<人类的私有化封装的操作>

# 声明一个人类

class Human:
    # 成员属性
    name = '张三' # 允许别人使用
    __sex = '男'   # 除非别人告诉你,不允许别人访问
    age = 18        # 可以访问
    heart = '健康心脏'  # 不允许别人访问
    __kidney = '强大的肾脏' # 不允许别人访问


    # 成员方法
    # 唱歌
    def sing(self):
        print('douruannifasonglaxidou')

    # 吃饭
    # 允许别人访问
    def eat(self):
        print('西红柿炖牛腩')


    # 跑步
    # 设定为不允许别人访问
    def __run(self):    # 私有化操作
        print('123321,锻炼身体')


    # 聊天方法
    # 用于测试类, 对象内部访问私有化成员
    def talk(self):
        print('唠嗑,我的名字都是',self.name)
        # 在类/对象的内部访问私有成员
        print('我的肾脏是非常好的',self.__kidney)
        # 在类或者对象的内部访问私有成员方法
        self.__run()
# shili实例化对象
zs = Human()
'''
print(zs)

# 访问对象的成员属性和方法

print(zs.sex)

# 访问肾脏
print(zs.kidney)

# 调用方法
# 嗲用唱歌方法
zs.sing()

# 嗲用跑步方法
zs.run()

# 只要是脱离了
# 领扣

'''
# 范文性别
# print(zs.sex) # 私有化封装后,类的外部无法访问
# print(zs.__sex)
zs.talk()







'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
