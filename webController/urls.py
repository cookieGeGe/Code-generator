# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:17 
# @Author :  
# @Site :  
# @File : urls.py 
# @Software: PyCharm


from flask import Blueprint

from webController import views

code_generator = Blueprint('code', __name__)

code_generator.add_url_rule('/', methods=['get', ], view_func=views.code_page)
code_generator.add_url_rule('/create/', methods=['post', ], view_func=views.create_code)
