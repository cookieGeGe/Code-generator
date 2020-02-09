# -*- coding: utf-8 -*-
# @Time : 2020/2/6
# @Author : zhang
# @Site :
# @File : functions.py
# @Software: PyCharm
from GeneratorFlask import CodeGenerator
# from NewApp.regist import regist

codeGenerator = CodeGenerator()


def init_ext(app):
    codeGenerator.init_app(app)
    # regist(codeGenerator)
