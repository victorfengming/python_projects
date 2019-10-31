# # 元类是指创建类对象的类
#     对象怎样产生的:由类创建出来的
#     类是不是对象:类本事上是对象(万物皆对象)
#     所以类是不是由另外一个类创建出来的呢? 是的
#         创建类对象的类就是元类

num = 10
# #   这个10 是不是一个对象
# 那这个对象也应该是由一个类创建(实例化)出来的吧
print(num.__class__)
# 这个__class__就是这个对象的类
# int 看见了吧 int就是这个类
# 10是通过__class__来引用这个类的
s = "abc"
print(s.__class__)

class Person:
    pass
p = Person()
#这个p
print(p.__class__)
#   这个Person 和 num s 都是同一个级别的,本来系统带了好多类,但是有时候系统的不够用了,我们才自己创建类的

# 这个对象是由谁创建出来的???
# 那 int 也是一个对象 ,找一下 他的类

print(int.__class__)
#type 是int的类,这类和对象就想文件夹目录一样,一路有很多级别
print(str.__class__)
print(Person.__class__)
#有个牛逼的类type 都装的下他们
# 所以这个type就是元类,元类就是创建类对象的类
print(type.__class__)       #type 的 类也是 type
print(type.__class__)       #type 的 类也是 type
# type是最上层的类了




