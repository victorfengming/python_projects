#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<输入参数,返回一个url编码后的参数>

from urllib.parse import urlencode
content = input("请输入要搜索的关键字:")
ting = int(input("请输入下载图片个数:"))
inp = {
    'keyword':content
}


res = urlencode(inp, encoding='utf8')

print(res)
or_url = 'https://search.jd.com/Search?keyword=口红&enc=utf-8&wq=口红&pvid=8c0619abac2b459a9068a70bb2e92fb5'
url = 'https://search.jd.com/Search?'

url += res

url += '&enc=utf-8'

print(url)











'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
