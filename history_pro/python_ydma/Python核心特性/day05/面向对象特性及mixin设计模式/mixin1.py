#水果类
class Fruit:
    pass

#=========方位============
#南方水果类
class SouthFruit(Fruit):
    pass

#北方水果类
class NorthFruit(Fruit):
    pass
#==========送礼=============

''''''
#南方礼物水果
class SouthGiftFruit(SouthFruit):
    pass
#南方非礼物水果
class SouthNotgiftFruit(SouthFruit):
    pass

#北方礼物水果
class NorthGiftFruit(NorthFruit):
    pass
#北方非礼物水果
class NorthNotgiftFruit(NorthFruit):
    pass

#=============去皮=============

#==========真是水果==============
#苹果类
class Apple(NorthGiftFruit):
    pass

#梨类
class Pear(NorthNotgiftFruit):
    pass

#香蕉
class Banana(SouthNotgiftFruit):
    pass

#桔子
class Orange(SouthGiftFruit):
    pass