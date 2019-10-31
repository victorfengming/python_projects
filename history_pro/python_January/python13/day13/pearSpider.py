import requests
import re
from urllib.request import urlretrieve
import os

# 发送请求,获取响应

def pearvidoe_page(url):
    # url = 'https://www.pearvideo.com/category_8'
    html = requests.get(url).text
    # print(html)
    '''
    <a href="video_1512129" class="vervideo-lilink actplay" target="_blank">
    <a href="video_1512129" class="vervideo-lilink actplay">
    '''
    ret = re.findall('<a href="(.*?)" class="vervideo-lilink actplay">',html)
    # print(ret)
    # https://www.pearvideo.com/video_1512192
    start_url = 'https://www.pearvideo.com/'
    for end_url in ret:
        video_url = start_url + end_url
        # print(video_url)
        video_html = requests.get(video_url).text
        # print(video_html)
        video_down = re.findall('srcUrl="(.*?)",vdoUrl=srcUrl',video_html)
        # print(video_down)
        # 判断路径path是否存在
        path = 'pearVideo'
        if path not in os.listdir():
            os.mkdir(path)
        video_name = re.findall('<h1 class="video-tt">(.*?)</h1>',video_html)
        # print(video_name)
        print('正在下载: %s' % video_name[0])
        video_name = re.sub(r'''[\\/ :*?”<>|“：？"']''','',video_name[0])

        # urlretrieve(下载地址,保存位置)
        urlretrieve(video_down[0],path+'/'+video_name+'.mp4')

'''

https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=12
https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=24
https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=36


'''

def down_all():
    start_url = 'https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start='
    for end_url in range(1,1009):
        if end_url == 1:
            new_url = start_url + str(end_url)
            # print(new_url)
        elif end_url % 12 == 0:
            new_url = start_url + str(end_url)
        pearvidoe_page(new_url)

# 调用
# pearvidoe_page()
down_all()