#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

#父类
class LiuBei:
    # 属性
    __wife = ('甘夫人','糜夫人','孙尚香')
    money = '100块'
    skin = '黄色' #公共的

    # 成员方法
    # 吃饭
    def eat(self):
        print('打死我***也不吃~ 真香啊~')

    #学习
    def __study(self):    # 私有化
        print('好好学习,天天向上!')

    #做鞋
    def makeshoes(self):
        print('编草鞋~~~')


    # 内部测试受保护成员
    def test(self):
        print('shoboauh')
    pass


# 子类
class LiuShan(LiuBei):
    pass


# 检测私有化和公共的封装

# 实例化对象
ls = LiuShan()

print(ls.skin)  #公共的成员可以在子类/子对象中调用

ls.eat()

lb = LiuBei()












'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
