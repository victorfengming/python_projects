#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>



# 声明抽象类
# 导入抽象类功能模块
# 指定了开发规则--> 抽象类
import abc
class User(metaclass = abc.ABCMeta):
    # 制作抽象类必须另外指定猿类
    # 添加属性
    id = 999
    # 定义方法

    # 添加用户的方法 -> {小赵}
    # 对象方法 -> 抽象的对象方法
    # 用装饰器进行装饰城为抽象方法
    @abc.abstractmethod
    def user_add(self):
        pass

    # 修改用户的方法 ->{小钱}
    # 把他做成一个抽象的类方法
    # @classmethod
    @abc.abstractclassmethod
    def user_update(self):
        pass

    # 删除用户的方法 ->{小孙}
    # 绑定类的方法
    # 抽象的绑定类的方法
    @abc.abstractmethod
    def user_del(self):
        pass

    # 查找用户的方法 ->{小李}
    # 静态方法
    # 抽象的静态方法
    @abc.abstractstaticmethod
    def user_find():
        pass
    pass

    # 抽象类中的可以有正常的方法 -> 这个是我来完成的
    def user_lock(self):
        print('封禁用户的方法')
        pass



# 小赵的工作
class XZUser(User):
    # 添加用户的方法   对象方法{小赵}
    def user_add(self):
        print('添加用户的方法-小赵完成的')


# 小钱的工作
class XQUser(XZUser):
    # 修改用户的方法   类方法{小钱}
    @classmethod
    def user_update(self):
        print('设置用户的方法-小钱完成的')


# 小孙的工作
class XSUser(XQUser):
    # 删除用用户的方法  绑定类的方法{小孙}
    def user_del(self):
        print('删除用户的方法-小孙完成的')
        pass


# 小李的工作
class XLUser(XSUser):
    # 查找用户的方法   静态方法{小李}
    def user_find():
        print('查找用户的方法-小李完成的')


# 这里可以使用小李的类了
u = XLUser()

u.user_lock()
u.user_add()
XLUser.user_update()
XSUser.user_del()
u.user_find()







'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
