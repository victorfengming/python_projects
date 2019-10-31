#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

#locals()

'''
#在页面中使用locals函数
#定义变量
girls = '西施'
boys = '吕布'

result = locals()
print(result)

#检测某个变量是否声明
have = 'girls' in result
print(have)

#打印系统提供的变量
print(__file__)
'''

#函数内部使用locals
#页面中定义变量
mother = '妈妈'
father = '爸爸'

def myhome():
    #定义内部变量
    sister = '小姐姐'
    brother = '小哥哥'
    #在函数内部使用locals
    print(locals())

#调用函数
myhome()

#在页面当中使用locals
#print(locals())#此处可以获取mother，father和myhome三个自定义变量
'''
#abs()
var = -99
result = abs(var)
print(result)


#sum()
var = [1,2,3,4,5,6]
result = sum(var)
print(result)


#max()
#格式1：
nums = [1,2,41,23,12,5423,4,243,635,74,57]
result = max(nums)
print(result)

#格式2：
result = max(2,123,2,342,34,35,74,673,45,345,23,41,341,34)
print(result)


#min()
#格式1：
nums = [1,2,41,23,12,5423,4,243,635,74,57]
result = min(nums)
print(result)

#格式2：
result = min(2,123,2,342,34,35,74,673,45,345,23,41,341,34)
print(result)


#pow()
result = 5 * 5 * 5 * 5 * 5* 5
print(result)

result = pow(5,6)
print(result)


#round()
var = 7.5
result = round(var)
print(result)


#range()
#格式1  产生0-100之间的连续整数，包含0不包含100
result = range(100)
print(result)

for i in result:
    print(i)

#格式2：
result = range(50,90)
print(result)
for i in result:
    print(i)
'''

#格式3：
result = range(20,100,5)
print(result)

for i in result:
    print(i)

#bin（）
var = 55
result = bin(var)
print(result,type(result))

#oct()
var = 155
result = oct(var)
print(result,type(result))

#hex()
var = 255
result = hex(var)
print(result,type(result))

#chr()
result = chr(57)
print(result,type(result))

#ord()
result = ord('A')
print(result,type(result))

'''
#repr()
var = '小明明\n明明白\'小红\t喜欢自己'
print(var)

result = repr(var)
print(result)
'''


#input()
result = input('请输入您的年龄：')
print(result,type(result))















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
