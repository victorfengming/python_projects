#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming



# 相对路径,绝对路径
# open("文件","模式")
#
# 1.打开文件
#
# 2.读写操作
#
# 3.关闭文件
#
# f = open("a.txt", "r", encoding="utf-8")
#
# content = f.read()
# print(content)
# f.close()
#
# print(f)
import collections
f = open("abc.txt", "r", encoding="utf-8")


print(isinstance(f,collections.Iterator))
# f.write("qwertyuisdfghjk")
# print(content)
# f.close()
#
# for i in f:
#     print(i,end="")
# # print(f)

content = f.readlines()
for i in content:
    print(i,end="")













