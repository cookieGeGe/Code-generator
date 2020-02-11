# -*- coding: utf-8 -*-
# @Time : 2020/2/11
# @Author : zhang
# @Site :
# @File : settings.py
# @Software: PyCharm
import os

from NewApp.functions import get_db_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates_dir = os.path.join(BASE_DIR, 'template')

static_dir = os.path.join(BASE_DIR, 'static')

DATABASE = {
    # 用户
    'USER': 'root',
    # 主机
    'HOST': '127.0.0.1',
    # 密码
    'PASSWORD': 'admin123',
    # 端口
    'PORT': '3306',
    # 数据库类型
    'DB': 'mysql',
    # 数据库驱动
    'DRIVER': 'pymysql',
    # 使用的数据库
    'NAME': 'csms',
}

SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_POOL_TIMEOUT = 20
SQLALCHEMY_POOL_RECYCLE = 60
SQLALCHEMY_MAX_OVERFLOW = 5