#!/usr/bin/env python

# -*- Coding: UTF-8 -*-
# @Time    : 11/15/18 5:10 PM
# @Author  : Terry LAI
# @Email   : terry.lai@hotmail.com
# @File    : backend.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
