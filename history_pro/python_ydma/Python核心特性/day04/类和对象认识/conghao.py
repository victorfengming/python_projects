#声明一个丛浩的类
class CongHao:
    #成员属性
    name = '丛浩'
    sex = '女'
    age = 38
    color = 'yellow'
    height = '180cm'
    weight = '180斤'
    house = '180'

    #成员方法
    #聊天
    def talk(self):
        print('对象的方法中打印',self,id(self))
        print('我的名字是'+ self.name)#此处需要使用对象的属性来输出名字，性别年龄等
        print('我的性别是:'+ self.sex)#此处需要使用对象的属性来输出名字，性别年龄等
        print('我的年龄是:' + str(self.age))#此处需要使用对象的属性来输出名字，性别年龄等

    #唱歌
    def sing(self):
        print('你存在于我深深的脑海里~')

    #洗澡
    def wash(self):
        #洗澡的时候唱歌(调用自己的唱歌功能)
        self.sing()
        print('沐浴露和小香皂，水温干刚好~')

    #吃饭
    def eat(zhen):#非绑定类的方法
        print('我的体重是'+zhen.weight)
        print('我最喜欢吃烤羊腿~')

    #self设计为接受次数的参数
    def cry(self): #绑定类的方法
        print('我哭了'+self+'次')

    #没有self参数的方法
    def smoking():
        print('饭后一支烟，赛过活神仙！吸烟有害健康。')


'''
#实例化一个对象（做出一个丛浩对象）
ch = CongHao()
print('打印实例化的对象',ch,id(ch))#打印实例化的对象
#修改对象信息
#ch.name = '丛好'
#print(ch.__dict__)
#使用对象
#调用聊天功能
ch.talk()


#再次实例化一个对象（在做一个丛浩对象）
hnr = CongHao()
#调用聊天功能
hnr.talk()
'''


'''
#实例化对象
ch = CongHao()
#调用洗澡方法
ch.wash()
'''

'''
#测试使用其他单词单体self参数
ch = CongHao()
#调用吃饭方法
ch.eat()
'''

#没有self参数的方法的使用
#ch = CongHao()
#ch.smoking()#无法通过对象调用没有接受对象参数的方法

#CongHao.smoking()#通过类可以访问没有接受对象参数的方法