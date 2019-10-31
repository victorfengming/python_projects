#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


from urllib.request import *
from requests import *
from re import *
from os import *
from random import *

def all_using(ori_url,link_rules,title_rules):
    '''
    gongnengfanhui
    功能返回一个匹配到的结果url

    :param ori_url:
    :param rules:
    :return:
    '''
    response = get(ori_url)
    response = response.text
    rep = findall(title_rules, response, S)
    picp = findall(link_rules, response, S)
    info = dict(zip(rep, picp))
    # print(info)
    return info



#
# def save_file():
#     '''
#     保存文件
#     :return:
#     '''











'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
