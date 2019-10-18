# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 12:48 
# @Author :  
# @Site :  
# @File : CodeGeneratorBase.py 
# @Software: PyCharm
from abc import ABCMeta, abstractmethod

from CodeGenerator.PyCodeGenerator import CodeGenerator


class GeneratorBase(metaclass=ABCMeta):
    template_dir = ''

    def __init__(self, db, template):
        self._generator = None
        self.db = db
        self.template = template
        self.table_info = None
        self._init()

    def _init(self):
        self._generator = CodeGenerator(self.template_dir)

    def render(self, *args, **kwargs):
        self._generator.set_template(self.template)
        self._generator.render(*args, **kwargs)

    def save(self, out_file_path, encoding='utf-8'):
        self._generator.save(out_file_path, encoding)

    @abstractmethod
    def query_data(self, db_name, tb_name, expect_field=['ID']):
        query_sql = r"""SELECT COLUMN_NAME as name,COLUMN_COMMENT as content,DATA_TYPE as datatype 
                        FROM information_schema.COLUMNS 
                        WHERE TABLE_NAME='{}' AND TABLE_SCHEMA='{}';""".format(tb_name, db_name)
        self.table_info = self.db.query(query_sql)
        filter_data = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
        return filter_data

    @abstractmethod
    def formatter_data(self):
        pass
