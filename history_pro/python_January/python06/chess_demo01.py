#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

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


def ori_ini():
    while True:
        hang = input("行数:")
        lie = input("列数:")

        if hang.isdigit() and lie.isdigit():

            # 判断输入的字符是不是数字
            hang = int(hang)
            lie = int(lie)
            # 判断输入的点位置有没有之前下过
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


def des_ini():
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

def ju      ():
    global des_hang
    global des_lie
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
            for i in (ori_hang+1,des_hang):
                if [i,ori_lie] in user1 or [i,ori_lie] in user2:
                    break
                    pass
                pass
            else:
                return des_hang,des_lie

        print("车不能这么走,重新输入要到的位置:")
        position = des_ini()
        des_hang = position[0]
        des_lie = position[1]

    pass
def ma      ():
    print("这是马")

    while True:
        if ori_hang == des_hang or ori_lie == des_lie:
            return des_hang,des_lie
        else:
            print("要到的位置:")
            position = des_ini()
            des_hang = position[0]
            des_lie = position[1]

    pass
    pass
def pao     ():
    print("这是炮")
    global des_hang
    global des_lie
    global current_user
    global other_user
    while True:
        if ori_hang == des_hang:
            j = 0
            for i in (ori_lie + 1, des_lie):
                if [ori_hang, i] in current_user or [ori_hang, i] in other_user:
                    j += 1
                    pass
                pass
            if j == 0 :
                return des_hang, des_lie
            elif j == 1 and [des_hang, des_lie] in other_user:
                return des_hang, des_lie

        elif ori_lie == des_lie:
            j = 0
            for i in (ori_hang + 1, des_hang):
                if [i,ori_lie] in current_user or [i,ori_lie] in other_user:
                    j += 1
                    pass
                pass
            if j == 0:
                return des_hang, des_lie
            elif j == 1 and [des_hang, des_lie] in other_user:
                return des_hang, des_lie
            else:
                pass
        print("炮不能这么走,重新输入要到的位置:")
        position = des_ini()
        des_hang = position[0]
        des_lie = position[1]

    pass
    pass
def xiang   ():
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
def shi     ():
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
def bing    ():
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
def shuai   ():
    print("这是帅")
    while True:
        if ori_hang == des_hang or ori_lie == des_lie:
            return des_hang,des_lie
        else:
            print("要到的位置:")
            position = des_ini()
            des_hang = position[0]
            des_lie = position[1]

    pass



def choice_type():

    if current_user.index([ori_hang,ori_lie]) == 0 or current_user.index([ori_hang,ori_lie]) == 1:
        return ju()# 这是个车
        pass
    elif current_user.index([ori_hang,ori_lie]) == 2 or current_user.index([ori_hang,ori_lie]) == 3:
        # print("这是一个马")
        return ma()
        # 这是个马
        pass
    elif current_user.index([ori_hang,ori_lie]) == 4 or current_user.index([ori_hang,ori_lie]) == 5:
        return pao()
        # 这是个炮
        pass
    elif current_user.index([ori_hang,ori_lie]) == 6 or current_user.index([ori_hang,ori_lie]) == 7:
        return xiang()
        # 这是个相
        pass
    elif current_user.index([ori_hang,ori_lie]) == 8 or current_user.index([ori_hang,ori_lie]) == 9:
        return shi()
        # 这是个士
        pass
    elif 10 <= current_user.index([ori_hang,ori_lie]) <= 14:
        return bing()
        # 这是个兵
        pass
    elif current_user.index([ori_hang,ori_lie]) == 15:
        return shuai()
        # 这是个帅
        pass
    else:
        pass
    pass
    pass

i = 0
current_user = user2
other_user = user1

display()
while True:
    print(current_user)
    print(other_user)
    i += 1
    current_user,other_user = other_user,current_user
    postion = ori_ini()
    ori_hang = postion[0]
    ori_lie = postion[1]
    postion = des_ini()
    des_hang = postion[0]
    des_lie = postion[1]

    postion = choice_type()
    des_hang = postion[0]
    des_lie = postion[1]
    current_user[current_user.index([ori_hang, ori_lie])] = [des_hang, des_lie]
    if [des_hang, des_lie] in other_user:
        other_user[other_user.index([des_hang, des_lie])] = [-1,-1]

    display()

















