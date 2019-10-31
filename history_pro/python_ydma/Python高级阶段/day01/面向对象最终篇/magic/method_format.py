#声明一个类
class Girl:
    #成员属性
    name = '熊初墨'
    sex = '女'
    age = 18

    #成员方法
    def __format__(self,arg):#arg 接受的是限定符号的字符串
        #print('format方法被触发')
        #print('arg的内容是',arg)
        #return self.name

        #实现format自带的对其和填充功能
        #1.接受限定符号
        flag = arg
        #2.拆分限定符号
        fillchar = flag[0]#填充字符
        align = flag[1]#对其方式
        length = int(flag[2:])#字符长度
        #3.根据不同的符号进行不同的填充操作
        #判断对其方式
        if align == '>':#右对齐
            newname = self.name.rjust(length,fillchar)
            return newname
        elif align == '^':#居中对其
            newname = self.name.center(length,fillchar)
            return newname
        elif align == '<':#左对齐
            newname = self.name.ljust(length,fillchar)
            return newname
        else:
            return ''

    def shopping(self):
        print('买买买~~')

    def eat(self):
        print('吃烧烤~')


#实例化一个对象
xcm = Girl()
print(xcm)

#使用format来操作我们的对象
action = '我和我的闺蜜{:$<30}去逛街'
result = action.format(xcm)
print(result)