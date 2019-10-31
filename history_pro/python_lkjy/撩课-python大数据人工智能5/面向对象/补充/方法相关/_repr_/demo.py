# # 使用一个字符串来取描述类产生的实例
# # __repr__ 面向的不是用户了,而是开发人员


# class Person:
	# def __init__(self,n,a):
		# self.name = n
		# self.age = a
	# def __str__(self):
		# return "此人的姓名是%s,这个人的年龄是%s"%(self.name,self.age)
	# def __repr__(self):
		# return "---------------repr----------------------"
# p1 = Person("sz",18)
# # print(p1.name)
# # print(p1.age)
# # print(p1)#这个是开发人员看的,用户是看不懂的	
# # s = str(p1)		#他们是意义是不一样的
# # print(s,type(s))
# #当我们加上了 了 def str 就能够打印出一些用户需要的东西了	
# p2 = Person("zhangsan",19)
# # print(p2.name)
# # print(p2.age)
# # print(p2)
# # print(str(p2))
# #我现在想要查看这个实例对象的内存地址,那应该怎么写呢?

# print(repr(p1))
# # 先找到repr这个方法,没有实现就是走repr,实现了就  
# # 通过这个方法可以获取实例的信息





import datetime
# t = datetime.datetime.now()
t = datetime.datetime.now()
print(t)
print(repr(t))

temp = repr(t)
result = eval(temp)
print(result)

# eval()