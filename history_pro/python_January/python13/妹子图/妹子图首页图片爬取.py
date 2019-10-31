#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<爬好看的图片>


from urllib.request import *
from requests import *
from re import *
from os import *
from random import *

def danye(url):
    response = get(url)

    response = response.text

    rep = findall('<li>.*?target="_blank">.*?target="_blank">(.*?)</a>', response, S)
    # <a href="https://www.mzitu.com/166998" target="_blank">甜美尤物徐微微透明睡衣私房照 妩媚红唇诱惑十足</a>
    # print(rep)
    picp = findall(r'https://i.meizitu.net/thumbs/(.*?).jpg', response, S)
    # 打印标题信息
    # for i in rep:
    #     print(i)
    pic = []
    for j in picp:
        j = 'https://i.meizitu.net/thumbs/' + j + '.jpg'
        pic.append(j)
        # print(j)
    info = dict(zip(rep, pic))
    return info


# def baocun(home_info):
#     ml_name = '妹子首页图'
#     # makedirs(ml_name)
#     for file_name,pic_url in home_info.items():
#         print(pic_url)
#         urlretrieve(pic_url,ml_name+'/'+file_name)
#     pass
# url = 'https://www.mzitu.com/'
# url = 'https://www.mzitu.com/page/2/'
ori_url = 'https://www.mzitu.com/page/'
start_page = int(input("请输入起始页数:"))
end_page = int(input("请输入结束页数:"))

for page in range(start_page,end_page+1):
    # 第一页特殊
    if page == 1:
        url = 'https://www.mzitu.com/'
    else:   # 其他不是第一页的页面
        url = ori_url + str(page) + '/'
    # info为一个俩个元素的元祖,前者是图片标题,第二个是图片的子网页链接
    info = danye(url)

    for file_name,pic_url in info.items():
        print(pic_url)
        # urlretrieve(pic_url,file_name)
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
