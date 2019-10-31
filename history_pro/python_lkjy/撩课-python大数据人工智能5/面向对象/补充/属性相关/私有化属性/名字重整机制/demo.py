# 私有属性的实现机制
	# 名字重整(Name Mangling)
		# 在python里面,并不是真正的支持私有化,而是通过__的方式伪私有属性
		# 主要是通过名字重整机制,更改__x 为另外一个名称,,如_类名__x 
	# 目的:
		# 防止外界直接访问
		# 防止被子类同名称属性覆盖
		
		
# # 私有属性 也就是添加__(两个下划线)
class Animal:
	__x = 10
	def test(self):
		print(Animal.__x)
		print(self.__x)
	
	
print(Animal.__dict__)

'''
{'__module__': '__main__', '_Animal__x': 10, 'test': <function Animal.test at 0x0000023DF48C9510>, '__dict__': <attribute '__dict__' of 'Animal' objects>, '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None}
ECHO 处于打开状态。
请按任意键继续. . .
名字确实该了吧
'''
print(Animal._Animal__x)
'''
这样写就可以了傲,所以才说这是伪私有属性,OK???
'''
