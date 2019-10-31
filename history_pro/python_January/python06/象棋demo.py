#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
定义两个数组，一个用户一个，列表一个16个元素，二维列表，每个元素存储位置信息，如果被吃掉，位置越界，走子规则在判断验证模块单独验证，输入数之前要加格式验证模块，循环进入win校验模块判断输赢

'''
zili = '''
 0  1  2  3  4  5 6  7  8
0车 马 相 士 将 士 相 马 车
1
2   炮               炮
3兵    兵    兵    兵    兵
4
5
6卒    卒    卒    卒    卒
7   炮               炮
8
9車 馬 象 仕 帅 仕 象 馬 車
'''
# 车车马马炮炮相相士士兵兵帅
# print(zili)
qizi1 = ("车","车","马","马","炮","炮","相","相","士","士","兵","兵","兵","兵","兵","帅")
qizi2 = ("車","車","馬","馬","鞄","鞄","象","象","仕","仕","卒","卒","卒","卒","卒","将")
user1 = [[0,0],[0,8],[0,1],[0,7],[2,1],[2,7],[0,2],[0,6],[0,3],[0,5],[3,0],[3,2],[3,4],[3,6],[3,8],[0,4]]
user2 = [[9,0],[9,8],[9,1],[9,7],[7,1],[7,7],[9,2],[9,6],[9,3],[9,5],[6,0],[6,2],[6,4],[6,6],[6,8],[9,4]]
def display():
    print(" 0 1 2 3 4 5 6 7 8")
    for hang in range(0,10):
        print(hang,end="")
        for lie in range(0,9):
            # print(" ",end="")
            if [hang,lie] in user1:
                chessman = qizi1[user1.index([hang,lie])]
                print("%s"%chessman,end="")
            # print(hang,lie)
            elif [hang,lie] in user2:
                chessman = qizi2[user2.index([hang,lie])]
                print("%s" % chessman, end="")
                # print("#",end="")
            else:
                print("〇",end="")
                pass
        print()
    pass


def ini():
    while True:
        hang = input("行数:")
        lie = input("列数:")

        if hang.isdigit() and lie.isdigit():

            # 判断输入的字符是不是数字
            hang = int(hang)
            lie = int(lie)
            # 判断输入的点位置有没有之前下过
            if [hang,lie] in current_user:
                print("你这不能吃自己的子啊,重新输入")
            else:
                # 判断输入的数字范围在不在 棋盘空间内
                if hang in range(0,10) and lie in range(0,9):
                    return hang,lie
                else:
                    print("你输入的数值不再棋盘范围内,重新输入")
                pass
        else:
            print("你这输入的也不是数字啊,逗我玩呢啊")
            print("赶紧的,重新输入")
    pass

class Chessman:
    def ju      (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是车")
        while True:
            if ori_hang == des_hang :
                for i in (ori_lie+1,des_lie):
                    if [ori_hang,i] in user1 or [ori_hang,i] in user2:
                        break
                        pass
                    pass
                else:
                    return des_hang,des_lie
            elif ori_lie == des_lie :
                for i in (ori_lie+1,des_lie):
                    if [i,ori_lie] in user1 or [i,ori_lie] in user2:
                        break
                        pass
                    pass
                else:
                    return des_hang,des_lie
            else:
                print("车不能这么走,重新输入要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
    def ma      (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是马")

        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
        pass
    def pao     (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是炮")
        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
    def xiang   (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是像")
        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
    def shi     (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是士")
        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
    def bing    (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是兵")
        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass
    def shuai   (self,ori_hang,ori_lie,des_hang,des_lie):
        print("这是帅")
        while True:
            if ori_hang == des_hang or ori_lie == des_lie:
                return des_hang,des_lie
            else:
                print("要到的位置:")
                position = ini()
                des_hang = position[0]
                des_lie = position[1]

        pass


demo = Chessman()


def chess_type():
    global user1
    global user2
    # 判断子力种类,可以返回相应的函数名
    if current_user.index([ori_hang,ori_lie]) == 0 or current_user.index([ori_hang,ori_lie]) == 1:
        demo.ju()# 这是个车
        pass
    elif current_user.index([ori_hang,ori_lie]) == 2 or current_user.index([ori_hang,ori_lie]) == 3:
        # print("这是一个马")
        demo.ma()
        # 这是个马
        pass
    elif current_user.index([ori_hang,ori_lie]) == 4 or current_user.index([ori_hang,ori_lie]) == 5:
        demo.pao()
        # 这是个炮
        pass
    elif current_user.index([ori_hang,ori_lie]) == 6 or current_user.index([ori_hang,ori_lie]) == 7:
        demo.xiang()
        # 这是个相
        pass
    elif current_user.index([ori_hang,ori_lie]) == 8 or current_user.index([ori_hang,ori_lie]) == 9:
        demo.shi()
        # 这是个士
        pass
    elif 10 <= current_user.index([ori_hang,ori_lie]) <= 14:
        demo.bing()
        # 这是个兵
        pass
    elif current_user.index([ori_hang,ori_lie]) == 15:
        demo.shuai()
        # 这是个帅
        pass
    else:
        pass
    pass







display()
# 定义一个计数变量,用于判断当前用户
i = 0
while True:
    print(user1)
    print(user2)
    i += 1
    if i%2 :
        current_user = user1
        other_user = user2
    else:
        other_user = user1
        current_user = user2


    ori_hang = int(input("行"))
    ori_lie  = int(input("列"))

    des = chess_type()
    print("要到的位置:")
    position = ini()
    des_hang = position[0]
    des_lie = position[1]

    des_postion = des()
    des_hang = des_postion[0]
    des_lie = des_postion[1]


    current_user[current_user.index([ori_hang, ori_lie])] = [des_hang, des_lie]
    if [des_hang, des_lie] in other_user:
        other_user[other_user.index([des_hang, des_lie])] = [-1,-1]

    display()












