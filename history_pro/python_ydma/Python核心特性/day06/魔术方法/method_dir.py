#声明一个类
class Human:
    #属性
    color = 'yellow'
    hair = '黑色'

    #方法
    def __init__(self):
        self.name = '王老五'
        self.sex = '男'
        self.age = 38


    #魔术方法d
    def __dir__(self):
        #print('dir方法被触发')
        #预先处理对象成员信息，返回值作为dir函数的结果
        #只返回用户定义的成员

        #1.获取所有成员
        allmember = list(self.__dict__) + list(Human.__dict__)
        #2.筛选用户定义成员
        ownmember = [i for i in  allmember if  not i.startswith('__')  and not i.endswith('__')]
        #3.返回结果
        return ownmember

    #吃饭
    def eat(self):
        print('夏天就要吃小龙虾·!')

    #喝水
    def drink(self):
        print('我喜欢喝冰糖雪梨')

#实例化对象
wlw = Human()
#print(wlw)

#dir函数:获取当前对象所有可以访问的成员名称组成的列表
result = dir(wlw)
print(result)