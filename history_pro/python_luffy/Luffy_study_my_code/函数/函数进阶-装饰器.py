# 这节内容就是比较nb啦
# 首先他有三集的内容
# 假如的是一加视频网站的后端开发工程师，你们的网站有以下的几个板块
'''
def home():
    print("---首页---")

def america():
    print("---欧美专区---")

def japan():
    print("---日韩专区---")

def henan():
    print("---河南专区---")
'''
# 视频刚上线，为了吸引客户，你们采用了免费开放的服务，但是一段时间之后他那个要赔钱了
# 所以需要加一个验证，只有VIP才能看了，加一个模块开进行认证
# 优酷现在都没有挣钱，视频费用是非常昂贵的，专享带宽，才被阿里收购了
# 谴责一下那些看盗版视频的，都不容易，还是冲冲会员吧
# 现在你家这个网站，其中欧美和河南专区比较受欢迎，需要加一个认证模块
# 如果是vip让你看，否则，看不了
# 你思考了一下，想了想，单独整出来一个模块，轻松的实现了这个功能
# 但是后来发现：有点瑕疵
#     有啥瑕疵呢？
# 看傲：

user = False #首先呢 定义一个布尔类型的变量 用于存放用户是否验证成功

def login(func):
    def inner():
        print("登录模块")
        _username = "victor"
        _password = "123456"
        global user

        if user == False:
            username = input("请输入用户名：")
            password = input("请输入密码：")

            if username == _username and password == _password:
                print("welcome you are login")
                user = True
            else:
                print("wrong username or password")
        # else:
        #     print("用户已登录，验证通过...")
        if user == True:
            func()
    return inner


def home():
    print("---首页---")

def america():
    print("---欧美专区---")

def japan():
    print("---日韩专区---")
@login #这个@加函数名，就相当于 henan = login（henan）且不会再赋值时运行函数模块
def henan():
    print("---河南专区---")
# henan = login(henan)
# america()
henan()

