# -*- coding: utf-8 -*- 
# @Time : 2019/10/16 13:01 
# @Author :  
# @Site :  
# @File : codeGeneratorfacotry.py 
# @Software: PyCharm
from CodeGenerator.CodeGeneratorBase import GeneratorTeseHtml, GeneratorTesePY


class CodeGeneratorFactory:

    def __init__(self):
        pass

    def get_codegenerator(self, generator_type):
        """
        获取指定代码生成器对象
        :param generator_type:对象类型
        :return:
        """
        if generator_type == 'test':
            return GeneratorTeseHtml()
        elif generator_type == "testpy":
            return GeneratorTesePY()
