#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<仅仅实现压缩功能,暂时不用图形化界面开发>
# 本次加入了提示弹窗的功能

# 在添加文件的时候,不能追加添加,添加多次的结果就是最后一次选中的文件(以完善)
# 类的使用,在类的成员方法中可以使用类中的成员属性,而不需要考虑变量的作用域的问题
# 只需要在变量前面加上一个self的对象本身调用
# 进行实例化类的同时,执行了__init__ 初始化方法
# 并在__init__方法中 调用控制函数 进行其他方法的执行,并加入了tkinter的图形化操作

# TODO 1.重复文件列表处理(完成)
# TODO 2.移除文件列表实现(完成)
# TODO 3.压缩包文件名需要用户输入(完成)
# TODO 4.压缩包文件名需要用户输入(完成)




import zipfile

import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.simpledialog



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
        btn_jy = tkinter.Button(root, text='清空列表', command=self.clear_file)
        btn_jy.grid(row=2, column=0)


        self.val = tkinter.StringVar()
        self.val.set('暂无文件信息')
        label1 = tkinter.Label(root, textvariable=self.val, bg='pink')
        label1.grid(row=1, column=0, columnspan=3)

        # 加入主消息循环
        root.mainloop()

    def clear_file(self):
        self.file_list.clear()
        self.val.set('暂无文件信息!')
    # 添加文件
    def add_file(self):
        print('添加文件')
        # 获得需要添加的文件路径列表
        file_name_temp = list(tkinter.filedialog.askopenfilenames(title='请选择要压缩的文件'))
        self.file_list += file_name_temp
        file_set = set(self.file_list)
        file_set_list = list(file_set)
        # ori_path = input('请输入要压缩的文件路径')
        # self.file_list.append(ori_path)
        tkinter.messagebox.showinfo('提示', '文件添加成功,可在列表中查看')
        # print('添加文件成功!文件列表如下:')
        for i in file_set:
            print(i)

        self.val.set('\n'.join(file_set_list))
        pass


    # 压缩文件
    def press_file(self):
        print('压缩文件')

        # 目标
        # 弹出对话框返回压缩路径
        self.des_path = tkinter.filedialog.askdirectory(title='请选择压缩包保存的路径')
        print('压缩的路径是:')
        print(self.des_path)
        # 提示输入压缩文件名
        file_name = tkinter.simpledialog.askstring(\
            title='获取信息', prompt='给你的新压缩包起个名字吧', initialvalue='demo')
        file_name = file_name + '.zip'
        print(file_name)
        zp = zipfile.ZipFile(self.des_path+'/'+file_name, 'w',zipfile.ZIP_DEFLATED)
        for i in set(self.file_list):
            zp.write(i,self.get_file_name(i)[1])
        else:
            tkinter.messagebox.showinfo(\
                '提示', '压缩文件%s保存成功' % self.des_path+'/'+file_name)
        # print('压缩文件成功')
        zp.close()
        pass


    # 解压文件
    def depress_file(self):
        print('解压文件')
        src_path_list = tkinter.filedialog.askopenfilenames(title='请选择解压文件路径')
        # des_path = self.get_file_name(self.src_path)[0]
        # 这里测试出一个bug
        # 如果用户没有添加文件,而直接点击了解压文件按钮
        # TODO 应该提供一个提示信息

        for src_path in src_path_list:
            des_path = self.get_file_name(src_path)[0]
            zp = zipfile.ZipFile(src_path,'r')
            for file in zp.namelist():
                print(file)
                zp.extract(file,des_path)
            else:
                tkinter.messagebox.showinfo('提示', '解压缩文件%s成功' % src_path)
                # print()
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
