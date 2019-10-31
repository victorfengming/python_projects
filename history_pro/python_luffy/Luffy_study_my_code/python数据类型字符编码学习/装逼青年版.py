# 多级菜单
# 现在有 省,市,县 3级结构 ,要求程序启动后,允许用户可依次选择进入各子菜单
# 可在任意子菜单返回上一级
# 可以在任意一级菜单退出程序
# 提示: 列表  字典

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
                    "沈阳理工大学":{
                        "自动化与电气工程学院":{
                            "电子科学与技术":{
                                "一班":{
                                    "404":{
                                        "1":{

                                            "高数":{},
                                            "英语":{},
                                            "半导体":{
                                                "第一章":{},
                                                "第儿章":{},
                                                "第三目章":{}
                                            }
                                        },
                                        "2":{},
                                        "3":{},
                                        "4":{},

                                    }
                                },
                                "二班":{
                                    "604":{}
                                }

                            },
                            "测控技术与仪器":{
                                "一班":{
                                    "304":{}
                                }
                            }
                        }
                    },
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

current_layer = main
layers = []
j = 0#中国
# layers.append(current_layer)
print(j)
while True:
    # print(layers)
    for k in current_layer:
        print(k)
    choice = input(">>>:").strip()

    if not choice:
        continue
    if choice in current_layer:
        layers.append(current_layer)

        # print(layers[j])
        # j += 1#辽宁
        # print(j)
        current_layer = current_layer[choice]
    elif choice == "b":
        # j -= 1#中国
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print("这已经是最后一级了,不能再退了")
    elif choice == "q":
        exit("baibai")
        # print(j)

        # print(layers[j])





