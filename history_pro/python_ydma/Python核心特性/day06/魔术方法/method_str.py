#创建一个类
class Human:
    #成员属性
    color = '黄色'
    sex = '女'
    age = 18
    name = '史珍香'

    #成员方法
    #__str__魔术方法
    def __str__(self):#重载魔术方法__str__（继承自object类的）
        print('str方法被触发')
        return self.name

    def eat(self):
        print('真香~')

    def smile(self):
        print('哇哈哈哈哈哈哈')


#实例化对象
szx = Human()
#打印对象
#print(szx)

#触发__str__第二个时机
str(szx) #类型转换


'''
我打印列表（List类的对象）？给我是真正列表内容
我打印字符串(Str类的对象)，给我的是字符串的内容
'''