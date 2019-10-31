'''
#issubclass
class Father(object):
    pass

class Son(Father):
    pass

result = issubclass(Son,object)
print(result)
'''


'''
#isinstance

class Monkey:
    pass

class Human:
    pass

ren = Human()

result = isinstance(ren,(Monkey,Human))
print(result)
'''

'''
#hasattr()
class Human:
    #成员属性
    age = 1
    sex = 'man'

    #成员方法
    def cry(self):
        print('555555')

#对类进行成员检测
result = hasattr(Human,'smile')
print(result)

#实例化对象
ren = Human()
result = hasattr(ren,'age')
print(result)
'''

'''
#getattr()
class Monkey:
    #属性
    age = 10
    sex = '雄'
    color = 'golden'

    #方法
    def say(self):
        print('叽叽叽叽~')

#实例化对象
houzi = Monkey()

#获取猴子的颜色
#print(houzi.color)#语法方式

#result = getattr(houzi,'color')#函数方式
#print(result)

#获取不存在的成员
#print(houzi.name)
result = getattr(houzi,'name','小猴子~')
print(result)
'''

'''
#setattr()
class Monkey:
    #属性
    age = 10
    sex = '雄'
    color = 'golden'

    #方法
    def say(self):
        print('叽叽叽叽~')

#实例化对象
houzi = Monkey()
print(houzi.__dict__)

#设置对象成员
#houzi.name = '小悟空'#语法方式
#houzi.color = '黑色'

setattr(houzi,'weight','100斤')#函数方式

print(houzi.__dict__)
'''

#delattr()
class Monkey:
    #属性
    age = 10
    sex = '雄'
    color = 'golden'


    #方法
    def __init__(self):
        self.name = 'xwk'
        self.height = 100

    def say(self):
        print('叽叽叽叽~')


#实例化对象
houzi = Monkey()

print(houzi.__dict__)
#del houzi.name #语法方式
delattr(houzi,'height')
print(houzi.__dict__)
