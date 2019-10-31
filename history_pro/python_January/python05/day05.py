#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 变量的作用域  - 变量的有效范围
'''
全局变量: 当前页面声明
    全局变量在函数内部可以正常使用,只有用global 声明的全局变量才可以被函数内部更改和查看,没有使用global声明的全局变量,只可以查看,不可以更改
    全局变量在函数外部可以正常使用
局部变量: 函数内部声明
    局部变量可以在函数内部正常使用
    局部变量不可以在函数外部正常使用
'''

# 定义一个全局变量

var = 10
def func():
    # 在函数内部打印全局变量
    print("全局变量",var)

# 调用函数

func()
print("在函数外部使用",var)

# 定义一个局部变量
# 在函数内部声明一个变量

def func():
    # 生明一个局部变量
    print("在函数内部打印局部变量",var)

# 调用函数u

func()

print(var)

#-----------------------------------------------------

'''
全局变量: 全身麻醉

局部变量: 局部麻醉
'''
# 声明一个函数

def func():
    # 将局部变量提升为全部变量
    global mazuiji
    mazuiji = "局部麻醉剂"
    print("在嘴里拔牙是时候使用",mazuiji)

    pass

func()

print("在手上使用",mazuiji)

mazuiji = 10

def func():
    # 在函数中只能查看全局变量,但是是不能更改的
    # 所以这个全局变量,不是一个完全的全局变量

    pass

func()

print("在手上使用",mazuiji)

# --------------------------------------------------
def func1():
    print("我是func1")

def func2():
    print("我是func2的第一次打印")

    func1()
    print("我是func2的第二次打印")

func2()
#-------------------------------------------------
# 递归函数

# 在函数本身自己调用自己本身,就是递归

def digui(num):
    print(num)
    if num > 0:
        digui(num - 1)

    # 第二次打印num
    print(num)

# 调用递归函数
digui(5)

# 局部变量: 每次变量的值,只对当前调用有效

# 用递归函数求 斐波那契额数列
def fbnq(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fbnq(i-1) + fbnq(i-2)

print(fbnq(15))

# 用递归函数球儿阶乘
def jc(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    else:
        return  jc(i-1) * i

print(jc(5))

# 递归升级版
def digui(num):
    print(num)
    if num > 0:
        digui(num - 1)
    if num == 0:
        print("---------------------------")
    print(num)

digui(3)

# -------------------------------------------------
def outer():
    # 定义一个变量
    var = 11

    def inner():
        # nonlocal 声明var 变量 var是inner函数 的外部变量
        nonlocal  var
        # nonlocal 关键字声明,既不是全局变量,也不是局部变量    var = var + 56
        print(var)
    inner()

outer()

# -----------------------------------------------
# lambda 表达式
# lambda 表达式是一种简介格式的函数.该表达式