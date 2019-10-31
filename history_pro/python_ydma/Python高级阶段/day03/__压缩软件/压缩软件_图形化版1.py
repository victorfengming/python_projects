#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<实现压缩功能,用图形化界面开发>
# 暂时实现基础功能,有待完善

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
        self.src_path = tkinter.filedialog.askopenfilename(title='请选择解压文件路径')
        des_path = self.get_file_name(self.src_path)[0]
        # self.des_path = tkinter.filedialog.askdirectory(title='请选择压缩路径')

        # src_path = input('请输入要解压的文件路径')
        # self.depress_list.append(src_path)
        # zipfile.ZipFile.extractall(src_path)
        # print('解压文件到当前文件夹')
        # des_path = input('请输入目标文件路径')
        zp = zipfile.ZipFile(self.src_path,'r')
        for file in zp.namelist():
            print(file)
            zp.extract(file,des_path)
        else:
            print('解压缩到当前文件夹成功')
        zp.close()
        pass


    # 用于获取路径后面的文件名称
    def get_file_name(self,path):
        import os
        new_name = os.path.split(path)
        return new_name


    # # 定义逻辑主函数,用于模拟tkinter的操作,简化程序先
    # def main(self):
    #     info = '''
    #             1.添加文件
    #             2.压缩文件
    #             3.解压文件
    #             0.退出
    #             '''
    #
    #     print(info)
    #     cho = input('请选择:')
    #     # print('控制逻辑部分')
    #     if cho == '1':
    #         self.add_file()
    #         # self.add_file()
    #         self.main()
    #     elif cho == '2':
    #         self.press_file()
    #         self.main()
    #     elif cho == '3':
    #         self.depress_file()
    #         self.main()
    #     elif cho == '0':
    #         return
    #     else:
    #         print('输入有误!重新输入')
    #         self.main()


z = Zip_file()






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
