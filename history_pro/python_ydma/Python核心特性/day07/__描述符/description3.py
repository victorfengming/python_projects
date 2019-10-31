#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# class Descriptor:
    # 临时成员 自己定义
    # 临时变量    自己定义
    # __get__    管理获取值
    # __set__    管理设置值
    # __delete__    管理删除值


# 声明一个邮箱类
class Email:


    # 成员属性
    username = '匿名用户'
    password = 1235468

    # 成员方法
    def __init__(self):
        self.tmpvar = '匿名用户```'

    # 直接定义一个方法(将原来的变量变成一个函数)
    @property   # 讲用户名username交给描述符管理{默认用作获取的方法}
    def username(self):
        # 管理获取操作
        result = self.tmpvar[0:3]
        return result
        pass

    @username.setter
    def username(self,val):
        self.tmpvar = val
        pass

    @username.deleter
    def username(self):
        del self.tmpvar
        pass

    def login(self):
        print('登陆邮箱的方法')

    def logout(self):
        print('退出邮箱的方法')


# 实例化对象
mail = Email()

# 获取操作
# print(mail.username)
# #
# # 设置操作
# mail.username = '今生为你偷'

# 删除操作
print(mail.username)

del mail.username

print(mail.username)







'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
