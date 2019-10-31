#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15469409'
API_KEY = 'ZTnBlD5SIn0muCLKLKUflVWI'
SECRET_KEY = 'xdl7fDgwt5H0nUpuEEwSG62lYa4L5X74'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('picture/text/1.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image, options)

url = "http//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
# result = client.basicGeneralUrl(url, options)
print(result)





















