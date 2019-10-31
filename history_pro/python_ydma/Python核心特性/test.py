#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<用于暂时测试>

# i = 0 # 代表行数
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d ' %(j,i,i*j),end="")
#     print()
#

#
# i = 0 # 代表行数
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print('%d*%d=%d ' %(j,i,i*j),end="")
#     print()
#
#
#


# 输入三个字,要求按照从小到大的顺序输出
a = []
a.append(int(input('请输入第一个数字')))
a.append(int(input('请输入第二个数字')))
a.append(int(input('请输入第三个数字')))
a.sort()
for i in a:
    print(i)

# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print('%dx%d=%d'%(i,j,j*i),end="\t")
#     print()






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
