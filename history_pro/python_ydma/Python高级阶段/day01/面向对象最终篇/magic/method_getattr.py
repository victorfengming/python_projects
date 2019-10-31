#声明一个类
class Human:
    #添加成员属性（加入对象）
    def __init__(self):
        self.name = '东方不败'
        self.sex = '男'
        self.age = 18

    #添加成员方法
    #魔术方法
    def __getattr__(self,item):
        #print('getattr方法被触发')
        #print(item)
        #检测用于访问与name相关的信息都返回名称 (name)
        if 'name' in item:
            return self.name


    def eat(self):
        print('一天三顿小烧烤~')

    def drink(self):
        print('喝啤酒~')


#实例化对象
df = Human()
print(df)

#访问对象成员
print(df.name2)