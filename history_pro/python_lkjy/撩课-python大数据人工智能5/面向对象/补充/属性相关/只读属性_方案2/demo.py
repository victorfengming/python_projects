# # # python在经典类和新式类的使用方式 先定义一个新式类,需要考虑版本问题 为了兼容起见,我们统统加上object 

# # class Person(object):
	# # def __init__(self):
		# # self.__age = 18
		
	# # def get_age(self):
		# # return self.__age
		
	# # def set_age(self,value):
		# # print("--------------set函数------------")
		# # self.__age = value
		
	# # age = property(get_age,set_age,)		#关联起来了


# # p = Person()
# # print(p.age)

# # p.age = 67
# # print(p.age)

# # print(p.__dict__)
# # '''
# # # 运行结果
	# # # 18
	# # # 67
	# # # {'_Person__age': 67}
	# # # 请按任意键继续. . .
# # '''



# # 第二种使用方式

# # class Person(object):
	# # def __init__(self):
		# # self.__age = 17
		
	# # @property
	# # def age(self):
		# # print("---get方法------")		
		# # return self.__age
	# # @age.setter
	# # def age(self,value):
		# # print("---set方法------")
		# # self.__age = value
# # p = Person()
# # print(p.age)
# # p.age = 18
# # print(p.age)

# #---------------------------property在经典类中的应用----------------------------

# class Person:
	# def __init__(self):
		# self.__age = 17
	# # @property
	# def get_age(self):
		# print("---get方法------")		
		# return self.__age
	# # @age.setter
	# def set_age(self,value):
		# print("---set方法------")
		# self.__age = value
		
	# age = property(get_age, set_age)
# #在python2中就是经典类了	
# p = Person()	
# p.age = 19
# print(p.age)
# print(p.__dict__)
# '''运行结果:
	# ---set方法------
	# ---get方法------
	# 19
	# {'_Person__age': 19}
	# 请按任意键继续. . .
# '''
class Person:
	def __setattr__(self, key, value):
		print(key,value)

		'''
		1.判定,key,是否是我们要设置的只读属性的名称
		2.如果说不是,只读属性的名称,真正的给它添加到这个实例里面去
		'''
		if key == "age" and key in self.__dict__.keys():
		#拦截赋值操作
			print("这个属性是只读属性,不能设置数据")
		else:
			# self.key = value
			self.__dict__[key] = value
			
			
p1 = Person()
p1.age = 18
# p1.name = "xiaoming"
print(p1.age)
p1.age = 999
print(p1.age)

print(p1.__dict__)
#)__dict__ 里面啥也没有.......
#屏蔽修改操作
#允许新增操作

