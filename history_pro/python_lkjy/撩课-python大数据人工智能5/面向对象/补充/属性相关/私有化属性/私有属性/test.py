# import demo
# print(demo.__a)
# # 没有问题

from demo import *
print(__a)

# 报错了 ,就 不好使 
# __all__ 就行