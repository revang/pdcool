#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from pdcool.utils.config import dbconfig as config
import logging

logging.basicConfig(level=logging.DEBUG)

# class DBUtil(dutool.DBUtil):
#     """
#     数据库工具类: 继承dutool.DBUtil，自动加载配置
#     """

#     def __init__(self):
#         super().__init__(dbconfig)


class DBUtil:
    def __init__(self):
        self.username = config.get("username")
        self.password = config.get("password")
        self.host = config.get("host")
        self.port = int(config.get("port"))
        self.database = config.get("database")

    def conn(self):
        self.db = pymysql.connect(user=self.username, passwd=self.password, host=self.host, port=self.port, database=self.database)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def queryone(self, sql):
        self.conn()
        logging.debug(sql)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.close()
        return res

    def query(self, sql):
        self.conn()
        logging.debug(sql)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.close()
        return res

    def show(self, sql):
        self.conn()
        logging.debug(sql)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.close()
        for row in rows:
            print(row)

    def __execute(self, sql):
        self.conn()
        logging.debug(sql)
        count = self.cursor.execute(sql)
        self.db.commit()
        self.close()
        return count

    def insert(self, sql):
        return self.__execute(sql)

    def update(self, sql):
        return self.__execute(sql)

    def delete(self, sql):
        return self.__execute(sql)

    def execute(self, sql):
        self.conn()
        logging.debug(sql)
        self.cursor.execute(sql)
        self.db.commit()
        self.close()

    def execute_list(self, sql_list):
        self.conn()
        for sql in sql_list:
            logging.debug(sql)
            self.cursor.execute(sql)
        self.db.commit()
        self.close()
