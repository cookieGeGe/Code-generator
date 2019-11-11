# -*- coding: utf-8 -*-
# @Time : 2019/10/23 15:27
# @Author :
# @Site :
# @File : urls.py
# @Software: PyCharm


from flask import Blueprint

from . import views

devalarm = Blueprint('devalarm', __name__)

devalarm.add_url_rule('/devalarm/query', methods=['get', ], view_func=views.QueryDevalarm.as_view('query_devalarm'))
devalarm.add_url_rule('/devalarm/create', methods=['post', ], view_func=views.CreateDevalarm.as_view('create_devalarm'))
devalarm.add_url_rule('/devalarm/delete', methods=['delete', ], view_func=views.RemoveDevalarm.as_view('remove_devalarm'))
