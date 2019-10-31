#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 模块的功能:<>
# from other import *
# print(num1)
# print(num2)
# print(num3)
# # print(_te)
# # 在自己的命名空间执行 导入的代码
def test():
    import other
    import other
    import other
    # 导入后就会执行other代码,然后创建一个模块的对象,并且会分配空间给他
    print(other)
    print(id(other))
    print(type(other))
    print(other.__dict__)
    # 会创建一个叫other 的模块对象

test()
#
# import other
# import other
# import other
# # 导入后就会执行other代码,然后创建一个模块的对象,并且会分配空间给他
# print(other)
# print(id(other))
# print(type(other))
# print(other.__dict__)
# # 会创建一个叫other 的模块对象


# 所有的对象都是以一个属性的形式,附加在了这个模块对象上面
# 只是在顶层(不是在函数内部定义是变量,是直接在模块中创建的)的变量会绑定在模块对象上
num1 = 99

# other.run()
# 在对应的模块的命名空间中执行对应代码,与导入的主模块中的命名空间不相干

'''
注意:
    导入模块后具体做了什么事儿:
        第一次导入时:
            在自己的当下的命名空间中,执行了所有的代码
            创建一个模块对象,并将模块内所有的顶级变量以属性的形式绑定在模块对象上面
            在import的位置引入import后面的变量名称到当前的命名空间(在本模块中的函数里面导入后,函数外面不能用)
        第二次导入时:
            直接执行上述的第三个步骤,从性能上面这样也是合理的
        结论:
            注意:两种导入方式都会大致执行以上步骤
            1.多次导入模块,该模块并不会执行
            2.两种导入方式(import /from import)不存在哪一种更省内存,区别在于把哪一部分内容拿到当前位置来用
            带from的也是全部执行了对应到如的模块,所以对于内存空间来说是一样的

'''







'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
