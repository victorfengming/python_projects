# 继承是指的是资源的使用权,并不是复制

# class Person:
	# pass
class Animal:
	# 属性和方法
	#设置不同权限的属性和方法,继承当中进行测试,
	#在子类当中,能否访问到这些数据
	a = 1
	_b = 2
	__c = 3

	def t1(self):
	# 共有的
		print("ti")
		
	def _t2(self):
	# 受保护的
		print("t2")
		
	def __t3(self):
	# 私有的资源
		print("t3")
		
	def __init__(self):
		print("init,anmimal")
		
class Person(Animal):
	def test(self):
		print(id(Animal))
		print(self.a)
		print(self._b)
		# print(self.__c)
		
		
		self.t1()
		self._t2()
		# self.__t3()
		self.__init__()
		
p = Person()
p.test()

Animal.a = 555
p.test()	

print(id(Animal.a))
Animal.a = 666
print(id(Animal.a))

p.test()

