#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
import math
# 百钱买百鸡 母鸡5块钱 公鸡 3块钱 小鸡 一块钱3只 总共买100只鸡 花100元

for i in range(0,21):
    for j in range(0,34):
        for k in range(0,100):
            if (5*i+3*j+k/3)==100 and (i+j+k)==100:
                print(str(i)+"只母鸡",str(j)+"只公鸡",str(k)+"只小鸡")


















