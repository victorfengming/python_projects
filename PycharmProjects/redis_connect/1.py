#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from flask import Flask,render_template,request
import redis



app = Flask(__name__)

@app.route('/add.html')

def add():
    return render_template('add.html')

@app.route('/addData',methods=['POST'])
def addData():
    data = {}
    info = request.values
    for k,v in info:
        data[k] = v
    # 联接数据库
    r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
    # 自增值
    r.incr('uid')
    # 哈希的批量存储
    # r.hmset('user:',data)
    return '添加成功'

if __name__ == '__main__':
    app.run(debug=True)

