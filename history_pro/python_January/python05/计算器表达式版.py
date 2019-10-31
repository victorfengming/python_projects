#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


result = int(input("请输入一个源操作数"))
# print(result)
while True:
    var = input(result)
    # if var[0] != "+" and var[0] != "-" and var[0] != "*" and var[0] != "/" :
    #     print("输入操作有误,重新输入")
    # else:
    try:
        result = eval(str(result)+var)
    except:
        print("输入有误,请重新输入")
# print(result)




















