#资料描述器 get set 
# 非资料描述器 仅仅实现了 get 方法, 那么他就是一个飞资料描述器
# 资料描述器 > 实例属性 > 非资料描述器

class Age(object):
	def __get__(self, instance , owner):
		print("get")
		
	def __set__(self , instance, value):
		print("set")
		
	def __delete__(self , instance):
		print("delete")
		
		
class Person(object):
	age = Age()
	def __init__(self):
		self.age = 10
		
p = Person()

p.age = 10
print(p.age)
0










