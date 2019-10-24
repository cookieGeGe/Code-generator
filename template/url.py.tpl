# -*- coding: utf-8 -*-
# @Time : 2019/10/23 15:27
# @Author :
# @Site :
# @File : urls.py
# @Software: PyCharm


from flask import Blueprint

from . import views

{{ baseurl }} = Blueprint('{{ baseurl }}', __name__)

{{ baseurl }}.add_url_rule('/{{ baseurl }}/query', methods=['get', ], view_func=views.{{ queryName }}.as_view('query_{{ baseurl }}'))
{{ baseurl }}.add_url_rule('/{{ baseurl }}/create', methods=['post', ], view_func=views.{{ createName }}.as_view('create_{{ baseurl }}'))
{{ baseurl }}.add_url_rule('/{{ baseurl }}/delete', methods=['delete', ], view_func=views.{{ removeName }}.as_view('remove_{{ baseurl }}'))

