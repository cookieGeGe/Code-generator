# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:12 
# @Author :  
# @Site :  
# @File : flask_app.py 
# @Software: PyCharm
import os
from flask import Flask

from webController.urls import code_generator

basedir = os.path.dirname(os.path.abspath(__name__))

templates_dir = os.path.join(basedir, 'template')
static_dir = os.path.join(basedir, 'static')

app = Flask(__name__,template_folder=templates_dir, static_folder=static_dir)

app.register_blueprint(code_generator, url_prefix='/code')


if __name__ == '__main__':
    app.run(port=8081)
