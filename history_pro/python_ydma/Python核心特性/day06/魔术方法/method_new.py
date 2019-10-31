#__new__  构造方法    构建，创造！

class Human:
    #属性
    eye = 2
    skin = 'yellow'


    #方法

    #魔术方法 （重载object内部自带的__new__）
    def __new__(cls,sex):
        #print('new方法被触发')
        #print(cls)
        #自己控制对象的生成过程（女的生，男的不生）
        if sex == '女':
            #生成对象并且返回
            return object.__new__(cls)#上帝之手
        else:
            #不生成对象
            return None


    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法')


#实例化对象
one = Human('男') # 实例化对象 【1.制作一个对象 （new）2，初始化对象 （init）】
print(one)
