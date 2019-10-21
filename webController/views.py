# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:17 
# @Author :  
# @Site :  
# @File : views.py 
# @Software: PyCharm


from flask import render_template,request


def code_page():
    return render_template('code.html', **{
        'table_list': [
            {
                "name": 'test',
                "value": 1
            },
            {
                "name": 'test1',
                "value": 2
            }
        ],
        "template_list":[
            {
                "name": 'list.html-列表页面',
                "value": 'list.html'
            },
            {
                "name": 'edit.html-新建编辑页面',
                "value": 'edit.html'
            },
            {
                "name": 'view.html-查看详情页面',
                "value": 'view.html'
            },
            {
                "name": 'views.py-后端视图',
                "value": 'views.py'
            },
            {
                "name": 'options_obj.py-表对象',
                "value": 'options_obj.py'
            },
            {
                "name": 'urls.py-路由管理',
                "value": 'urls.py'
            },
        ]
    })
