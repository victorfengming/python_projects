#多继承
'''
音乐老师类：
体育老师类：
爸爸类：
妈妈类：
'''

#音乐老师类
class MusicTeacher:
    #属性
    cloth = '晚礼服'
    #方法
    def sing(self):
        print('门前大桥下，路过一群鸭，快来快来数一数，2，4，6，7，8.。')

#体育老师类
class SportTeahcer:
    #方法
    def run(self):
        print('跑步功能')

    def jump(self):
        print('you jump，i jump')
#爸爸类
class Father:
    #方法
    def smoking(self):
        print('抽烟中~~')

#妈妈类
class Mother:
    #方法
    def clear(self):
        print('打扫房间。。')

#我的类（多继承）
class Me(Mother,Father,MusicTeacher,SportTeahcer):
    pass


#实例化对象
i = Me()

#调用成员
print(i.cloth)
i.sing()
i.jump()
i.run()
i.smoking()
i.clear()