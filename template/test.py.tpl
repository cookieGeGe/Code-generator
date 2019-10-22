# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 15:26 
# @Author :  
# @Site :  
# @File : test.py
# @Software: PyCharm

def test():
    {% for column in columns %}
    {{column.name}} = '{{column.content}}'
    {% endfor %}
