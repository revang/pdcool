#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 18:47:01
Last Modified by  : revang
Last Modified time: 2022-01-01 18:47:01
"""

import datetime
import logging
import time

from pdcool.utils.string import string_replace


def current_date(date_length=10):
    """ 获取当前日期

    :param date_length: 日期长度
    :return: 当前日期
    """
    if date_length == 8:
        return time.strftime("%Y%m%d", time.localtime())
    if date_length == 10:
        return time.strftime("%Y-%m-%d", time.localtime())
    raise ValueError(f"invalid length: {date_length}")


def current_time():
    """ 获取当前时间

    :return: 当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def date_range(begin_date, end_date, date_length=10):
    """ 遍历日期

    :param begin_date: 开始日期
    :param end_date: 结束日期
    :return: 日期列表
    """
    if date_length == 8:
        begin = datetime.date(int(begin_date[0:4]), int(begin_date[4:6]), int(begin_date[6:8]))
        end = datetime.date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
        date_list = []
        for i in range((end-begin).days+1):
            curr_date = begin+datetime.timedelta(days=i)
            curr_date = curr_date.strftime("%Y%m%d")
            date_list.append(curr_date)
        return date_list

    if date_length == 10:
        begin = datetime.date(int(begin_date[0:4]), int(begin_date[5:7]), int(begin_date[8:10]))
        end = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))

        date_list = []
        for i in range((end-begin).days+1):
            curr_date = begin+datetime.timedelta(days=i)
            curr_date = curr_date.strftime("%Y-%m-%d")
            date_list.append(curr_date)
        return date_list

    raise ValueError(f"invalid date_type: {date_length}")


def date_format(curr_date, origin_type="YYYY-MM-DD", target_type="YYYYMMDD"):
    """ 格式化日期

    :param curr_date: 输入日期
    :param origin_type: 输入日期类型
    :param target_type: 输出日期类型
    :return: 输出日期
    """
    replace_dict = {
        "YYYY": "%Y",
        "MM": "%m",
        "DD": "%d",
        "HH24": "%H",
        "MI": "%M",
        "SS": "%%S"
    }
    origin = string_replace(origin_type, replace_dict)
    target = string_replace(target_type, replace_dict)
    res = datetime.datetime.strptime(curr_date, origin)  # 字符串 ---> 日期
    res = datetime.datetime.strftime(res, target)        # 日期 ---> 字符串
    return res
