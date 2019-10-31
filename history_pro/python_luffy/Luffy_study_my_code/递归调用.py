# 递归调用经典问题
# 求阶乘问题：
# n! = n * (n-1)!
def factorial( n):
    if n==1 :
        return 1
    return n * factorial(n-1)

a = int(input("请输入"))
print(factorial(a))


