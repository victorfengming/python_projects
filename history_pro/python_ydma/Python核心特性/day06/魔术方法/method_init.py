#__init__初始化魔术方法

class Human:
    #属性
    eye = 2
    skin = 'yellow'


    #方法
    #魔术方法__init__
    def __init__(self,kidname,petname):#petname init的形参
        #print('init方法被执行')
        #为对象添加成员
        self.sex = '男'
        self.age = 1
        self.name = kidname
        self.petname = petname #self.petname 对象的成员


    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法')

#实例化一个人的对象
one = Human('邓玉琪','妮妮')#实例化对象 【1.制作一个对象  2.为对象初始化操作】
print(one.__dict__)#打印对象成员

print(one)