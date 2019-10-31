#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<计算器程序>
'''
版本说明:
    实现计算器的基本计算功能
    加入了乘方和地板除按钮
    对图形中的元素按钮进行了等比缩放
    TODO 结构框中的字体大小没有修改
    TODO 面向对象中类的结构层次还是不够清晰
    TODO __init__ 初始化魔术方法 使用不够熟练
'''

# 导入图形化模块
import tkinter

class Calculation:
    # 成员属性

    # 每个按钮的大小
    but_chang = 80
    but_kuan = 60
    win_chang = 400
    win_kuan = 500
    # 运算标志(是否按下了运算按钮 True 按了 False没按)
    isys = False
    # 用于存储运算列表
    yslist = []


    # 成员方法
    # 初始化方法
    def __init__(self):
        self.run_logic()
        pass

    # 数字按钮操作
    def press_num(self,no):
        print(self.yslist)
        # 判断用户是否按下了运算按钮
        if self.isys == True:
            # 按下了运算按钮
            self.num.set(no)
            # 将运算标志复位
            self.isys = False
            pass
        else:
            # 没按下运算按钮
            # 判断原始数字是否为0
            oldno = self.num.get()
            if oldno == '0':
                # 如果界面为0,如果界面不为0
                self.num.set(no)
            else:
                self.num.set(self.num.get() + no)
            # 获取用户按下的数字,显示到界面中
        # 获取界面中的输入内容

        pass

    # 符号按钮操作
    def press_sym(self,ysflag):
        # 设置运算被按下的标志
        self.isys = True

        # 将每次运算的操作的信息计入一个列表['22','*','88']
        # result = eval(''.join([''''''']))

        self.yslist.append(self.num.get())
        print(self.yslist)
        # 计算结果
        self.cal_res()
        # 将下一个字符添加到列表中
        if ysflag == '=':
            self.yslist.clear()
        # 如果按的是符号
        elif ysflag == 'clear':
            self.yslist.clear()
            self.num.set('')
        else:
            self.yslist.append(ysflag)

        pass

    # 结果运算
    def cal_res(self):
        res = eval(''.join(self.yslist))
        # print(res)
        self.num.set(res)
        pass

    # 按钮摆放方法
    def button_put(self,contain,com_func, x, y):
        btn = tkinter.Button(self.root, text=contain, command=lambda: com_func(contain))
        btn.place(relx = (self.but_chang * x ) / self.win_chang, rely = (self.but_kuan * y) / self.win_chang, relwidth = (self.but_chang) / self.win_chang, relheight = (self.but_kuan) / self.win_chang)
    # 整体执行逻辑
    def run_logic(self):

        self.root = tkinter.Tk()
        self.root.title('最强计算器')
        # self.root.minsize(self.win_chang, self.win_kuan)

        # 计算器显示内容应该用字符串显示

        self.num = tkinter.StringVar()
        self.num.set(0)

        # 创建label显示
        label = tkinter.Label(self.root, textvariable = self.num, bg='white', font=('黑体', 30), anchor='e')
        label.place(relx=10/300, rely=10/400, relwidth=380/400, relheight=40/300)

        for i in range(1, 10):
            self.button_put(str(i), self.press_num, x=(i + 2) % 3, y=4 - (i // 3.1))

        # 运算符按钮参数列表
        sym_list = [
            ['0',    self.press_num,1,5],
            ['.',    self.press_num,2,5],
            ['=',    self.press_sym,3,5],
            ['+',    self.press_sym,3,4],
            ['-',    self.press_sym,3,3],
            ['*',    self.press_sym,3,2],
            ['/',    self.press_sym,3,1],
            ['clear',self.press_sym,0,5],
            ['**',self.press_sym,2,1],
            ['//',self.press_sym,1,1],
        ]
            
        for i in sym_list:
            # 数字0
            self.button_put(*i)

        # 加入主消息循环
        self.root.mainloop()


my_cal = Calculation()







'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
