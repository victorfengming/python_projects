#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<用于测试时间模块的方法>


import time

# 时间模块中的常年
# print(time.timezone)
# print(time.altzone)
# print(time.daylight)
'''
-28800
-32400
0
'''
# 时间模块中的函数

# asctime()
# 功能:返回一给正常可读的时间字符串
# 格式:time.asctime(时间元祖)
# 返回值:时间字符串

# time_char = time.asctime()
# print(time_char)
'''
Tue Feb 12 15:27:05 2019
'''

# localtime()
# 功能：获取当前时间元组
# 格式1：time.localtime()
#     返回值：本地时间元组
#
# 格式2：time.localtime(时间戳)
#     返回值:指定时间戳的本地时间元组

# res = time.localtime()
# print(res)
'''
time.struct_time(tm_year=2019, tm_mon=2, tm_mday=12, tm_hour=15, tm_min=29, tm_sec=16, tm_wday=1, tm_yday=43, tm_isdst=0)
'''
# gmtime()
# 功能：获取当前UTC时间元组
# 格式1：time.gmtime()
#     返回值：当前UTC时间元组
#
# 格式2：time.gmtime(时间戳)
#     返回值：指定时间戳的UTC时间元组

# res = time.gmtime()
# print(res)
'''
time.struct_time(tm_year=2019, tm_mon=2, tm_mday=12, tm_hour=7, tm_min=30, tm_sec=46, tm_wday=1, tm_yday=43, tm_isdst=0)
'''

# ctime()
# 功能：获取本地时间的字符串格式
# 格式1： time.ctime()
#     返回值：时间格式字符串 相当于 asctime(localtime())
#
# 格式2： time.ctime(时间戳)
#     返回值：时间格式字符串 相当于asctime(localtime（时间戳）)

# res = time.ctime()
# print(res)
'''
Tue Feb 12 15:31:46 2019
'''

# mktime()
# 功能：使用时间元组制作时间戳
# 格式：time.mktime(时间元组)
# 返回值:时间戳
# 注意：按照本地时间来进行计算，如果想按照UTC时间计算，则是calendar.timegm()

# res = time.mktime(('2019','2','12','7','30','46','1'))
# print(res)

# print(time.clock())
# print(time.clock())

# print("beginnn")
# time.sleep(3)
# print("enddddd")

# print(time.time())

'''
strftime()
功能：格式化输出时间字符串（str foramt time）
格式：time.strftime('字符串格式'[,时间元组])
返回值：格式化之后的哦字符串
格式    含义        备注
%a    本地（locale）简化星期名称
%A    本地完整星期名称
%b    本地简化月份名称
%B    本地完整月份名称
%c    本地相应的日期和时间表示
%d    一个月中的第几天（01 - 31）
%H    一天中的第几个小时（24 小时制，00 - 23）
%I    一天中的第几个小时（12 小时制，01 - 12）
%j    一年中的第几天（001 - 366）
%m    月份（01 - 12）
%M    分钟数（00 - 59）
%p    本地 am 或者 pm 的相应符    注1
%S    秒（01 - 61）    注2
%U    一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周    注3
%w    一个星期中的第几天（0 - 6，0 是星期天）    注3
%W    和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始
%X    本地相应时间
%y    去掉世纪的年份（00 - 99）
%Y    完整的年份
%z    用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）
%%    %号本身
'''



# t = time.localtime()
# print(t)

# for i in t:
#     print(i)
# t_char = time.strftime('%c',t)
t_char = time.strftime('%c',(2019,2,12,16,9,15,1,43,0))
print(t_char)

# strptime()
# 功能：解析时间字符串成一个元组，strftime的逆向操作（str parse time）
# 格式：time.strptime('时间字符串','时间字符串格式')
# 返回值：时间元组

# t_2 = time.strptime(t_char,'%c')





