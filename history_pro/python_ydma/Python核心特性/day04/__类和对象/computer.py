#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

class Computer:
    # 成员属性
    cpu = 'i7-7700K'
    memory = '32GB'
    disk = '2TB'
    monitor = '144Hz'
    color = '白色'


    # 成员方法
    # 播放电影
    def play_film(self):
        print('电脑播放电影中')

    # 播放音乐
    def play_music(self):
        print('电脑播放云音乐中')

    # 玩游戏
    def play_games(self):
        print('正在使用电脑来玩游戏')



# 实例化类 获取电脑的对象

peco = Computer()

# 对于类的相关操作(很少使用)
#
# 检测类中的成员
print(Computer.__dict__)    # 打印类中的信息所构成的字典


# 对于对象的相关操作

# 检测对象中成员的方法
# print(peco.__dict__)    # 这个字典是空的


# 成员属性
'''
# 访问
print('处理器型号',Computer.cpu)
print('内存条',Computer.memory)


#修改
print(Computer.__dict__)
Computer.color = '灰色'   # 相当于变量重新赋值
print(Computer.__dict__)



# 添加

Computer.keyboard = '机械键盘'

print(Computer.__dict__)



# 删除

del Computer.memory

print(Computer.__dict__)
'''

# 成员方法
# 访问
# Computer.play_film(None)
# 添加(work功能)    # 不推荐使用
# 定义一个函数
# def work():
#     print('使用电脑办公中')
#
# Computer.work = work    # 也可以使用lambda表达式添加
# print(Computer.__dict__)

# # 修改
# Computer.play_film(None)
#
# Computer.play_film = lambda: print("电影展厅中")
#
# Computer.play_film()

# 删除
# del Computer.play_film  # 一定不要加括号,
#
# print(Computer.__dict__)

# peco.cpu = 'i9-8900Q'
# print(peco)
# print(peco.cpu)

# 对对象进行修改,修改的内容会保存在自己的里面


# 成员方法的操作

# 访问
# peco.play_film()    # 对象访问的时候不需要加参数了,这回,和类的访问不同,self会自动穿进去

# 添加
# print(peco.__dict__)
# peco.www = lambda : print('电脑上网中')
# print(peco.__dict__)

# 修改
# peco.play_games()
# peco.play_games = lambda : print('cf中.........')
# peco.play_games()
# print(peco.__dict__)

# 删除
# 添加一个方法
peco.input = lambda : print("电脑打字中")
print(peco.__dict__)
del peco.input

print(peco.__dict__)
