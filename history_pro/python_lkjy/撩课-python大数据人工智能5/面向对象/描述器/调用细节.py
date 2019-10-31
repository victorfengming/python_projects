#调用细节: 

# 描述器只能在新式类中生效,而且 什么宿主类 和 描述器对应的类 应该全部都是 新式类才行


'''

方法拦截:
	一个实例属性的正常访问顺序:
		实例对象自身的__dict__字典
		对应类对象的__dict__ 字典
		如果有父类,会再往上层的__dict__ 字典中检测
		如果没有找到,又定义了__getattr__方法

'''
class Age:
	def __get__(self, instance ,owner):
		print("gettttt")
		
	def __set__(self, instance ,owner):
		print("settttt")
		
	def __delete__(self, instance):
		print("deleteeeeeeeeeeee")
		
	

class Person:

	age = Age()
	def __getattribute__(self, item):
		print("xxx")
p = Person()

# p.set_age(-10)


p.age = 19
print(p.age)
del p.age

print(Person.age)
Person.age = 28
del Person.age


