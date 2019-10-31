#声明一个类（汽车类）
class MyCar:
    #成员属性
    grand = '宝马'  #品牌
    price = 15      #价格
    color = '粉色'  #颜色
    persons = 7     #座位数

    #成员方法
    #运动
    def move(self):
        print('汽车开始运动啦~')

    #制冷
    def make_cool(self):
        print('汽车空调制冷中')

    #加入
    def make_hot(self):
        print('汽车空调加入中')

#将汽车类实例化一个对象
car = MyCar()  #调用类得到一个对象


#查看类的信息
#类的id
print(id(MyCar))
#类的类型   type类型 <class 'type'>
print(type(MyCar))
#类的值     <class '__main__.MyCar'>
print(MyCar)

'''
补充信息：其实所有数据类型本质上都是一个类。

print(int)
print(float)
print(tuple)

int,float.list,tuple,set,dict  统统都是类，这些类是系统预先定义好的。
'''

#查看对象的信息
#对象的id
print(id(car))
#对象的类型      <class '__main__.MyCar'>
print(type(car))
#对象的值
print(car)


#对象的数据类型就是实例化他的类！