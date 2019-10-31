

class Person:
	def __init__(self,n,a):
		self.name = n
		self.age = a
	def __str__(self):
		return "此人的姓名是%s,这个人的年龄是%s"%(self.name,self.age)
		# return self.age
p1 = Person("sz",18)
print(p1.name)
print(p1.age)
print(p1)#这个是开发人员看的,用户是看不懂的	
s = str(p1)		#他们是意义是不一样的
print(s,type(s))
#当我们加上了 了 def str 就能够打印出一些用户需要的东西了	
p2 = Person("zhangsan",19)
print(p2.name)
print(p2.age)
print(p2)
print(str(p2))
#你传什么东西,创建出来的就是什么东西

#高不高,__str__是不是贼强
# 还可以使用str()函数来触发这个方法		





