##万物皆对象
#删除del 类名.属性
#删除不能删除上层的对象
class Money:
    age = 18
    count = 1
    num = 666
one = Money()
print(Money.age)
#通过类来删除
del Money.age
# print(Money.age)
del one.age
print(one.age)
#只能删除自己身上的属性
