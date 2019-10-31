#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<仅仅实现压缩功能,暂时不用图形化界面开发>
#

import zipfile


class Zip_file:
    # 成员属性
    file_list = []
    # depress_list = []


    # 成员方法
    def __init__(self):

        self.main()
    # 添加文件
    def add_file(self):
        print('添加文件')
        ori_path = input('请输入要压缩的文件路径')
        self.file_list.append(ori_path)
        print('添加文件成功!列表如下:')
        for i in self.file_list:
            print(i)
        pass


    # 压缩文件
    def press_file(self):
        print('压缩文件')
        # 目标
        des_path = input('请输入目标路径')
        zp = zipfile.ZipFile(des_path, 'w',zipfile.ZIP_DEFLATED)
        for i in self.file_list:
            zp.write(i,self.get_file_name(i))
        print('压缩文件成功')
        # print('目标文件位置为:')
        # print(res)
        pass


    # 解压文件
    def depress_file(self):
        print('解压文件')
        src_path = input('请输入要解压的文件路径')
        # self.depress_list.append(src_path)
        # zipfile.ZipFile.extractall(src_path)
        # print('解压文件到当前文件夹')
        des_path = input('请输入目标文件路径')
        zp = zipfile.ZipFile(src_path,'r')
        for file in zp.namelist():
            zp.extract(file, self.get_file_name(file))
        else:
            print('解压缩成功')
        zp.close()
        pass


    # 用于获取路径后面的文件名称
    def get_file_name(self,path):
        import os
        new_name = os.path.split(path)[1]
        return new_name


    # 定义逻辑主函数,用于模拟tkinter的操作,简化程序先
    def main(self):
        info = '''
                1.添加文件
                2.压缩文件
                3.解压文件
                0.退出
                '''

        print(info)
        cho = input('请选择:')
        # print('控制逻辑部分')
        if cho == '1':
            self.add_file()
            # self.add_file()
            self.main()
        elif cho == '2':
            self.press_file()
            self.main()
        elif cho == '3':
            self.depress_file()
            self.main()
        elif cho == '0':
            return
        else:
            print('输入有误!重新输入')
            self.main()


z = Zip_file()






'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
