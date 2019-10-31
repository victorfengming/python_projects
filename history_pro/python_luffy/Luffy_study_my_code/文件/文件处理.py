# 文件处理
# 为你一个文件“兼职白领学生空姐模特护士联系方式”
# python 文件处理
# 先从读文件开始
f = open("xiaoming.txt",mode="r",encoding="gbk")
date = f.read()
print(date)
f.close()
# data = f.read()
# f.close()