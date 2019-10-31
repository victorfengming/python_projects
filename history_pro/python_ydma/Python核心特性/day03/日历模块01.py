#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xiaoming

# 本模块的功能:<>

# 1553387882

import calendar

# calendar()
# 功能:获取指定年份的日历字符串
# 格式:calendar.carlendar(年份,w = 2,l = 1,c = 6,m = 3)
# 返回值:字符串
#     w 表示 2个日期之间的间隔字符长度
#     l 表示 一个周占用几个行高度
#     c 表示2个月份之间的空白间隔
#     m 表示一行显示几个月
#
#
# cal_char = calendar.calendar(2019)
#
# print(cal_char)
'''
2019

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31


'''

# month()
# 功能:获取指定年月的日历字符串
# 格式:calendar.month(年,月,w = 2,l = 1)
# 返回值:字符串A

# eryue = calendar.month(2019,2)
#
# print(eryue)

'''
February 2019
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28
'''

# monthcalendar()
# 功能：获取一个年月的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 返回值：二级列表

# llist = calendar.monthcalendar(2019,2)
#
# print(llist)

'''
[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 0, 0, 0]]

'''
# 这个二级列表中每个元素都是一个星期的信息,第几个元素就是第几周,每个元素中的第一个子元素就是这周的星期几的日期日数,若没有这天,则为0
# 结果中0表示不是该月的数值，1-31才是当月信息


# isleap()
# 功能:检测指定年份是不是润年
# 格式:calendar.isleap(年份)
# 返回值:布尔值
#

# b = calendar.isleap(2020)
# print(b)
'''
True
'''
# b = calendar.isleap(2019)
# print(b)
'''
False
'''


# leapdays()
# 功能：检测指定年份之间的闰年个数
# 格式：calendar.leapdays(开始年份，结束年份)
# 返回值：整数
# 注意：包含开始年份不包含结束年份

# rnum = calendar.leapdays(1930,2020)
# print(rnum)
'''
22
'''


# monthrange()
# 功能：获取一个月的周几开始及当月天数
# 格式：calendar.monthrange(年，月)
# 返回值：元组(周几，天数)
# 注意：0-6表示周一到周天

# mtuple = calendar.monthrange(2019,2)
# print(mtuple)

'''(4, 28)'''


# weekday()
# 功能：根据年月日计算周几
# 格式：calendar.weekday(年，月，日)
# 返回值：整型  0-6 表示周一到周天

# week = calendar.weekday(2019,2,12)
# print(week)


# timegm()
# 功能：将时间元组转化为时间戳
# 格式：calendar.timegm(时间元组)
# 返回值：时间戳

sj = calendar.timegm((2019,2,12,14,47,3))
print(sj)


























