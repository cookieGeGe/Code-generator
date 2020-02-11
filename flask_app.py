# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:12 
# @Author :  
# @Site :  
# @File : flask_app.py 
# @Software: PyCharm

from APP.APP import create_app
from APP.config import Config
from webController.urls import code_generator

app = create_app(Config)

app.register_blueprint(code_generator, url_prefix='/code')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
