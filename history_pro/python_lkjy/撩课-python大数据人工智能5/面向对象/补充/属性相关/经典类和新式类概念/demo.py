# 经典类和新式类的概念
	# 经典类
		# 没有继承(object)
	# 新式类
		# 继承(object)
		
class Person:
	pass
	#类的描述
	'''
	想看他的类型,怎么看的呢,要借助一个属性__bases__
	'''

print(Person.__bases__)	
	'''运行结果如下:
			(<class 'object'>,)
		请按任意键继续. . .
	所以他是一个新式类,为什么我没有写继承object类,怎么能继承呢
	这要追溯到python2.x和python3.x 版本的问题
		python2.x 如果定义一个类,没写继承object,他就是一个经典类,是不自动继承object类的,必须继承object,他才是一个新式类
		python3.x 自动继承object类,如果继承一个类,会隐式的继承object类,默认情况下,就已经是一个新式类
	所以,建议你写出来object,因为这样写的化,就在python2和python3中兼容
	
		
	'''
