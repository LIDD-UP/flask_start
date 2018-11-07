# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: test_login.py
@time: 2018/11/7
"""
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello World!</h1><a href="http://127.0.0.1:5000/signin">登录</a>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''
@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='123' and request.form['password']=='123':
        return '<h2>hello,admin</h2>'
    return '<h2>bad username or password</h2>'

if __name__ == '__main__':
    app.run()