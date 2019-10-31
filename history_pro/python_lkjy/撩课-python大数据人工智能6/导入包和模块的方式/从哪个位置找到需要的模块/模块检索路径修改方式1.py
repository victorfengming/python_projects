#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<临时添加系统路径>
'''
追加路径方式:
    1.直接修改sys.path 只作用于本次
    2.修改环境变量:
        PYTHONPATH
        注意:
            仅仅在shell中有效
            pycharm需要另外一种

    3.添加.pth文件

'''
#
import sys

res = sys.path
res.append("C:\\Users\\Administrator\\Desktop\\my_directory")
# 手动添加了一个目录,临时的加
# for i in res:
#     print(i)
import demo

print(demo.name)

# 这个只是在程序中临时改的,只有在程序运行的时候才改了,程序结束了就恢复了,这个不会污染到大环境
# 要是运行完这个文件,其他文件还要再添加









'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
