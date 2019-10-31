#电脑类
class Computer:
    #成员属性
    cpu = 'i7-7890'
    memory = '32G'
    disk = '1T'
    display = '120Hz'
    color = '黑色'

    #成员方法
    #播放电脑
    def play_movie(self):
        print('电脑播放电影中')

    #播放音乐
    def play_music(self):
        print('电脑播放音乐中')

    #玩游戏
    def play_game(self):
        print('正在使用电脑玩游戏')


#实例化类 获取电脑的对象
pc = Computer()

#对于类的相关操作（很少使用）
#检测类中的成员
#print(Computer.__dict__)

#成员属性
'''
#访问
print(Computer.cpu)
print(Computer.memory)
#修改
print(Computer.__dict__)
Computer.color = '灰色'#相当于变量重新赋值
print(Computer.__dict__)

#添加
print(Computer.__dict__)
Computer.keyboard = '机械键盘' 
print(Computer.__dict__)

#删除
print(Computer.__dict__)
del Computer.cpu
print(Computer.__dict__)
'''

#成员方法
'''
#访问
Computer.play_movie(None)

#添加(work)  不推荐使用
#定义一个函数
def work():
    print('使用电脑办公中')

Computer.work = work #也可以使用lambda表达式添加
print(Computer.__dict__)

#修改
Computer.play_movie(None)
Computer.play_movie = lambda : print('电影暂停中')
Computer.play_movie()

#删除
print(Computer.__dict__)
del Computer.play_movie #一定不要加括号。
print(Computer.__dict__)
'''




#=============================================
#对于对象的相关操作
#检测对象中成员
#print(pc.__dict__)

#成员属性的操作
'''
#访问
print(pc.cpu)
print(pc.disk)

#修改
print(pc.__dict__)
pc.cpu = 'i9-7890'
print(pc.__dict__)


#添加
print(pc.__dict__)
pc.closth = '钢化膜'
print(pc.__dict__)


#删除
print(pc.__dict__)
#del pc.cpu #不可以删除不属于当前对象的成员
#添加一个成员
pc.closth = '钢化膜'
print(pc.__dict__)
del pc.closth
print(pc.__dict__)
'''

#成员方法的操作
'''
#访问
pc.play_movie()   #和类访问不同，self会自动传入一个数据
#添加
print(pc.__dict__)
pc.www = lambda : print('电脑上网中')
print(pc.__dict__)

#修改
pc.play_game()
pc.play_game  = lambda :print('LOL中~')
pc.play_game()
print(pc.__dict__)

#删除
#添加一个方法
pc.input = lambda : print('电脑打字中~')
print(pc.__dict__)
del pc.input
print(pc.__dict__)
'''
