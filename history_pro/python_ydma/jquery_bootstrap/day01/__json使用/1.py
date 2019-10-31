from flask import Flask
from flask import render_template
from flask import request
import json
import time
# 实例化flask对象
app = Flask(__name__)


# Flask已经内置了一个服务软件

# 路由
@app.route('/')
# 这个/代表根
def index():
    return '你好,晓明'


# 返回一个字符串
@app.route('/hello')
def hello():
    # 返回的的东西就是返回的内容
    return "<h1>你好你好哇</h1>"


@app.route('/page')
def page():
    return render_template('1.html')


@app.route('/daohang')
def daohang():
    return render_template('daohang.html')

@app.route('/post',methods=['POST','GET'])
def posts():
    return '没啥返回的了'

# 处理带参数的post请求,将拿到的数据返回给前端用户
@app.route('/msgposts',methods=['POST'])
def msgposts():
    # 接受数据
    userinfo = request.values.to_dict()
    print(userinfo)
    # 将数据入库
    # return str(userinfo)
    # json.jumps()将数据编码成json 的数据格式
    return json.jumps(userinfo)
# 带参数的get请求

@app.route('/msg')
def msg():
    # 接受用户发送的数据
    # request 请求对象 获取用户提交的数据必须通过request
    # value 获取用户请求的属性
    uname = request.values['name']
    print(uname)
    return render_template('2.html')

# 处理ajax方法的请求
@app.route('/ajax',methods=['POST','GET'])
def ajax():
    goosinfo = request.values.to_dict()
    # 给用户响应
    time.sleep(4)
    return json.dumps(goosinfo)





if __name__ == '__main__':
    # debug开启调试模式
    app.run(debug=True, port=9000, host='0.0.0.0')
    # host指定监听的ip地址,如果不指定,只能本机通过127.0.0.1访问
    # 可以指定为'0.0.0.0'监听所有本机可用的ip
