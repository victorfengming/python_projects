# 声明一个类
class Human:
    sex = '男'
    # 添加成员属性（加入对象）
    def __init__(self):
        self.name = '东方不败'
        self.age = 18

    # 添加成员方法
    #魔术方法
    def __setattr__(self,attrname,value):#相当于在重载object中的__setattr__
        #print('setattr方法被触发')
        #1.禁止修改性别，2.修改名称最多使用三个字符多余的舍弃
        if attrname == 'sex':
            pass
        else:
            object.__setattr__(self,attrname,value)


    def eat(self):
        print('一天三顿小烧烤~')

    def drink(self):
        print('喝啤酒~')


# 实例化对象
df = Human()
print(df.__dict__)
#修改对象成员
df.name = '西门吹雪'
#查看修改之后的信息
print(df.__dict__)


#访问性别
print(df.sex)
#修改性别
df.sex = '女'
print(df.sex)