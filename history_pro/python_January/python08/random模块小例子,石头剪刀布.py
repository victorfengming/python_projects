
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 先学一个模块的用法
# 导入模块和包
# python 有很多自带的模块和包是没有自动加载的
import random

# res = random.randint(1,10)
# print(res)

# 猜拳游戏
# 我和计算机进行猜拳游戏
# 输入 拳头 用1表示 剪刀用2表示 布用3表示

# 自己输入猜的拳数,和计算机比较,返回输赢

# 拳头 赢 剪刀
# 剪刀 赢 布
# 布 赢 拳头
#
# import random
# t = ("拳头","剪刀","布")
# while True:
#     user = int(input("猜吧"))
#     computer = random.randint(1,3)
#     print("你猜的是",t[user-1])
#     print("计算机猜的是",t[computer-1])
#     if computer == 1 and user == 2 or\
#             computer == 2 and user == 3 or\
#             computer == 3 and user == 1:
#         print("你输了")
#     elif computer == user:
#         print("平局")
#     else:
#         print("你赢了")
#


# import random
# t = ("拳头","剪刀","布")
# while True:
#     user = input("请输入'拳头'、'剪刀'或者'布':")
#     user = t.index(user)
#     computer = random.randint(0,2)
#     print("计算机猜的是",t[computer])
#     if user-computer == 1 or computer - user == 2:
#         print("你输了,别气馁")
#     elif computer == user:
#         print("平局,再来一把")
#     else:
#         print("你赢了,继续加油")
#     if '结束' == input("选择'继续'或者'结束':"):
#         break
#
# #
# while 1:
#     b =int(input('请输入你要出的拳   拳头 (1)  剪刀(2)   布(3)   按0退出'))
#     a = random.randint(1, 3)
#     if b > 3 or b < 0:
#         print('请输入1-3之间的数字')
#
#     elif b == 0:
#         break
#
#     else:
#         if a == 2 and b == 3:
#             print('剪刀赢了布')
#             print('winner')
#         elif a == 3 and b == 1:
#             print('布赢了拳头')
#             print('winner')
#         elif a == 1 and b == 2:
#             print('拳头赢了剪刀')
#             print('winner')
#         elif a == b:
#             print('平局')
#         else:
#
#             print('lost')
# print('游戏结束')
#


# i=1
# import random
# while i<10:
#     cq=int(input('输入猜拳编号:'))
#     res=random.randint(1,3)
#     if  (cq==1 and res==2)  or (cq==2  and res==3 )  or  (cq==3 and  res==1):
#         print(res)
#         print('我赢')
#     elif (res==1 and  cq==2)  or (res==2 and  cq==3) or (res==3  and  cq==1):
#         print(res)
#         print('计算机赢')
#     else:
#         print(res)
#         print('平局')
#     i+=1



#
#
# while 1:
#     t = ("退出","拳头", "剪刀", "布")
#     user =input("猜拳游戏:请输入拳头\剪刀\布\退出:")
#     user = t.index(user)
#     if user > 3 or user < 0:
#         print('请输入拳头\剪刀\布\退出:')
#     elif user == 0:
#         break
#     else:
#         computer = random.randint(1, 3)
#         print("计算机猜的是", t[computer])
#         if user - computer == 1 or computer - user == 2:
#             print("你输了")
#         elif computer == user:
#             print("平局")
#         else:
#             print("你赢了")
# print('游戏结束')

while 1:
    t = ("退出","拳头", "剪刀", "布")
    user =input("猜拳游戏:请输入拳头\剪刀\布\退出:")
    user = t.index(user)
    if user > 3 or user < 0:
        print('请输入拳头\剪刀\布\退出:')
    elif user == 0:
        break
    else:
        computer = random.randint(1, 3)
        print("计算机猜的是", t[computer])
        if user - computer == 1 or computer - user == 2:
            print("你输了")
        elif computer == user:
            print("平局")
        else:
            print("你赢了")
print('游戏结束')





















