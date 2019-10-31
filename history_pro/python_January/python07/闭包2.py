#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
当函数被调用的时候才会真正确定对应的值到底是什么,在之前都是以普通的变量标识名称而存在

'''
#
# def test():
#     num = 10
#     def test2():
#         nonlocal num # 关键字声明,代表不是局部变量
#
#         num = 666
#         # print(a)
#         print(num)
#     print(num)
#     test2()
#     print(num)
#     return test2
#
# result = test()
#
# # result()

# 简单版
# def test():
#     a = 1
#     def test2():
#         print(a)
#     a = 2
#
#     return test2
#
# newfunc = test()
# # newfunc -> print(a)
#
#
# newfunc()

#
# def test():
#     print(b)
#
#
# print("xxx")
# b = 5
# test()
#
#
#
#
# 普通版
# def test():
#     funcs = []
#     for i in range(1,4):
#         def test2():
#             print(i)
#         funcs.append(test2)
#     return funcs
#
# newfuncs = test()
# # newfunc -> print(a)
# print(newfuncs)
# newfuncs[0]()
# newfuncs[1]()
# newfuncs[2]()
#
# print(newfuncs[0] is newfuncs[1])

# 小幅度升级版
# def test():
#     funcs = []
#     for i in range(1,4):
#         def test2(num):
#             def inner():
#                 print(num)
#             return inner
#         funcs.append(test2(i))
#     return funcs
#
# newfuncs = test()
# # newfunc -> print(a)
# print(newfuncs)
# newfuncs[0]()
# newfuncs[1]()
# newfuncs[2]()
#
# print(newfuncs[0] is newfuncs[1])



# 小幅度升级版2
def test():
    funcs = []
    for i in range(1,4):
        def test2(num):
            def inner():
                print(num)
            return inner
        funcs.append(test2(i))
    return funcs

newfuncs = test()
# newfunc -> print(a)
print(newfuncs)
newfuncs[0]()
'''
newfuncs[0]()   
test()[0]()
funcs[0]()
test2(0)()
inner()
print(num)
'''
newfuncs[1]()
newfuncs[2]()

print(newfuncs[0] is newfuncs[1])

# # 大幅度升级版
# def test():
#     funcs = []
#     for i in range(1,4):
#         def test2(i):
#             def inner():
#                 print(i)
#             return inner
#         funcs.append(test2(i))
#     return funcs
#
# newfuncs = test()
# # newfunc -> print(a)
# print(newfuncs)
# newfuncs[0]()
# newfuncs[1]()
# newfuncs[2]()
#
# print(newfuncs[0] is newfuncs[1])
#
#
