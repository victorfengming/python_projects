#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 函数 function 功能,函数
'''
把程序中的一些功能组成一些代码组或代码块儿

在计算机程序中,具有一定功能的代码结构
特点:
    1.提高代码的复用率,避免重复开发
    2.可以提升开发效率,
    3.便于后期维护
    4.函数未调用不执行
    5.函数调用前需要定义,函数可以无数次的调用
'''
# def 打印(hang,lie):
#     var = 0
#     while var<hang:
#         num = 0
#         while num < lie:
#             print("☆",end="")
#             num += 1
#         print()
#         var += 1
#
# 打印(5,5)

'''
函数名定义规则:
    1.可以使用英文,不可以是中文
    2.可以使用数字,但是不能开头
    3.不能使用特殊字符,除下划线
    4.区分大小写
    5.函数命名要有意义
    6.不能用系统关键字
    7.不能和系统内置函数重复
'''
# def func():
#     print("人生苦短,我学python")
#     pass
# # 调用函数
# func()
# func()
#
'''
参数:
    形参:定义函数时,函数名后面的括号内的参数,形式上的参数
        带有默认值的形参:如果没有传入形参,使用默认值进行运算,如果传入了实参,则使用实参进行计算
    实参:调用函数时,函数名后面括号内的参数,实际的参数
        其实实参传递到形参就是一个变量赋值的过程
        带有关键字的实参可以准确传入到对应的实参当中
    收集参数:
        普通收集参数:一个*
            没有形参接收的实参,被收集到普通收集参数中,形成一个元祖
        关键字收集参数:两个**
            没有形参接收的关键字实参,被关键字收集参数收集,形成一个字典,关键字作为字典中的键,值作为字典中的值.
'''

# #定义一个求和函数
# def 求和(nu1 = 5,nu2 = 5):
# #     nu1 = 10
# #     nu2 = 23
#     result = nu1 + nu2
#     print(result)
#
# 求和(3,5)

# 现在我要求多个数的和

# def sums(nu1,nu2,*abc):
#     #abc为一个元祖
#     print(abc)
#     result = nu1 + nu2
#     print(result)
#
# 定义函数
def sums(*abc):
    sum = 0
    for i in abc:
        sum += i
    return sum

# # 调用函数
# print(sums(1,45,6,5,7,9))



# # 刺激战场
def cjzc(tk,fdy,ssn,bb,jlz):
    print("头上戴着",tk)
    print("身上穿着",fdy)
    print("手上拿着",ssn)
    print("背上背着",bb)
    print("脖子戴着",jlz)
    pass
#
# # 调用函数
# cjzc("三级包","九八k","大金链子","三级头","三级甲")
# cjzc(bb = "三级包",tk = "九八k",fdy = "大金链子",ssn = "三级头",jlz = "三级甲")
#
def func(a,b,c,**num):
    # num 是一个字典类型
    pass
    print(a,b,c)
    result = 0
    for i in num.values():
        # print(i)
        result += i
    print(result)
#
# # func(a = 1,b = 2,c = 3, e = 4, f = 5)
# func(1,2,3,e = 4, f = 5)
# 不能同时传两个实际参给一个形式参

# 普通形参,普通实参,关键字实参,普通收集参数,关键字收集参数
# 定义
def func(a,b,c,*num,**var):
    print(a)
    print(b)
    print(c)
    print(num)
    print(var)
    print("参加大会的人员有100人")
#
# func(1,2,3,4,5,6,q = 4,e = 5,f = 6,g = 8)
# 这里需要注意的是哪些实参会被哪些参数拿走
# 标准写法:
def 函数名 (普通形参,普通收集参数,关键字收集参数):
    pass

# 调用函数
# 函数名(普通实参,关键字实参)
# 在实用的时候,能不混用就不混用

# 普通收集参数 拿到的是 元祖
# 关键字收集参数 拿到的是 字典

# key value item 的用法
#
# dic = {"黑旋风":"李逵","小李广":"花容"}
# for name in dic:    #默认打印键
#     print(name)
#
# for name in dic.keys():
#     print(name)
#
# for zhi in dic.values():
#     print(zhi)
#
# for i,j in dic.items():
#     print(i,j)

