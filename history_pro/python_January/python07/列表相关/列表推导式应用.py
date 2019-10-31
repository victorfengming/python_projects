#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
# xdl521
# 用for 写99乘法表 列表推导式 实现
# 结果存在一个列表中
# 完成要求
# result = [i*j for i in range(1,10) for j in range(1,10) if j<=i]
# print(result)

result = [i*j for i in range(1,10) for j in range(1,i+1)]
print(result)
# for i in result:
#     print(i,end="")

# # 99
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:<2} ".format(i,j,i*j),end="")
#
#     print()

res = [str(j)+"x"+str(i)+"="+str(i*j) for i in range(1,10) for j in range(1,i+1)]
print(res)
# 这个就NB啦,直接打印结果
# for i in range(10):
#     print(" ".join(["%d*%d=%-2d"%(j,i,j*i) for j in range(1,i+1)]))

















