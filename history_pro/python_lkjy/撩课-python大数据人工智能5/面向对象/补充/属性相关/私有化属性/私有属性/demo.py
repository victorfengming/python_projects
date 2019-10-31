# # 私有属性 也就是添加__(两个下划线)
# class Animal:
	# __x = 10
	# def test(self):
		# print(Animal.__x)
		# print(self.__x)
	
# class Dog(Animal):
	# def test2(self):
		# print(Dog.__x)
		# print(self.__x)
# a = Animal()
# a.test()

# d = Dog()
# d.test2()
#在子类内部不能访问

# print(Animal.__x)
# print(Dog.__x)
# print(a.__x)
# print(d.__x)

# 在模块外面也不能访问 


__a = 98
__all__ = ['__a'] #指在其他模块里面,哪些模块会被导入过去
# _开头的对象是受保护的属性  不能乱访问
# 要是指明了 也是能访问的