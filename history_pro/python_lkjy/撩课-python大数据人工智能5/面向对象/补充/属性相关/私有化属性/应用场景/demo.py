# 私有化属性应用场景
class Person:
	''' 类属性 or 实例属性 
	要设计成实例属性,因为之后访问的时候 ,每个实例是不一样的,所以不能设计成为 类属性
	'''
	# age = 17
	''' 主要作用:当我们创建好一个实例对象之后,,会自动的调用这个方法,来初始化这个对象
	'''
	def __init__(self):
		# self.age = 18
		self.__age = 18		#这样的化 就只能在 类的内部访问 了
		# 往后再创建一个新的对象,就会自带一个属性,默认值18,并且互相不影响
	def setAge(self,value):
		if isinstance(value, int) and 0 < value < 200 :
			self.__age = value
		else:
			print("您输入的数据有问题,请重新输入")
		#在方法里面拦截过滤数据
		
	def getAge(self):
		return self.__age
		#这样就可以访问了,并且做了一层保护
		#还能加一个数据过滤,是吧
	pass
p1 = Person()

p1.setAge(201)
print(p1.getAge())
# print(p1._Person__age)
'''这样写也可以'''
# print(P1.__age)		
# print(p1._Person__age)		
'''这样写就行了
但是不要这么搞,这样是强行访问,建议不能这么搞
'''
p2 = Person()
# p2.age = -10 #这样写容易不安全
# p2.age = 2

# 这样写的话可以,方便添加,但是添加后没有默认的属性,这可怎么办呢?
p3 = Person()
# p3.age = 3

# print(p1.age)
# print(p1.__dict__)
# print(p2.age)
# print(p3.age)