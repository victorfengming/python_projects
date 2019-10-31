#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


import requests
# 导入request模块
from urllib import request
import re
# 导入输入参数模块,from方式导入
from input_parameter import *
# *代表所有模块中的属性
# 导入系统模块,创建文件夹
import os
os.makedirs(content)
print()
# 下载1页的内容
def page_one(url):
    # 确定url 向服务器发送请求,获取相应
    # url = 'https://www.qiushibaike.com/text/'
    hearders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    html = requests.get(url, headers=hearders).text
    # print(html)

    # 正则匹配内容
    ret = re.findall('data-sku.*?data-lazy-img=\"(.*?)jpg\"', html, re.S)
    # print(ret)
    j = 0
    for i in ret:
        if j == ting:
            break
        j += 1
        i = i + 'jpg'
        print(i)
        # i = i[]
        i = 'http:' + i
        request.urlretrieve(i, content+'/第' + str(j) + '张图片.jpg')

# 爬取所有内容
def main():
    # url = 'https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2'
    page_one(url)

main()
# 函数调用
# main()

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练

def utf8(a):
	from urllib import request,parse
	# a = input("请输入")
	keyword = {
		"keyword":a
	}
	inp = parse.urlencode(keyword,encoding='utf8')
	return inp


'''
