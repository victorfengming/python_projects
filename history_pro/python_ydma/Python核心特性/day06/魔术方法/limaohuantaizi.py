#仅供娱乐，没事别玩。
#猴子类
class Monkey:
    pass

#人类
class Human:
    #重载人类的构造方法 用猴子类来做人的对象
    def __new__(cls):
        #使用猴子类代替人类创建对象
        return object.__new__(Monkey)
    pass

#实例化一个人类
ren = Human()
print(ren)


