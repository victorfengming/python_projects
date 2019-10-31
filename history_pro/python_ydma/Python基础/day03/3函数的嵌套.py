#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

def func1():
    print("我是func1身份")

    print("sdjkf")

def func2():
    print("我是func2的第一次打印")
    # 在函数内部调用 func1
    func1()
    print("我是func2的第二次打印")
# 调用func2
func2()


















