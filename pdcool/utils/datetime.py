import logging
import time
import datetime
from pdcool.utils.string import string_replace


def current_date(date_length=10):
    """
    当前日期
    """
    if date_length == 8:
        return time.strftime("%Y%m%d", time.localtime())
    if date_length == 10:
        return time.strftime("%Y-%m-%d", time.localtime())
    raise ValueError(f"invalid length: {date_length}")


def current_time():
    """
    当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def date_range(begin_date, end_date, date_length=10):
    """
    日期遍历
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
    """
    格式化日期
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
