#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

def test():
    print("开始")
    yield 1
    print("第一个")

    yield 2
    print("第二个")

    yield 3
    print("第三个")


g = test()

print(g.__next__())
print(g.__next__())
# print(g.__next__())
#
# # 在写一行就抛出异常了
# print(g.__next__())

# 关闭生成器
# g.close()
print(g.__next__())




















