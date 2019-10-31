# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # coding by xiaoming
#
'''
流程控制
对程序执行顺序进行控制的过程,就是流程控制

顺序结构
    系统默认执行,了解
分支解构
		必须熟练掌握
		单向分支
        if 条件表达式
            python代码
            python代码
            python代码
            python代码
    特点:
    当条件满足时,执行if条件下的代码组,如果条件不满足则不执行
    双向分支
			if 条件表达式
				python代码
				python代码
				python代码
				python代码
			else:
				python代码
				python代码
				python代码
				python代码
特点:
    当条件满足时,执行if 条件下的代码组,如果条件不满足则不执行
    双向分支
        if 条件表达式
            python代码
            python代码
            python代码
            python代码
            python代码
        else:
            python代码
            python代码
            python代码
            python代码
    特点:
    当条件满足时,执行if 下的代码组,当条件不满足时,执行else下的代码组
    真区间:if条件下的代码组 if区间
    假区间:else 条件下的代码组 else 区间
    多项分支
        if 条件表达式
            python代码
            python代码
        elif 判断条件:
            python代码
        elif 判断条件:
            python代码
            python代码
        else:
            python代码
            python代码
        特点:
        多项分支执行了一个分支后,其他代码将不再执行
        当一个分支条件被执行后,其他分支将不再执行
        当所if 及 elif 判断条件 都不满足时,执行else区间
    潮装分支
        其他分支结构嵌套使用
        if 判断条件:
            python代码
            python代码
            if 判断条件:
                python 代码
            else:
        else:
            python代码
循环结构
    while 循环

    for ... in 循环

if False:
    print("agh")
if True
    print("sag")

if 条件
    python代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

elif 条件:
    python 代码

else:
    python代码
'''
#
# 猜字游戏
# 有一个默认值10 然后input输入你猜想的值,
# 如果值对,就输入正确答案,
# 如果不对,输入比默认值大 还是比默认值小
#
# 设定一个默认值
# ver = 37
# 输入数字 并转换为整形
# inpvar = int(input("请输入数字:"))
# if var == inpvar:
#     print("恭喜你,答对了,结果是",var)
# elif var < inpvar:
#     print("你猜的数字,稍小")
# #
# # 判断一个数是否能被2整除,同时能被3整除,分别输出不同情况的结果
# # 输入一个数值 19
# num = int(input("请输入数字"))
# if num% 2 == 0:
#     if num % 3 == 0:
#         print(num,"能被2整除,同时能被3整除")
#     else:
#         print(num,"能被2整除,不能被3整除")
# else:
#     if num % 3 == 0:
#         print(num,"不能被2整除,能被3整除")
#     else:
#         print(num,"不能被2整除,不能被3整除")
#
# # # 循环
# #
# # 提升代码复用率,有助于代码后期维护
# # 循环基本格式:
# # # 死循环
# while 判断条件:
#     python代码....
#     python代码....
# 带有判断条件的循环
# 初始化一个技术变量
# while 判断条件:
#     python代码
#     技术变量的自增自减操作
#
# while True:
#     print("今天天气不错,心情挺好的,下午有课")
#
# var = 0
# while var < 10:
#     print(var)
#     var += 1
#
# 用循环写一个十行十列的#
#
# num = 0
# while num < 10:
#     var = 0
#     while var < 10:
#         print("#",end = "")
#         var +=1
#     print()
#     num += 1
# 写一个格列变色 十行十列的星星
# '''
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# ▽▼▽▼▽▼▽▼▽▼
# '''
# 打印十行
# hang = 0
# while hang < 10:
#     lie = 0
#     while lie < 10:
#         if lie % 2 == 0:
#             print("▼",end = "")
#         else:
#             print("▽",end="")
# #         lie += 1
# #     添加换行
# #     print()
# #     hang += 1
# # 十行十列隔行变色
# # var = 0
# while var < 100:
#     print('△',end="")
# #     if var % 10 == 9:
# #         print()
# #     var += 1
#
# # 字符串格式化输出 %
# strs = "今天买了二斤牛肉花了%d元"%200
# print(strs)
# strs = "我给老板%d元,他找给我%d元"%(200,15)
#
# strs = "给对方%-5d暗示法" % 200
# print(strs)
#
#




