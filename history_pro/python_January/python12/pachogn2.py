#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<分页>

import requests
import re
import os


# 下载1页的内容
# 确定url 向服务器发送请求,获取相应
def main():
    url = 'https://www.qiushibaike.com/text/page/'
    page_k = int(input("请输入起始页数:"))
    page_e = int(input("请输入结束页数:"))
    for page in range(page_k,page_e+1):
        url += str(page)
        page_one(url,page)

def page_one(url,page):
    hearders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    html = requests.get(url,headers = hearders).text
    # print(html)

    # 正则匹配内容
    ret = re.findall(r'<div class="content">.*?<span>(.*?)</span>',html,re.S)
    print(ret)
    i = 0

    os.makedirs('糗事百科'+str(page))
    # ret = re.sub(r'<.*?>','',ret)
    for content in ret:
        i += 1
        x = re.sub(r'<.*?>','',content)
        # print(x.strip())  # 默认去掉首尾两边的空格和换行
        x = x.strip()
        # 存储到文件中
        # 创建文件夹
        # os.mkdir()
        file_name= '糗事百科'+str(page)+'/糗事百科'+str(page)+'.txt'
        with open(file_name,'a',encoding='UTF-8') as f:
            f.write('-'*40)
            f.write(str(i))
            f.write('-'*40)
            f.write('\n')
            f.write(x)
            f.write('\n')


# # 爬取所有内容
# def main():
#     for x in range(1,14):
#         url = 'https://www.qiushibaike.com/text/page/%d/' % x
#         page_one(url)

#函数调用
main()














'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
