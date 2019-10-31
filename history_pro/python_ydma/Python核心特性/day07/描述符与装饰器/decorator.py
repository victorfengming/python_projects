'''
#第一步：声明一个普通函数即可
def love():
    print('亲亲')

#调用函数：
love()
love()
'''

'''
#第二步：增加功能
#定义增加功能的函数
def decor(func):
    #增加功能1
    print('抱抱')
    #调用基本函数
    func()#相当于调用love
    #增加功能2
    print('举高高')

#基本函数
def love():
    print('亲亲')

love = decor(love)#将基本函数作为参数传入装饰函数中

#调用函数
#love()
print(love)
'''

'''
#第三步：基本的装饰器

#装饰器函数
def decor(func):
    #声明一个内部函数
    def inner():
        # 增加功能1
        print('抱抱')
        # 调用基本功能
        func()
        # 增加功能2
        print('举高高')

    #必须返回函数
    return inner #未来的love函数

#基本函数
def love():
    print('亲亲')

love = decor(love)#装饰操作

#print(love)
#调用函数
love()
love()
love()
'''

'''
#第四步：装饰器语法
#装饰器函数
def decor(func):
    #定义内部函数 就是未来的love函数
    def inner():
        #增加功能1
        print('抱抱')
        #调用基本函数
        func()
        #增加功能2
        print('举高高')

    #返回内部函数
    return inner

#定义基本函数
@decor #装饰操作   等价于  love = decor(love)
def love():
    print('亲亲')

#调用函数
love()
love()

'''

#第五步：为基本函数添加 返回值和参数

"""
#返回值的处理方式
#定义装饰函数
def decor(func):
    #定义一个内部函数
    def inner():
        #增加的功能
        print('抱抱')
        #基本功能
        var = func()#相当于调用了love
        #增加的功能
        print('举高高')

        #返回一个值 是原有基本函数的返回值
        return var
    
    #返回内部函数
    return inner


#定义基本函数
@decor # love = decor(love)
def love():
    print('亲亲')
    return '❤'

#调用函数
result = love()
print(result)

result = love()
print(result)
"""
"""
#参数的处理方式
#定义装饰函数
def decor(func):
    #定义内部函数
    def inner(w1,w2):
        #增加功能1
        print('抱抱')
        #调用基本功能
        func(w1,w2) #相当调用love
        #增加功能2
        print('举高高')

    #返回内部函数inner  是未来的love函数
    return inner


#定义基本函数
@decor  # love = decor(love)
def love(who1,who2):
    print('{}亲亲{}'.format(who1,who2))


#调用函数
love('妈妈','女儿')
"""

'''
#第六步 加上收集参数（收集参数，关键字收集参数）

#定义装饰器
def decor(func):
    #定义内部函数
    def inner(*p,**w):#装饰之后的love函数
        #增加功能
        print('抱抱')
        #基本函数
        func(*p,**w)
        #增加功能2
        print('举高高')
    #返回内部函数
    return inner

#定义基本函数
@decor  # love = decor(love)
def love(*parent,**child):
    print(parent,'亲亲',child)

#调用基本函数
love('爸爸','妈妈',son = '儿子',girl = '女儿')
'''

'''
#第七步： 为装饰器添加参数

#定义装饰器  一个装饰器同时装饰多个函数（不同的函数装饰不同的内容）
def outer(arg): #调用outer返回装饰器
    #定义装饰器  #---------------------start----------------------
    def decor(func):
        #定义内部函数
        def inner():
            #判断正在装饰的函数
            if arg == 'xiao':
                # 增加功能
                print('我给你将一个笑话')
                # 调用基本函数
                func()
                # 增加功能
                print('肚子疼了吧')
            elif arg == 'ku':
                #增加功能1
                print('告诉你一个不行的消息')
                # 调用基本函数
                func()
                #增加功能2
                print('没事，节哀顺变~')
        #返回内部函数
        return inner
    #-----------------end---------------------------
    #返回装饰器
    return decor

#基本函数1
@outer('xiao')#@outer('xiao') ->@decor     #@函数
def smile():
    print('哈哈哈哈哈~')

#基本函数2
@outer('ku')#@outer('ku')  ->@decor #@函数
def cry():
    print('呜呜呜呜~')

#调用smile
#smile()

#调用cry
#cry()

'''

'''
#第八步： 将类作为参数传入装饰器中使用
#存在一个类，类中的方法是需要装饰的功能
class Parent:
    #成员方法
    #抱抱
    def baobao():
        print('抱抱')
    #举高高
    def jugaogao():
        print('举高高')


#装饰器外层
def outer(cls):
    #装饰器
    def decor(func):
        #定义内部函数
        def inner():
            #增加功能
            cls.baobao()
            #基本函数
            func()
            #增加功能2
            cls.jugaogao()
        #返回内部函数
        return inner
    #返回装饰器
    return decor
    
#基本函数
#@函数(类)  ->@装饰器
@outer(Parent)
def love():
    print('亲亲')


#调用函数
love()
'''

#第九步  将类作为装饰器 （用类做装饰器）

'''
#定义装饰器
#装饰器外层
def outer(arg):
    #装饰器
    def decor(func):
        #内部函数
        def inner():
            #增加功能
            print('抱抱')
            #基本函数
            func()
            #增加功能2
            print('举高高')

        #返回函数
        return inner
    #返回装饰器
    return decor
'''

#定义类作为装饰器
'''
1.可以带有区分或者使用的参数arg
2.具有接受基本函数传入的参数func
3.定义未来的函数 inner
'''

'''
class Outer:
    #初始化魔术方法
    def __init__(self,arg): #相当与outer函数
        #接受的参数为了其他成员方法可以使用  存入对象中
        self.arg = arg

    #一定要具有__call__魔术方法使得对象可以当作函数使用
    def __call__(self,func):#[这是装饰器的本体 相当于 decor函数]
        #将call接受的参数func 存入对象
        self.func = func
        #返回内部函数inner
        return self.inner

    # 定义内部函数inner
    #将inner作为类的方法存在
    def inner(self):
        # 增加功能
        print('抱抱')
        # 基本功能
        self.func()
        # 增加功能2
        print('举高高')

#基本函数
@Outer('ai') #@类() ->#@对象【对象可以当作函数使用】
def love():
    print('亲亲')

#调用函数
love()
'''

'''
#第十步 为类添加装饰器

#定义装饰器
def decor(cls):
    #定义内部信息（相当于原来的inner）
    def inner():
        #产生Human类的对象 [相当于基本功能]
        obj = cls()
        #添加内容 【相当于增加功能】
        obj.age = 1
        obj.sex = 'man'

        #返回对象
        return obj

    #返回inner函数
    return inner

#定义基本类
@decor
class Human:
    pass

#使用类  实例化对象
ren = Human() #相当于调用Human函数 得到了一个结果【对象】
print(ren)
print(ren.__dict__)

'''


# 第十一步： 多层装饰器嵌套
# 定义装饰器1
def decor1(func):
    # 定义内部函数
    def inner():
        # 增加功能1
        print('抱抱')
        # 调用基本功能
        func()
        # 增加功能2
        print('举高高')

    # 返回内部函数
    return inner


# 定义装饰器2
def decor2(func):
    # 定义内部函数
    def inner():
        # 增加功能
        print('转转')
        # 基本功能
        func()
        # 增加功能2
        print('笑一笑')

    # 返回内部函数
    return inner


#定义基本函数
@decor2
@decor1
def love():
    print('亲亲')


# 调用函数
love()

