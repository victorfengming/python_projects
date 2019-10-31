#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<仅仅实现图形化压缩功能>
# 扩展内容: 解压文件可以直接解压添加后的列表中的文件
# TODO 压缩文件中暂时没有指定目标文件名称

import zipfile

import tkinter

import tkinter.filedialog
class Zip_file:
    # 成员属性
    file_list = []


    # 成员方法
    def __init__(self):
        self.logic()

    # 控制窗口逻辑
    def logic(self):
        # 创建窗口对象
        root = tkinter.Tk()
        root.minsize(300, 300)
        btn_add = tkinter.Button(root, text='添加文件', command=self.add_file)
        btn_add.grid(row=0, column=0)
        btn_ys = tkinter.Button(root, text='压缩文件', command=self.press_file)
        btn_ys.grid(row=0, column=1)
        btn_jy = tkinter.Button(root, text='解压文件', command=self.depress_file)
        btn_jy.grid(row=0, column=2)


        self.val = tkinter.StringVar()
        self.val.set('暂无文件信息')
        label1 = tkinter.Label(root, textvariable=self.val, bg='pink')
        label1.grid(row=1, column=0, columnspan=3)

        # 加入主消息循环
        root.mainloop()
    # 添加文件
    def add_file(self):
        print('添加文件')
        # 获得需要添加的文件路径列表
        self.file_list = tkinter.filedialog.askopenfilenames(title='请选择要压缩的文件')
        # ori_path = input('请输入要压缩的文件路径')
        # self.file_list.append(ori_path)
        print('添加文件成功!文件列表如下:')
        for i in self.file_list:
            print(i)
        self.val.set('\n'.join(self.file_list))
        pass


    # 压缩文件
    def press_file(self):
        print('压缩文件')
        # 目标
        # 弹出对话框返回压缩路径
        self.des_path = tkinter.filedialog.askdirectory(title='请选择压缩路径')
        print('压缩的路径是:')
        print(self.des_path)
        zp = zipfile.ZipFile(self.des_path+'/demo.zip', 'w',zipfile.ZIP_DEFLATED)
        for i in self.file_list:
            zp.write(i,self.get_file_name(i)[1])
        print('压缩文件成功')
        zp.close()
        pass


    # 解压文件
    def depress_file(self):
        print('解压文件')
        # src_path_list = tkinter.filedialog.askopenfilenames(title='请选择解压文件路径')
        # self.val.set('\n'.join(src_path_list))
        # self.val.set()
        for src_path in self.file_list:
            des_path = self.get_file_name(src_path)[0]
            zp = zipfile.ZipFile(src_path,'r')
            for file in zp.namelist():
                print(file)
                zp.extract(file,des_path)
            else:
                print('解压缩文件%s成功' % src_path)
            zp.close()
        pass


    # 用于获取路径后面的文件名称
    def get_file_name(self,path):
        import os
        new_name = os.path.split(path)
        return new_name



z = Zip_file()






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
