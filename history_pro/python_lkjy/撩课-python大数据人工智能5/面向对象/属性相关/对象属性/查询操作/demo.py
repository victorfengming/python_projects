#1. 定义一个类
class Person:
	pass
#2. 根据类,创建一对象
p = Person()

#3. 给P对象,增加一些属性
p.age = 134
p.height = 180
p.sex = 'nan'

#4. 验证是否有添加成功
# print(p.age)
p.age = 123
print(p.__dict__)
print(p.age)
print(p.sex)
# 对象