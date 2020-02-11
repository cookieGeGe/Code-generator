# -*- coding: utf-8 -*-
# @Time : 2020/2/6
# @Author : zhang
# @Site :
# @File : functions.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy

from GeneratorFlask import CodeGenerator


def get_db_uri(DATABASE):
    user = DATABASE.get('USER')
    passwd = DATABASE['PASSWORD']
    host = DATABASE['HOST']
    port = DATABASE['PORT']
    name = DATABASE['NAME']
    db = DATABASE['DB']
    driver = DATABASE['DRIVER']

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, passwd,
                                           host, port,
                                           name)


codeGenerator = CodeGenerator()
db = SQLAlchemy()


def init_ext(app):
    db.init_app(app)
    codeGenerator.init_app(app)
