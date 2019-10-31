#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<装饰器>
#
# def love():
#     print(
#         'qiiqqinqin'
#     )
#
# # 调用函数
#
# love()
# love()
# love()
#
# # 增加功能
# # 定义增加功能函数
# def decor(func):
#     print('抱抱')
#     func()
#     print('举高高')
#     pass
#
# # 基本函数
# def love():
#     print(
#         'qiiqqinqin'
#     )
# a = 0
#
# love = decor(love)

'''
# 第五步:为基本函数添加 返回值和参数

# 返回值
# 定义装饰器函数
def decor(func):
    # 定义一个内部函数
    def inner():
        # 增加的功能
        print('前面增加的功能')
        # 基本功能
        var = func()    # 相当于调用love
        # 增加的功能
        print('后面增加的功能')
        return var
    return inner

# 定义基本函数
@decor
def love():
    print('主内容')
    return '❤'


# 调用函数
result = love()
print(result)


'''

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
'''

# 参数的处理方式
# 定义装饰函数
def decor(func):
    # 定义内部函数
    def inner(who1,who2):
        # 增加功能1
        print('(づ｡◕‿‿◕｡)づ抱抱')
        # 调用基本功能
        func(who1,who2)
        # 增加功能2
        print('(づ｡◕‿‿◕｡)づ举高高')

    # 返回内部函数inner
    return inner
# 定义基本函数

@decor
def love(who1,who2):
    print('{}亲亲{}'.format(who1,who2))

# 调用函数
love('张三','王二麻子')
'''

'''
# 第六步 加上收集参数

# 定义装饰器函数
def decor(func):
    # 定义内部函数
    def inner(*p,**w):    # 装饰之后的love函数
        # 增加功能
        print('前面增加的功能')
        # 基本函数
        func(*p,**w)
        # print('包ba')
        # 增加功能2
        print('后面增加的功能')
    # 返回内部函数
    return inner
    pass

# 定义基本函数
@decor # 语法糖
def love(*parent,**child):
    print(parent,'亲亲',child)


# 调用基本函数
love('爸爸','妈妈',son = '儿子',girl = '小女儿')

'''
'''
# 第七步 :为装饰器添加参数

# 定义装饰器函数
# 一个装饰器同时装饰多个函数(不同的函数装饰不同的内容)
# 要让装饰器能够区分开被装饰的函数类别
def outer(arg):
    def decor(func):
        # 定义内部函数
        def inner():
            # 判断正在装饰的函数
            if arg == 'xiao':
                # 增加功能
                print('我给你讲个笑话')
                # 调用基本函数
                func()
                # 增加功能
                print('肚子疼了吧')
            elif arg == 'ku':
                print('增加功能1')
                func()
                print('增加功能2')
                pass
        # 返回内部函数
        return inner

    # 返回装饰器
    return decor


# @decor
def smile():
    print('哈哈哈``')

# @decor
def cry():
    print('呜呜呜``')


cry()


'''


'''
# 第八部 :将类作为参数传入装饰器中使用
# 存在一个类,类中的方法是需要装饰的功能
class Parent:
    # 成员方法
    # 抱抱
    def baobao():
        print('抱抱')

    # 举高高
    def jugaogao():
        print('举高高')

# 装饰器外层
def outer(cls):

    # 装饰器
    def decor(func):
        # 定义内部函数
        def inner():
            # 增加功能
            cls.baobao()
            # 基本函数
            func()
            # 增加功能2
            cls.jugaogao()
        # 返回内部函数
        return inner
    # 返回装饰器
    return decor
# 装饰器
def decor():
    pass

# 基本函数
# @函数(类)
# @装饰器
@outer(Parent)
def love():
    print('卡卡')


love()

'''



# # 第九步 用类作为装饰器
# # 需要对类 魔术方法 装饰器 有很深的了解
#
# '''
# # 定义装饰器
# # 装饰器外层
# def outer(arg):
#     # 装饰器
#     def decor(func):
#         # 返回函数
#         def inner():
#             #增加功能1
#             print('抱抱')
#             # 基本函数
#             func()
#             #增加功能2
#             print('举高高')
#             pass
#
#         # 返回内部函数
#         return inner
#
#     # 返回装饰器
#     return decor
# '''
# # 定义类作为装饰器
# '''
# 1.可以带有区分或者使用的参数arg
# 2.具有接收基本函数传入的参数func
# 3.定义未来函数
# '''
#
# class Outer:
#     # 初始化魔术方法
#     def __init__(self,arg): # 相当于outer函数
#         # 接受的参数为了其他成员方法可以使用 存入对象中
#         self.arg = arg
#         pass
#     # 一定要有__call__魔术方法 使得对象能够作为装饰器使用
#     def __call__(self,func):
#         # 这是装饰器的本体 相当于decor函数
#         # print(func)
#         # 将call接受的参数func存入对象
#         self.func = func
#         return self.inner
#         pass
#
#
#     '''
#             通常这个inner函数不写在类里面
#             :param func:
#             :return:
#             '''
#
#     def inner(self):
#         # 增加功能
#         print('增加的功能')
#         # 基本功能调用
#         self.func()
#         # 增加功能2
#
#         print('举高高')
#
#     pass
#
#
# # 基本函数
# @Outer('ai')
# # @类()  -> @对象
# # 但是装饰器都是一个函数啊
# def love():
#     '''
#     基本函数
#     :return:无返回值
#     '''
#     print('么么哒(✪ω✪)')
#
# love()
#
# # 第十步 为类添加装饰器
#
#
# # 定义装饰器
# def decor(cls):
#
#     #定义颞部信息(相当于原来的inner)
#     def inner():
#         # 产生Human对象 [相当于基本功能]
#         obj = cls()
#         # 添加内容 [相当于增加功能]
#         obj.age = 1
#         obj.sex = 'man'
#
#         # 返回对象
#         return obj
#
#     # 返回inner函数
#     return inner
#
# # 定义基本类
# @decor
# class Human:
#     pass
#
#
# # 使用类 实例化对象
# # ren = Human()
# # 相当于调用Human函数 得到了一个结果{对象}
# # print(ren.__dict__)
#
#
#
# ren = Human()
#
# print(ren.__dict__)
#


# 第十一步 : 多层装饰器嵌套

# 定义装饰器1

def decor1(func):
    # 定义内部函数
    def inner():
        # 增加功能1
        print('抱1抱````')
        # 调用基本功能
        func()
        # 增加功能2
        print('举高1高')

    return inner
    pass


# 定义装饰器2

def decor2(func):
    # 定义内部函数
    def inner():
        # 增加功能1
        print('抱2抱````')
        # 调用基本功能
        func()
        # 增加功能2
        print('举高2高')

    return inner
    pass

# 定义基本函数
@decor1
@decor2
def love():
    print('亲亲')


love()










