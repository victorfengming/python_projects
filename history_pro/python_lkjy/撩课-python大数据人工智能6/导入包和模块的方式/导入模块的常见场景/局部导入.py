#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<局部导入(函数内部导入模块,节约资源)>

#
# 局部导入:
#     在某个局部范围内导入模块 在其他范围无法使用
#     如果,想要全部范围都能使用,在文件顶部导入相关模块
#     使用场景
#
#
# # 函数可以产生命名空间
# import other
#
# # 只有在这个位置才会使用到 ,这个里面的一些资源,num1,num2 等等,其他资源用不到
#
# # 往后这个run函数被不被调用还不一定 呢,但是不管怎么样,other还是执行了
# def run():
#     name = "sjagdla"
#
#     print(num1)
#     print(num2)
# # print(name)


# 函数可以产生命名空间,这次在函数中导入other,这回将other放到函数内部的命名空间中了,在外部不能访问
def run():
    name = "sjagdla"
    import other
    print(num1)
    print(num2)
# print(name)


# 类也可以产生一个命名空间








'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
