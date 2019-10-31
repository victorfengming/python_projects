#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding by xiaoming

'''
当你的才华还撑不起你的野心时,那你就应该静下心来学习
当你的能力还驾驭不了你的目标时,那就应该沉下心来历练
'''

#
# # rongyu冗余的代码
# if file_extension == 'txt':
#     import txt_parse as txt
#
#     txt.open()
#     txt.read()
#     txt.close()
#
# elif file_extension == 'doc':
#     import txt_parse as doc
#
#     doc.open()
#     doc.read()
#     doc.close()
#
# elif file_extension == 'pdf':
#     import pdf_parse as pdf
#
#     pdf.open()
#     pdf.read()
#     pdf.close()
#

# rongyu冗余的代码
if file_extension == 'txt':
    import txt_parse as p

elif file_extension == 'doc':
    import txt_parse as p

elif file_extension == 'pdf':
    import pdf_parse as p

p.open()
p.read()
p.close()

# 这样来写就将代码合并了,更高效




















