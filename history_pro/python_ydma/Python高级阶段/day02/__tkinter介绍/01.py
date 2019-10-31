#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<tkinter测试>

# 导入tkinter模块
import tkinter

# 创建tkinter的主界面

root = tkinter.Tk()
# 界面出线了一瞬间

# 设置主界面大小
root.minsize(300,300)
# 添加按钮
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack(side = 'left')

btn2 = tkinter.Button(root,text = '按钮2')
btn2.pack(side = 'top')
# 将主页面的显示加入消息循环
root.mainloop()

















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
