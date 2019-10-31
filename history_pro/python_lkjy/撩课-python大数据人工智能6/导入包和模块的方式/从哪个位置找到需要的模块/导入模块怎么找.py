#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<>

# 先找到对应的代码文件,在执行对应代码
import other

# 解释器是不知道other在哪里面
# 只知道other这个名字而已了
# 他会挨个找找文件
# 只能一个一个去试,并不能正向的推导出来
# 现在要分析查找的顺序
'''
从哪个位置查找需要导入的模块:
    第一次导入时:
        按照模块检索路径顺序去找:
            第一级:
                内置模块
            第二级:
                sys.path:
                    构成:
                        当前目录
                        环境变量
                        特定路径下的.pth文件路径列表:
                            查看特定路径
                            后缀名为.pth文件
                        在Python安装路径lib库中搜索
                    注意:
                        自己测试优先级顺序
                追加路径的方式:
                    1.直接修改sys.path
                    2.修改环境变量:
                        PYTHONPATH
                        注意:
                            仅仅在shell中有效
                            pycharm需要另外一种设置方式
                    3.添加pth文件
    第二次导入时:

'''


# 内置模块里面,有一个模块 sys
# import sys
#
# print(sys.name)
# 报错:
# module 'sys' has no attribute 'name'
# 内置模块的优先级比普通的用户定义的模块的优先级高
# 内置模块才是最nb的,要导入先导入他


import fnmatch

print(fnmatch.fnmatch)
# 这个就是先导入自己定义的模块


'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
