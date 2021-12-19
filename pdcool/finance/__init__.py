
from pdcool.utils.database import DBUtil


def get_stock_name(stock_code):
    db = DBUtil()
    return db.queryone(f"select c_name from tstock where c_fina_code='{stock_code}'")[0]


def get_fund_name(fund_code):
    db = DBUtil()
    return db.queryone(f"select c_name from tfund where c_fina_code='{fund_code}'")[0]
