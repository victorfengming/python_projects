'''

我们可以直接使用的

内置特殊属性
	类属性
		__dict__			类的属性
		__bases__		类是所有父类构成的元组
		__doc__			类的文档字符串
		__name__		类名
		__module__		类定义所在的模块
	实例属性
		__dict__			实例的属性
		__class__			实例对应的类
	'''
	
class Person:
	'''
	这是一个'人'类
	'''
	age = 18
	def __init__(self):
		self.name = 'xiaoming'
	
	def run(self):
		print("---------------run-----------")

		
		
		
print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
help(Person)
print(Person.__name__)
print(Person.__module__)

'''
-------------运行结果-------------------------
{'__module__': '__main__', '__doc__': '\n\t这是一个人类\n\t', 'age': 18, '__init__': <function Person.__init__ at 0x00000235F0779510>, 'run': <function Person.run at 0x00000235F0779598>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
(<class 'object'>,)

        这是一个人类

Help on class Person in module __main__:

class Person(builtins.object)
 |  这是一个人类
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  run(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  age = 18
Person
__main__
ECHO 处于打开状态。
请按任意键继续. . .

'''
p = Person()
print(p.__class__)