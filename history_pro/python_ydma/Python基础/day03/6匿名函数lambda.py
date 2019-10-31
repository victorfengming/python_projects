#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
# 教案
lambda表达式
lambda表达式是一种简洁格式的函数。该表达式不是正常的函数结构，而是属于表达式的类型。 基本格式：

lambda 参数,参数...：函数功能代码
如：lambda x,y:x + y    获取2个值的和的lambda函数
带分支格式:

lambda 参数,参数... :值1  if 条件表达式  else 值2
如：lambda sex : '有胡子' if sex == 'man' else '没胡子'
调用函数格式：

lambda 参数,参数...:其他函数(...)
如：lambda x:type(x)
lambda表达式的优缺点:

优点：
    书写简单不需要def关键字
    不需要费脑子想函数名(匿名函数)看起来高大上！

缺点：
    lambda表达式功能受限，无法使用循环和多项分支
    复杂的操作，不适合lambda表达式
示例


#方式1.声明一个简单的lambda表达式
mylamb = lambda x,y:x+y
#调用函数
result = mylamb(4,5)
print(result)

#方式2.声明一个带有分支的lambda表达式
mylamb= lambda sex : '有胡子' if sex == 'man' else '没胡子'
#调用函数
result = mylamb('woman')
print(result)

#方式3.声明一个调用函数的lambda表达式
mylamb = lambda x:type(x)
#调用函数
result = mylamb('拾元')
print(result)

'''

# lambda 表达式
# 是函数的另外一种写法,本质上还是函数
'''
汽车人：
    人型形态：函数

    汽车形态：lambda 表达式
            只能实现一些简单的数据运算或者判断
            无法使用循环或者复杂的操作
基本格式:
    普通的表达式:
        变量名 lambda 参数1,参数2 : 返回值
    带有分支结构的表达式:
        变量名 lambda 参数,参数2 : if 区间的返回值 if条件 else else区间的返回值

'''

# 求和函数

# def sum(no1 = 10,no2 = 20):
#     result = no1 + no2
#     print(result)
#
# # 调用函数
# sum()


# lambda 函数 自带返回值,
# result = lambda no1,no2 :no1 + no2
#
# print(result(5, 6))

# 带有判断条件的lambda
# def func(no1,no2):
#     if no1 > no2:
#         return no1
#     else:
#         return no2
#     pass
#
# # 调用函数
# max = func(3,4)
# print(max);
# 利用lambda 函数 进行简单的流程控制
# maxvar = lambda no1,no2:no1 if no1>no2 else no2
#
# print(maxvar(5,3))


# 用lambda 表达式写一个判断性别函数
# 普通的
# def func(sex):
#     if sex == "男":
#         print("这个一个真男人")
#     else:
#         print("这个可能是个女人,也有可能是个人妖")
#
# func = lambda sex :"这个一个真男人" if sex == "男" else "这个可能是个女人,也有可能是个人妖"
# print(func("男"))


# 我获取并且打印数据类型 print(type(数据))
# 在lambda 表达式中调用其他函数
# printtype = lambda var: print(type(var))
# printid = lambda var: print(id(var))
# 调用函数
# printtype(True)
# printtype(1)

# 过程式函数就是没有返回值的函数




