# #类属性会被各个对象所共享
# 类属性 通过类的多个对象都访问属性 一旦类对象被改变,对象在访问也会对应修改了
class Money:
    age = 18
    name = "xiuaomign"
one = Money()
two = Money()

print(one.age)
print(two.age)

Money.age = 20      #修改类的属性

print(one.age)
print(two.age)


