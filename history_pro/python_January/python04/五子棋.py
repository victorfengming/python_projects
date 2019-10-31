#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


# 定义显示方法
def dis(user1,user2):
    print("    1 2 3 4 5 6 7 8 9 101112131415")
    for i in range(15):
        print(i+1,end="")
        print("\t",end="")
        for j in range(15):

            if [i+1,j+1] in user1:
                print("○ ", end="")
                pass
            elif [i+1,j+1] in user2:
                print("□ ", end="")
                pass
            else:
                print("+ ",end="")
            pass
        print()
    pass
# 定义输入校正方法
def ini():
    while True:
        hang = int(input("行数:"))
        lie = int(input("列数:"))
        if [hang,lie] in user1 or [hang,lie] in user2:
            print("这个点已经下过了,请重新输入")
        else:
            if hang in range(1,16) and lie in range(1,16):
                return hang,lie
            else:
                print("你输入的数值不再棋盘范围内,重新输入")
            pass
    pass


user1 = []
user2 = []
corr1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
corr2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# hanglist1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0
dis(user1,user2)
while True: # 死循环 输入
    i += 1
    if i%2 :
        yonghu = 1
    else:
        yonghu = 2
    print("请用户%d输入" %yonghu)
    posi = ini()
    hang = posi[0]
    lie = posi[1]

    if yonghu == 1:
        user1.append([hang, lie])
        pass
    else :
        user2.append([hang, lie])
        pass
    # else:
    #     print("错了")
    if yonghu == 1:
        corr1[hang].append(lie)
        for j in range(16):
            corr1[j].sort()
            print(len(corr1[j]))
            # if len(corr1[j])==5 and corr1[j][-1]-corr1[j][0]==5
            # print(len(corr1[j]))
            # if len(corr1[j]) == 5 :
            #     print("成了")
            #     break
    else:
        corr2[hang].append(lie)
        for j in range(16):
            corr2[j].sort()
            print(len(corr2[j]))
    # 调用显示方法
    dis(user1, user2)
    print(user1)
    print(user2)
    print(corr1)
    print(corr2)
# 判断胜负
# for i in user1:
#     i[0]
# 如何排序???7

# 在第三行将列的数值存下来,判断列表的数量是不是大于5,并且最大值减最小值是不是等于长度减一













