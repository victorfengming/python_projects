'''

在python 里面 只能通过 一些间接是手段,来让他变成只读属性

第一种方式: 将读写操作给他禁止掉
	方案
		全部隐藏
			私有化
				既不能读
				也不能写
		部分公开
			公开读的操作
	具体实现
		私有化
			通过"属性前置双下划线"实现
		部分公开
			通过公开方法
			优化

'''
#直接上代码

class Person:
	#添加一个age属性
	def __init__(self):
		self.__age = 18
	def getAge(self):
		return self.__age

p1 = Person()		
print(p1.getAge())

# p1.__age = 5	#这样写就增加了一个属性
# print(p1.__dict__)

