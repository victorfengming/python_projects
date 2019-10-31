# 作用域

#python中函数就是一个作用域（JavaScript）
# c#、java中的作用域{}
# 代码定义完成后，作用域已经生成，作用域链条向上查找

age = 18
def func1() :
    age = 73
    def func2():
        print(age)
    return func2
val = func1()
val ()
# 什么结果？
'''在哪调用函数，函数都回到它定义的地方来执行
函数名还可以当做返回值'''