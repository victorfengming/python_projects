#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 制作一个类
class Girl:
    # 成员属性

    name = '小宁'
    sex = '女'
    age = 18

    # 成员方法

    # 添加魔术方法
    def __format__(self, format_spec):  # format_spec 是限定符号的字符串
        # print('format方法被触发')
        # print('参数的内容是',format_spec)
        # return self.name


        # 实现format自带的对齐和填充功能
        # 1.接收限定符号
        flag = format_spec
        # 2.拆分限定符号
        fillchar = flag[0]  # 填充字符
        align = flag[1] #对其方式
        length = int(flag[2:])   # 字符长度
        # 根据不同的符号进行不同的填充操作
        # 判断对其方式
        if align == '>':
            # 右对齐
            new_name = self.name
            new_name = new_name.rjust(length,fillchar)
            return new_name
        elif align == '^':
            new_name = self.name.center(length,fillchar)
            return new_name
            #剧中对其
        elif align == '<':
            new_name = self.name.ljust(length,fillchar)
            # 左对齐
        else:
            return ''
        print(fillchar) #
        print(align)
        print(length)






    def shopping(self):
        print('买买买``````````')

    def eat(self):
        print('吃烧烤`````````')

    pass



# 实例化一个对象
xcm = Girl()
print(xcm)

#
# # 使用format来操作我们的对象
# action = '我和我的guimi{}去逛街'
# res = action.format('宁宁')
#
# print(res)

# 使用format来操作我们的对象
action = '我和我的闺蜜{: >10}去逛街'
res = action.format(xcm)

print(res)













'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
