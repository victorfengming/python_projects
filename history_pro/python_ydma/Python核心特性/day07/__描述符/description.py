#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 声明描述符类(道士)
class Descriptor:

    # 初始化一个临时成员的属性(代替原有的username的操作)
    def __init__(self):
        self.tmpvar = 'azksd'    # 道士手中的布娃娃
        # 在描述符中要是操作这个对象
    # 定义描述符的三个成员

    def __get__(self, instance, owner):
        # self 描述符对象 instance是 Email 对象/owner Email类本身
        # print('get方法中的self:',self)
        # print('第二个参数',instance)
        # print('第三个参数',owner)

        # 希望获取用户的时候仅仅返回第一个字符 其余的都隐藏
        res = self.tmpvar[0] + '*' + self.tmpvar[-1]
        return res
        pass

    def __set__(self, instance, value):
        # 设置值的时候一定要设置当前描述符对象的临时变量
        # 限制用户名 不能超过8个字符,若超出,截取
        # 检测字符个数
        if len(value) > 8:
            self.tmpvar = value[0:8]
        else:
            self.tmpvar = value
        # self.tmpvar = value
        print(self)
        print(instance)
        print(value)
        pass

    def __delete__(self, instance):
        print(self)
        print(instance)
        # 现在我们希望用户名不能被删除
        # pass就行了
        # del self.tmpvar

        # 删除临时变量
        if instance.isallowed_username == True:
            del self.tmpvar





# 声明一个邮箱类

class Email:


    # 成员属性
    # username = 'xioaming'
    # 实例化一个描述符对象
    username = Descriptor() # 交界行为'
    # 设置一个允许删除username的标志
    password = '12345667'
    phone = 13940206091

    # 成员方法
    # 登录
    def login(self):
        print('这是登录方法')

    # 退出
    def logout(self):
        print('这是一个退出的方法')


# 想要描述,先要选一个成员属性来进行描述/



# 实例化对象
mail = Email()

# 访问用户名
# print(mail.username)

# 设置用户名
# mail.username = 'lovembababbabay'
print(mail.username)

# 访问
print(mail.username)
# 删除用户名的操作

del mail.username

print(mail.username)





'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
