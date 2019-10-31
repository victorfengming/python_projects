#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


'''
capitalize()
功能：首字母大写
格式：字符串.capitalize()
返回值：新字符串

title()
功能：将每个单词首字母变为大写
格式：字符串.title()
返回值：新字符串

upper()
功能：将所有字母变为大写
格式：字符串.upper()
返回值：新字符串

lower()
功能：将所有字母变为小写
格式：字符串.lower()
返回值：新字符串

swapcase()
功能：大小写互换
格式：字符串.swapcase()
返回值:新字符串

len()
功能：计算字符串的长度
格式:len(字符串)
返回值：整型

count()
功能：计算指定字符串出现的次数
格式：字符串.count(查找字符串[,开始索引[,结束索引]])
返回值：整数

find()
功能：查找指定字符串第一次出现的位置
格式：字符串.find(查找字符串[,开始索引[,结束索引]])
返回值：整数   找不到返回-1

index()
功能：查找指定字符串第一次出现的位置
格式：字符串.index(查找字符串[,开始索引[,结束索引]])
返回值：整数   找不到抛出错误！

startswith()
功能：检测字符串是否以指定的字符串开头
格式：字符串.startswith(查找字符串)
返回值：布尔值

endswith()
功能：检测字符串是否以指定的字符串结尾
格式：字符串.endswith(查找字符串)
返回值：布尔值

isupper()
功能：检测一个字符串中的英文是否都是大写字母，符号不算
格式：字符串.isupper()
返回值:布尔值

islower()
功能：检测一个字符串中的英文是否都是小写字母，符号不算
格式：字符串.islower()
返回值：布尔值

isalnum()
功能：检测字符串是否由数字，字母和文字等组成
格式：字符串.isalnum()
返回值：布尔值  汉字当作普通字符处理，没有标点和特殊字符就是真，空字符串为false

isalpha()
功能：检测字符串是否有字母和文字组成
格式：字符串.isalpha()
返回值：布尔值，汉字当作普通字母处理。空字符串为false

isdigit()
功能：检测字符串是否由纯数字组成  十进制
格式：字符串.isdigit()
返回值：布尔值

isnumeric()
功能：检测字符串是否是数值字符串  数字整数
格式:字符串.isnumeric()
返回值：布尔值

isdecimal()
功能：检测字符串是否是纯数值字符串组成
格式:字符串.isdecimal()
返回值：布尔值

isspace()
功能：检测字符串是否由空白字符组成
格式:字符串.isspace()
返回值：布尔值

istitle()
功能：检测字符串是否符合title()的结果
格式：字符串.istitle()
返回值:布尔值

---------------------------------------------
split()
功能：将字符串按照指定字符进行切割操作
格式：字符串.split(切割指定字符串)
返回值：列表

splitlines()
功能：将字符串按照换行位置进行切割操作
格式：字符串.splitlines([结束符号])
返回值：列表

join()
功能：将列表中的内容按照指定字符连接成一个字符串
格式:连接字符串.join(列表)
返回值：字符串

zfill()
功能：在原有字符串长度不足指定长度时，用0填充
格式:字符串.zfill(指定长度)
返回值：字符串   不足的长度使用0填满，原来的字符串内容靠右

center()
功能：指定字符串长度，并且使得元字符串内容居中，其余位置使用指定字符填充
格式: 字符串.center(指定长度[，填充字符])
返回值：字符串  填充字符默认空格，可以指定其他

ljust()
功能：指定字符串长度，并且使得元字符串内容靠左，其余位置使用指定字符填充
格式：字符串.ljust(指定长度[，填充字符])
返回值：字符串  填充字符默认空格，可以指定其他

rjust()
功能：指定字符串长度，并且使得元字符串内
格式：字符串.rjust(指定长度[，填充字符])
返回值：字符串  填充字符默认空格，可以指定其他

strip()
功能：去掉左右2侧的指定字符，默认空格
格式:字符串.strip([指定字符])
返回值：字符串

lstrip()
功能：去掉左侧的指定字符，默认空格
格式:字符串.lstrip([指定字符])
返回值：字符串

rstrip()
功能：去掉右侧的指定字符，默认空格
格式:字符串.rstrip([指定字符])
返回值：字符串

maketrans() 和 translate()
maketrans()
    功能：制作用于字符串替换的映射表
    格式: 字符串.maketrans('查找字符','替换字符')    两个字符必须长度相等
    返回值：字典

translate()
    功能：进行字符串替换操作
    格式：字符串.translate(映射表)
    返回值：替换之后的字符串

'''

strr = "python,java,php,c,css,html,mysql"
print(strr)

#首字母大写
result = strr.capitalize()
print(result)

# 标题格式,每个单词的首字母大写strr.title()
result = strr.title()
print(result)

# 转大写
print(strr.upper())

# 转小写
print(strr.lower())

# 相互转换
print(strr.swapcase())

# 求长度
print(len(strr))

# 指定字符串的次数
print(strr.count("h"))

print("find",strr.find("t"))

print("index",strr.index("t"))
print(strr.startswith("pyt"))
print(strr.endswith("pyt"))
print(strr.isupper())
print(strr.islower())
print(strr.isalnum())
print(strr.isalpha())
print(strr.isdigit())
print(strr.isnumeric())
print(strr.isdecimal())
print(strr.isspace())
print(strr.istitle())
print(strr.split())
print(strr.splitlines())
print(strr.join(["32","dg"]))
















