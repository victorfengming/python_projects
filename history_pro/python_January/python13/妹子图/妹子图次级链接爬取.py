#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# https://www.mzitu.com/162937

from urllib.request import *
from requests import *
from re import *
from os import *
from random import *

def danye(url):
    response = get(url)
    response = response.text
    rep = findall('<li>.*?target="_blank">.*?target="_blank">(.*?)</a>', response, S)
    picp = findall(r'</a><span><a href="(https://www.mzitu.com/\d{6})"', response, S)
    info = dict(zip(rep, picp))
    # print(info)
    return info


# def baocun(home_info):
#     ml_name = '妹子首页图'
#     # makedirs(ml_name)
#     for file_name,pic_url in home_info.items():
#         print(pic_url)
#         urlretrieve(pic_url,ml_name+'/'+file_name)
#     pass


def inner_page(ori_url):
    # url = ori_url
    response = get(ori_url)
    response = response.text
    ori_pic = findall('<span>(\d\d)</span></a><a.*?><span>',response,S)
    # ori_pic = findall("<span>(\d+)</span></a><a href='https://www.mzitu.com/.*?/2'><span>下一页",response,S)
    end = int(ori_pic[0])

    # print(ori_pic[-1])
    for i in range(2,end+1):
        print(i)
        url = ori_url + '/' +str(i)
        response = get(url)
        response = response.text
        ori_pic = findall('https://i.meizitu.net/(\d\d\d\d.*?)jpg', response, S)
        last_pic = 'https://i.meizitu.net/' + ori_pic[0] + 'jpg'
        print(last_pic)
        pass

# https://i.meizitu.net/2018/12/12c03.jpg
# https://i.meizitu.net/2018/12/12c04.jpg

# url = 'https://www.mzitu.com/'
# url = 'https://www.mzitu.com/page/2/'
ori_url = 'https://www.mzitu.com/page/'
start_page = int(input("请输入起始页数:"))
end_page = int(input("请输入结束页数:"))

for page in range(start_page, end_page + 1):
    # 第一页特殊
    if page == 1:
        url = 'https://www.mzitu.com/'
    else:  # 其他不是第一页的页面
        url = ori_url + str(page) + '/'
    # info为一个俩个元素的元祖,前者是图片标题,第二个是图片的子网页链接
    info = danye(url)
    # print(info)
    for file_name, pic_url in info.items():
        # print(file_name)
        # print(pic_url)
        inner_page(pic_url)
        # urlretrieve(pic_url,file_name)
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

# url = 'https://www.mzitu.com/page/5/'
# danye(url)