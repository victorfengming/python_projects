#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content('audio/baiduai.aac'),"aac")
# # 识别本地文件
# client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
#     'dev_pid': 1536,
# })




















