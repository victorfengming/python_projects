#单继承案例
'''
爷爷类
爸爸类
儿子类
'''

#爷爷类
class GroundFather:
    #属性
    skin = '黄色'

    #方法
    def say(self):
        print('说话中')


#爸爸类
class Father(GroundFather):
    #属性
    eye = '水汪汪的小眼睛'

    #方法
    def walk(self):
        print('走走~停停中~')


#儿子类
class Son(Father):
    pass


#实例化儿子对象
erzi = Son()
print(erzi)


#调用方法或者属性
print(erzi.skin)
print(erzi.eye)

erzi.say()
erzi.walk()