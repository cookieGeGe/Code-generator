# Code-generator

### 适用于python的代码生成器

该代码生成器目的旨在通过模板文件，生成相同模板的不同数据的代码文件（说白了就是为了在写web时偷懒少写一些针对表的增删改查操作）。

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