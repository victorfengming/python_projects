#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 关于赋值是改变的是指针指向对象还是复制值过来的测试

a = [2]
print("a是",a)

b = a
print("a是",a)
print("b是",b)

b[0] = 6
print("a是",a)
print("b是",b)

#
# b = [3]
# print("a是",a)
# print("b是",b)





















