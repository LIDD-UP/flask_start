# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: flask_start.py
@time: 2018/11/2
"""
from flask import Flask


# 实例化flask

app = Flask(__name__)

# 定义view函数

@app.route('/')
def index():
    return 'hello my flask'


@app.route('/user/<int:id>')
def user(id):
    return 'hello %d'%id


from flask import abort
# 如果出现错误可以终止试图函数的运行；
# 这个可以用来给前端传递http状态吗；
@app.route('/test_abort')
def test_abort():
    abort(404)
    return 'hello it flask',999


# flask 通过装饰器来捕获异常
@app.errorhandler(404)
def error(e):
    return '你请求的页面不存在%s'%e


# 重定向示例
from flask import redirect


@app.route('/test_redirect')
def test_redirect():
    return redirect('/')


# 测试正则匹配指定的url
from werkzeug.routing import BaseConverter

class Regex_url(BaseConverter):
    def __init__(self,url_map,*args):
        super(Regex_url,self).__init__(url_map)
        self.regex = args[0]

app.url_map.converters['re'] = Regex_url

@app.route('/test_regex/<re("[a-z]{3}"):id>')
def test_regex(id):
    return 'hello flask %s' %id


# 设置和获取cookie
from flask import make_response
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username','bler')
    return resp

# 获取cookie
from flask import request
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp


# 使用Manager；即flask_script
from flask_script import Manager

manage = Manager(app)



# 启动flask

if __name__ == '__main__':
    # app.run(debug=False)
    manage.run()