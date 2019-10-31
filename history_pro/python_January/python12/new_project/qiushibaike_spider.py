#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<爬取糗事百科>
from requests import *
from re import *

# url = 'https://www.qiushibaike.com/text/'
# url = 'https://www.qiushibaike.com/text/page/2/'

def page_one(url,page):
    '''
    功能:下载一页的内容
    :return:
    '''

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = get(url, headers=head).text
    # response = Request(url,headers = head)
    content = findall('class="content".*?<span>(.*?)</span>', response, S)

    # print(response)
    # print(content)
    print("-" * 100)
    j = 0
    for i in content:
        j += 1
        res = sub(r'<.*?>', ' ', i)
        res = res.strip()
        print(res)
        print("-" * 150)
        # 存储文件
        with open('糗事百科第'+str(page)+'页.txt','a',encoding='utf-8') as f:
            f.write('-'*42)
            f.write(str(j))
            f.write('-'*42)
            f.write('\n')
            f.write(res)
            f.write('\n')
    pass

def main():
    url = 'https://www.qiushibaike.com/text/page/'
    page_start = int(input("请输入要爬的起始页:"))
    page_end = int(input("请输入要爬的结束页:"))
    for page in range(page_start,page_end + 1):
        url += str(page)
        page_one(url,page)


main()


'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
