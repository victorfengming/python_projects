#类对象两种不同的创建方式
#   class声明创建
#   type函数调用创建
#
#元类的检索机制
#   指明通过哪一个元类创建出的对象,就能拦截类对象的创建
#   元类的流程的机制
##自己定义 了一个元类
    # 还能自己定义呢

#你还能拦截并且   控制类对象的创建
#
# 类的继承:
#     Animinal:
#         Person:
#             man
#             woman
#
#         dog
#         cat

# 模块级别的元类指明
# ------------------------------------------------------------------------
# __metaclass__ = xxx
# 写在哪里的作用域是不一样的
class Animal:
    pass


class Person(Animal):      #继承类
    # __metaclass__ = xxx

    pass

# 写好类描述,解释器就会创建类对象,他会首先看看有没有元类,怎么指明元类呢???











