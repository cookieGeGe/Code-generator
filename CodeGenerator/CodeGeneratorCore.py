# -*- coding: utf-8 -*- 
# @Time : 2019/9/27 12:32 
# @Author :  
# @Site :  
# @File : CodeGeneratorCore.py
# @Software: PyCharm
import os
from jinja2 import Environment, FileSystemLoader


class CoreCodeGenerator(object):

    def __init__(self, template_dir):
        self.jinja = None
        self.template_dir = template_dir
        self._file_content = None
        self.template = None
        self.init()

    def init(self):
        """
        初始化对象
        :return:
        """
        if not os.path.exists(self.template_dir):
            raise Exception('路径不存在')
        if not os.path.isdir(self.template_dir):
            raise Exception('请选择正确的路径')
        self.jinja = Environment(loader=FileSystemLoader(self.template_dir))

    def get_template(self):
        """
        获取模板对象
        """
        return self.template

    def set_template(self, template):
        self.template = self.jinja.get_template(template)

    def render(self, *args, **kwargs):
        """
        渲染模板
        :param kwargs:模板中的参数
        :return:
        """
        if self.template is None:
            raise Exception('请选择设置模板')
        self._file_content = self.template.render(*args, **kwargs)

    def save(self, file_path, encoding='utf-8'):
        """
        模板输出到具体文件
        :param file_path:输出文件路径
        :param encoding:输出编码格式
        :return:
        """
        out_dir = os.path.dirname(file_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        try:
            with open(file_path, '+w', encoding=encoding) as f:
                f.write(self._file_content)
        except Exception as e:
            raise Exception(e)
