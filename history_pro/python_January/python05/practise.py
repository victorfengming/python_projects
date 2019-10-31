'''

s = ''rfrradsfghjkrrqebr''

# 将字符串按照指定字符进行切割操作
# 返回的是一个列表
print(s.split("a"))

# 将字符串按照换行位置进行切割操作
# 返回的是一个列表
print(s.splitlines())

# 将列表中的内容按照指定字符连接成一个字符串
# 返回字符串
print(s.join(["1","2","6","sjk"]))

# 在原有字符串长度不足指定长度时,在前面用0填充
# 返回字符串
print(s.zfill(5))

# 指定字符串长度,并且使得元字符串内容居中,其余位置使用指定字符填充
# 格式: 字符串.center(指定长度,填充字符)
# 返回字符串
print(s.center(8,"u"))

# 指定字符串长度,并且使得元字符串内容靠左,其余位置使用指定字符填充
# 格式: 字符串.ljust(指定长度,填充字符)
print(s.ljust(12,"b"))

# 指定字符串长度,并且使得元字符串内容靠右,其余位置使用指定字符填充
# 格式: 字符串.rjust(指定长度,填充字符)
print(s.rjust(12,"c"))

# 去掉左右两侧的指定字符,默认空格
# 格式: 字符串.strip(指定字符)
print(s.strip("r"))


# 去掉左侧的指定字符,默认空格
# 格式: 字符串.lstrip(指定字符)
print(s.lstrip("r"))

# 去掉右侧的指定字符,默认空格
# 格式: 字符串.rstrip(指定字符)
print(s.rstrip("r"))
'''

char = "qwertyuiopasdfghjklzxcvbnm"
# 制作用于字符串替换的映射表
# 格式: 字符串.maketrans(查找字符,替换字符)
# 返回值:字典
# print(char.maketrans("o","i"))
t = char.maketrans("o","i")
# 这里打印的字典是什么东东
'''
E:\PycharmProjects\python_January\venv\Scripts\python.exe E:/PycharmProjects/python_January/python05/practise.py
{111: 105}

Process finished with exit code 0
'''

char = "qwertyuiopasdfghjklzxcvbnm"
# 进行字符串替换操作
# 格式: 字符串.translate(映射表)
# 返回值: 替换之后的字符串
print(char.translate(t))
# 这个函数的参数应该是和上一个函数配合使用的,
# 这参数和上一个的返回值有一拼




