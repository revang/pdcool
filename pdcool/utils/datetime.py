import time
import datetime


def current_date(length=8):
    """
    当前日期
    """
    if length == 8:
        return time.strftime("%Y%m%d", time.localtime())
    if length == 10:
        return time.strftime("%Y-%m-%d", time.localtime())
    raise ValueError(f"invalid length: {length}")


def current_time():
    """
    当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
