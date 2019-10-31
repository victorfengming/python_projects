# 1. 定义一个类
class person:
    pass


# 2. 根据类,创建一对象
p = person()

# 3. 给p对象,增加一些属性
p.age = 134
p.height = 180
p.sex = 'nan'

# 4. 验证是否有添加成功
# print(p.age)
p.age = 123
print(p.__dict__)
print(p.age)
print(p.sex)
# 修改对象的属性值
# 对象.属性.值
# 如果这个属性没有那就是新增属性,要是有的话就是赋值
p.pets = ["小花", "小黑"]
a = 1
del a
# print(a)
del p.age
print(p.age)  # id没有改变,不会开辟一块儿新的空间
# 不同空间的值不一样



