#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<正则表达式>
'''
python正则表达式:
    一个特殊的字符序列,检查一个字符串是否匹配一定的序列模式

re 模块 :提供了正则函数
'''
from re import *
#
# re.match()
#     常识从字符串的开头,起始位置去匹配一个模式,如果其实位置没有成功,返回None,只会匹配一次
# re.search()
#     尝识从整体字符串去匹配一个模式,如果没有成功,返回None,只会匹配一次
# re.findall()
#     匹配多次,并返回一个列表,爬虫中使用的最多的是findall
#
# . 匹配所有除\n
#
# char = 'asfdghk13243546578!@$#%$^%&^*&('
#
# com = re.findall('3',char)
# print(com)
#
# ret = match('\d\d\d\d\d',text,S)
# print(ret.group())
#又懒又贪又笨的大胖子
# text = 'uio我@q132465www.python.org'
# text = 'uio400-987654322@$#%$^hon.org'
# text = '123hee123agf123sdf'
# rul = 'e(\d+)a'
# ret = search(rul,text)
# print(ret.group(1))
# **********************小案例*****************
# 验证手机号
phone_number = '13940206091'
rul = '1[34578]\d{9}'
ret = search(rul,phone_number)
print(ret.group())
# **********************小案例*****************
# 验证身份证号
id_number = '231181209812212331'
ret = search('\d{17}[xX\d]',id_number)
print(ret.group())
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
