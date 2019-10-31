#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '15469885'
API_KEY = 'PKk1bfNEuBgl4zyzfNRdldKf'
SECRET_KEY = 'EC5xVDKrtqMwRGHyxLKSKtXKmf8VrVIv'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
wenjianlujing = "picture/cars/2.jpg"
image = get_file_content(wenjianlujing)
""" 调用通用物体识别 """
result = client.advancedGeneral(image);
print(result)




















