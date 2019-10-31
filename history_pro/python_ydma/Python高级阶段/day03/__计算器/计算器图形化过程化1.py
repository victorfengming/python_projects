#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# from .. import 花里胡哨

# strr = input('请输入:')
# eval(strr)
import tkinter

root = tkinter.Tk()
root.title('最强计算器')
root.minsize(400,500)

chang = 80
kuan = 60
# 计算器显示内容应该用字符串显示

num = tkinter.StringVar()
num.set(0)

# 创建label显示
label = tkinter.Label(root,textvariable = num,bg = 'white', font = ('黑体',30), anchor = 'e')
label.place(x = 10, y = 10,width = 380, height = 40)

#运算标志(是否按下了运算按钮 True 按了 False没按)
isys = False
# 用于存储运算列表
yslists = []
# 按钮
# 数字按钮操作
def pressno(no):
    # print(no)
    # 全局变量
    global isys
    # 判断用户是否按下了运算按钮
    if isys == True:
        # 按下了运算按钮
        num.set(no)
        # 将运算标志复位
        isys = False
        pass
    else:
        # 没按下运算按钮
        # 判断原始数字是否为0
        oldno = num.get()
        if oldno == '0':
            # 如果界面为0,如果界面不为0
            num.set(no)
        else:
            num.set(num.get()+no)
        # 获取用户按下的数字,显示到界面中
    # 获取界面中的输入内容


# 运算按钮操作
def pressys(ysflag):
    global isys
    # 设置运算被按下的标志
    isys = True

    #将每次运算的操作的信息计入一个列表['22','*','88']
    # result = eval(''.join([''''''']))

    yslists.append(num.get())
    print(yslists)
    # 计算结果
    cal_res()
    # 将下一个字符添加到列表中
    if ysflag == '=':
        yslists.clear()
    # 如果按的是符号
    elif ysflag == 'clear':
        yslists.clear()
        num.set('')
    else:
        yslists.append(ysflag)


# 计算中间结果
def cal_res():
    global yslists
    res = eval(''.join(yslists))
    print(res)
    num.set(res)
    pass
# #

# def cls_contain():
#     # 清除屏幕
#     yslists.clear()
#     num.set('')

# 定义摆放方法
def baifang_num(contain,com_func,x,y):
    btn = tkinter.Button(root,text = contain, command = lambda : com_func(contain))
    btn.place(x = chang*x, y = kuan*y, width = chang, height = kuan)

for i in range(1,10):
    baifang_num(str(i),pressno,x = (i+2)%3, y = 4-(i//3.1))


# 数字0
baifang_num('0',pressno,1,5)

# 数字.
baifang_num('.',pressno,2,5)

# 等号
baifang_num('=',pressys,3,5)

# 加号
baifang_num('+',pressys,3,4)

# 加号
baifang_num('-',pressys,3,3)

# 加号
baifang_num('*',pressys,3,2)

# 加号
baifang_num('/',pressys,3,1)


# 清空
baifang_num('clear',pressys,0,5)

#
# btn2 = tkinter.Button(root,text = '0', command = lambda : pressno('0'))
# btn2.place(x = 70, y = 5*50, width = 70, height = 50)

#
# # 数字.
# btn2 = tkinter.Button(root,text = '.', command = lambda : pressno('.'))
# btn2.place(x = 70*2, y = 5*50, width = 70, height = 50)

#
# #等号
# btneq = tkinter.Button(root,text = '=', command = lambda : pressys('='))
# btneq.place(x = 0, y = 250, width = 70, height = 50)



#
#
# # 数字2
# btn2 = tkinter.Button(root,text = '2', command = lambda : pressno('2'))
# btn2.place(x = 10, y = 50, width = 50, height = 50)
#
#
# # 数字8
# btn8 = tkinter.Button(root,text = '8', command = lambda : pressno('8'))
# btn8.place(x = 240, y = 50, width = 50, height = 50)
#
# #运算
# btnx = tkinter.Button(root,text = 'x', command = lambda : pressys('*'))
# btnx.place(x = 10, y = 250, width = 50, height = 50)
#
# #等号
# btneq = tkinter.Button(root,text = '=', command = lambda : pressys('='))
# btneq.place(x = 240, y = 250, width = 50, height = 50)

# 加入主消息循环
root.mainloop()












'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
