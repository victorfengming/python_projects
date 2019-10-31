# # 如何打印一行 10个#
# print(help(print))
# print(1,end="")
#
# i = 0
# while i<10:
#     j = 0
#     while j<10:
#         print("#",end = "")
#         j += 1
#     print()
#     i += 1

# 乘法表
# i = 1#行数
# while i <= 9 :
#     j = 1
#     while j <= i :
#         print( str(j)+"*"+str(i)+"="+str((i)*j)+"  ",end = "")
#         if i*j<10 :
#             print("\t",end ="")
#         j+=1
#     print()
#     i+=1

# 隔行变色
# i = 0
# while i<10:
#     j = 0
#     while j<10:
#         if j%2 :
#             if i%2:
#                 print("*",end = "")
#             else :
#                 print("#", end="")
#         else:
#             if i%2:
# #                 print("#",end = "")
# #             else :
# #                 print("*", end="")
#
#         j += 1
#
#     print()
#     i += 1

# 菲薄纳妾数列
# j = 7
# i = 0
# a = [1,3,2,4]
# while i <= j:
#
#     if i == 0:
#         result = 0
#     elif i == 1:
#         result = 1
#     else:
#         result = a[-1] + a[-2]
#     a.append(result)
#     print(a)
#     i += 1

# print(a)

# 一个循环打印10行10列
# i = 99
# while i>=0:
#     if i%10 :
#         print("*",end="")
#     else:
#         print("*")
#     i -= 1



# # 菲薄纳妾数列
# def feibonaqie(j):
#     i = 0
#     a = []
#     while i < j:
#         if i == 0:
#             a.append(0)
#         elif i == 1:
#             a.append(1)
#         else:
#             a.append(a[-1] + a[-2])
#         i += 1
#     return a
# while True:
#     j = int(input("看看实力"))
#     print(feibonaqie(j))

# while 与 else 一起用,当while循环结束后,执行else
# 字符串格式化输出
# strs = "sjklgj%d"%124
# %d  整形
# %f  浮点型
# %s  字符串型
# print(strs)

#
# i = 1# 行数
# j = 0# 每行的列数
# while i<=9 :
#     j = 1
#     while j <= i:
#         print(str(j)+"*"+str(i)+"="+str(i*j)+"  ",end = "")
#         if i*j < 10:
#             print("\t",end="")
#         j += 1
#     print()
#     i += 1
#

# # 斐波那数列
# a = 0
# b = 1
# i = 0
# print(a)
# while i<7:
#     i += 1
#     a,b = b,a+b
#     print(b)
#