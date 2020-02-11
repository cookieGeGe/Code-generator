# Code-generator

### 适用于python的代码生成器

该代码生成器目的旨在通过模板文件，生成相同模板的不同数据的代码文件（说白了就是为了在写web时偷懒少写一些针对表的增删改查操作）。


### 构建Flask版本

#### 文档说明

    GeneratorFlask/__init__.py  Flask版本代码生成器核心对象
    
    GeneratorFlask/template.py  Flask版本模板处理对象基类
    
    GeneratorFlask/mysqlUtils.py    Flask版本基于SQLAlchemy链接mysql内部使用对象

#### 使用方法

1. 配置代码生成器模板目录：

```python
# 在Flask app的配置文件中加入 
CODEGENERATOR_TEMPLATE_DIR = '/temp/test'
```

2. 实例化代码生成器对象，并初始化

```python
from flask_sqlalchemy import SQLAlchemy

from GeneratorFlask import CodeGenerator

codeGenerator = CodeGenerator()
db = SQLAlchemy()

# SQLAlchemy的初始化必须在代码生成器的初始化之前，否则会出现在代码生成器初始化时找不到数据库连接对象
def init_ext(app):
    db.init_app(app)
    codeGenerator.init_app(app)
```

3. 实现对应模板处理子类

```python
from APP.functions import codeGenerator


class GeneratorTeseHtml(codeGenerator.Template):
    """
    test.html模板渲染类 
    """
    # 模板文件在代码生成器模板目录中的相对位置
    template = 'test.html.tpl'

    def __init__(self):
        super(GeneratorTeseHtml, self).__init__()

    # 重写该方法实现将数据转换为模板文件中需要的数据格式，带返回值
    def formatter_data(self, other_data, expect_field=['ID']):
        filter_data = []
        for column in self.table_info:
            if column['name'] not in expect_field:
                filter_data.append(column)
        data = {
            'columns': filter_data
        }
        data.update(dict(other_data))
        return data

```

4. 模板注册

- 调用模板注册
```python
from flask import Flask

from APP.functions import init_ext, codeGenerator
from APP.regist import regist
from APP.settings import templates_dir, static_dir


def create_app(config):
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.config.from_object(config)
    init_ext(app)
    # 实现模板注册的调用，之后则可以在全局下通过codeGenerator对象获取到指定模板的处理子类
    regist(codeGenerator)
    return app
```

-   模板注册
```python
from APP.templates import GeneratorTeseHtml


def regist(code):
    code.register_template('test', GeneratorTeseHtml)
```

5. 代码生成器的使用
- 基于codeGenerator对象中的已注册模板子类获取
```python
from APP.functions import codeGenerator

template_obj = codeGenerator.get_register_template('注册的模板名')
if template_obj:
    template_obj = template_obj()
    template_obj.default_render_save('db_name', 'tb_name', 'output_path')
```

- 引用具体的模板子类对象
```python
from APP.templates import GeneratorTeseHtml


template_obj = GeneratorTeseHtml()
template_obj.default_render_save('db_name', 'tb_name', 'output_path')
```

### 老版本

###### 使用说明：

    CodeGeneratorCore.py   代码生成器核心对象

    CodeGeneratorBase.py    代码生成器对象基类

    codeGeneratorfactory.py     代码生成工厂
    
    PyCodeGenerator.py      使用代码生成器可继承父类
    
### 测试生成

```python
import os

from CodeGenerator.PyCodeGenerator import CodeGenerator
from CodeGenerator.codeGeneratorfactory import CodeGeneratorFactory

BaseDir = os.path.dirname(os.path.abspath(__name__))
templatedir = os.path.join(BaseDir, 'template')


def generator_file(generator_type, export_file_path, db_name, tb_name, other_dict):
    """生成文档"""
    factory = CodeGeneratorFactory()  # 初始化代码生成器工厂
    template = factory.get_codegenerator(generator_type)  # 获取指定类型代码生成器对象
    template.query_data(db_name, tb_name)  # 查询指定表数据
    data = template.formatter_data(other_dict)  # 格式化数据并返回
    template.render(data)  # 渲染模板
    out_put = os.path.join(templatedir, *export_file_path.split('/'))  # 输出文件
    template.save(out_put)  # 生成代码文件


if __name__ == '__main__':
    generator_file('test', '/test/', 'waterdevice', 'wd_device', {'title': '设备测试页面'})
    generator_file('test', '/test/', 'waterdevice', 'wd_manager', {'title': '设备管理测试页面'})
    generator_file('test', '/test/', 'waterdevice', 'wd_devstatus', {'title': '设备状态测试页面'})

    code_generator = CodeGenerator()
    code_generator.generator_file('test', 'waterdevice', 'wd_device', '/test/', {'title': '设备测试页面'})

```

#### 下一步计划

    1. 完善生成的文件输出问题。
    2. 进一步完善flask版本代码生成器功能，查找设计不合理的地方并修改，避免循环引用的问题