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
    for hang in range(0,10):
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


class Rule():
    def ju(self):
        if [destination_hang,destination_lie] in user1:
            pass
        pass
    def ma(self):
        pass
    def pao(self):
        pass
    def shi(self):
        pass
    def xiang(self):
        pass
    def bing(self):
        pass
    def jiang(self):
        pass


def walking_rules():
    pass
display()
# 定义一个计数变量,用于判断当前用户
i = 0
while True:
    i += 1
    if i%2 :
        yonghu = 1
    else:
        yonghu = 2


    original_hang = int(input("行"))
    original_lie  = int(input("列"))


    destination_hang = int(input("要到的行"))
    destination_lie  = int(input("要到的列"))

    user1[user1.index([original_hang,original_lie])] = [destination_hang,destination_lie]
    # user2[user2.index([original_hang,original_lie])] = [destination_hang,destination_lie]
    display()












