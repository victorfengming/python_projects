# 直接上代码
# 不同的方法访问不同的属性
# 属性都要有宿主(不是类就是一个实例)
class Person:

    age = 0     #类属性
    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)     #这回就行了,高不高
    @classmethod        #装饰器,类方法
    def leifangfa(cls):
        print(cls)
        print(cls.age)
        # print(cls.num)
    @staticmethod       #装饰器,静态方法
    def jingtaifangfa():        #在这里面你拿不到实例,所以访问不了实例属性
        #这里面什么多没有
        print("jklsjl")
p = Person()
p.num = 10      #实例属性

p.shilifangfa()
# p.leifangfa()     #baocuo
Person.leifangfa()      #报错
Person.jingtaifangfa()      #行吧

#访问实例属性,只能通过实例
#范文类属性,可以通过类,也可以通过实例
#

# #访问类属性
# print(Person.age)
# print(p.age)
# print(p.age)
#
# #访问实例属性
# print(p.num)

#类找不到实例,实例能找到类,所以只能从下往上找
