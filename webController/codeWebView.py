# -*- coding: utf-8 -*- 
# @Time : 2019/10/22 14:01 
# @Author :  
# @Site :  
# @File : codeWebView.py 
# @Software: PyCharm
import os

from APP.config import GENERATOR_DB, GENERATOR_TEMPLATES
from CodeGenerator.codeGeneratorfactory import CodeGeneratorFactory
from utils.sqlutils import mysql_db

BaseDir = os.path.dirname(os.path.abspath(__name__))


class CodeViewOptions:

    def __init__(self):
        pass

    @staticmethod
    def get_all_tables():
        query_tables = r"""
            select table_name,table_comment from information_schema.tables where table_schema='{}';
            """.format(GENERATOR_DB)
        all_tables = mysql_db.query(query_tables)
        table_list = []
        for table in all_tables:
            table_list.append({
                "name": table['table_comment'] if table['table_comment'] != '' else table['table_name'],
                "value": table['table_name']
            })
        return table_list

    @staticmethod
    def get_all_tamplates():
        templates_list = []
        for template in GENERATOR_TEMPLATES.keys():
            templates_list.append({
                "name": GENERATOR_TEMPLATES[template]['name'],
                "value": template
            })
        return templates_list

    @staticmethod
    def generator_file(generator_type, export_file, db_name, tb_name, other_dict):
        """生成文档"""
        factory = CodeGeneratorFactory()  # 初始化代码生成器工厂
        template = factory.get_codegenerator(generator_type)  # 获取指定类型代码生成器对象
        template.query_data(db_name, tb_name)  # 查询指定表数据
        data = template.formatter_data(other_dict)  # 格式化数据并返回
        template.render(data)  # 渲染模板
        if not os.path.exists(os.path.dirname(export_file)):
            os.makedirs(os.path.dirname(export_file))
        # if os.path.exists(export_file):
        #     raise Exception('文件已存在！')
        template.save(export_file.replace('.tpl', ''))  # 生成代码文件

    def formatter_and_create(self, tb_name, output, templates):

        for template in templates:
            if template not in GENERATOR_TEMPLATES.keys():
                continue
            template_file = GENERATOR_TEMPLATES[template]['template']
            export = os.path.join(BaseDir, *output.split('/'), template_file)
            self.generator_file(template, export, GENERATOR_DB, tb_name, {})
