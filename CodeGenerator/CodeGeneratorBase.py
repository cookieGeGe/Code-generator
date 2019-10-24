# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 12:48 
# @Author :  
# @Site :  
# @File : CodeGeneratorBase.py 
# @Software: PyCharm
from abc import ABCMeta, abstractmethod

import os

from jinja2 import TemplateNotFound

from CodeGenerator.CodeGeneratorCore import CodeGenerator
from dbConnect.sqlutils import mysql_db


class GeneratorBase(metaclass=ABCMeta):
    """
        模板代码生成器基类
    子类继承该类，实现formatter_data方法格式化数据到模板对象需要的数据类型
    template    指定模板路径及名称
    template_dir    jinja查找模板目录
    """
    template = None
    BaseDir = os.path.dirname(os.path.abspath(__name__))
    template_dir = os.path.join(BaseDir, 'template')

    def __init__(self, db=None):
        self._generator = None
        self.db = db
        self.tb_name = None
        self.table_info = None
        self._init()

    def _init(self):
        """
        初始化代码生成器核心对象，指定模板目录
        :return:
        """
        self._generator = CodeGenerator(self.template_dir)
        if self.db is None:
            self.db = mysql_db

    def render(self, *args, **kwargs):
        """
        渲染模板
        :param args:
        :param kwargs:
        :return:
        """
        if not self.template:
            raise TemplateNotFound('内部错误，没有找到模板文件')
        self._generator.set_template(self.template)
        self._generator.render(*args, **kwargs)

    def save(self, out_file_path, encoding='utf-8'):
        """
        保存文件
        :param out_file_path:
        :param encoding:
        :return:
        """
        save_path = os.path.join(out_file_path, self.template.replace('.tpl', ''))
        self._generator.save(save_path, encoding)

    def query_data(self, db_name, tb_name):
        self.tb_name = tb_name
        query_sql = r"""SELECT COLUMN_NAME as name,COLUMN_COMMENT as content,DATA_TYPE as datatype 
                        FROM information_schema.COLUMNS 
                        WHERE TABLE_NAME='{}' AND TABLE_SCHEMA='{}';""".format(tb_name, db_name)
        self.table_info = self.db.query(query_sql)

    @abstractmethod
    def formatter_data(self, *args, **kwargs):
        """
        针对子类进行数据格式化
        :param args:
        :param kwargs:
        :return:
        """
        pass


class GeneratorTeseHtml(GeneratorBase):
    """
    test.html模板渲染类
    """
    template = 'test.html.tpl'

    def __init__(self, db=None):
        super(GeneratorTeseHtml, self).__init__(db)

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


class GeneratorTesePY(GeneratorBase):
    """
    test.py模板文件渲染类
    """
    template = 'test.py.tpl'

    def __init__(self, db=None):
        super(GeneratorTesePY, self).__init__(db)

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


class GeneratorViewPY(GeneratorBase):
    """
    test.py模板文件渲染类
    """
    template = 'views.py.tpl'

    def __init__(self, db=None):
        super(GeneratorViewPY, self).__init__(db)

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

class GeneratorUrlPY(GeneratorBase):
    """
    test.py模板文件渲染类
    """
    template = 'url.py.tpl'

    def __init__(self, db=None):
        super(GeneratorUrlPY, self).__init__(db)

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
