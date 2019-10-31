#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

# freeimages爬取

from urllib import request
import hashlib, re, random, os

'''
程序说明:
可以爬取freeimages的图片,通过用户输入的关键字搜索
并且保存到本地文件夹
'''


# "class=\"item\".*?<img src=\"(.*?)\""

def utf8(a):
    from urllib import request, parse
    # a = input("请输入")
    keyword = {
        "q": a
    }
    inp = parse.urlencode(keyword, encoding='utf8')
    return inp


def dan(url, j):  # 传入参数为每个页面的url,p为第多少页
    req = request.Request(url)
    rr = request.urlopen(req)
    strr = rr.read().decode('utf-8')
    # 获取图片域名,同上
    tup = re.compile("class=\"item\".*?<img src=\"(.*?)\"", re.S)
    tu = tup.findall(strr)
    # print(tu)
    print()
    os.makedirs(nei)

    i = 0
    # 下载拿到网址的图片到img文件夹
    for item in tu:
        i += 1
        request.urlretrieve(item, "./" + nei + "/" + str(i) + ".jpg")
        print("成功保存第" + str(i) + "张图片:" + item)
        if i >= j:
            break
    print("--保存完毕--")
    pass


list_url = "https://cn.freeimages.com/search/"
biao = '''
┍┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┑
┇  welcome using our product!┇
┕┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┙

'''
print(biao)
nei = input("please input the key word\nwe need a English word:")
num = int(input("how much do you want:"))
# neirong = utf8(nei)
list_url = list_url + nei
dan(list_url, num)
print("-------------------the program is end-------------------")






















