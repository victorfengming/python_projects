class Person:
    pass
p1 = Person()
p2 = Person()
#不同的对象是不能访问其他对象的属性的
p1.age = 18
p2.address = "深圳"

print(p1.address)#测试验证出错
