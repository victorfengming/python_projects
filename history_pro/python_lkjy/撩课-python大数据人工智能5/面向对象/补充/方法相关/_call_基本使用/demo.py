class Person:
	def __call__(self, *args, **kwargs):		#写上他就可以被调用了
		print("xxxx", args , kwargs)
	
	pass
	
	
p = Person()

p(123,456,name = "xioaming")

#p是不能实现被调用的能力的
# 函数是可以被调用,函数的本质也是一个对象
# __call__方法











