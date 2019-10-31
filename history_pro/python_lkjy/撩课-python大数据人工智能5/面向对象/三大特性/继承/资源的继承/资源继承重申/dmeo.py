'''
#继承 不能继承私有的属性
class B:
	age = 10
	
class A(B):
	pass
	
print(A.age)
A.age = 3
#给A对象新增了一个age属性

print(A.age)
print(B.age)
print(A.__dict__)
print(B.__dict__)
'''
------------------单继承--------------------

class C:
	pass

class B(C):
	pass
	
class A(B):
	pass

--------------无重叠的多继承----------------
class D:
	pass
	
class E:
	pass
	
class B(D):
	pass
	
class C(E):
	pass
	
class A(B,C):
	pass
	
-------------有重叠的多继承链------------	
class D:
	pass
	
class B(D):
	pass
	
class C(D):
	pass
	
class A(B,C):
	pass

















