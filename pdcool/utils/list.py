#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 18:47:20
Last Modified by  : revang
Last Modified time: 2022-01-01 18:47:20
"""


def list_split(list_collection, num):
    """
    将集合均分，每份n个元素
    :param list_collection:
    :param num:
    :return: 返回的结果为均分后的每份可迭代对象
    """
    for i in range(0, len(list_collection), num):
        yield list_collection[i: i + num]
