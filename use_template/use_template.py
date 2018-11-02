# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: use_template.py
@time: 2018/11/2
"""
from flask import Flask,render_template

# 定义flask实例
app = Flask(__name__)

@app.route('/test_template/<name>')
def test_template(name):
    return render_template('test_template.html',name=name)


@app.route('/test_template2')
def test_template2():
    dict1 = {'name':'bler'}
    list1 = ['a','b','c']
    return render_template('test_template.html',dict1=dict1,list1=list1)


if __name__ == '__main__':
    app.run(debug=True)