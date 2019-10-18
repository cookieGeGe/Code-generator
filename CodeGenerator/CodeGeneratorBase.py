# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 12:48 
# @Author :  
# @Site :  
# @File : CodeGeneratorBase.py 
# @Software: PyCharm
from abc import ABCMeta, abstractmethod

import os

from CodeGenerator.CodeGeneratorCore import CodeGenerator
from utils.sqlutils import mysql_db


class GeneratorBase(metaclass=ABCMeta):
    BaseDir = os.path.dirname(os.path.abspath(__name__))
    template_dir = os.path.join(BaseDir, 'template')

    def __init__(self, template, db=None):
        self._generator = None
        self.db = db
        self.template = template
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
        self._generator.set_template(self.template)
        self._generator.render(*args, **kwargs)

    def save(self, out_file_path, encoding='utf-8'):
        """
        保存文件
        :param out_file_path:
        :param encoding:
        :return:
        """
        self._generator.save(out_file_path, encoding)

    def query_data(self, db_name, tb_name):
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

    def __init__(self, template, db=None):
        super(GeneratorTeseHtml, self).__init__(template, db)

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
