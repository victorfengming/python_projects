# 对象.属性 = 值
# 类:
#     变量
# 类.变量 = 值
class Tset:
    sex = "男"
#fangwen访问类属性可以通过对象来访问
class Money:
    age = 18    #给一个类添加属性的方式2
    count = 1   #以后我们常用的就是这种方式
    num = 666   #这个有点儿像C语言中的结构体

# 访问方式2:通过类对象来访问
one = Money()   #Money实例化出来的对象
one.sex = '女'
one.vi = 'sb'
print(one.__class__)
print(one.age)
print(one.count)
print(one.num)
print(one.sex)
print(one.vi)