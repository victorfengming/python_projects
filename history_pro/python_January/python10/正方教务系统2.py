#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''


# author: HuYong
#-*-coding:utf-8-*-
import os
import re
# from lxml import etree
import requests
import sys
import importlib
#设置编码
importlib.reload(sys)
sys.setdefaultencoding( "utf-8" )
#初始参数
studentnumber = "1030614418"
password = "342626199509064718"
#访问教务系统
s = requests.session()
url = "http://202.195.144.163/jndx/default2.aspx"
response = s.get(url)
# 使用正则表达式获取 __VIEWSTATE
# __VIEWSTATE = re.findall("name=\"__VIEWSTATE\" value=\"(.*?)\"",response.content)[0]
# 使用xpath获取__VIEWSTATE
# selector = etree.HTML(response.content)
# __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
# #获取验证码并下载到本地
# imgUrl = "http://202.195.144.163/jndx/CheckCode.aspx?"
# imgresponse = s.get(imgUrl, stream=True)
# print(s.cookies)
# image = imgresponse.content
# DstDir = os.getcwd()+"\\"
# print(("保存验证码到："+DstDir+"code.jpg"+"\n"))
# try:
#     with open(DstDir+"code.jpg" ,"wb") as jpg:
#         jpg.write(image)
# except IOError:
#     print("IO Error\n")
# finally:
#     jpg.close
# #手动输入验证码
# code = input("验证码是：")
#构建post数据
RadioButtonList1 = "学生".encode('gb2312','replace')
data = {
"RadioButtonList1":RadioButtonList1,
"__VIEWSTATE":__VIEWSTATE,
"TextBox1":studentnumber,
"TextBox2":password,
# "TextBox3":code,
"Button1":"",
"lbLanguage":""
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}
#登陆教务系统
response = s.post(url,data=data,headers=headers)
print("成功进入教务系统！")





















