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
        self._init()

    def _init(self):
        self._generator = CodeGenerator(self.template_dir)

    def render(self, *args, **kwargs):
        self._generator.set_template(self.template)
        self._generator.render(*args, **kwargs)

    def save(self, out_file_path, encoding='utf-8'):
        self._generator.save(out_file_path, encoding)

    @abstractmethod
    def query_data(self):
        pass

    @abstractmethod
    def formatter_data(self):
        pass
