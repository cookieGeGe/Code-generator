# -*- coding: utf-8 -*-
# @Time : 2020/2/6
# @Author : zhang
# @Site :
# @File : regist.py
# @Software: PyCharm
from APP.templates import GeneratorTeseHtml, GeneratorTesePY, GeneratorUrlPY, GeneratorViewPY


def regist(code):
    code.register_template('test', GeneratorTeseHtml)
    code.register_template('testpy', GeneratorTesePY)
    code.register_template('url', GeneratorUrlPY)
    code.register_template('view', GeneratorViewPY)
