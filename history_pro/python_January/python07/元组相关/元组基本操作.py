#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
# xdl521
# 元祖的相关操作
'''
成明一个空元祖:变量 = () 方式2
变量 = tuple()
创建一个只有单一元素的元组
创建一个多元素的元组

元组的基本操作:
变量[索引] 访问元组中的元素
注意:元组的元素只可以访问,不可以修改
'''
# 如何创建一个空元祖
tupvar = ()
print(tupvar,type(tupvar))

tupvar = tuple()
print(tupvar,type(tupvar))

# 当创建只有一个元素的元祖时:
tupvar = ("核算",)
print(tupvar,type(tupvar))

# 当创建只有一个元素的元祖时:
tupvar = "核算",
print(tupvar,type(tupvar))
# 你可以没有小括号,但是你得有逗号

# 创建多个元素的元组
tupvar = ("H","Q","W","T","U","H",)
print(tupvar,type(tupvar))

# 2 元组的基本操作
tupvar = ("python","php","c++","c","html","Java")

print(tupvar[0])


















