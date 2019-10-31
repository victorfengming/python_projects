#random模块
import random#导入随机模块
import string
a = random.randint(1,100)
print(a)
'''
C:\Users\小明>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help(random)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
>>> import random
>>> random.randint(1,100)
53
>>> random.randint(1,100)
87
>>> random.randint(1,100)
52
>>> random.randint(1,100)
58
>>> random.randint(1,100)
30
>>> random.randint(1,100)
28
>>> random.randint(1,100)
23
>>> random.randint(1,100)
28
>>> random.randint(1,100)
42
>>> random.randint(1,100)
43
>>> ^Z


C:\Users\小明>dir
 驱动器 C 中的卷是 system
 卷的序列号是 8EBA-5A8D

 C:\Users\小明 的目录

2018/10/19  09:57    <DIR>          .
2018/10/19  09:57    <DIR>          ..
2018/04/27  12:27    <DIR>          .android
2018/09/19  18:17    <DIR>          .eclipse
2018/09/15  21:08    <DIR>          .idlerc
2018/09/18  17:32    <DIR>          .jmc
2018/09/19  18:17    <DIR>          .p2
2018/09/16  17:17    <DIR>          .PyCharmCE2018.2
2018/04/26  12:52    <DIR>          .tooling
2018/10/09  18:28    <DIR>          .WebStorm2017.2
2018/09/01  17:34    <DIR>          3D Objects
2018/09/01  17:34    <DIR>          Contacts
2018/10/21  11:20    <DIR>          Desktop
2018/09/22  13:45    <DIR>          Documents
2018/10/20  08:15    <DIR>          Downloads
2018/09/09  14:10    <DIR>          Favorites
2018/09/29  11:40    <DIR>          Links
2018/09/01  17:34    <DIR>          Music
2018/09/01  17:34    <DIR>          Pictures
2018/10/19  09:57               169 quartus2.ini
2018/09/01  17:34    <DIR>          Saved Games
2018/09/02  11:43    <DIR>          Searches
2018/07/22  20:51    <DIR>          temp
2018/09/15  15:21    <DIR>          Videos
2018/10/09  13:31               811 _viminfo
               2 个文件            980 字节
              23 个目录 35,539,623,936 可用字节

C:\Users\小明>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import
  File "<stdin>", line 1
    import
         ^
SyntaxError: invalid syntax
>>> import random
>>> random.choice("sjadhjkg")
'g'
>>> random.choice("sjadhjkg")
'g'
>>> random.choice("sjadhjkg")
'j'
>>> random.choice("sjadhjkg")
's'
>>> random.choice("sjadhjkg")
'j'
>>> random.choice("sjadhjkg")
'g'
>>> random.sample("klsjaljangen")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sample() missing 1 required positional argument: 'k'
>>> random.sample("klsjaljangen",2)^S
  File "<stdin>", line 1
    random.sample("klsjaljangen",2)
                                   ^
SyntaxError: invalid syntax
>>> random.sample("klsjaljangen",2)
['l', 'j']
>>> random.sample("klsjaljangen",2)
['a', 's']
>>> random.sample("klsjaljangen",2)
['e', 'j']
>>> random.sample("klsjaljangen",2)
['k', 's']
>>> random.sample("klsjaljangen",2)
['l', 'n']
>>> random.sample("klsjaljangen",2)
['l', 'g']
>>> random.sample("klsjaljangen",2)
['a', 'g']
>>> random.sample("klsjaljangen",2)
['j', 'k']
>>> random.sample("klsjaljangen",2)
['a', 'k']
>>> random.sample("klsjaljangen",2)
['l', 'e']
>>> random.sample("klsjaljangen",2)
['j', 'j']
>>> random.sample("klsjaljangen",2)
['n', 'j']
>>> random.sample("klsjaljangen",2)
['l', 's']
>>> random.sample("klsjaljangen",2)
['a', 'j']
>>> random.sample("klsjaljangen",2)
['l', 'l']
>>>
'''
