''''''
#声明一个类
class Human:
    #成员属性
    color = '黄色'
    age = 18
    name = '菊花'

    #成员方法
    #__repr__魔术方法  在通常的类中 repr重载相当于 str也被重载
    def __repr__(self):
        print('repr方法被触发')
        return 'repr返回的数据'

    #所有类默认都存在一个等式
    #__str__ = __repr__  将repr的方法赋值给str方法  完全一样
    #重新定义str魔术方法
    def __str__(self):
        return 'str返回的数据'

    def eat(self):
        print('海鲜真好吃~')

    def drink(self):
        print('啤酒很好喝')

#实例化对象
jh = Human()
#打印对象
print(jh)
#使用repr转换之后进行打印
print(repr(jh))



'''
#repr的应用
mysong = '我\n喜欢\t你'
#正常打印字符串（打印字符串对象）
print(mysong)
print(str(mysong))

#使用repr函数转换并且打印
print(repr(mysong))
'''
'''
mylist = [1,2,3,3,54,5,5]
print(str(mylist))
print(repr(mylist))
'''