#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<猜年龄>

count = 0
age = 26
while count < 3:
    user_guess = int(input("your guess:"))
    if user_guess == age :
        print("恭喜你答对了，可以抱得傻姑娘回家！")
        break
    elif user_guess < age :
        print("try bigger")
    else :
        print("try smaller")

    count += 1















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
