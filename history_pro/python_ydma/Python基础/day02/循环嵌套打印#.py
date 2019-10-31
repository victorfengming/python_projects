#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


# # 如何打印一行 10个#
print(help(print))
print(1,end="")

i = 0
while i<10:
    j = 0
    while j<10:
        print("#",end = "")
        j += 1
    print()
    i += 1
