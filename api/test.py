#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:TT
#导包
import hashlib
from flask import request
from flask import Flask
#初始化一个实例
app = Flask(__name__)

#基础请求
@app.route('/')
def helloworld():
	return "helloword"
#get请求
@app.route('/get_request',methods=['GET'])
def get_request():
	return "get_request"
#post请求
@app.route('/post_request',methods=['POST'])
def post_request():
	return "post_request"
#get、post请求
@app.route('/get_post_request',methods=['POST','GET'])
def get_post_request():
	return "get_post_request"
#模拟带参数的请求
@app.route('/login',methods=['POST'])
def login():
	username = request.values.get("username")
	password = request.values.get("password")
	print(username,password)
	if username=='admin' and password =='123':
		return "sucess"
	else:
		return "fail"
#md5 加密
def md5(args):
	return hashlib.md5(str(args).encode('utf-8')).hexdigest()
	
#模拟带参数的请求,MD5加密
@app.route('/login_md5',methods=['POST'])
def login_md5():
	username = request.values.get("username")
	password = request.values.get("password")
	print(username,password)
	if username==md5('admin') and password ==md5('123'):
		return "sucess"
	else:
		return "fail"
	
	

if __name__== '__main__':
	app.run()
	#print(md5("admin"))
	