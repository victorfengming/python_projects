#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming


#
# 字典专用函数
# clear()
#
# 功能：清空字典
# 格式：字典.clear()
# 返回值：None
# 注意：直接改变原有字典
# copy()
#
# 功能：复制字典
# 格式：字典.copy()
# 返回值：新的字典
# fromkeys()
# 使用指定的序列作为键创建字典
# 功能：使用指定的序列作为键创建字典
# 格式：字典.fromkeys(序列,值)
# 返回值：字典
# get()
#
# 功能：根据键获取指定的值
# 格式：字典.get(键[，默认值])
# 返回值:值
# 注意:如果键不存在，则使用默认值,如果没有默认值则返回None
# items()
#
# 功能：将字典的键值转化成类似元组的形式方便遍历
# 格式：字典.items()
# 返回值：类似元组的类型
# keys()
#
# 功能：将字典的所有键组成一个序列
# 格式：字典.keys()
# 返回值:序列
# values()
#
# 功能：将字典的所有值组成一个序列
# 格式：字典.values()
# 返回值：序列
# pop()
#
# 功能：移除字典中指定的元素
# 格式：字典.pop(键[,默认值])
# 返回值：被移除的键对应的值
# 注意：如果键不存在，则报错，如果键不存在，默认值设置，则返回默认值
# popitem()
#
# 功能：移除字典中的键值对,官方说是随机删除,其实是删除最后一个
# 格式：字典.popitem()
# 返回值：键值对组成的元组
# 注意：弹一个原字典就少一个，字典为空就不可以弹出，会报错
# setdefault()
#
# 功能：添加一个元素
# 格式：字典.setdefault(键,值)
# 返回值:None
# 注意：添加是键存在则不进行任何操作，键不存在则添加，添加是不写值，默认None值
# update()
#
# 功能：修改字典中的值
#
# 方式1：
#     格式： 字典.update(键=值)
#     返回值：None
#     注意:此处的键作为关键字参数使用，不可以添加''
#
# 方式2：
#     格式: 字典.update({键:值})
#     返回值：None
#


# 定义一个字典
# dictvar = {1:"知乎",2:"今日头条",3:"百度网盘",4:"安全卫士",5:"网易云",6:"腾讯",7:"阿里"}
#
# # dictvar.clear()
# # newdict = dictvar.copy()
# # newdict = dictvar.fromkeys([3,4,5,6,7,8,9],["zhu","sakjg","dgw","gw","sdhw","sdhg","dhgw"])
# newdict = dictvar.fromkeys([3,4,5,6,7,8,9],"z")
# print(newdict)
#
#
# result = dictvar.get(3)
# print(result)
#
# yuanz = dictvar.items()
# print(type(yuanz))
#
# # 键和值转换为元组形式,组成一个新的字典,不i对,组成的是字典的item类型
# xuli = dictvar.keys()
#
# print(xuli,type(xuli))

# fromkeys 这个方法有点儿瑕疵,参数dict没jier用啊
# d = [1,2,3]
# dict1 = {"吉林":"长春","黑龙江":"哈尔滨"}
# dict=dict1.fromkeys(d)
# print(dict)                          #{1: None, 2: None, 3: None}
# dict=dict.fromkeys(d,'xiaodeng')    #xiaodeng为默认值
# print(dict)                          #{1: 'xiaodeng', 2: 'xiaodeng', 3: 'xiaodeng'}


# dictvar = {1:"知乎",2:"今日头条",3:"百度网盘",4:"安全卫士",5:"网易云",6:"腾讯",7:"阿里"}


dictvar = {"1":"知乎","t":"今日头条",3:"百度网盘",4:"安全卫士",5:"网易云",6:"腾讯",7:"阿里"}
# print(id(dictvar))
# dictvar.clear()
# print(id(dictvar))
# print(dictvar[8])

dictvar.update(t="斗鱼")
print()
# fromkeys()
# print(dictvar,id(dictvar))
# new = dictvar.fromkeys([3,5,6,8,31],"asdhjkg")
# print(new,id(new))























