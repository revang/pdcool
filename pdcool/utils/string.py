#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 18:47:41
Last Modified by  : revang
Last Modified time: 2022-01-01 18:47:41
"""




def string_replace(text, replace_dict):
    """  根据字典替换字符串的值

    :param text 字符串
    :param replace_dict 替换字典
    :return: 替换后的值
    """
    res = text
    for key, val in replace_dict.items():
        res = res.replace(key, val)
    return res


def is_valid_mail(text):
    """ 验证邮件地址 """
    None


def is_valid_mobilephone(text):
    """ 验证手机号码 """
    None


def is_valid_identiynumber(text):
    """ 验证身份证号 """
    None
