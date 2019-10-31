#父类
class LiuBei:
    #属性
    __wife = ('甘夫人','糜夫人','孙尚香')#私有化
    _money = '100'#受保护（不是语法是约定）
    skin = '黄色'# 公共
    #方法
    #吃饭
    def eat(self):#公共的
        print('打死我***也不吃~ 真香啊~')

    #学习
    def __study(self):#私有化
        print('好好学习天天向上')

    #做鞋
    def _makeshoes(self):
        print('编草鞋')

    #内部测试受保护成员
    def test(self):
        print(self._money)
        self._makeshoes()

#子类
class LiuShan(LiuBei):
    pass

#检测私有化和公共的封装
#实例化对象
ls = LiuShan()
#print(ls.wife) #私有成员无法在子类.子对象中调用
#ls.study()#私有成员无法在子类.子对象中调用

#print(ls.skin)#公共的成员可以在子类/子对象中调用
#ls.eat()#公共的成员可以在子类/子对象中调用

#调用受保护的成员
#实例化刘备的对象
lb = LiuBei()

#在类和对向外（随便访问）
print(lb._money)
lb._makeshoes()

#在类和对象的内部（随便访问）
lb.test()

#在子类和子对象中
print(ls._money)
ls._makeshoes()


