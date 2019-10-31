#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<99乘法表>


# # 如何打印一行 10个#
# print(help(print))
# print(1,end="")
#
# i = 0
# while i<10:
#     j = 0
#     while j<10:
#         print("#",end = "")
#         j += 1
#     print()
#     i += 1

# 乘法表
i = 1#行数
while i <= 9 :
    j = 1
    while j <= i :
        print( str(j)+"*"+str(i)+"="+str((i)*j)+"  ",end = "")
        if i*j<10 :
            print("\t",end ="")
        j+=1
    print()
    i+=1

# 隔行变色
# i = 0
# while i<10:
#     j = 0
#     while j<10:
#         if j%2 :
#             if i%2:
#                 print("*",end = "")
#             else :
#                 print("#", end="")
#         else:
#             if i%2:
# #                 print("#",end = "")
# #             else :
# #                 print("*", end="")
#
#         j += 1
#
#     print()
#     i += 1
