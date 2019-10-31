# 要是你比较穷，买不起大的内存，只有1024MB的内存
# 所以说要循环读文件
# f = open("xiaoming.txt",'r',encoding="gbk")
# for line in f :
#  print(line)
# f.close()
'''有点儿瑕疵：他每行之间多了一个空行
那拥护啥呢？？？就是这个print函数吧，它自带了一个换行
知道吧
'''
'''
写文件，来来来 走起
先试试之前的那个读取文件（这回是绝对的路径傲）'''
f = open(file="E:/使用说明.txt",mode="r",encoding="gbk")
for line in f :
 print(line)
'''
好使，没毛病
下面试试，写的功能了傲
'''
f = open(file="E:/使用说明.txt",mode="w",encoding="gbk")
f.write('北大本科美国留学一次90，微信号：16060606')
f.close()

