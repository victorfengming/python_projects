from urllib import request,parse
# import re,time,random

# url = "http://218.25.35.27:8080"

# 登录后的界面
url = "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/xscjcx.aspx?xh=1606030113&xm=%D3%DA%B7%EF%C3%F7&gnmkdm=N121605"

data = {

"TextBox1": "1606030113",
"TextBox2": "43EWsn"
}
header = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    # "Host": "218.25.35.27:8080",
    # "Referer": "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/default2.aspx",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# # 课程表界面
# url = "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/xs_main.aspx?xh=1606030113"
# header = {
#     # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     # "Accept-Encoding": "gzip, deflate",
#     # "Accept-Language": "zh-CN,zh;q=0.9",
#     # "Cache-Control": "max-age=0",
#     # "Connection": "keep-alive",
#     # "Host": "218.25.35.27:8080",
#     # "Referer": "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/default2.aspx",
#     # "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#
# }

#
# # 成绩18-19界面
# url = "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/xscjcx.aspx?xh=1606030113&xm=%D3%DA%B7%EF%C3%F7&gnmkdm=N121605"
#
# header = {
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Content-Length": "4223",
# "Content-Type": "application/x-www-form-urlencoded",
# "Host": "218.25.35.27:8080",
# "Origin": "http://218.25.35.27:8080",
# "Referer": "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/xscjcx.aspx?xh=1606030113&xm=%D3%DA%B7%EF%C3%F7&gnmkdm=N121605",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#
# }

#
# # 登录界面2
# url = 'http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/bm_main.aspx?xh=zidonghua'
#
# header = {
#
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Host": "218.25.35.27:8080",
# "Referer": "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/default2.aspx",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }

#
# # 信息界面
# url = "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/readimagexs.aspx?xh=1506030102"
#
# header = {
#
# "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Connection": "keep-alive",
# "Host": "218.25.35.27:8080",
# "R,ferer": "http://218.25.35.27:8080/(fb11ctawsjagao55gv3rbvyi)/xsxx.aspx?xh=zidonghua&xm=%D7%D4%B6%AF%BB%AF%B8%A8%B5%BC%D4%B1&gnmkdm=N120306",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }

# 学生登录页面
# url = ''
#
# header = {
#
#
# }

req = request.Request(url,data = data,headers=header)
'''
def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
'''
rr = request.urlopen(req)
print(rr)
print(req)
strr = rr.read().decode("gb2312")

print(strr)