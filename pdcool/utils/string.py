
def string_replace(text, replace_dict):
    """
    字符串替换多个值
    """
    res = text
    for key, val in replace_dict.items():
        res = res.replace(key, val)
    return res
