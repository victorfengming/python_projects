#水果类
class Fruit:
    pass
#方位
#南方类
class South:
    pass
#北方类
class North:
    pass


#苹果类
class Apple(Fruit,North):
    pass

#梨类
class Pear(Fruit,North):
    pass

#香蕉
class Banana(Fruit,South):
    pass

#桔子
class Orange(Fruit,South):
    pass