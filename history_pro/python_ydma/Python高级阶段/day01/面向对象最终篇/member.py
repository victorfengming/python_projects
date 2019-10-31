#声明一个类
class Animal:
    pass

#声明一个类
class Action:
    pass

#声明一个类
class Human(Animal,Action):
    '''
    这是类的文档
    成员    信息
    成员    信息
    成员    信息~
    成员    信息
    '''
    #成员属性
    sex = 1
    age = 18
    color = 'yellow'

    #成员方法

    def smile(self):
        print('哈哈哈哈哈')

    def cry(self):
        print('呜呜呜呜~~')

#实例化对象
ren = Human()

#__dict__
#print(Human.__dict__)
#print(ren.__dict__)

#__doc__
#print(Human.__doc__)

#__name__
#print(Human.__name__)

#__module__
#print(Human.__module__)

#__bases__
print(Human.__bases__)