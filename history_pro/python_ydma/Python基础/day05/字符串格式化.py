#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming


'''
字符串 % 格式化内容
format()
'''
# 普通格式化
mystr = "今年过年放假回家,还不给工资,%d块都不给我" % 100

print(mystr)

# format()函数
# format有个好处就是不需要声明数据类型,这个样写更加的方便
mystr = "今年过年放假回家,还不给工资,{}块都不给我".format(100)

print(mystr)
# 普通格式
mystr1 = "今天{}年{}月{}日".format(2019,1,21)

print(mystr1)
# 稍微升级一点儿
mystr2 = "今天{2}年{0}月{1}日".format(1,21,2020)

print(mystr2)

# 填充和对齐
'''
居中      ^
向左偏     <
向右偏     >
'''
mystr3 = "i have a {:10} ".format("dream")
print(mystr3)
mystr4 = "i have a {:^10} ".format("dream")
print(mystr4)
mystr5 = "i have a {:!^10} ".format("dream")
print(mystr5)
mystr6 = "i have a {:!<10} ".format("dream")
print(mystr6)
mystr7 = "i have a {:!>10} ".format("dream")
print(mystr7)

# 精度问题 添加数据类型
# 保留两位
mystr8 = "π的值是{:.2f}".format(3.1415926535589)
print(mystr8)
# 保留超过范围用零补充
mystr9 = "π的值是{:.10f}".format(3.141592)
print(mystr9)

# 进制问题
# 二进制
mystr = "二进制数{:b}".format(20)
print(mystr)

# 八进制
mystr = "二进制数{:o}".format(20)
print(mystr)

# 十六进制
mystr = "二进制数{:x}".format(200)
print(mystr)

'''
b       二进制
o       八进制
x       十六进制
'''

# 可以用逗号作为千分符,

mystr = "全部家当加起来{:,}块".format(77418529638945623)
print(mystr)

