#设定抽象类 定义动物规则
import abc
class Animal(metaclass = abc.ABCMeta):

    #设定抽象方法 叫
    @abc.abstractmethod
    def say(self):
        pass


    #设定抽象方法 跑
    @abc.abstractmethod
    def run(self):
        pass


#声明小狗的类
class Dog(Animal):
    #设定抽象方法 叫
    def say(self):
        print('小狗汪汪叫')


    #设定抽象方法 跑
    def run(self):
        print('小狗四条腿跑~')


#声明小猫的类
class Cat(Animal):
    #设定抽象方法 叫
    def say(self):
        print('小猫喵喵叫~')


    #设定抽象方法 跑
    def run(self):
        print('小猫撒腿就跑~')

#声明小鸡的类
class Chick(Animal):
    #设定抽象方法 叫
    def say(self):
        print('小鸡咯咯叫')


    #设定抽象方法 跑
    def run(self):
        print('小鸡两条腿跑')


#实例化小狗，小猫和小鸡的对象
xiaohei = Dog()#小狗
xiaohua = Cat()#小猫
xiaofei = Chick()#小鸡


#声明行为类
class Action:
    #初始化方法
    def __init__(self,animal):
        #将接受的动物 保存到当前对象中
        self.animal = animal

    #叫的方法
    def jiao(self):
        #调用动物的叫的方法
        self.animal.say()

    #跑的方法
    def pao(self):
        self.animal.run()


#实例化行为类的对象
action = Action(xiaohei)

#调用行为对象的方法
action.jiao()
action.pao()

#修改传入的动物
action.animal = xiaohua
#调用行为对象的方法
action.jiao()
action.pao()

#修改传入的动物
action.animal = xiaofei
#调用行为对象的方法
action.jiao()
action.pao()