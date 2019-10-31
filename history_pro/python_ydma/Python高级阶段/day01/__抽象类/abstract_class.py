#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

'''
class Car:
    pass



# 查看一个类的猿类1
print(type(Car))
# 查看一个类的猿类2
print(Car.__class__)

'''

# 声明抽象类
# 导入抽象类功能模块
import abc
class User(metaclass = abc.ABCMeta):
    # 制作抽象类必须另外指定猿类
    # 添加属性
    id = 999
    # 定义方法

    # 添加用户的方法
    # 对象方法 -> 抽象的对象方法
    # 用装饰器进行装饰城为抽象方法
    @abc.abstractmethod
    def user_add(self):
        pass

    # 修改用户的方法
    # 把他做成一个抽象的类方法
    # @classmethod
    @abc.abstractclassmethod
    def user_update(self):
        pass

    # 删除用户的方法
    # 绑定类的方法
    # 抽象的绑定类的方法
    @abc.abstractmethod
    def user_del(self):
        pass

    # 查找用户的方法
    # 静态方法
    # 抽象的静态方法
    @abc.abstractstaticmethod
    def user_find():
        pass
    pass

    # 抽象类中的可以有正常的方法
    def user_lock(self):
        pass
# 只要有一个抽象的方法就是抽象类


# 常是实例化抽象类User

# u = User()
'''
TypeError: Can't instantiate abstract class User with abstract methods user_add, user_del, user_find, user_update
'''

# 声明一个类 继承 User 类 来使用
class Myuser(User):
    # 实现所有抽象类中的方法
    # 添加用户的方法

    # 添加用户方法
    # 对象方法 -> 抽象的对象方法
    def user_add(self):
        print('这是一个添加用户的方法')
        pass

    # 修改用户的方法
    # 把他做成一个抽象的类方法
    @classmethod
    # @abc.abstractclassmethod
    def user_update(self):
        print('这是一个设置用户的方法')
        pass

    # 删除用户的方法
    # 绑定类的方法
    # 抽象的绑定类的方法
    # @abc.abstractmethod
    # @staticmethod
    def user_del():
        print('这是一个删除用户的方法')
        pass

    # 查找用户的方法
    # 静态方法
    @staticmethod
    # 抽象的静态方法
    # @abc.abstractstaticmethod
    def user_find():
        print('这是一个查找用户的方法')
        pass
    pass

    # 抽象类中的可以有正常的方法
    def user_lock(self):
        print('这是一个封禁用户的方法')
        pass
    pass


mu = Myuser()

print(mu)

# 调用方法
# 调用userlock方法
mu.user_lock()
# 调用user_add 方法
mu.user_add()
# 调用设置类的方法
# 这是一个类方法,所以需要用类来调用
Myuser.user_update()
# 调用删除用户的方法
Myuser.user_del()
# 调用查找用户的方法
mu.user_find()

# 这么折腾有啥用
# 有个卵用

# 抽象类可以在你实现功能前,将你的对应的方法信息来先写进去,方便于多人开发


# 多态是一种设计思想 而非是一种语法
# 不同的数据库 传入进来 都能够进行增删改查操作
'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
