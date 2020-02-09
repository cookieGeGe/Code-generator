# -*- coding: utf-8 -*-
# @Time : 2020/2/6
# @Author : zhang
# @Site :
# @File : APP.py
# @Software: PyCharm
from flask import Flask

from NewApp.functions import init_ext,codeGenerator
from NewApp.regist import regist


def create_app(templates_dir, static_dir):
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    init_ext(app)
    regist(codeGenerator)
    return app