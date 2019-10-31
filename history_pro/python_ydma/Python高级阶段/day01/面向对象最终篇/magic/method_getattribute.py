#声明一个类
class Human:
    #添加成员属性（加入对象）
    def __init__(self):
        self.name = '东方不败'
        self.sex = '男'
        self.age = 18

    #添加成员方法
    #添加魔术方法__getattribute__
    def __getattribute__(self, item):#item接受的是访问成员的名称字符串
        #print(item)
        #print('getattribute被触发')
        #一定不能使用当前对象的成员访问，会再次触发当前魔术方法进入递归循环!
        result = object.__getattribute__(self,item)
        #隐藏用户名（你的操作）
        newname = result[0] + '*' + result[-1]
        #返回数据
        return  newname

    def eat(self):
        print('一天三顿小烧烤~')

    def drink(self):
        print('喝啤酒~')


#实例化对象
ls = Human()
print(ls)

#访问对象的名称
print(ls.sex)



'''
医院叫号显示：
    张三    -> 张*三
    李大嘴  -> 李*嘴

'''