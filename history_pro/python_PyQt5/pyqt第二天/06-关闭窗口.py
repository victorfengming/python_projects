#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>
'''
TODO 要做的可多了
'''
# 关闭一个窗口最直观的方式就是点击标题栏的那个×,这个例子里面
# print(我们展示的是如何用程序关闭一个窗口)
# print(这里我们将解除)到一点single和slots的知识
# 本例子使用的是QPushButton组件类
# QPushButton(string text,Qwidget parent = None)
# text参数是想要显示的按钮名称,parent参数是放在按钮上的组件
# 在我们的例子里面,这个参数是QWidget.应用中的组件都是一层一层(继承而来的)
# 在这个层里,大部分的组件都有自己的父级,没有父级的组件,是顶级的窗口

# 还是tmd要导入对应的包和模块
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QCoreApplication
# 程序需要QtCore对象

# 上来先来一个类
class Example(QWidget):

    # 初始化魔术方法
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('退出就退出',self)
        # 创建一个继承自 QPushButton 的按钮.
        # 第一个参数是按钮的文本,第二个参数是按钮的父级组件
        # 这个例子中,父级组件就是我们创建的继承自QWidget 的 Example 类
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 事件传递系统在PyQt5内建的single和slot机制里面.点击按钮之后,信号会被捕捉并给出既定的反应
        # QCoreApplication包含了事件的主循环,它能添加和删除所有的事件
        # instance()创建 了一个它的实例.
        # QCoreApplication是在QApplication里创建的
        # 点击事件和能终止进程并退出应用的quit函数绑定在了一起.
        # 在发送者和接受者之间建立了通讯,发送者就是按钮,接受者就是应用对象
        qbtn.move(50,50)

        self.setGeometry(300,200,250,150)
        self.setWindowTitle("退出按钮练习")
        # 显示
        self.show()

yingyong = QApplication(sys.argv)
ex1 = Example()
sys.exit(yingyong.exec_())
# 这里创建了一个点击之后就退出窗口的按钮







'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''
