

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










