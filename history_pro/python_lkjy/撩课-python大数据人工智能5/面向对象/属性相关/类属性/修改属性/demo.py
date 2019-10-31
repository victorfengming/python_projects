#修改类属性

class Person:
    sex = '男'
    age = 18
    num = 666
# Person.age = 22
#改了吧，不是直接改的，而是又开辟了一块内存空间 存22 ，然后指向到22
one = Person()
print(Person.age)
one.age = 19
print(one.__dict__)
#赋值语句只会操作自己本身,有就是修改,没有就是新增
print(Person.age)

#xxx是加在one对象的身上的
# print(one.xxx)
# 访问类对象的属性，有两种方式
# 现在能不能通过one来找到age并且修改它
