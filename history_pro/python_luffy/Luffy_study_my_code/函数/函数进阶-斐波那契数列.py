# 斐波那契数列fibonacci
# 除了第一个数和第二个数除外
# 其他的数都等于前两个数相加
# 1,1,2,3,5,8,13,21,34,...

# '''下面这是我写的代码，上面这行代码就比较吊了，他是同时赋值的
# 要是没学过这种写法的，得多定义一个变量了'''
#         # d = a+b
#         # a = b
#         # b = d
#
# '''有瑕疵，
#     a,b = b, a+b
#             zheyang这样整不需要一个临时的值来存放a啦
#             这么写贼高级的很哦
# '''
#
#
# 
#
def fib(max):
    n,a,b = 0,0,1
    while n < max :
        yield  b#把函数执行的过程冻结在这里
        #吧b的值返回给外面 next()

        a,b = b,a+b
        n = n+1
    return 'done'

f = fib(10)
for i in f :
    print(i)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
print("this program is end")
   # 这玩意和生成器有什么关系啊

