# 定义方式1 : property类实现
# 定义方式2 : 
'''
class Person:
	def __init__(self):
		self.__age = 10
		
	def get_age(self):
		return self.__age
		
	def set_age(self,value):
		if value < 0:
			value = 0
		self.__age = value
	
	def del_age(self):
		del self.__age
		
		
	age = property(get_age, set_age ,del_age)
	name = "xiaoming"
# endclass		
p = Person()

# p.set_age(-10)


p.age = 19
print(p.age)

help(Person)

'''


class Person:
	def __init__(self):
		self.__age = 10
	@property	
	def age(self):
		print("jijsijdi")
		return self.__age
	@age.setter	
	def age(self,value):
		print("jinrule setter")
		if value < 0:
			value = 0
		self.__age = value
	@age.deleter
	def age(self):
		print("jinrule deleter")
		del self.__age
		
		
	# age = property(get_age, set_age ,del_age)
	name = "xiaoming"
# endclass		
p = Person()

# p.set_age(-10)


p.age = 19
print(p.age)

# help(Person)


