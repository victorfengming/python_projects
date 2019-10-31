#声明抽象类 【指定了开发的规则】
#导入抽象类的功能模块
import abc
class User(metaclass = abc.ABCMeta):#注意制作抽象类必须另外指定元类
    #属性
    id = 999

    #定义方法

    #添加用户的方法     对象方法 -> 抽象的对象方法 【小赵】
    @abc.abstractmethod
    def user_add(self):
        pass

    #修改用户的方法     类方法 -> 抽象的类方法    【小钱】
    @abc.abstractclassmethod
    def user_update(cls):
        pass

    #删除用户的方法     绑定类的方法 - > 抽象的绑定类的方法 【小孙】
    @abc.abstractmethod
    def user_del():
        pass

    #查找用户的方法     静态方法 -> 抽象的静态方法   【小李】
    @abc.abstractstaticmethod
    def user_find():
        pass

    #抽象类中可以有正常的方法  【自己】
    def user_lock(self):
        print('封禁用户的方法')


#小赵的工作  [但是可以在一个单独的文件中开发]
class XZUser(User):
    # 添加用户的方法     对象方法 【小赵】
    def user_add(self):
        print('添加用户的方法-小赵完成的')


#小钱的工作[但是可以在一个单独的文件中开发]
class XQUser(XZUser):
    # 修改用户的方法     类方法   【小钱】
    @classmethod
    def user_update(cls):
        print('设置用户的方法-小钱完成的')

#小孙的工作[但是可以在一个单独的文件中开发]
class XSUser(XQUser):
    # 删除用户的方法     绑定类的方法【小孙】
    def user_del():
        print('删除用户的方法-小孙完成的')

#小李的工作[但是可以在一个单独的文件中开发]
class XLUser(XSUser):
    # 查找用户的方法     静态方法 -> 抽象的静态方法   【小李】
    @staticmethod
    def user_find():
        print('查找用户的方法-小李完成的')

#这里可以使用小李的类
u = XLUser()

#调用方法
u.user_lock()
u.user_add()
XLUser.user_update()
XLUser.user_del()
u.user_find()