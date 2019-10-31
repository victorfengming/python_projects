# '''class Person:
	# def __call__(self, *args, **kwargs):		#写上他就可以被调用了
		# print("xxxx", args , kwargs)
	
	# pass
	
	
# p = Person()

# p(123,456,name = "xioaming")

# 偏函数是使用场景,偏函数即为某个函数他偏爱某个参数 故称之为偏函数
# eg 我有一个画笔
	# 创建了很多画笔,画笔的类型(钢笔,铅笔)

# '''
# '''
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","红色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","橙色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","黄色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","绿色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","青色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","蓝色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","紫色"))
# print("创建了一个%s这个类型的画笔,它是%s的颜色"%("钢笔","白色"))
# '''

# def createPen(p_color,p_type):
	# print("创建了一个%s这个类型的画笔,它是%s的颜色"%(p_type,p_color))

# # createPen("钢笔","红色")
# # createPen("钢笔","绿色")		
# # createPen("钢笔","黑色")		
# #前面的变化率比较低,后边的变化率比较低,所以就要用到我们的偏函数

# import functools
# gangbiFunc = functools.partial(createPen, p_type = "钢笔")
# gangbiFunc("红色")
# gangbiFunc("黄色")
# gangbiFunc("绿色")


class PenFactory:

	def __init__(self, p_type):
		self.p_type = p_type
		
	def __call__(self, p_color):
		print("创建了一个%s这个类型的画笔,它是%s的颜色"%(self.p_type, p_color))
		
gangbiF  = PenFactory("钢笔")
gangbiF("红色")
gangbiF("绿色")
gangbiF("黑色")
gangbiF("白色")

qianbiF = PenFactory("铅笔")
qianbiF("花色")
qianbiF("白色")
qianbiF("黑色")
qianbiF("灰色")
