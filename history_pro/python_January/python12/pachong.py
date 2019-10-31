#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


from re import *
from requests import *
from urllib import request
#1.物色对象(确定url的目标)

url = 'http://economy.southcn.com/e/node_321237.htm'
#2.下手攻击(发送请求,GET方式请求,byes)构造一个user_agent

# response = get(url,headers = headers)
req = Request(url)
rr = urlopen(req)
strr = rr.read().decode('utf-8')
print(strr)
# response = get(url)

#3.等待回复嘿嘿嘿(读取响应数据)
# response = response.text
# print(response)
#
# # 转码
# strr = response.read().decode('utf-8')

#4 正则表达式筛选
res = findall("class=\"itm j-link.*?target=\"_blank\">(.*?)</a></h3>",strr)

# print(res)

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
