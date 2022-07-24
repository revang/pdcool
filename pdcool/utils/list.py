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


def find_list_in_twolist(list1, twolist1):
    """ 查找list是否在双重列表组中 
    案例: 
        list1 = [1, 2]
        twolist1 = [[[0, 1], [0, 2]], [[4, 4]]]
        print(find_list_in_twolist(list1, twolist1))

        list1 = [0, 2]
        twolist1 = [[[0, 1], [0, 2]], [[4, 4]]]
        print(find_list_in_twolist(list1, twolist1))
    """
    for idx1, val1 in enumerate(twolist1):
        for idx2, val2 in enumerate(val1):
            if list1 == val2:
                return [idx1, idx2]
    return [-1, -1]


def init_twoarray(row, column, val):
    """ 初始化二维数组
    案例: 
        twolist1 = init_twolist(3, 4, -1)
        print(twolist1)
    """
    return [[val]*column for i in range(row)]
