#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<>
#
# import other
#
# print(other.num)
# print(other.num2)
# xinaz 现在我想要只导入num ,而num2不导入

# 作用:
#     想要导入一个模块或者包中的某个部分
# from A import B(as C)
#     理论:
#         明确一点:
#             只能从大的地方找小的地方
#             从小的地方到大的范围就会出现问题
#         按照大小啊顺序可以分为几个层级:
#             # 包:
#                 # 子包:
#                 #     模块:
#                 #         子资源
#         注意面向关系:
#             就是说包里面只能看到模块,看不到模块中的资源,不能跨级别调用
#             模块里面只能看到模块资源
#
#
#     最终组合:
#         从包中导入模块:
#             单个
#             多个
#             起别名
#             包有多层级
#
#         从模块中导入资源:
#             单个
#             多个
#             起别名
#             模块有多层级
#
# 补充 form xxx import *
# 啥都导入

# 导入单个模块
# from p1 import Tool,Tool2
#
# print(Tool.num)
# print(Tool2.name)

# 要保证import后的内容最简单化
# 尽可能将层级关系放在from后面






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
