# 多级菜单
# 现在有 省,市,县 3级结构 ,要求程序启动后,允许用户可依次选择进入各子菜单
# 可在任意子菜单返回上一级
# 可以在任意一级菜单退出程序
# 提示: 列表  字典
'''
中国
    黑龙江
        哈尔滨
        齐齐哈尔

    吉林
        长春
        通化
    辽宁
        沈阳
        鞍山
        朝阳
    深圳

美国
    华盛顿
    纽约
    费城


'''
main = {
    "中国":{
        "黑龙江":{
            "哈尔滨":{}
        },
        "吉林":{
            "长春":{},
            "通化":{},
        },
        "辽宁":{
            "沈阳":{
                "铁西":{},
                "皇姑":{},
                "浑南":{
                    "沈阳理工大学":{},
                    "东北大学":{}
                },
            },
            "鞍山":{},
        }
    },
    "美国":{
        "华盛顿":{},
        "纽约":{},
        "费城":{}
    }

}

# def f(ini):
#     lieb = ini.keys()
#     for i in lieb:
#         print(i)
#     # print(country)
#     choicee = input("请选择:")
#     for i in lieb:
#         if i == choicee:
#             return i
#         else:
#             return None
#
#     return choicee

# while True:
# print(f(main))
# f(main)
while True:
    for i in main:
        print(i)#中国

    choice = input("请选择:")
    if not choice:
        continue
    if choice in main:
        while True:#进入第二层
                    #二极
            for i in main[choice]:
                print(i)#辽宁

            choice2 = input("请选择:")
            if not choice2:
                continue
            if choice2 in main[choice]:
                while True:
                    for i in main[choice][choice2]:
                        print(i)#沈阳
                    choice3 = input("请选择:")
                    if not choice3:
                        continue
                    if choice3 in main[choice][choice2]:
                        while True:
                            for i in main[choice][choice2][choice3]:
                                print(i)#浑南
                            choice4 = input("请选择:")
                            if not choice4:
                                continue
                            if choice4 in main[choice][choice2][choice3]:
                                for i in main[choice][choice2][choice3][choice4]:
                                    print(i)
                            elif choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit("baibai")
                            else:
                                print("节点不存在")
                    elif choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit("baibai")


else:

    print("节点不存在")
    elif choice2 == "b":
                break
            elif choice2 == "q":
                exit("baibai")

            else:
                print("节点不存在")

