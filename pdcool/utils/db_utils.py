#!/usr/bin/env python
# -*- coding:utf-8 -*-

import dutool
from pdcool.utils.config import dbconfig


class DBUtil(dutool.DBUtil):
    """
    数据库工具类: 继承dutool.DBUtil，自动加载配置
    """

    def __init__(self):
        super().__init__(dbconfig)
