#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


import os

while True:
    dynamic = input('输入计算器表达式：')
    if dynamic != 'cls':
        try:
            result = eval(dynamic)
            print('计算结果' + str(result))
        except:
            print('表达式有误')
    else:
        command = 'cls'
# os.system(commond)
# ---------------------



















