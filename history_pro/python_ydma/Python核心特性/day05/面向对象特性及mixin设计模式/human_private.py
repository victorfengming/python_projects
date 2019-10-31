#声明一个人类
class Human:
    #成员属性
    name = '张三'#允许别人使用
    __sex  = '男' #不允许别人访问
    age = 18
    heart = '健康心脏'#不允许别人访问
    __kidney  = '强大的肾脏'#不允许别人访问

    #成员方法
    #唱歌
    def sing(self):
        print('都如艾米发馊拉稀都')

    #吃饭 #允许别人访问
    def eat(self):
        print('我最喜欢吃西红柿炒番茄了！')

    #跑步 #不允许别人访问
    def __run(self):#私有化
        print('121,121,锻炼身体')

    #聊天(用于测试类.对象的内部访问私有成员)
    def talk(self):
        print('我的名字是',self.name)
        #在类/对象的内部访问私有成员属性
        print('我的肾脏是非常好的',self.__kidney)
        #在类/对象的内部访问私有成员方法
        self.__run()


#实例化对象
zs = Human()
print(zs)

#访问对象的成员属性和方法
#访问性别
#print(zs.sex)
#print(zs.__sex) #私有化封装之后，类/对象的外部无法访问！

#访问肾脏
#print(zs.kidney)
#print(zs.__kidney)#私有化封装之后，类/对象的外部无法访问！

#调用唱歌方法
#zs.sing()

#调用跑步方法
#zs.run()
#zs.__run()#私有化封装之后，类/对象的外部无法访问！


#测试类./对象内部访问私有成员
zs.talk()
