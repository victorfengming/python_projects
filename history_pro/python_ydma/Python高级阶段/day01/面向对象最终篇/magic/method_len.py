#声明一个类
class Car:
    #成员属性
    color = '黑色'
    weight = '2T'
    grand = '奥利奥'
    circle = ['左前轮','右前轮','左后轮','右后轮']

    #成员方法

    #len魔术方法
    def __len__(self):
        #print('len方法被触发')
        #返回轮子的个数
        num = len(self.circle)
        return num

    def playmusic(self):
        print('你存在我深深的脑海里~')

    def move(self):
        print('请注意倒车，请注意倒车')

#实例化一个对象
mycar = Car()

#可以使用len函数检测对象么？
result = len(mycar)
print(result)

'''
列表也是List类，我们定义的列表不就是List类的一个对象？  确确实实

'''