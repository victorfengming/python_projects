#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''

格式:
    #1 普通
    变量 = {k:v for k,v in 字典.items()}
    变量 = {建表达式:值表达式 for k,v in 字典.items()}

    #2 带有条件的推导式
    变量 = {k:v for k,v in 字典.items() if 条件表达式}
    变量 = {建表达式:值表达式 v for k,v in 字典.items() if 条件表达式}

    #3 多个循环的字典推导式
    变量 = {k+i:v+j for k,v in 字典.items() for i,j in 字典2.items() }

    #4 带有条件的表达式的多个循环的字典推导式推导式
    变量 = {k+i:v+j for k,v in 字典.items() for i,j in 字典2.items() if 条件表达式}


'''

# dictvar = {"黑旋风":"李逵","浪里白条":"䎠小二","大刀":"关胜","股上调":"时迁"}
#
# # dictvar = {""}
# newvar = {k:v for k,v in dictvar.items()}
#
# print(dictvar)
# print(newvar)
#
# dictvar = {"黑旋风":"李逵","浪里白条":"䎠小二","大刀":"关胜","股上调":"时迁"}
#
# newvar = {k+"e":v for k,v in dictvar.items() if k != "大刀"}
#
# print(dictvar)
# print(newvar)
#
# dictvar = {"黑旋风":"李逵","浪里白条":"䎠小二","大刀":"关胜","股上调":"时迁"}
# dict1 = {"A":"1","B":"2","c":"3","d":"4","I":"2"}
# newvar = {k+"e":v for k,v in dictvar.items() if k != "大刀"}
#
# print(dictvar)
# print(newvar)
#

# 最后那个例子就不写了
















