#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 其他流程控制语句

'''
break 破坏,结束
continue 继续
pass 跳过
'''
# 带有4的我都不要
# var = 0
# while var <= 100:
#     if var//10==4 or var%10==4:
#     # if "4" in str(var):
#         var += 1
#         continue
#     print(var)
#     var += 1
#
#
# # 带有4的我都不要,第二种写法
# var = 0
# while var <= 100:
#     # if var//10==4 or var%10==4:
#     if "4" in str(var): #检测
#         var += 1
#         continue
#     print(var)
#     var += 1
#
# # pass 语句就是用来占位的,
# if 5>3:
#     pass    #什么都不做,不能空着
# else:
#     print("sdjkg")
# pass无任何意义,主要是用来占位用

# 不要55 66 77 这样的
for i in range(1,101):
    if i%11 == 0:
        # print()
        continue
    print(i)
















