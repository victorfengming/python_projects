import requests
import re
import os
from urllib import request
import time
'''
妹子图网站反扒手段 ,限制方位来源,需在headers中加入 Referer 跳转来源
urlretrieve 无法加入请求头headers
我们使用bytes直接下载图片
同时需注意限制访问时间间隔,访问频次过快,服务器进制访问

#### 注意图片下载地址是.jpg格式,我们下午使用链接不正确所以可以下载但无法打开

'''
def ori_video(meizi_url):
    headers = {
        'Referer': 'https://www.mzitu.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    # print(meizi_url)
    meizi_html = requests.get(meizi_url,headers = headers).text
    end_url = re.findall("<span>(\d+?)</span></a><a href='https://www.mzitu.com/\d*?/2'><span>下一页&raquo",meizi_html)
    name_id = re.search('<h2 class="main-title">(.*?)</h2>',meizi_html).group(1)
    name = re.sub('!','',name_id)
    print(end_url)
    end_url = int(end_url[0])

    for x in range(1,end_url):
        newurl = meizi_url + '/' + str(x)

        # print(name)
        newurl = meizi_url + '/' +  str(x)
        # print(newurl)
        html = requests.get(newurl,headers = headers).text
        end_re = re.findall(r'<div class="main-image"><p><a href=".+?" ><img src="(.*?)"',html)
        print(end_re[0])



        headers = {
            'Referer': 'https://www.mzitu.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
        }
        # urlretrieve(end_re[0],path+'/'+ str(x)) 不能加请求头
        req = request.Request(end_re[0],headers = headers)
        response = request.urlopen(req)
        fname = end_re[0].split('/')[-1]
        print('正在下载: ',fname)

        if name not in os.listdir():
            os.mkdir(name)
        with open(name + '/' + fname, 'wb') as f:
            f.write(response.read())
        ''' 反反爬  设置时间间隔 防止服务器封锁IP或禁止访问'''
        time.sleep(1)


# 下载一页的内容
def page_one():
    url = 'https://www.mzitu.com/'
    headers = {
        'Referer': 'https://www.mzitu.com',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    html = requests.get(url,headers = headers).text
    # print(html)
    ret = re.findall('<li><a href="(.*?)" target="_blank"><img class=',html)
    print(ret)
    # for meizi_url in ret:
    meizi_url = 'https://www.mzitu.com/166998'
    ori_video(meizi_url)











# 调用
page_one()