#直接上代码

	
class Person(object):		#让他继承object
	#添加一个age属性
	def __init__(self):
		self.__age = 18
	@property		#加了一个装饰器, at property
	def age(self):
		return self.__age
	

p1 = Person()		
print(p1.age)

#p1.age = 666		#报错 了 
#所以现在你不看上面的,就是只读属性了,还不是操作函数来访问的
#现在需要通过方法调用才能获取值了,这就麻烦了一丢丢,
#而且当你再赋值的时候,并不是报错,而是增加了一个新的属性,容易让人误解,下面来优化一下:
#p1.age = 1这样要实现能够访问,并且需要报错
# p1.__age = 5	#这样写就增加了一个属性,叫__age
# print(p1.__dict__)

