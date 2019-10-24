# -*- coding: utf-8 -*- 
# @Time : 2019/10/24 16:36 
# @Author :  
# @Site :  
# @File : PyCodeGenerator.py 
# @Software: PyCharm
import os

from CodeGenerator.codeGeneratorfactory import CodeGeneratorFactory


class CodeGenerator:
    """
    使用的代码生成器对象
    """

    def __init__(self):
        self.factory = CodeGeneratorFactory()
        self.generator = None
        self.data = None

    def init_generator(self, type):
        self.generator = self.factory.get_codegenerator(type)
        return self.generator

    def check_generator(self):
        if not self.generator:
            raise Exception('生成器没有初始化')

    def query_data(self, db_name, tb_name):
        self.check_generator()
        self.generator.query_data(db_name, tb_name)
        return self.generator.table_info

    def formatter_data(self, other_data={}, expect_field=[]):
        self.check_generator()
        self.data = self.generator.formatter_data(other_data, expect_field)
        return self.data

    def render(self, data=None):
        self.check_generator()
        if data is None:
            if self.data is None:
                raise Exception('未找到数据')
            data = self.data
        self.generator.render(data)

    def save(self, save_path):
        self.check_generator()
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        # if os.path.exists(export_file):
        #     raise Exception('文件已存在！')
        self.generator.save(save_path)  # 生成代码文件

    def generator_file(self, template_type, db_name, tb_name, save_path, other_data={}):
        self.init_generator(template_type)
        self.query_data(db_name, tb_name)
        self.formatter_data(other_data)
        self.render()
        self.save(save_path)
