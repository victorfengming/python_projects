''''

私有化方法,不管是属性也好方法也罢,都是存在__dcit__ 里面 ,是一个字典,字典就由键值对儿组成 要不就是属性的名称,要不就是方法的名称 要是函数就成为方法, 要不是,就是一个属性

'''

class Person:
	__age = 18
	def __run(self):
		print("跑")
	def _Person__run(self):
		print("跳")
p = Person()
p._Person__run()
# print(Person.__dict__)

# 我们可以通过__(两个下划线)变成私有的









