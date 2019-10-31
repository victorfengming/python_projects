#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>
'''
#创建集合
#空集合
setvar = set()
#打印数据类型和值
print(setvar,type(setvar))

#具有数据的集合
setvar = {'小明','小刚','小红','小吕','小朱'}
#打印数据类型和值
print(setvar,type(setvar))

#测试：集合中具有多个相同的数据
animal = {'小青蛙','小鸭鸭','小狗狗','小猫猫','小鸭鸭','小猫猫','小鸭鸭'}
print(animal,type(animal))


#测试2：集合中可以存放什么数据(列表不行,字典不行,正常集合不可以)
data = {10,2.5,True,2 + 3j,'小狗狗',(1,2,3)}
print(data,type(data))
'''

#
#声明一个集合
colors = {'红色','橙色','黄色','绿色','青色','蓝色','紫色'}
print(colors,type(colors))
#in
result = '棕色' in colors
print(result)

#not in
result = '棕色' not in colors
print(result)
#len()
girls= {'麦当娜','麦当劳','肯德基','汉堡王'}
result = len(girls)
print(result)

#max()
num = {23,223,24,6,23,42,46,458,579,1545,634}
result = max(num)
print(result)

#min()
num = {123,243,1234,24,53,6,234,24,64,-8,433,2347,483,25}
result = min(num)
print(result)

#set()  创建空集合  转换类型
lists = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(lists)

setvar = set(lists)
print(setvar)

#集合的遍历
#普通集合
computer = {'CPU','MEMORY','AUDIO','VIDEO','DISPLAY'}
for var in computer:
    print(var)

#嵌套集合的变量
friends = {
    ('小北','小京'),
    ('小上','小海'),
    ('小广','小州')
}

for one,two in friends:
    print(one,two)

#集合推导式
#普通推导式
nums = {1,2,3,4,5,6,7,8,9,10,11}
#要求：所有集合中的数据*5得到新的集合
result = {i * 5 for i in nums}
print(result)

#带有判断条件的集合推导式
nums = {1,2,3,4,5,6,7,8,9,10,11}
#要求：获取集合中所有的奇数，并且* 5组成新的集合
result = {i * 5 for i in nums if i % 2 == 1}
print(result)

#多循环集合推导式
set1 = {1,3,5,7,9}
set2 = {2,4,6,8,10}
#要求：集合1和集合2中的每个数据互相相加组成新的集合
result = {i + j for i in set1 for j in set2}
print(result)

#带有判断条件的多循环集合推导式
set1 = {'张飞','诸葛亮','赵云','黄月英'}
set2 = {'夏侯惇','典韦','许褚','曹操'}

#要求2个阵营的人物对抗，只选择2个字的人参战
result = {i + '--' + j for i in set1 for j in set2 if len(i) == 2 and  len(j) == 2}
print(result)

'''
#add()
#声明一个集合
fruits = {'apple','orange','pear'}
print(fruits)
#添加数据
fruits.add('banana')
print(fruits)


#pop()
#声明一个集合
it = {'php','java','lua','python','c','c++'}
print(it)
#删除数据
result = it.pop()
print(it,result)


#remove()
#声明一个集合
it = {'php','java','lua','python','c','c++'}
print(it)
#删除指定数据
result = it.remove('javascript')
print(it,result)


#discard()
#声明一个集合
it = {'php','java','lua','python','c','c++'}
print(it)
#删除指定数据
result = it.discard('javascript')
print(it,result)


#clear()
drink = {'冰糖雪梨','橙子汁','西瓜汁','椰汁','草莓汁'}
print(drink,id(drink))
#清空操作
result = drink.clear()
print(drink,id(drink),result)~


#copy()
fruit = {'樱桃','水蜜桃','扁桃','油桃','猕猴桃'}
print(fruit,id(fruit))
#复制集合
newfruit = fruit.copy()
print(newfruit,id(newfruit))


#集合运算
#差集  difference()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

#计算集合1相对于集合2的差集  （存在与集合1但是不存在于集合2的数据）
result = fruit1.difference(fruit2)
print(result)

#差集更新 difference_update()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

fruit1.difference_update(fruit2) #相当于 集合1变量 = 集合1 和集合2的差集
print(fruit1)


#交集 intersection()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

result = fruit1.intersection(fruit2)
print(result)



#交集更新 intersection_update()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

fruit1.intersection_update(fruit2)
print(fruit1)


#并集 union()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

result = fruit1.union(fruit2)
print(result)


#并集更新 update()

fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','草莓','樱桃','橘子'}

fruit1.update(fruit2)
print(fruit1)


#检测是否是超集  issuperset()
fruit = {'西瓜','椰子','香蕉','葡萄','芒果','猕猴桃'}
yellowfruit = {'香蕉','芒果'}

result = fruit.issuperset(yellowfruit)
print(result)


#检测是否是子集  issubset()
fruit = {'西瓜','椰子','香蕉','葡萄','芒果','猕猴桃'}
yellowfruit = {'香蕉','芒果'}

result = yellowfruit.issubset(fruit)
print(result)


#检测是否相交 isdisjoint()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','柚子','樱桃'}

result = fruit1.isdisjoint(fruit2)
print(result)


#对称差集  symmetric_difference()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','柚子','樱桃'}

result = fruit1.symmetric_difference(fruit2)
print(result)
'''

#对称差集更新  symmetric_difference_update()
fruit1 = {'苹果','梨','橘子','柚子','西瓜','草莓'}
fruit2 = {'橙子','桃子','葡萄','提子','柚子','樱桃'}

fruit1.symmetric_difference_update(fruit2)
print(fruit1)


'''
#空的冰冻集合
myset = frozenset()
#打印类型和值
print(myset,type(myset))

#创建具有数据的冰冻集合
myset = frozenset(['冰淇淋','老冰棍','奶油冰棍','小豆冰棍'])
print(myset,type(myset))


#冰冻集合不可以操作！
myset = frozenset(['红色','绿色','蓝色'])
print(myset,type(myset))

#复制操作可以使用
result = myset.copy()
print(result)
'''

color1 = frozenset(['red','green','blue','yellow'])#冰冻集合
color2 = {'cyan','blue','purple','pink'}#普通集合

'''
#difference()
result = color1.difference(color2)#冰冻集合作为主体的操作结果依然是冰冻集合
print(result)

result = color2.difference(color1)#普通集合作为主题的操作结果依然是普通集合
print(result)
'''

#difference_update()  冰冻集合作为主体不可以使用的
#color1.difference_update(color2)
color2.difference_update(color1)
print(color2)

















'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
