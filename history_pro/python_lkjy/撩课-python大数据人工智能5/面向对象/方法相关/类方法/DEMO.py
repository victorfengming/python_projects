class Person:
    # def __trunc__(self):#自动帮我们不全一个参数
    #     pass
    @classmethod
    def leifangfa(cls,a):
        print("这是一个类方法",a)

a = Person.leifangfa
def log(x):
    print("扩展内容1")
    return x;
# a(5)
a = log(a)
# a(9)

def ini(x):
    print("扩展内容2")
    return x

a = ini(a)
a(45)