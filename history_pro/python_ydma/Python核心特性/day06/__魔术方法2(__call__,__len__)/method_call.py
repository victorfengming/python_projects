#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

class Human:
    # 成员属性

    name = '张三'
    age = 18
    sex = 'man'

    # 成员方法
    '''
    我有一个小小的疑问,我们的类带括号
    '''
    # 魔术方法
    def __call__(self):
        print('call方法被触发')

    def eat(self):
        print('吃货的世界我们不懂~')

    def cry(self):
        print('5555555555555~~~~~~~`~~```')


# shilihua实例化对象
zs = Human()
print(zs)


# 对象能够使用括号调用么???
zs()
# 正常情况下,对象不能当做函数调用

class MakeCake:
    # huo和面
    def huomian(self):
        print('和面操作')
    # 发酵
    def fajiao(self):
        print('发酵操作~`')
    # 烘烤
    def hongkao(self):
        print('烘烤操作')
    # 切形状
    def qiexingzhuang(self):
        print('切形状操作')
    # 抹奶油
    def monaiyou(self):
        print('抹奶油操作')
    # 放水果
    def fangshuiguo(self):
        print('防水果')
    # 打包
    def dabao(self):
        print('打包')


    def __call__(self,kouwei):
        self.huomian()
        self.fajiao()
        self.hongkao()
        self.qiexingzhuang()
        self.monaiyou()
        self.fangshuiguo()
        self.dabao()
        print("我们要制作一个{}口味的蛋糕".format(kouwei))

        # 返回值
        return '蛋糕'
'''
    #得到蛋糕的方法(j结合)
    def get_cake(self):
        self.huomian()
        self.fajiao()
        self.hongkao()
        self.qiexingzhuang()
        self.monaiyou()
        self.fangshuiguo()
        self.dabao()
        
        # 那你看这个会比较麻烦
        # 为了将用起来方便
        pass
    pass


# 制作一个蛋糕

dg = MakeCake()
# 得到一个制作蛋糕的对象

# 自己使用对象制作蛋糕
dg.get_cake()



'''

dangao = MakeCake()
res = dangao('巧克力')
print(res)


'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
