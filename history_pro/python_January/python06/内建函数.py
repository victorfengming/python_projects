#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

# 内键函数
'''
类型相关
int()       整形
float()     浮点型
bool()      布尔型
complex()   复数类型
str()       字符串类型
set()       集合
tuple()     元祖
dict()      字典

print()     打印
type()      类型
locals()    返回当前环境中的所有变量
id()        打印id地址

数学相关:
abs()       获取一个数值的绝对值
'''
'''
num = 12
result = abs(num)
print(result)

# sum()
lists = [5,67,7,32,4,5,6]
res = sum(lists)
print(res)

# max()
# min()
result = max(lists)
print(result)

# pow()   # 求一个数的次方
num = 10
result = (num,2)
print(result)

# round() 四舍五入
# num = 2.222222222222
num = 2.49999999999
result = round(num)
print(result)
print()

# hex() 十进制转十六进制
# oct() 十进制转八进制
# bin() 十进制转二进制
print(hex(100))
print(oct(100))
print(bin(100))
'''
# ord() 普通字符转化为ASCII
# result = chr(98)
# print(result)
# # chr() 将ASCII吗转为字符
# result = ord("B")
# print(result)
#
# # repr() 获取任意数据的原格式字符串
# # repr() 可以将双引号转义
# res = "字符串换行\n制表符\t 单引号\'双引号\""
# yres = r"字符串换行\n制表符\t 单引号\'双引号\""
# # res = [1,4,9,534,224,6,73,6]
# # 如果是字符串,将原字符串"python" 转换后""python""
# result = repr(res)
# print(res,type(res))
# print(result,type(result))
# print("元字符串:",yres,type(yres))
# # 转义功能没有被去除
#
# # eval() 将一个字符串当做python代码执行,字符串需要符合代码规范
# mystr = "print('打印撒娇的刻录机')"
# print(mystr)
# eval(mystr)
# print(type(mystr))

# 字符串符合lambda表达式 ,打印出 1,4,9,16,25

char = '''
n = 1
while n < 6:
    result = lambda n: n ** 2
    print(result(n))
    n += 1
'''
#"

# eval()6

# n = 0
# while n<5:
#     n += 1
#     print(n**2)

charr = '''
for i in range(1,6):
    print(i**2)
'''

# print(
result = repr(charr)
eval(result)






