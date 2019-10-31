#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming



'''王者荣耀
默认账号登陆
控制台输入账号和密码,
账号或密码不对,则重新输入,返回错误次数,超过三次输入错误则冻结账号
账号和密码对了
输出登陆成功
并可以选择英雄位置

'''



# # ------version1-----------------------------------------------
#
# # 定义选择英雄函数
# def hero_choice():
#     yingxionginfo = {"中单": "妲己,小乔,貂蝉",
#                      "打野": "李白,韩信,上官婉儿",
#                      "边路": "花木兰,曹操,程咬金",
#                      "辅助": "明世隐,张飞,盾山",
#                      "射手":"孙尚香,后裔,狄仁杰"}
#     while True:
#         keyy = input('''请选择您的英雄位置:
#         "中单"、"打野"、"边路"、"辅助"、"射手":
#         ''')
#         # 判断输入的位置时候在字典里面
#         if keyy not in yingxionginfo:
#             print("[系统提示]:您输入的位置不正确,重新输入")
#         else:
#             print("推荐您在以下英雄中选择:")
#             print(yingxionginfo[keyy])
#             yx = input("请选择英雄:")
#             print("您选择的英雄是%s"%yx)
#             break
#         pass
#
#     pass
#
# # 定义登陆函数
# def login():
#     # 系统的密码库 字典
#     lib = {"xiaoming":"19981221",\
#            "xiaoqiang":"19981223",\
#            "xiaohong":"19981225",\
#            "xiaogang":"19981227"}
#     i = 4   # 计数变量 用于验证输入次数
#     while i:    # i>0 循环
#         i -= 1  # 自减
#         print("[系统提示]:目前您有%d次错误机会"%i)
#         curr_account = input("请输入账号:")
#         curr_password = input("请输入密码:")
#         # 验证用户名是后在密码库中,并且密码与用户名匹配
#         if curr_account in lib and curr_password == lib[curr_account]:
#             # 如果匹配成功,打印提示信息
#             print("[系统提示]:密码输入正确,用户'%s'登陆成功"%curr_account)
#             return True     # 返回真,代表登陆成功
#         else:
#             print("[系统提示]:用户名或密码不正确,请重新输入")
#     else:   # 若循环正常结束,则为超出次数限制
#         print("您输入错误次数超过3次,账号已被冻结,请联系客服解冻")
#         return False    # 返回假,登陆失败
#     pass
#
#
#
#
# # 执行逻辑代码,将登陆功能与英雄选择功能分开,提升了代码的复用性和可维护性
# # 如果登陆成功
# if login():
#     # 调用英雄选择函数
#     hero_choice()
#

#
#
# # -----------------------version2--------------------------
# def hero_choice():
#     yx_info = {"中单": "妲己,小乔,貂蝉",
#                      "打野": "李白,韩信,上官婉儿",
#                      "边路": "花木兰,曹操,程咬金",
#                      "辅助": "明世隐,张飞,盾山",
#                      "射手":"孙尚香,后裔,狄仁杰"}
#     while True:
#         position = input('''请选择您的英雄位置:
#         "中单"、"打野"、"边路"、"辅助"、"射手":
#         ''')
#         if position not in yx_info:
#             print("[系统提示]:您输入的位置不正确,重新输入")
#         else:
#             print("推荐您选择以下英雄:")
#             print(yx_info[position])
#             break
#         pass
#
#     pass
#
# def login():
#     lib = {"xiaoming":"19981221","xiaoqiang":"19981223","xiaohong":"19981225","xiaogang":"19981227"}
#     i = 4
#     while i:
#         i -= 1
#         print("[系统提示]:目前您有%d次错误机会"%i)
#         curr_account = input("请输入账号:")
#         curr_password = input("请输入密码:")
#         if curr_account in lib and curr_password == lib[curr_account]:
#             print("[系统提示]:密码输入正确,用户'%s'登陆成功"%curr_account)
#             return True
#         else:
#             print("[系统提示]:用户名或密码不正确,请重新输入")
#     else:
#         print("您输入错误次数超过3次,账号已被冻结,请联系客服解冻")
#         return False
#     pass
#
#
#
#
#
# if login():
#     hero_choice()


#

# # -----------------------version3--------------------------
# def hero_choice():
#     yx_info = {"中单": "妲己,小乔,貂蝉",
#                      "打野": "李白,韩信,上官婉儿",
#                      "边路": "花木兰,曹操,程咬金",
#                      "辅助": "明世隐,张飞,盾山",
#                      "射手":"孙尚香,后裔,狄仁杰"}
#     while True:
#         position = input('''请选择您的英雄位置:
#         "中单"、"打野"、"边路"、"辅助"、"射手":
#         ''')
#         if position not in yx_info:
#             print("[系统提示]:您输入的位置不正确,重新输入")
#         else:
#             print("推荐您在以下英雄中选择:")
#             print(yx_info[position])
#             yx = input("请选择英雄:")
#             print("您选择的英雄是%s"%yx)
#             break
#         pass
#
#     pass
#
# def login():
#     lib = {"xiaoming":"19981221","xiaoqiang":"19981223","xiaohong":"19981225","xiaogang":"19981227"}
#     i = 4
#     while i:
#         i -= 1
#         print("[系统提示]:目前您有%d次错误机会"%i)
#         curr_account = input("请输入账号:")
#         curr_password = input("请输入密码:")
#         if curr_account not in lib :
#             print("[系统提示]:用户名不存在,请重新输入")
#         else:
#             if curr_password == lib[curr_account]:
#                 print("[系统提示]:密码输入正确,用户'%s'登陆成功"%curr_account)
#                 return True
#             else:
#                 print("[系统提示]:您输入的密码不正确,请重新输入")
#     else:
#         print("您输入错误次数超过3次,账号已被冻结,请联系客服解冻")
#         return False
#     pass
#
#
# if login():
#     hero_choice()
#
# #
# #cy
#
# i = 0
# while i<3:
#     i += 1
#     zh = input("请输入账号:")
#     mm = input("请输入密码:")
#     if zh!='cy' :
#         print("用户名或密码错误,请重新输入")
#     else:
#         if mm =='123':
#             print("用户'%s'登陆成功"%zh)
#             t = ('退出', '中单', '打野', '边路', '辅助', '射手')
#             wz = input("选择英雄位置(中单,打野,边路,辅助,射手)或退出游戏:")
#             wz = t.index(wz)
#             if wz > 5 or wz < 0:
#                 print('选择英雄位置(中单,打野,边路,辅助,射手)或退出游戏:')
#             elif wz == 0:
#                 break
#             else:
#                 if wz == 1:
#                     print("妲己,小乔,貂蝉")
#                 elif wz == 2:
#                     print("李白,韩信,上官婉儿")
#                 elif wz == 3:
#                     print("花木兰,曹操,程咬金")
#                 elif wz == 4:
#                     print("明世隐,张飞,盾山")
#                 elif wz == 5:
#                     print("孙尚香,后裔,狄仁杰")
#                 break
#         else:
#             print("密码不正确,请重新输入")
# else:
#     print("您输入错误次数超过3次,账号已被冻结,请联系客服解冻")

# -----------------------version4--------------------------

# 定义选择英雄函数
def hero_choice():
    # 英雄的位置信息
    yx_info = {"中单": "妲己,小乔,貂蝉",
               "打野": "李白,韩信,上官婉儿",
               "边路": "花木兰,曹操,程咬金",
               "辅助": "明世隐,张飞,盾山",
               "射手": "孙尚香,后裔,狄仁杰"}
    while True:
        position = input('''请选择您的英雄位置:
        "中单"、"打野"、"边路"、"辅助"、"射手":
        ''')
        if position not in yx_info:
            print("[系统提示]:您输入的位置不正确,重新输入")
        else:
            print("推荐您在以下英雄中选择:")
            print(yx_info[position])
            yx = input("请选择英雄:")
            print("您选择的英雄是%s" % yx)
            break
        pass

    pass


def login():
    # 用户的密码库信息
    lib = {"xiaoming": "19981221",
           "xiaoqiang": "19981223",
           "xiaohong": "19981225",
           "xiaogang": "19981227"}
    i = 4  # 用于计数输入密码错误的次数
    while i:  # 当i > 0 时循环
        curr_account = input("请输入账号:")
        curr_password = input("请输入密码:")
        # 判断用户名是否在密码库中
        if curr_account not in lib:
            print("[系统提示]:用户名不存在,请重新输入")
        else:
            # 验证用户密码是否正确
            if curr_password == lib[curr_account]:
                print("[系统提示]:密码输入正确,用户'%s'登陆成功" % curr_account)
                return True
            else:
                i -= 1
                print("[系统提示]:您输入的密码不正确,请重新输入")
                if i:
                    print("[系统提示]:目前您有%d次错误机会" % (i - 1))

    else:
        print("您输入错误次数超过3次,账号已被冻结,请联系客服解冻")
        return False
    pass


# 执行逻辑代码,将登陆功能与英雄选择功能分开,提升了代码的复用性和可维护性
# 如果登陆成功
if login():
    hero_choice()
