#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 字符集
    # 多种字符的集合就是字符集

# 字符集的发展
'''
第一步:
最早的计算机使用的英文键盘,系统只能识别数字和英文等内容
ascii码: 美国标准信息交换代码
    键盘上的字母,数字,符号

    ascii码
    a - z 97 - 122
    A - Z 65 - 90
    0 - 9 48 - 57
ASCII只能对英文使用

第二步:
 研究了设置每种语言的字符集合
 GB系列的字符集合:支持中文的字符集
    GB2312 包含大多数的中文
    GBK    支持几乎所有的汉字
    BIG5   繁体汉字

同样的内容,在不用的字符集下,占用的存储空间是不同的

第三步:
国际通用字符集UTF
    utf-8 (最常用的)
    utf-16
    utf-32
'''
mystr ='美国'
result = mystr.encode('utf-8')
print(result)

res = result.decode('gbk')
print(res)
















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
