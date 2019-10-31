'''
    临时变量            自己定义     ok
    __get__             管理获取值
    __set__             管理设置值
    __delete__          管理删除值


'''
#声明一个邮箱类
class Email:
    #成员属性
    #username = '匿名用户' #直接注释
    password = 123570

    #成员方法
    def __init__(self):
        self.tmpvar = '匿名用户'

    @property #将用户名username交给描述符管理  【默认用作获取的方法】
    def username(self):
        #管理获取操作
        result = self.tmpvar[0:3]
        return result

    @username.setter
    def username(self,val):#用于设置的方法
        #管理设置操作
        self.tmpvar = val

    @username.deleter
    def username(self):#用于删除的方法
        del self.tmpvar



    def login(self):
        print('登陆邮箱的方法')

    def logout(self):
        print('退出邮箱的方法')


#实例化对象
mail = Email()

#获取操作
#print(mail.username)

#设置操作
#mail.username = '今生为你偷'
#print(mail.username)

#删除操作
print(mail.username)
del  mail.username
print(mail.username)
