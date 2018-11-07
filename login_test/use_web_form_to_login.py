# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: use_web_form_to_login.py
@time: 2018/11/7
"""
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

#设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_test'

#设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s'% self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s'%self.name

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password = request.form['password']
        print(username,password)
        return password
    return render_template('index.html',method="")


if __name__ == '__main__':
    app.run(debug=True)