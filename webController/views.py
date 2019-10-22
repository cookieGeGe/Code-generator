# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 11:17 
# @Author :  
# @Site :  
# @File : views.py 
# @Software: PyCharm


from flask import render_template, request, jsonify

from webController.codeWebView import CodeViewOptions


def code_page():
    return render_template('code.html', **{
        'table_list': CodeViewOptions.get_all_tables(),
        "template_list": CodeViewOptions.get_all_tamplates()
    })


def create_code():
    table_name = request.form.get('tablename', '')
    templates = request.form.getlist('templates[]')
    output = request.form.get('output', '')
    if table_name == '' or len(templates) == 0 or output == '':
        return jsonify({'code': 400, 'msg': '必填参数'})
    try:
        CodeViewOptions().formatter_and_create(table_name, output, templates)
        return jsonify({'code': 200, 'msg': '请求成功', 'data': request.form.to_dict()})
    except Exception as e:
        if len(e.args) > 1 and e.args[0] == '文件已存在！':
            return jsonify({'code': 200, 'msg': '指定目录下存在同名文件，停止创建。'})
        import traceback
        print(traceback.format_exc())
        return jsonify({'code': 0, 'msg': '生成失败'})
