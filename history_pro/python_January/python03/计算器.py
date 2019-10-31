#!/usr/bin/env python
# -*- coding:utf-8 -*-*
# coding by xiaoming
def jiaozheng(num):
    while True:
        if num == "\n":
            pass
        if type(eval(num)) == int:
            return int(num)
        if type(eval(num)) == float:
            return float(num)
        if type(eval(num)) == str:
            print("输入的有瑕疵,请正确输入")
            num = input("请输入源操作数")
# 加减乘除混合运算
result = input("请输入源操作数")
# print(result)
result = jiaozheng(result)
# print(type(result))
# result = int(result)

def jia(i):
    return result + i
def jian(i):
    return result - i
def cheng(i):
    return result * i
def chu(i):
    return result / i
# print('''
# 1   加法
# 2   减法
# 3   乘法
# 4   除法
# ''')
while True:
    print(result)
    op = input("请选择你要的操作")
    i = input("请输入操作数")
    i = jiaozheng(i)
    if op == "/" and i == 0:
        print("净乱输,别闹,重新输入")
        continue
    if op == "+":
        result = jia(i)
    elif op == "-":
        result = jian(i)
    elif op == "*":
        result = cheng(i)
    elif op == "/":
        result = chu(i)
    else:
        print("输入有误请重新输入")

























