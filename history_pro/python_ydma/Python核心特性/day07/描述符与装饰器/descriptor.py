# 声明描述符类(道士)
class Descriptor:
    # 初始化一个临时的成员属性（代替原有uername的操作）
    def __init__(self):
        self.tmpvar = '匿名用户'  # 道士手中的布娃娃

    # 定义描述符的三个成员

    def __get__(self, obj, cls):  # self 描述符的对象  / obj Email对象mail  / cls Email类

        # 希望获取用户名的时候仅仅返回第一个字符 其余的都隐藏
        result = self.tmpvar[0] + '*' + self.tmpvar[-1]
        return result

    def __set__(self, obj, val):  # self 描述符的对象   / obj Email对象mail  /val 要设置的值
        # 设置值的时候一定要设置当前描述符对象的临时变量
        # 限制用户名不能超过8个字符
        # 检测字符个数
        if len(val) > 8:
            self.tmpvar = val[0:8]
        else:
            self.tmpvar = val

    def __delete__(self, obj):  # self 描述符的对象/ obj Email对象mail
        # 删除临时变量即可
        if obj.isallowdel_username == True:
            del self.tmpvar


# 声明一个类（邮箱）
class Email:
    # 成员属性
    username = Descriptor()  # 用户名 交给描述符管理 [交接行为]
    # 设置一个是否允许删除username的标志
    isallowdel_username = True
    password = '123456'
    phone = 1234567890

    # 成员方法
    # 登陆
    def login(self):
        print('这是登陆的方法')

    # 退出
    def logout(self):
        print('这是一个退出的方法')


# 实例化对象
mail = Email()
# 访问用户名
# print(mail.username)

# 设置用户名
# mail.username = 'lovemybaby'
# print(mail.username)


# 删除用户名的操作
print(mail.username)
del mail.username
print(mail.username)
