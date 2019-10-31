#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
import os
# os.chdir("")


# # 复制文件
# 1.只读模式, 打开要复制的文件
# 2.追加模式, 打开副本文件

source_file = open("a.txt","r",encoding="utf-8")
dst_file = open("d_bat.txt","a",encoding="utf-8")

# 2,从源文件中读取内容
# 写入到目标文件中

content = source_file.read()
dst_file.write(content)
# 3.关闭源文件和目标文件

source_file.close()
dst_file.close()


















