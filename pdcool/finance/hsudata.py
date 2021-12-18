import numpy as np
from hs_udata import set_token, stock_list, fund_list
from dutool import DateUtil
from pdcool.utils.dataframe import *
from pdcool.utils.list import *
from pdcool.system.param import *


token = get_param("dutool", "finance", "hs_udata_token")
set_token(token=token)

"""
数据同步流程:
1. 获取dataframe
2. 处理dataframe: 补充缺失列, 处理异常值和字典转换, 重命名列, 列筛选排序, 重命名列(和数据库列名一致)
3. 加载dataframe到临时表
4. 处理临时表到目的表
5. 删除临时表
6. 显示结果
"""


def sync_stock():
    """
    同步股票信息: https://udata.hs.net/datas/202/
    """
    df = stock_list()

    # 补充缺失列
    df["source"] = "hsudata"
    df["exchange"] = df["hs_code"].map(lambda x: x.split(".")[1])

    # 处理异常值和字典转换
    df["secu_abbr"] = df["secu_abbr"].map(lambda x: x.replace(" ", ""))

    # 重命名列
    df.rename(columns={"hs_code": "fina_code", "secu_code": "code", "secu_abbr": "name", "chi_name": "full_name"}, inplace=True)

    # 列筛选排序
    df = df[["fina_code", "code", "exchange", "name", "full_name", "listed_state", "listed_sector", "source"]]

    # 重命名列(和数据库列名一致)
    df.set_axis(["c_fina_code", "c_code", "c_exchange", "c_name", "c_full_name", "c_listed_state", "c_listed_sector", "c_source"], axis="columns", inplace=True)

    dataframe_to_table(df, "ttmp_stock")
    db = DBUtil()

    update_count = db.update("""update tstock t,ttmp_stock s
    set t.c_fina_code     = s.c_fina_code     ,
        t.c_code          = s.c_code          ,
        t.c_exchange      = s.c_exchange      ,
        t.c_name          = s.c_name          ,
        t.c_full_name     = s.c_full_name     ,
        t.c_listed_state  = s.c_listed_state  ,
        t.c_listed_sector = s.c_listed_sector ,
        t.c_source        = s.c_source        ,
        t.c_update_time   = now()    
    where t.c_fina_code = s.c_fina_code""")

    insert_count = db.insert("""insert ignore into tstock(c_fina_code, c_code, c_exchange, c_name, c_full_name, c_listed_state, c_listed_sector, c_source, c_create_time, c_update_time)
    select c_fina_code,
        c_code,
        c_exchange,
        c_name,
        c_full_name,
        c_listed_state,
        c_listed_sector,
        c_source,
        now(),
        now()
    from ttmp_stock""")

    db.execute("drop table ttmp_stock")
    print(f"sync stock complete, update={update_count}, insert={insert_count}")


def __get_fund_dataframe(fina_code=None, foundation_type=None, float_type=None):
    """
    获取基金信息dataframe. foundation_type 基金运作方式; float_type 发售方式
    """

    # 注意: 如果获取不到数据, 例如: fund_list("600570.SH"), 会直接报错: TypeError: catching classes that do not inherit from BaseException is not allowed, 后续需要异常处理
    df = fund_list(symbols=fina_code, foundation_type=foundation_type, float_type=float_type)

    if df.empty:
        return

    # 补充缺失列
    df["source"] = "hsudata"
    df["code"] = df["secu_code"].map(lambda x: x.split(".")[0])

    # 处理异常值和字典转换
    df["foundation_type"].replace({
        "1": "契约型封闭式",
        "2": "开放式",
        "3": "LOF",
        "4": "ETF",
        "5": "FOF",
        "6": "创新型封闭式",
        "7": "开放式(带固定封闭期)",
        "8": "ETF联接基金",
        "9": "半开放式"}, inplace=True)
    df["float_type"].replace({"1": "场内", "2": "场外", "3": "场内场外"}, inplace=True)

    # 重命名列
    df.rename(columns={"secu_code": "fina_code", "secu_abbr": "name", "fund_full_name": "full_name", "fund_company_code": "company_code", "fund_company_abbr": "company_name", "fund_company_name": "company_full_name"}, inplace=True)

    # 列筛选排序
    df = df[["fina_code", "code", "name", "full_name", "company_code", "company_name", "company_full_name", "foundation_type", "float_type", "source"]]

    return df


def __put_fund_dataframe(df):
    """
    保存基金信息dataframe到数据库
    """
    # 重命名列(和数据库列名一致)
    df.set_axis(["c_fina_code", "c_code", "c_name", "c_full_name", "c_company_code", "c_company_name", "c_company_full_name", "c_foundation_type", "c_float_type", "c_source"], axis="columns", inplace=True)

    dataframe_to_table(df, "ttmp_fund")
    db = DBUtil()

    update_count = db.update("""update tfund t,ttmp_fund s
    set t.c_fina_code         = s.c_fina_code         ,
        t.c_code              = s.c_code              ,
        t.c_name              = s.c_name              ,
        t.c_full_name         = s.c_full_name         ,
        t.c_company_code      = s.c_company_code      ,
        t.c_company_name      = s.c_company_name      ,
        t.c_company_full_name = s.c_company_full_name ,
        t.c_foundation_type   = s.c_foundation_type   ,
        t.c_float_type        = s.c_float_type        ,
        t.c_update_time       = now()    
    where t.c_fina_code = s.c_fina_code""")

    insert_count = db.insert("""insert ignore into tfund(c_fina_code, c_code, c_name, c_full_name, c_company_code, c_company_name, c_company_full_name, c_foundation_type, c_float_type, c_source, c_create_time, c_update_time)
    select c_fina_code,
        c_code,
        c_name,
        c_full_name,
        c_company_code,
        c_company_name,
        c_company_full_name,
        c_foundation_type,
        c_float_type,
        c_source,
        now(),
        now()
    from ttmp_fund""")

    db.execute("drop table ttmp_fund")
    print(f"sync stock complete, update={update_count}, insert={insert_count}")


def sync_fund():
    """
    同步基金信息: https://udata.hs.net/datas/409/

    统计各个类型的基金数量
        (基金运作方式=1) ---> 69
        (基金运作方式=2) ---> 大于6000, 获取数量一次无法全部获取, 需要再根据发售方式细分
            (基金运作方式=2, 发售方式=1) ---> 8
            (基金运作方式=2, 发售方式=2) ---> 大于6000, 获取数量一次无法全部获取, 除了根据基金代码已经无法再细分
            (基金运作方式=2, 发售方式=3) ---> 251
        (基金运作方式=3) ---> 433
        (基金运作方式=4) ---> 721
        (基金运作方式=5) ---> 0
        (基金运作方式=6) ---> 365
        (基金运作方式=7) ---> 2047
        (基金运作方式=8) ---> 615
        (基金运作方式=9) ---> 报错: KeyError: 'result_msg' ---> TypeError: catching classes that do not inherit from BaseException is not allowed ---> 不处理
    """
    df1 = __get_fund_dataframe(foundation_type="1")
    df2_1 = __get_fund_dataframe(foundation_type="2", float_type="1")
    df2_2 = __get_fund_dataframe(foundation_type="2", float_type="2")
    df2_3 = __get_fund_dataframe(foundation_type="2", float_type="3")
    df3 = __get_fund_dataframe(foundation_type="3")
    df4 = __get_fund_dataframe(foundation_type="4")
    df5 = __get_fund_dataframe(foundation_type="5")
    df6 = __get_fund_dataframe(foundation_type="6")
    df7 = __get_fund_dataframe(foundation_type="7")
    df8 = __get_fund_dataframe(foundation_type="8")
    df = dataframe_concat([df1, df2_1, df2_2, df2_3, df3, df4, df5, df6, df7, df8])

    __put_fund_dataframe(df)


def sync_fund_by_code(fina_code):
    df = __get_fund_dataframe(fina_code=fina_code)
    __put_fund_dataframe(df)

    # def sync_stock_quote_daily(fina_code, trade_date):
    #     """
    #     同步股票日行情信息: https://udata.hs.net/datas/332/
    #         1. 获取dataframe
    #         2. 处理dataframe
    #         3. 加载dataframe到临时表
    #         4. 处理临时表到目的表
    #         5. 删除临时表
    #         6. 显示结果
    #     """
    #     # 1. 获取dataframe
    #     df = stock_quote_daily(en_prod_code=fina_code, trading_date=trade_date)

    #     # 2.1 补充缺失列
    #     if "issue_price_change" not in df.columns:
    #         df["issue_price_change"] = 0
    #     if "issue_price_change_rate" not in df.columns:
    #         df["issue_price_change_rate"] = 0
    #     df["source"] = "hsudata"

    #     # 2.2 补充缺失值
    #     df.replace(to_replace=r"^\s*$", value=np.nan, regex=True, inplace=True)  # 将空字符串变更为空值
    #     df.fillna({
    #         "n_prev_close_price": 0,
    #         "n_open_price": 0,
    #         "n_high_price": 0,
    #         "n_low_price": 0,
    #         "n_close_price": 0,
    #         "n_avg_price": 0,
    #         "n_px_change": 0,
    #         "n_px_change_rate": 0,
    #         "n_turnover_ratio": 0,
    #         "n_business_balance": 0,
    #         "l_turnover_deals": 0,
    #         "n_amplitude": 0,
    #         "n_issue_price_change": 0,
    #         "n_issue_price_change_rate": 0,
    #         "c_recently_trading_date": "1970-01-01",
    #         "n_ratio_adjust_factor": 0,
    #         "n_business_amount": 0,
    #     }, inplace=True)

    #     # 2.3 重命名列
    #     df.rename(columns={"prod_code": "fina_code", "trading_date": "trade_date"}, inplace=True)

    #     # 2.4 列排序筛选
    #     df = df[["fina_code", "trade_date", "prev_close_price", "open_price", "high_price", "low_price", "close_price", "avg_price",
    #              "px_change", "px_change_rate", "turnover_ratio", "business_balance", "turnover_deals", "amplitude", "issue_price_change", "issue_price_change_rate",
    #              "recently_trading_date", "ratio_adjust_factor", "business_amount", "up_down_status", "turnover_status", "source"]]

    #     # 2.5 重命名列：和数据库名保持一致
    #     df.set_axis(["c_fina_code", "c_trade_date", "n_prev_close_price", "n_open_price", "n_high_price", "n_low_price", "n_close_price",
    #                  "n_avg_price", "n_px_change", "n_px_change_rate", "n_turnover_ratio", "n_business_balance", "l_turnover_deals", "n_amplitude", "n_issue_price_change", "n_issue_price_change_rate",
    #                  "c_recently_trading_date", "n_ratio_adjust_factor", "n_business_amount", "c_up_down_status", "c_turnover_status", "c_source"], axis="columns", inplace=True)

    #     # 3. 加载dataframe到临时表
    #     dataframe_to_table(df, "ttmp_stock_quote_daily", if_exists="replace")

    #     # 4. 处理临时表到目的表
    #     db = DBUtil()
    #     update_count = db.update("""update tstock_quote_daily t,ttmp_stock_quote_daily s
    #     set t.n_prev_close_price        = s.n_prev_close_price        ,
    #         t.n_open_price              = s.n_open_price              ,
    #         t.n_high_price              = s.n_high_price              ,
    #         t.n_open_price              = s.n_open_price              ,
    #         t.n_high_price              = s.n_high_price              ,
    #         t.n_low_price               = s.n_low_price               ,
    #         t.n_close_price             = s.n_close_price             ,
    #         t.n_avg_price               = s.n_avg_price               ,
    #         t.n_px_change               = s.n_px_change               ,
    #         t.n_px_change_rate          = s.n_px_change_rate          ,
    #         t.n_turnover_ratio          = s.n_turnover_ratio          ,
    #         t.n_business_balance        = s.n_business_balance        ,
    #         t.l_turnover_deals          = s.l_turnover_deals          ,
    #         t.n_amplitude               = s.n_amplitude               ,
    #         t.n_issue_price_change      = s.n_issue_price_change      ,
    #         t.n_issue_price_change_rate = s.n_issue_price_change_rate ,
    #         t.c_recently_trading_date   = s.c_recently_trading_date   ,
    #         t.n_ratio_adjust_factor     = s.n_ratio_adjust_factor     ,
    #         t.n_business_amount         = s.n_business_amount         ,
    #         t.c_up_down_status          = s.c_up_down_status          ,
    #         t.c_turnover_status         = s.c_turnover_status         ,
    #         t.c_source                  = s.c_source                  ,
    #         t.c_update_time             = now()
    #     where t.c_fina_code  = s.c_fina_code
    #     and t.c_trade_date = s.c_trade_date""")

    #     insert_count = db.insert("""insert ignore into tstock_quote_daily(c_fina_code, c_trade_date, n_prev_close_price, n_open_price, n_high_price, n_low_price, n_close_price, n_avg_price, n_px_change, n_px_change_rate, n_turnover_ratio, n_business_balance, l_turnover_deals, n_amplitude, n_issue_price_change, n_issue_price_change_rate, c_recently_trading_date, n_ratio_adjust_factor, n_business_amount, c_up_down_status, c_turnover_status, c_source, c_create_time, c_update_time)
    #     select c_fina_code,
    #         c_trade_date,
    #         n_prev_close_price,
    #         n_open_price,
    #         n_high_price,
    #         n_low_price,
    #         n_close_price,
    #         n_avg_price,
    #         n_px_change,
    #         n_px_change_rate,
    #         n_turnover_ratio,
    #         n_business_balance,
    #         l_turnover_deals,
    #         n_amplitude,
    #         n_issue_price_change,
    #         n_issue_price_change_rate,
    #         c_recently_trading_date,
    #         n_ratio_adjust_factor,
    #         n_business_amount,
    #         c_up_down_status,
    #         c_turnover_status,
    #         c_source,
    #         now(),
    #         now()
    #     from ttmp_stock_quote_daily""")

    #     # 5. 删除临时表
    #     db.execute("drop table ttmp_stock_quote_daily")

    #     # 6. 打印结果
    #     print(f"sync stock_quote_daily complete, update={update_count}, insert={insert_count}")

    # def sync_stock_quote_daily_by_date(trade_date):
    #     db = DBUtil()
    #     rows = db.query("select c_fina_code from tstock")
    #     stock_list = [row[0] for row in rows]
    #     stock_list = split_list_by_n(stock_list, 100)  # 以固定长度分割数组list
    #     for stock in stock_list:
    #         stock_text = ",".join(stock)
    #         sync_stock_quote_daily(stock_text, trade_date)

    # def sync_stock_quote_daily_by_code(fina_code):
    #     begin_date = "19700101"
    #     end_date = time.strftime("%Y%m%d", time.localtime())
    #     date_list = DateUtil.date_range(begin_date, end_date)
    #     for trade_date in date_list:
    #         sync_stock_quote_daily(fina_code, trade_date)

    # # def sync_stock_quote_daily_by_code(fina_code):
    # #     begin_date = "19700101"
    # #     end_date = time.strftime("%Y%m%d", time.localtime())
    # #     df = stock_quote_daily_list(en_prod_code=fina_code, begin_date=begin_date, end_date=end_date)
    # #     print(df)

    # # sync_stock_quote_daily_by_code("000001.SZ")
    # # sync_stock_quote_daily_by_code("000")

    # df1 = dataframe_from_sql("select * from tstock limit 3")
    # df2 = dataframe_from_sql("select * from tstock limit 5")
    # df = dataframe_concat([df1, df2])
    # print(df)
