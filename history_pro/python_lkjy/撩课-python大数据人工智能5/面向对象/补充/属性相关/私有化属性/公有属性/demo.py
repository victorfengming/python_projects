
class Animal:
	x = 10
	def test(self):
		print(Animal.x)
		print(self.x)
	pass
class Dog(Animal):
	def test2(self):
		print(Dog.x)
		print(self.x)
	
	pass
	
# 测试代码
# a = Animal()
# a.test()
# d = Dog()
# d.test2()

# 有些资源能够继承下来
# 有些就继承不下来
# 第二个测试完毕
# 下面测试模块外能不能访问
# print(Animal.x)
# print(Dog.x)

# print(a.x)
# print(d.x)

# 定义一个公有的变量:
a = 666
print(a)






