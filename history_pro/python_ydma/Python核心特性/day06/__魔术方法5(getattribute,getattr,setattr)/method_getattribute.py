#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

class Human:
    # 添加成员属性
    def __init__(self):
        self.name = '东方不败'
        self.sex = 'man'
        self.age = 18

    # 添加成员方法
    # 添加魔术方法 __getattrbute__
    def __getattribute__(self, item):#item接受的是访问成员的名称字符串
        print(item)
        # print('getattrbute被触发')
        # return self.name # 这样会递归调用
        # 一定不能使用当前对象的成员访问,会再次触发当前魔术方法
        # 在获取数据时不用自己获取,而用最基本的获取方法
        res = object.__getattribute__(self,item)
        new_name = res[0]+'*'+res[-1]
        # 返回数据
        return new_name
    def eat(self):
        print('一天三顿小烧烤')

    def drink(self):
        print('喝啤酒`')


#实例化对象
ls = Human()
print(ls)


# 访问对象的名称
print(ls.name)
# 无论对象的属性是否存在

'''
医院叫号显示:
    张三 -> 张*三
    李大嘴 -> 李*嘴
    王二麻子 -> 王*子
'''














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
