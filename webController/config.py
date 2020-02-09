# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 13:12 
# @Author :  
# @Site :  
# @File : config.py 
# @Software: PyCharm

GENERATOR_DB = 'csms'
GENERATOR_TEMPLATES = {
    "test": {
        "template": 'test.html.tpl',
        "name": "test.html-测试模板"
    },
    "testpy": {
        "template": 'test.py.tpl',
        "name": "test.py-测试模板"
    },
    "view": {
        "template": 'views.py.tpl',
        "name": "views.py-视图函数"
    },
    "url": {
        "template": 'url.py.tpl',
        "name": "url.py-路由函数"
    }
}
