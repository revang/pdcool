
from pdcool.utils.database import DBUtil


def get_stock_name(stock_code):
    """ 获取股票名称

    :param stock_code 股票代码
    :return: 股票名称
    """
    db = DBUtil()
    return db.queryone(f"select c_name from tstock where c_fina_code='{stock_code}'")[0]


def get_fund_name(fund_code):
    """ 获取基金名称

    :param stock_code 基金代码
    :return: 基金名称
    """
    db = DBUtil()
    return db.queryone(f"select c_name from tfund where c_fina_code='{fund_code}'")[0]


def calc_today_income(row):
    """ 计算当日收益

    :param row: dataframe行
    :return 当日收益
    """
    # 场景分析
    #     1. 当日没有交易 = 当日市值-昨日市值
    #     2. 当日买入 = 原持有部分收益+买入部分收益 = [原份额](当日市值-昨日市值)+[买入份额](当日市值-当日成本)
    #     3. 当日卖出 = 剩余持有部分收益+卖出部分收益 = [剩余份额](当日市值-昨日市值)+[卖出份额](卖出金额-昨日市值)
    #     4. 当日发生买卖 = 原持有部分收益+买入部分收益 = (剩余持有部分收益+卖出部分收益)+买入部分收益

    if row["today_inc_share"] == 0 and row["today_dec_share"] == 0:
        val = row["share"]*(row["price"]-row["pre_price"])
    elif row["today_inc_share"] != 0 and row["today_dec_share"] == 0:
        income_1 = (row["share"]-row["today_inc_share"])*(row["price"]-row["pre_price"])
        income_2 = row["today_inc_share"]*row["price"]-row["today_cost"]
        val = income_1+income_2
    elif row["today_inc_share"] == 0 and row["today_dec_share"] != 0:
        income_1 = row["share"]*(row["price"]-row["pre_price"])
        income_2 = row["today_sell"]-row["today_dec_share"]*row["pre_price"]
        val = income_1+income_2
    else:
        income_1 = (row["share"]-row["today_inc_share"])*(row["price"]-row["pre_price"])
        income_2 = row["today_sell"]-row["today_dec_share"]*row["pre_price"]
        income_3 = row["today_inc_share"]*row["price"]-row["today_cost"]
        val = income_1+income_2+income_3
    return val


def calc_total_income(row):
    """ 计算累计收益

    :param row: dataframe行
    :return 累计收益
    """
    # 场景分析: 累计收益 = 当日市值+卖出金额-成本
    return row["share"]*row["price"]+row["sell"]-row["cost"]
