#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>


# 水果类
class Fruit:
    pass


# 南方水果类
class SouthFruit(Fruit):
    pass


# 北方水果类
class NorthFruit(Fruit):
    pass


#能不能送礼

# 南方礼物水果
class SouthGiftFruit(SouthFruit):
    pass
# 南方非礼物水果
class SouthNotGiftFruit(SouthFruit):
    pass

# 北方礼物水果
class NorthGiftFruit(SouthFruit):
    pass
# 南方非礼物水果
class NorthNotGiftFruit(SouthFruit):
    pass

# 苹果类
class Apple(NorthGiftFruit):
    pass

# lidelei
class Pear(NorthNotGiftFruit):
    pass

# 香蕉
class Banana(SouthFruit):
    pass


# 桔子
class Orange(NorthFruit):
    pass



'''
单继承这么写就比较复杂,我如果想要增加一个分类就需要增加几何倍数增长的继承类
'''









'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''
