import re
# with open('index.html','a+',encoding='utf-8') as f:
#     res = f.read()
#     print(res)
# res = '1243sfd1343dsfgd'
# comp = re.findall('4', res,re.S)
# print(comp)
# for i in comp:
#     print('----------------------------')
#     print(i)
#
# f = open('index.html','a',encoding='utf-8')
# res = f.read()
# print(res)
import requests

url = 'file:///E:/PycharmProjects/python_January/%E5%85%84%E5%BC%9F%E8%BF%9Epython%E8%AF%BE%E4%BB%B6/index.html'

res = requests.get(url)