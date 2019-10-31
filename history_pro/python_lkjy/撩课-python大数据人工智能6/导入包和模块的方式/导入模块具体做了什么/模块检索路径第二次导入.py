#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<第二次导入>

# 经过第一次导入,已经将这个模块加载到了内存中过了,
# 第二次导入,从已经加载的模块中去找
import sys
import other
import other
import other
import other
import other
import other
import other
import other
res = sys.modules
print(res)
for i in res:
    print(i)

import other

print("------------------------------------")
res = sys.modules
print(res)
for i in res:
    print(i)


#
# 第二次导入时:
#     从已经加载过的模块中去找
#     查看已经加载的模块:
#         import sys
#         sys.modules

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
