# -*- coding: utf-8 -*-
# @Time : 2019/10/23 15:28
# @Author :
# @Site :
# @File : views.py
# @Software: PyCharm
import datetime
from copy import deepcopy

from flask import request, jsonify

from utils import status_code
from utils.BaseView import BaseView


class {{ BaseName }}(BaseView):

    def __init__(self):
        super({{ BaseName }}, self).__init__()
        self.total_sql = r"""SELECT FOUND_ROWS() as total_row;"""
        self.success = deepcopy(status_code.SUCCESS)
        self.device_list = []

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        pass


class {{ queryName }}({{ BaseName }}):
    """
    type 不等于空的时候表示获取指定parts id 的数据，为空时表示获取某个设备下的
    请求参数： {
            "se_key": 请求的查找的字段,
            "type": 为空表示搜索，其他为获取单个设备的详情
        }
    """

    def __init__(self):
        super({{ queryName }}, self).__init__()

    def main_uery(self, args):
        query_sql = r"""select * from {{ tbname }} """
        query_where_list = []
        if args.get('se_key', '') != '':
            query_where_list.append(r""" CONCAT(IFNULL(t2.ID,''))  LIKE '%{}%' """.format(args.get('se_key')))
        if query_where_list:
            query_sql += ' where '
            query_sql += ','.join(query_where_list)
        limit_sql = r""" limit {},{};""".format(
            (int(args.get('page', '1')) - 1) * int(args.get('pagesize', 10)),
            int(args.get('pagesize', 10))
        )
        return query_sql + limit_sql

    def views(self):
        args = request.args
        if args.get('type', '') == '':
            query_sql = self.main_uery(args)

        else:
            query_sql = r"""select * from {{ tbname }}  where id={}""".format(args.get('id'))
        result = self._db.query(query_sql)
        for index, item in enumerate(result):
            {% if (formatter_time_list | length) > 0 %}
            {% for item in formatter_time_list %}
            if '{{item}}' in item.keys():
                item['{{item}}'] = datetime.datetime.strftime(item['{{item}}'], "%Y-%m-%d %H:%M:%S")
            {% endfor %}
            {% else %}
            pass
            {% endif %}
        self.success['data'] = result
        return jsonify(self.success)


class {{ createName }}({{ BaseName }}):
    """
        请求参数：{
            form: 前端提交的form表单数据，表单中的数据需要和数据库中的字段名称对应,
            id: 如果为空则表示创建，具体数值则是编辑指定ID下的数据
        }
    """

    def __init__(self):
        super({{ createName }}, self).__init__()

    def get_create_sql(self, form):
        key_list = []
        value_list = []
        for key in form.keys():
            key_list.append(key)
            if isinstance(form[key], int):
                value_list.append(r""" {} """.format(form[key]))
            else:
                value_list.append(r""" '{}' """.format(form[key]))
        return ','.join(key_list), ','.join(value_list)

    def get_update_sql(self, form):
        set_list = []
        for key in form.keys():
            if isinstance(form[key], int):
                set_list.append(r""" {}={} """.format(key, form[key]))
            else:
                set_list.append(r""" {}='{}' """.format(key, form[key]))
        return ','.join(set_list)

    def remove_keys(self, form, *args):
        for arg in args:
            if arg in form.keys():
                del form[arg]
        return form

    def views(self):
        args = request.get_json()
        form = args.get('form', {})
        form = self.remove_keys(form, 'ID')
        if args.get('id', '') == '' or args.get('id') is None:
            # create
            insert_sql = r"""insert into {{ tbname }}({}) value ({});""".format(*self.get_create_sql(form))
            self._db.insert(insert_sql)
        else:
            # edit
            update_sql = r"""update {{ tbname }} set {} where id={};""".format(
                self.get_update_sql(form), args.get('id')
            )
            self._db.update(update_sql)
        return jsonify(self.success)


class {{ removeName }}({{ BaseName }}):

    """
        id: 要删除的ID
    """

    def __init__(self):
        super({{ removeName }}, self).__init__()

    def views(self):
        args = request.get_json()
        if args.get('id', '') == '':
            return jsonify(status_code.CONTENT_IS_NULL)
        delete_sql = r"""delete from {{ tbname }} where id = {};""".format(args.get('id'))
        try:
            self._db.delete(delete_sql)
        except:
            return jsonify(status_code.DB_ERROR)
        return jsonify(self.success)

