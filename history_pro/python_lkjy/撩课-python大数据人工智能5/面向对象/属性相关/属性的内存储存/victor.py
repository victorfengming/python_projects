#类属性的内存存储问题
# 给一个类增加的属性后查看属性:
class Money:
    age = 21
    name = "xiaoming"
#类的dict属性是不能被修改的
#而这个对象中的dict属性是可以被修改的
# Money.__dict__ = {"age" = "男"}
# Money.__dict__["age"] = 20
# print(Money.age)
# print(Money.__dict__)

one = Money()
one.age = 18
one.height = 64
one.high = 185
# #
# # one.age = 19
# # one有一个属性就是__dict__属性，这个属性的值是一个字典，字典里面是键值对
# #对象改属性试试
# #列表
# # 通过one对象访问的就是one的属性__dict__中的字典的值
# one.__dict__ = {"name":'victor',"age":21}
# print(one.__dict__)
# #这样写和上面的效果是一样的
one.__dict__["age"] = 999
print(one.age)
#一般对象可以修改属性，而类的dict属性是不可以修改的