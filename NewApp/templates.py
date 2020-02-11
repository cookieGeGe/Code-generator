# -*- coding: utf-8 -*-
# @Time : 2020/2/5
# @Author : zhang
# @Site :
# @File : templates.py
# @Software: PyCharm
from NewApp.functions import codeGenerator


class GeneratorTeseHtml(codeGenerator.Template):
    """
    test.html模板渲染类 
    """
    template = 'test.html.tpl'

    def __init__(self):
        super(GeneratorTeseHtml, self).__init__()

    def formatter_data(self, other_data, expect_field=['ID']):
        filter_data = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
        data = {
            'columns': filter_data
        }
        data.update(dict(other_data))
        return data


class GeneratorTesePY(codeGenerator.Template):
    """
    test.py模板文件渲染类
    """
    template = 'test.py.tpl'

    def __init__(self):
        super(GeneratorTesePY, self).__init__()

    def formatter_data(self, other_data, expect_field=['ID']):
        filter_data = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
        data = {
            'columns': filter_data
        }
        data.update(dict(other_data))
        return data


class GeneratorViewPY(codeGenerator.Template):
    """
    test.py模板文件渲染类
    """
    template = 'views.py.tpl'

    def __init__(self):
        super(GeneratorViewPY, self).__init__()

    def formatter_data(self, other_data, expect_field=['ID']):
        filter_data = []
        time_list = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
                if column['name'].lower().find('time') != -1:
                    time_list.append(column['name'])
        capitalize_name = self.tb_name.split('_')[-1].capitalize()
        data = {
            'columns': filter_data,
            'tbname': self.tb_name,
            'BaseName': capitalize_name + 'Base',
            'queryName': 'Query' + capitalize_name,
            'createName': 'Create' + capitalize_name,
            'removeName': 'Remove' + capitalize_name,
            'formatter_time_list': time_list,
        }
        data.update(dict(other_data))
        return data

class GeneratorUrlPY(codeGenerator.Template):
    """
    test.py模板文件渲染类
    """
    template = 'url.py.tpl'

    def __init__(self):
        super(GeneratorUrlPY, self).__init__()

    def formatter_data(self, other_data, expect_field=['ID']):
        filter_data = []
        time_list = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
                if column['name'].lower().find('time') != -1:
                    time_list.append(column['name'])
        capitalize_name = self.tb_name.split('_')[-1].capitalize()
        data = {
            'columns': filter_data,
            'baseurl': self.tb_name.split('_')[-1].lower(),
            'BaseName': capitalize_name + 'Base',
            'queryName': 'Query' + capitalize_name,
            'createName': 'Create' + capitalize_name,
            'removeName': 'Remove' + capitalize_name,
        }
        data.update(dict(other_data))
        return data
