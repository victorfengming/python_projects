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
elif score in range(0,30):
    print("倔强青铜")
else :
    print("输入有误")

