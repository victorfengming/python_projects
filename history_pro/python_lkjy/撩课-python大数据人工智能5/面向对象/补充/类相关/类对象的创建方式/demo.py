# # 类对象的创建方式
# # 不是class来声明就行了么
#
# class Person:
#     count = 0
#     def run(self):
#         pass
#
# # 这个只是一个表像
#
# # 高级的创建不是这么创建的
#
# # dict属性指向一个字典,字典里面存储了属性,这么声明python会帮我们自动创建一个类

# 手动创建一个类
num = 10
# print(type(num))
# type是一个元类,我们可以通过元类创建一个类

def run(self):
    print(self)
    print("runnnn")
#shoudong手动创建类,调用type
xxx = type("Dog",(),{"count":0,"run":run})
print(xxx)
print(xxx.__dict__)

d = xxx()
print(d)
d.run()
# Tuple是一个元祖,他的父类
# ()元组
# {}字典
# []列表