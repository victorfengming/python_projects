#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''




# # 列表推掉式
# l = [i for i in range(1,10000000) if i % 2 == 0]
#
# iter(l)
#
# l = (i for i in range(1,10000000) if i % 2 == 0)
# print(l,type(l))
#
# iter(l)
# # 创建生成器 生成器表达式就是列表的推到式将中括号变成小括号
# l = (i for i in range(1,10000000) if i % 2 == 0)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
#
# print(l.__next__())
#
# for i in l:
#     print(i)
# print(l,type(l))

# iter(l)

# 创建生成器2生成器函数
# yield 可以去组断函数的执行,然后,当使用next()函数,或者,__next__(),都会让函数继续执行,然后,当执行到下一个yield语句的时候,又会被暂停
def test():
    print("xxx")
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("f")

    yield 4
    print("c")

    yield 5
    print("q")




g = test()

print(g)

print(next(g))
print(next(g))
# print(next(g))










