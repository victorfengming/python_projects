#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''




# #创建生成器
def test():
    print("xxxx")
    res1 = yield 12345
    print("res1",res1)

    res2 = yield 2
    print("res2",res2)



g = test()
#g就是一个生成器
# print(g.__next__())
# print(g.__next__())

# print(g.send("ooo"))
print(g.send(None))
# 第一次调用要传递一个none

print(g.send("哈哈哈"))


# send的参数用于给上一次挂起的yield语句传值







