# # 类,类产生的对象
# # 在python里面,万物皆对象,所以一个类也是一个对象,他也能够添加一个属性
# #该怎么样让一个类拥有一个属性
# class Money:
#     pass
#
# one = Money()
# one.age = 10 #增加属性
#
# one.age = 18 #修改属性
# Money.count = 1
# Money.age = 18
# Money.num = 666
# print(Money.count)
# print(Money.__dict__)
# #键值对儿
#
class Money:
    age = 18    #给一个类添加属性的方式2
    count = 1   #以后我们常用的就是这种方式
    num = 666   #这个有点儿像C语言中的结构体
print(Money.age)
print(Money.count)
print(Money.num)
print(Money.__dict__)