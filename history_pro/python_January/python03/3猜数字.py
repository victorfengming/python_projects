# Coding by xiaoming
# -*- coding:utf-8 -*-

# 猜数字游戏
defaultnum = 57

while True:
    num = int(input("请输入一个整数"))
    if num < defaultnum:
        print("猜小了,请重新输入")
    elif num > defaultnum:
        print("猜大了,请重新输入")
    else :
        print("猜对了^_^")
        break







