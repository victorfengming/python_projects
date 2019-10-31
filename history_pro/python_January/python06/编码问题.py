#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming
'''
# 字符集:多种字符的集合
# 字符的发展:
第一步:
    最早的计算机使用的英文键盘,系统只能识别数字和英文等内容
ASCII码:推行了一个ASCII吗,美国标准信息交换码
    键盘上字母,数字,符号
第二步:
    研究了设置每种语言的字符集
第三步:
    国际通用字符集UTF
    utf-8
    utf-16
    utf-32


'''

mystr = "声明"
result = mystr.encode("utf-8")
print(result)
res = result.decode("utf-8")

print(res)














