# -*- coding: utf-8 -*-
# @Time : 2020/2/5
# @Author : zhang
# @Site :
# @File : template.py
# @Software: PyCharm
import os
from abc import abstractmethod, ABCMeta

from jinja2 import TemplateNotFound

from GeneratorFlask.mysqlUtils import MysqlDB


class GeneratorTemplate(metaclass=ABCMeta):
    """
        模板代码生成器基类
    子类继承该类，实现formatter_data方法格式化数据到模板对象需要的数据类型
    template    指定模板路径及名称
    template_dir    jinja查找模板目录
    _generator      全局生成器对象
    """
    template = None
    # BaseDir = os.path.dirname(os.path.abspath(__name__))
    # template_dir = os.path.join(BaseDir, 'template')
    template_dir = None
    _generator = None
    _db = None

    def __init__(self):
        self.tb_name = None
        self.table_info = None

    @classmethod
    def init(cls, template, generator, db):
        """
        初始化代码生成器核心对象，指定模板目录
        :return:
        """
        cls.template_dir = template
        cls._generator = generator
        cls._db = MysqlDB(db.db)

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
        self.table_info = self._db.query(query_sql)

    @abstractmethod
    def formatter_data(self, *args, **kwargs):
        """
        针对子类进行数据格式化
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def default_render_save(self, base_name, tb_name, output):
        self.query_data(base_name, tb_name)
        tempdata = self.formatter_data({})
        self.render(tempdata)
        self.save(output)
