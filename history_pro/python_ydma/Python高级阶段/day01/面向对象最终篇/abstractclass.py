'''
关于元类：
'''
'''
#定义一个普通的类？
class Car:
    pass

#查看类的元类1
print(type(Car))
#查看类的元类2
print(Car.__class__)
'''

#声明抽象类
#导入抽象类的功能模块
import abc
class User(metaclass = abc.ABCMeta):#注意制作抽象类必须另外指定元类
    #属性
    id = 999

    #定义方法

    #添加用户的方法     对象方法 -> 抽象的对象方法
    @abc.abstractmethod
    def user_add(self):
        pass

    #修改用户的方法     类方法 -> 抽象的类方法
    @abc.abstractclassmethod
    def user_update(cls):
        pass

    #删除用户的方法     绑定类的方法 - > 抽象的绑定类的方法
    @abc.abstractmethod
    def user_del(self):
        pass

    #查找用户的方法     静态方法 -> 抽象的静态方法
    @abc.abstractstaticmethod
    def user_find():
        pass

    #抽象类中可以有正常的方法
    def user_lock(self):
        print('封禁用户的方法')


#尝试实例化抽象类User
#u = User()


#声明一个类继承User类来使用
class MyUser(User):
    #实现所有抽象类中的方法
    # 添加用户的方法     对象方法
    def user_add(self):
        print('这是一个添加用户的方法')

    # 修改用户的方法     类方法
    @classmethod
    def user_update(cls):
        print('这是一个设置用户的方法')

    # 删除用户的方法     绑定类的方法
    def user_del(self):
        print('这是一个删除用户的方法')

    # 查找用户的方法     静态方法
    @staticmethod
    def user_find():
        print('这是一个查找用户的方法')

#实例化MyUser类
mu = MyUser()
print(mu)

#调用方法
#调用user_lock方法
mu.user_lock()
#调用user_add方法
mu.user_add()
#调用user_update方法
MyUser.user_update()
#调用user_del的方法
MyUser.user_del()
#调用user_find方法
mu.user_find()
