# #
# def f(x,n):
#     return (x**2-1)**n
#
# def fd(x,n):
#     # a = (n*((x**2-1)**(n-1)))*(2*x)
#     return (n*((x**2-1)**(n-1)))*(2*x)
# # x = int(input("请输入x："))
# x = float(-1)
# # n = int(input("请输入n："))
# i = 10
# # while i>0 :
# #     n = float(10-i)
# #     print(f(x,n),end="")
# #     print("\t",end="")
# #     print(fd(x,n))
# #     i -= 1
#
# print(f(x,n),end="")
# print("\t",end="")ll
# print(fd(x,n))
#

# !/usr/bin/env python
# coding=utf-8

import re

'''
coeffTable 是 {变量：系数列表}, 如果不懂， 请运行看程序结果就懂了
建议看之前先运行一下看看结果
'''
coeffTable = {'__LENGTH__': 0, '__CONS__': []}


def parseEquation(str):
    # 分离系数与变量
    pattern = r'(^\s*\d*|[+-]\s*\d*)\s*(\w*)'  # 用来分离变量与系数的表达式。
    ptrn = re.compile(pattern)
    left, right = str.split('=')  # 方程左右两边分离

    coeffTable['__CONS__'].append(float(right.strip()))  # 右边加入到常量
    # 请将 1， 2， 3 结合起来看， 比较容易懂
    # 1. 原有变量的系数列表在后面添加一个0， 同时列表长度增加 1
    for key in coeffTable:
        if key not in ('__LENGTH__', '__CONS__'):
            coeffTable[key].append(0)
    coeffTable['__LENGTH__'] += 1

    # 遍历在新方程中出现的变量并转换其对应系数
    for val in ptrn.findall(left):
        # 转换系数
        if val[0] == '-':
            coeff = 1
        elif val[0][-1].isspace():
            if val[0][0] == '-':
                coeff = -1
            else:
                coeff = 1
        else:
            coeff = float(''.join(val[0].split()))  # 去掉所有空白字符后转换成 float 数

        varName = ''.join(val[1].split())  # 去掉所有空白字符，获得变量名
        coffList = coeffTable.get(varName)
        # 2. 将新出现的变量添加至系数表
        if coffList == None:
            coeffTable[varName] = []
            for i in range(coeffTable.get('__LENGTH__')):
                coeffTable[varName].append(0)
        # 3. 将该变量的系数列表的最后一个系数变成当前方程对应的系数
        coeffTable[varName][-1] = coeff


# 测试
if __name__ == '__main__':
    equation = '3x + 4y - z - a + b + 3c = 7'
    print(equation)
    parseEquation(equation)
    equation = '7x - 6y = 9'
    print(equation)
    parseEquation(equation)
    print(coeffTable)
    #       - --------------------
    # 作者：gfzeng
    # 来源：CSDN
    # 原文：https: // blog.csdn.net / gfzeng / article / details / 8606304
    # 版权声明：本文为博主原创文章，转载请附上博文链接！