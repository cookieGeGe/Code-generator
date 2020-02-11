# -*- coding: utf-8 -*-
# @Time : 2020/2/11
# @Author : zhang
# @Site :
# @File : mysqlUtils.py
# @Software: PyCharm


class MysqlDB(object):

    def __init__(self, db):
        self._db = db
        self._session = self._db.session

    def close(self):
        self._session.close()

    def query(self, sql):
        db_exe = self._session.execute(sql)
        data_list = list(map(lambda x: dict(zip(db_exe.keys(), x)), db_exe.fetchall()))
        return data_list

    def delete(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def update(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def insert(self, sql):
        db_exe = self._session.execute(sql)
        self._session.commit()
        return db_exe.lastrowid

    def execute(self, sql):
        sql_list = sql.split(';')
        for one_sql in sql_list:
            if one_sql != '':
                self._session.execute(one_sql + ';')
        self._session.commit()
