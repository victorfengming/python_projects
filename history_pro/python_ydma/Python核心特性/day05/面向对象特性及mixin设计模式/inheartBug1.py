#菱形继承
'''
A类（动物类）

B类（人类）

C类（鸟类）

D类（鸟人类）
'''

#动物类   A类
class Animal:
    #发声的方法
    def say(self):
        print('Animal类准备开始发音')
        print('Animal类发音结束')

#人类    B类
class Human(Animal):
    #发音的方法
    def say(self):
        print('Human类准备开始发音')
        #调用父类中的发音功能
        Animal.say(self)
        print('Human类发音结束')



#鸟类   C类
class Bird(Animal):
    #发音的方法
    def say(self):
        print('Bird类准备开始发音')
        #调用父类的发音功能
        Animal.say(self)
        print('Bird类发音结束')

#鸟人类
class BirdMan(Human,Bird):
    #发音的方法
    def say(self):
        print('BirdMan类准备开始发音')
        #调用人类的发音
        Human.say(self)
        #调用鸟类的发音
        Bird.say(self)
        print('BirdMan类发音结束')


#实例化一个鸟人对象
bm = BirdMan()
#调用说话方法
bm.say()

#菱形继承中的bug所在，某个方法在继承中被多次调用！。（如果该方法具有唯一或者计时类似的特性则无法使用。）