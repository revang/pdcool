#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author             : revang
Date               : 2022-01-01 17:38:01
Last Modified by   : revang
Last Modified time : 2022-01-01 17:38:01
"""

import pymysql
from pdcool.utils.database.config import db1 as dbconfig


class MysqlDBUtil:
    def __init__(self):
        self.username = dbconfig.get("username")
        self.password = dbconfig.get("password")
        self.host = dbconfig.get("host")
        self.port = int(dbconfig.get("port"))
        self.database = dbconfig.get("database")

    def conn(self):
        self.db = pymysql.connect(
            user=self.username,
            passwd=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def queryone(self, sql):
        self.conn()
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.close()
        return res

    def query(self, sql):
        self.conn()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.close()
        return res

    def show(self, sql):
        self.conn()
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.close()
        for row in rows:
            print(row)

    def __execute(self, sql):
        self.conn()
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
        self.cursor.execute(sql)
        self.db.commit()
        self.close()

    def execute_list(self, sql_list):
        self.conn()
        for sql in sql_list:
            self.cursor.execute(sql)
        self.db.commit()
        self.close()
