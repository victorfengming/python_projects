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
    # 是否允许删除的标志
    isallowdel_username = False
    # 成员方法
    # ---------------------描述符使用的区域begin---------------------
    # 初始化方法
    def __init__(self):
        self.tmpvar = 'niming匿名用户'

    # 管理获取的描述符的方法
    def get_username(self): # 这里只有一共self就够啦
        return self.tmpvar
        pass

    # 管理描述符设置的方法
    def set_username(self,val):
        # 管理设置操作
        self.tmpvar = val[0] + '*' + val[-1]
        # return self.tmpvar

        pass

    # 管理描述符删除的方法
    def delete_username(self):
        # 管理删除操作
        if self.isallowdel_username == True:
            del self.tmpvar
        pass

    # ---------------------描述符使用的区域end---------------------

    def login(self):
        print('登陆邮箱的方法')

    def logout(self):
        print('退出邮箱的方法')


    # 将成员交给描述符管理
    username = property(get_username,set_username,delete_username)


# 在类的外部实例化对象
mail = Email()

# 获取用户名
print(mail.username)

# 设置用户名
mail.username = '王老五'
print(mail.username)

del mail.username
print(mail.username)












'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
