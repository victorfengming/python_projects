#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming




from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '15470050'
API_KEY = 'H6iZtu1EvacpGG3FrLxBtWOj'
SECRET_KEY = '3wQQUKcUfUQ63RBxVg8RKhdf4O0aszjO'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
wenjianlujing = "picture/face/1.png"
image = get_file_content(wenjianlujing)
""" 调用通用物体识别 """
result = client.advancedGeneral(image);
print(result)























