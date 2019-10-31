#__del__魔术方法

class Human:
    #属性
    eye = 2
    skin = 'yellow'


    #方法
    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法')

    #析构方法
    def __del__(self):
        print('del方法被触发')

#实例化一个对象
one = Human()
#将对象同时赋值给另外一个变量
two = one
#print(one)
#主动删除对象
del one #删除变量，系统回收对象
del two

print('=========================')