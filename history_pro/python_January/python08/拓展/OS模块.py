#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


# os模块,操作系统模块
import os

# getcwd()
# 功能:# 获取当前的工作目录
# 格式: os.getcwd()
# 返回值:路径的字符串

# lj = os.getcwd()
# print(lj)

# chdir()
# 功能:修改当前目录
# 格式:os.chdir
# 返回值:None

# os.chdir("E:\PycharmProjects\python_January\python07")
#
# listt = os.listdir(lj)
# print(listt)
#
# listdir()
# 功能:获取指定文件夹中的所有文件和文件夹组成的列表
# 格式:os.listdir(目录路径)
# 返回值:目录中内容名称的列表


# mkdir()
# 功能:创建一个目录/文件夹
# 格式:os.mkdir()
# 返回值:none

# os.mkdir("E:\PycharmProjects\python_January\python10\demo\dssda")

# makedirs()
# 功能:递归创建文件夹,上面那个只能创建最后一级文件夹,这个就nb了,能创建好多层的
# 格式:os.makedirs()

# os.makedirs("E:\PycharmProjects\python_January\python11")
# os.makedirs("E:\PycharmProjects\python_January\python10\demo\dssda")


# rmdir()
# 功能:移除一个空的目录,必须是空目录
# 格式:os.rmdir()
# 返回值:none
# os.removedirs("E:\PycharmProjects\python_January\python10\demo\dssda")
# os.rename("E:\PycharmProjects\python_January\python11","E:\PycharmProjects\python_January\python12")
# info = os.stat("E:\PycharmProjects\python_January\兄弟连python课件\index.html")

# print(info)

# os.system("dir")
# hjbl = os.getenv("path")
# print(hjbl)

# os.putenv()
# 功能:设置系统环境变量
# 格式:os.putenv()
# 无返回值
# putenv设置的不能用getenv()检测到

# exit()
# 功能:推出当前执行命令,直接关闭当前操作
# 格式:exit()
# 无返回值

# # curdir()
# s = os.curdir
# print(s)

# path
# os的一个子模块,操作非常多


# name
# 功能:当前系统的内核名称 win->nt linux
# n = os.name
# print(n)

#
# # 获取单签系统的路径分隔符符号
# # window
# fgf = os.sep
# print(fgf)
#
# # 获取单签系统的文件扩展名和文件名的分隔符符号
# # window
# fgf = os.extsep
# print(fgf)
#
# # 获取单签系统的文件扩展名和文件名的换行符号
# # window
# fgf = os.linesep
# print(fgf)


# d = os.environ
#
# print(d)
#
# abspath()
# 功能:将一个相对路径转化为绝对路径
# 格式:os.path.abspath()
# 返回值:绝对路径字符串

# basename()
# 功能:获取路径中的文件夹或者文件名称
# 格式:os.path.basename()
#
# dirname()
# 功能:获取路径中的路径部分(除去文件名字部分)
# 格式:os.path.dirname()
# 返回一个路径字符串
# strr = os.path.dirname("E:/PycharmProjects/python_January/python08/OS模块.py")
# print(strr)

# join()
# 功能:将两个路径合成一个路径
# 格式:os.path.join()
# 返回值:合并之后的路径
# os.makedirs("E:/PycharmProjects/python_January/python14")
char = os.path.join("E:/PycharmProjects/python_January/python14","E:/PycharmProjects/python_January/python13")
print(char)


























