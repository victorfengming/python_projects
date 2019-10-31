'''
#声明一个类
class Human:
    #成员属性
    name = '张三'
    age = 18
    sex = '男'

    #成员方法
    #魔术方法
    def __call__(self):
        print('call方法被触发')


    def eat(self):
        print('吃货的世界我们不懂~')

    def cry(self):
        print('5555~~~')

#实例化对象
zs = Human()
print(zs)
#对象能够使用()调用干嘛？
zs()#正常情况下 对象不能当作函数调用
'''


#制作蛋糕的类
class MakeCake:
    #和面
    def huomian(self):
        print('和面操作')

    #发酵
    def fajiao(self):
        print('发酵操作')

    #烘烤
    def hongkao(self):
        print('烘烤操作')

    #切形状
    def qiexingzhuang(self):
        print('切形状操作')

    #抹奶油
    def monaiyou(self):
        print('抹奶油操作')

    #放水果
    def fangshuiguo(self):
        print('放水果')

    #打包
    def dabao(self):
        print('打包')

    #得到蛋糕的方法(结合步骤的操作)
    def __call__(self,kouwei):
        # 自己使用对象制作蛋糕
        self.huomian()
        self.fajiao()
        self.hongkao()
        self.qiexingzhuang()
        self.monaiyou()
        self.fangshuiguo()
        self.dabao()
        print('我们要制作一个{}口味的蛋糕'.format(kouwei))
        #返回值
        return '蛋糕'

#制作一个蛋糕（得到了做蛋糕的对象）
dg = MakeCake()#得到一个制作蛋糕的对象

#得到蛋糕
result = dg('巧克力')
print(result)