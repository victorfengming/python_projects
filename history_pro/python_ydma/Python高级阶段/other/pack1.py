#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

import tkinter

root = tkinter.Tk()

root.minsize(300,300)

btn1 = tkinter.Button(root,text = '按钮1')
#529
# padx,pady 设置组件摆放时候和其他组件的间距

btn1.pack(fill = 'x')

btn2 = tkinter.Button(root,text = '按钮2')
btn2.pack(pady = 10,ipadx = 20,ipady = 20)


root.mainloop()















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
