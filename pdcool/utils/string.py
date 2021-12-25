
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
