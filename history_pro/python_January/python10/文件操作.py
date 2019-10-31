#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

'''
打开文件        打开冰箱门:
    打开模式一共N种：
        普通的:
            w模式 写模式write 文件不存在时会创建文件，如果文件已存在则会清空文件
            r模式 读模式read 文件不存在就报错，存在则准备读取文件
            a模式 追加模式 append 文件不存在则新建，文件存在则在文件末尾追加内容
            x模式 抑或模式 xor 文件存在则报错，文件 不存在则新建文件
        扩展功能:
            b模式 二进制模式 binary 辅助模式不能单独使用
            +模式 增强模式plus 也是辅助模式不能单独使用
        # 扩展功能要和普通功能配合使用,相互组合
        
        组合功能:
            w+ 可读可写文件
            r+ 可读可写可叠加文件
            a+ 可读可写可追加文件
            x+ 可读可写文件
            
            wb 写入bytes类型文件
            rb 读取bytes类型文件
            ab 追加bytes类型文件
            xb 异或bytes类型文件
            
            wb+ 可读可写bytes类型文件
            rb+ 可读可写可叠加bytes类型文件
            ab+ 可读可写可追加bytes类型文件
            xb+ 可读可写bytes类型文件
            
读取文件、写入数据  把大象放冰箱里面
关闭文件        关闭冰箱门


write()函数
格式:
    文件对象.write(文件路径,执行模式,编码)
    
'''
# # 文件操作
#
# # 打开文件(写模式)
# f = open("test.txt","w",encoding="utf-8")
# # 文件内容
# content = "这是一个使用python写入的文件"
# # 写入文件
# f.write(content)
#
# # 打开文件(写模式)
# f = open("test.txt","w",encoding="utf-8")
# # 文件内容
# content = "这是第二次使用python写入的文件"
# # 写入文件
# # c = f.read()
# f.write(content)
# print(type(f))
#
# # 打开文件(读模式)
# f = open("test.txt","r",encoding="utf-8")
# # 文件内容
# content = "这是第二次使用python写入的文件"
# # 写入文件
# c = f.read()
# # f.write(content)
# print(c)

# 打开文件(读模式)
# f = open("test.txt", "r", encoding="utf-8")
# # 文件内容
# # r 模式 光标在文件的开头
# with open("test.txt", "r", encoding="utf-8") as i:
#     print(type(i))
#     con = i.read(10)
#     print(con)
# 将字符串和字节流进行相互转换
#
# encode() 编码 将字符串转换为字节流(Byte流)
# decode() 编码 将字节流(Byte流)转换为字符串
#
#
# read()
# seek()
# tell()
#
# with 语法 启动关闭文件 相当于帮你执行了f.close()
# 文件内容
# r 模式 光标在文件的开头
# readline()
# 返回一个字符串,当不满足一行内容时,输出参数的字符数.当满足一行时,只输出一行内容
# # 格式: 文件对象.readlines(字符数)
# with open("test.txt", "r", encoding="utf-8") as i:
#     print(type(i))
#     con = i.readline(2)
#     print(con,type(con))

# # readlines()
# 返回一个列表,每个元素是每行的内容,参数包括几行返回几行,不够也打印这一行
# # 格式: 文件对象.readlines(字符数)
# with open("test.txt", "r", encoding="utf-8") as i:
#     print(type(i))
#     con = i.readlines(9)
#     print(con,type(con))


# writelines()
# 功能: 将内容是字符串的可迭代对象写入文件中
# 参数: 内容
# with open("test.txt", "w", encoding="utf-8") as i:
#     i.writelines(["jingtiandi","jksahdlkjg"])


# truncate
# 功能: 字符串截取操作,即包括读,也包括写
# 参数: 内容
# 返回截取字节长度
# 光标还在文件开始的位置
with open("test.txt", "r+", encoding="utf-8") as i:
    print("文件的指针位置",i.tell())
    l = i.truncate(5)
    # i.write("324356576")
    print("文件的指针位置",i.tell())
    t = i.read()
    print("文件的指针位置",i.tell())
    i.seek(3)
    print("文件的指针位置",i.tell())
    i.seek(2,0)
    print("文件的指针位置",i.tell())
    # i.seek(2,1)
    # print("文件的指针位置",i.tell())
#
#     print(l)
#     print(t)
# # 查看文件的指针位置











