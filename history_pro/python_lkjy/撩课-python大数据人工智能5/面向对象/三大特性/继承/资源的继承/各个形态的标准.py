
# ------------------单继承--------------------

# 这个集成遵循从下到上的原则,先看看本层有没有,然后逐层网上找

class C:
	pass

class B(C):
	pass
	
class A(B):
	pass

# --------------无重叠的多继承----------------

# 单调原则,在继承多个父类中,优先从左边去找,都找不到,再找不到,在网上找
# 找的顺序a-b-d-c-e


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
	
# -------------有重叠的多继承链------------	
# 从下到上的原则,先到自己的里面找,
# a-b-c-d

class D:
	pass
	
class B(D):
	pass
	
class C(D):
	pass
	
class A(B,C):
	pass



















