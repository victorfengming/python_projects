#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 定义异常类型
# 不幸运的异常类型
class UnluckError(Exception):
    # 为当前异常类型添加更多的信息
    def __init__(self,errmsg,errno,errfile):
        # 记录错误信息
        self.errmsg = errmsg
        # 记录错误编号
        self.errno = errno
        # 记录错误文件
        self.errfile = errfile
    pass

# 写这些有什么用啊
try:
    # 检测容器中是否包含带有4的数据
    nums = [123,325,245,647,942,157,2,4,56,235,645,3423,3546,678,243]
    for i in nums:
        # 检测容器中是否包含带有4的数据
        # {1.有咩有异常需要自己判断}
        if '4' in str(i):
            # 出现不幸运异常
            raise UnluckError('程序中出现了不幸运的数字',4444,'c:/abc.py')
            # {2.有异常需要自己抛出}
            # 手动将我们的异常抛出到except块中 了
            # print('与偶问题')
            pass
        else:
            print('没问题')
    pass

except UnluckError as err:

    print('程序出席那了异常``')
    print(err)
    print(type(err))
    pass













'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
