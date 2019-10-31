#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

# 讲本质一点,生成器就是一个特殊的迭代器
# 生成器只能试用一次

def test():
    print("开始")
    yield 1
    print("第一个")

    yield 2
    print("第二个")

    yield 3
    print("第三个")

g = test()

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())


for i in g:
    print(i)

s = test()

for i in s:
    print(i)


# 生成器 中若果碰到return 会直接终止,抛出stopiteration
# 生成器只会遍历一次
# 要是想要再次的遍历,还要在创建一个生成器












