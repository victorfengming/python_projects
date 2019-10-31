#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


# 定义显示方法
def dis(user1,user2):
    print("\t1 2 3 4 5 6 7 8 9 101112131415")
    for i in range(15):
        print(i+1,end="")
        print("\t",end="")
        for j in range(15):
            # 遍历所有位置,判断是否有下过子
            if [i+1,j+1] in user1:
                print("o ", end="")
                pass
            elif [i+1,j+1] in user2:
                print("e ", end="")
                pass
            # else:
            #     print("  ",end="")
            else:
                print("+ ",end="")
            pass
        print()
    pass
# 定义输入校正方法

def ini():
    while True:
        hang = input("行数:")
        lie = input("列数:")

        if hang.isdigit() and lie.isdigit():
            hang = int(hang)
            lie = int(lie) # 判断输入的字符是不是数字
            # 判断输入的点位置有没有之前下过
            if [hang,lie] in user1 or [hang,lie] in user2:
                print("这个点已经下过了,请重新输入")
            else:
                # 判断输入的数字范围在不在 棋盘空间内
                if hang in range(1,16) and lie in range(1,16):
                    return hang,lie
                else:
                    print("你输入的数值不再棋盘范围内,重新输入")
                pass
        else:
            print("你这输入的也不是数字啊,逗我玩呢啊")
            print("赶紧的,重新输入")
    pass


# 定义判断方法
def win(user):
    # 遍历所有位置坐标
    for hang in range(1,15):
        for lie in range(1,15):
            # 判断 有没有5连子的情况,要是有返回真

            # 竖着5个子连上的情况
            if [hang  ,lie] in user and\
                [hang+1,lie] in user and\
                [hang+2,lie] in user and\
                [hang+3,lie] in user and\
                [hang+4,lie] in user :
                # print("恭喜用户%s赢了,游戏结束"%yonghu)
                return True
                pass
            # 横着5个子连接的情况
            elif [hang ,lie] in user and\
                [hang,lie+1] in user and\
                [hang,lie+2] in user and\
                [hang,lie+3] in user and\
                [hang,lie+4] in user :
                # print("恭喜用户%s赢了,游戏结束"%yonghu)
                return True
                pass
            # 斜着\这么斜的情况
            elif [hang ,lie] in user and\
                [hang+1,lie+1] in user and\
                [hang+2,lie+2] in user and\
                [hang+3,lie+3] in user and\
                [hang+4,lie+4] in user :
                # print("恭喜用户%s赢了,游戏结束"%yonghu)
                return True
                pass
            # 斜着/这么斜的情况
            elif [hang ,lie] in user and\
                [hang-1,lie+1] in user and\
                [hang-2,lie+2] in user and\
                [hang-3,lie+3] in user and\
                [hang-4,lie+4] in user :
                # print("恭喜用户%s赢了,游戏结束"%yonghu)
                return True
                pass
                pass
    return False
    pass

user1 = []  #用于记录用户1的下子信息
user2 = []  #用于记录用户2的下子信息
i = 0   # 用于记录下子的次数
print("-------欢迎使用连珠五子棋程序-------")
print("本游戏需要两名玩家一起玩")
wanjia1 = input("请输入玩家1的名字:")
wanjia2 = input("请输入玩家2的名字:")
print("用户1:o")
print("用户2:e")
dis(user1,user2)    # 先显示一下原始状态
while i<=225:   # 死循环 输入 其实用不着死循环,一共就那么多下
    i += 1      # 累加
    if i%2 :    # 判断出当前的用户
        yonghu = wanjia1
    else:
        yonghu = wanjia2
    print("请玩家%s输入" %yonghu)    #用于提示哪个用户输入
    posi = ini()    # 调用输入校正方法,防止用户下到已经下的位置上
    hang = posi[0]  # 将输入校正方法返回的返回值元祖拆开
    lie = posi[1]

    if yonghu == wanjia1:
        user1.append([hang, lie])   # 将坐标信息添加到对应用户的列表
        pass
    else:
        user2.append([hang, lie])   # 将坐标信息添加到对应用户的列表
        pass
    # 调用显示方法
    dis(user1, user2)
    # 游戏胜负判断
    if win(user1):
        print("五子连珠")
        print("恭喜玩家%s赢了,游戏结束" % yonghu)
        break   # 跳出循环终止程序
    if win(user2):
        print("五子连珠")
        print("恭喜玩家%s赢了,游戏结束" % yonghu)
        break
    # print(user1)  # 调试的时候用,游戏的时候可以隐藏了
    # print(user2)












