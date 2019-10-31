'''
#描述符类
#class Descriptor:
    临时变量            自己定义
    __get__             管理获取值
    __set__             管理设置值
    __delete__          管理删除值

'''
#声明一个邮箱类
class Email:

    #成员属性
    #username = '匿名用户'
    isallowdel_username = False#是否允许删除的标志
    password = 1235678

    #成员方法
    #------------描述符使用的区域 start--------------
    #初始化方法
    def __init__(self):
        self.tmpvar = '匿名用户'


    #管理获取的描述符的方法
    def getusername(self): #只有一个self
        #设置相关管理
        result = self.tmpvar[0] + '~' + self.tmpvar[-1]
        return result

    #管理描述符设置的方法
    def setusername(self,val):
        #管理设置操作
        self.tmpvar = val + 'sama'

    #管理描述符删除的方法
    def deleteusername(self):
        #管理删除操作
        if self.isallowdel_username == True:
            del self.tmpvar

    # ------------描述符使用的区域 end--------------

    def login(self):
        print('登陆邮箱的方法')

    def logout(self):
        print('退出邮箱的方法')

    #将成员交接给描述符管理
    username = property(getusername,setusername,deleteusername)

#在类外部实例化对象
mail = Email()

#获取用户名
#print(mail.username)

#设置用户名
#mail.username = '王老五'
#print(mail.username)


#删除用户名
print(mail.username)
del mail.username
print(mail.username)