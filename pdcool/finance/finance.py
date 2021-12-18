from common import *


def get_stock_name(code, exchange_market):
    db = DBUtil()
    statement = "select c_name from tstock where c_code=%s and c_exchange_market=%s"
    args = [code, exchange_market]
    name = db.queryone(statement, args)[0]
    return name


def get_fund_name(code):
    db = DBUtil()
    statement = "select c_name from tfund where c_code=%s"
    args = [code]
    name = db.queryone(statement, args)[0]
    return name


print(get_fund_name("501039.LOF"))
