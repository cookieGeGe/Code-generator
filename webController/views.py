# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:17 
# @Author :  
# @Site :  
# @File : views.py 
# @Software: PyCharm


from flask import render_template


def code_page():
    return render_template('code.html', **{'table_list': [
        {
            "name": 'test',
            "value": 1
        },
        {
            "name": 'test1',
            "value": 2
        }
    ]})
