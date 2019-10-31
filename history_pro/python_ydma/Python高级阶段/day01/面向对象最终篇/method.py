#声明一个类
class Human:
    #成员方法
    #吃方法  ->对象方法
    def eat(self):
        print(self)
        print('这是一个对象方法')

    #喝方法  ->类方法
    @classmethod
    def drink(cls):
        print(cls)
        print('这是一个类方法')

    #玩方法 -> 绑定类的方法
    def play():
        print('绑定类的方法')

    #乐方法 - > 静态方法
    @staticmethod
    def happy():
        print('这是一个静态方法')


#实例化对象 调用方法
ren = Human()
#调用对象方法
#ren.eat()

#调用类方法
#Human.drink()

#调用绑定类的方法
#Human.play()

#调用静态方法
#Human.happy()
#ren.happy()
