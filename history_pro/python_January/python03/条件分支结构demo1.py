# Coding by xiaoming
# -*- coding:utf-8 -*-
#
# age = int(input())
# if age >= 18:
#     print("chengnian")
# else:
#     print('miechengina')
#

'''
week = 3

if week == 1:
    print("今天是周一，路上人多，我做地铁")
elif week ==2:
    print("今天是周二,今天人很少,我去骑车上班")
elif week ==3:
    print("今天是周三,开手扶拖拉机上班")
elif week ==4:
    print("今天是周三,开手扶拖拉机上班")
elif week ==5:
    print("今天是周三,开手扶拖拉机上班")
elif week ==6:
    print("今天是周三,开手扶拖拉机上班")
else:#除了上面哪些条件,其余的情况,就执行这个代码
    print("因为周四翘班了,周末被领导抓到公司加班")

# 当一个分治执行后,其他分治将不再执行,当if和elif都不执行的时候,执行else
'''
'''
王者荣耀:
最强王者    100
至尊星耀    100-90
永恒钻石    90-80
尊贵铂金    80-70
荣耀黄金    70-60
秩序白银    60-30
倔强青铜    30以下
'''
score = int(input("请输入您的分数"))
# if score == 100:
#     print("最强王者")
# elif score >= 90:
#     print("至尊星耀")
# elif score >= 80:
#     print("永恒钻石")
# elif score >= 70:
#     print("尊贵铂金")
# elif score >= 60:
#     print("荣耀黄金")
# elif score >= 30:
#     print("秩序白银")
# else:
#     print("倔强青铜")
# while True:
score = int(input("请输入您的分数"))

if score in range(100,101):
    print("最强王者")
elif score in range(90,100):
    print("至尊星耀")
elif score in range(80,90):
    print("永恒钻石")
elif score in range(70,80):
    print("尊贵铂金")
elif score in range(60,70):
    print("荣耀黄金")
elif score in range(30,60):
    print("秩序白银")
else :
    print("倔强青铜")

