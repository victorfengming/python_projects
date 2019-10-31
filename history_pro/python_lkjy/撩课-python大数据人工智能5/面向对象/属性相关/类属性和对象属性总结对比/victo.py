#类属性和对象属性对比
class Person:
    age = 10
    num = 666
#类的本质也是一个对象
# 想要操作要通过Person这个变量名来操作

p = Person()
# p.age += 5      #这行代码会不会报错,然后打印出来的会是神马???
# p.age = p.age + 5      #赋值表达式先算右边的,P.age是在查询
# p.age = 10 + 5      #赋值表达式先算右边的,P.age是在查询
p.age = 15 #这么写代表新增属性,因为他之前自己没有
# 他俩之间的关系就是,对象是由类实例化出来的
# 绑在类里面的属性称为类属性,而在对象中的属性是对象属性
#
# Person.age = 23
# Person.age = 25
# del Person.age
# # Person.age


# 类的抽象层次更高,类更加虚拟的
# 对象属性的宿主是对象
# 类属性的宿主是Person
# # 类的属性可以直接写在里面,增加属性比较方便
# p.age = 11
# p.age = 18
# del p.age
# Person.age = 12

print(p.age)
print(Person.age)