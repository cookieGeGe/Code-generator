import functools

import pymysql
import time
from DBUtils.PooledDB import PooledDB

from utils.config import DBConfig


class OPMysql:
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.pool = OPMysql.getmysqlconn()
        # self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            DATABASE = DBConfig.get_db_config('dev')
            __pool = PooledDB(creator=pymysql,
                              mincached=DATABASE.mincached,
                              maxconnections=5,
                              blocking=True,
                              host=DATABASE.host,
                              user=DATABASE.user,
                              passwd=DATABASE.password,
                              db=DATABASE.db,
                              port=int(DATABASE.port),
                              charset=DATABASE.charset)
            # print(__pool)
        # return __pool.connection()
        return __pool

    def connection(self):
        coon = self.pool.connection()
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
        return coon, cur

    # 插入\更新\删除sql
    def insert(self, sql, *args):
        coon, cur = self.connection()
        insert_num = cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)
        return insert_num

    def update(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)

    def delete(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)

    # 查询
    def query(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)  # 执行sql
        select_res = cur.fetchall()  # 返回结果为字典
        self.close(cur, coon)
        return select_res

    def execute(self, sql):
        coon, cur = self.connection()
        sql_list = sql.split(';')
        for one_sql in sql_list:
            if one_sql != '':
                coon.execute(one_sql + ';')
        coon.commit()
        self.close(cur, coon)

    def close(self, cur, coon):
        cur.close()
        coon.close()


mysql_db = OPMysql()
