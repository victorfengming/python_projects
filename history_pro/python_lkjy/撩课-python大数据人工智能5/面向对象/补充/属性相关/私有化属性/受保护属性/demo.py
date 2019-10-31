# class Animal:
	# _x = 10
	# def test(self):
		# print(Animal._x)
		# print(self._x)
	
# class Dog(Animal):
	# def test2(self):
		# print(Dog._x)
		# print(self._x)
# a = Animal()
# a.test()

# d = Dog()
# d.test2()

# print(Animal._x)
# print(Dog._x)
# print(a._x)
# print(d._x)


_a = 98
__all__ = ['_a'] #指在其他模块里面,哪些模块会被导入过去
# _开头的对象是受保护的属性  不能乱访问
# 要是指明了 也是能访问的