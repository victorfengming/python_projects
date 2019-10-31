#声明一个类
class Human:
    #属性
    color = 'yellow'
    hair = '黑色'
    #方法
    def __init__(self):
        #性名
        self.name = '王老五'
        #性别
        self.sex = '男'
        #年龄
        self.age = 38

    #魔术方法  （重载了继承自object类的删除成员的方法）
    def __delattr__(self,attrname):
        #print('delattr被触发')
        #print(attrname,type(attrname))

        #添加一个判断，判断是否允许删除成员
        if attrname == 'sex':
            pass
        else:
            #调用object类的删除成员方法(最原始的操作)
            object.__delattr__(self,attrname)



    #吃饭
    def eat(self):
        print('夏天就要吃小龙虾·!')

    #喝水
    def drink(self):
        print('我喜欢喝冰糖雪梨')


#实例化对象
wlw = Human()
print(wlw.__dict__)


#删除对象的成员属性
#名字
del wlw.name

#性别(禁止删除性别)
del wlw.sex
#年龄
del wlw.age

print(wlw.__dict__)
