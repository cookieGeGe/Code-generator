# -*- coding: utf-8 -*- 
# @Time : 2019/10/18 13:31 
# @Author :  
# @Site :  
# @File : config.py 
# @Software: PyCharm


class DBConfig:

    def get_db_config(self, db_type):
        if db_type == 'dev':
            return Development()


class Development:
    host = 'localhost'
    user = 'root'
    password = 'admin123'
    port = 3306
    db = 'test'
    mincached = 2
    maxconnections = 5
    charset = 'utf8'
