#父类
class Father(object):
    #成员属性
    familyname = '刘' #姓氏
    __firstname  = '备' #名字
    sex = '男' #性别
    age = 48    #年龄
    color = '黄色'#肤色
    #媳妇进行私有化操作
    __wife = ('甘夫人','糜夫人','孙尚香')

    #成员方法

    #吃饭
    def eat(self):
        print('甜甜圈，咖啡，面包，方便面~')

    #跑
    def run(self):
        print('拔起腿就跑~')

    #做鞋
    def makeshoes(self):
        print('做草鞋')


#打印Father类的成员
print(Father.__dict__)


#声明一个子类
class Son(Father):
    #父类私有化之后，子类独自添加的成员
    firstname = '禅'
    #添加子类独有的成员
    weight = '200斤'

    #做鞋（父类已经具有）  这个操做称之为方法重载
    def makeshoes(self):
        #重新定义功能即可
        print('做皮鞋，不是人造革，是真的皮')


    #跑路(重载父类的操作->在覆盖的同时还要使用原有内容)
    def run(self):
        #添加一个操作
        print('穿上鞋子')

        #调用以下父类的跑路方法(方法1)
        #super().run()#暂时可以认为super表示寻找父类

        #用以下父类的跑路方法(方法2)
        Father.run(self)

        #添加一个操作
        print('好汉饶命')

#打印子类的成员
print(Son.__dict__)


#实例化子类的对象
ls = Son() #子类的对象
#访问子类的姓氏
#print(ls.familyname)
#print(ls.sex)
#print(ls.age)
#ls.makeshoes()
#私有成员，仅仅允许原有类和原有类的对象访问，子类也不可以继承或者访问。
#print(ls.__wife)

#私有化性名
#print(ls.firstname)
#访问子类独有的成员
#print(ls.weight)
#访问做鞋功能
#ls.makeshoes()
#访问跑的方法
ls.run()