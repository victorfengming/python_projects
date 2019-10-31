#先试试不用递归能不能做出来
a = int(input("请输入："))
while True :
    b = int(input("开始猜吧："))
    if a==b :
        print("行吧，算你厉害，猜对了")
        break
    elif a < b :
        print("哎哎，猜大了，从新猜：")
    elif a > b :
        print("哎哎，猜小了，从新猜：")
# 不对啊，做完好像不符合题目要求啊
# 等会儿，有点儿瑕疵，让我想想
