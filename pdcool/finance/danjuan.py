from logging import NOTSET
import requests
import json
from pdcool.utils.database.mysql import DBUtil
from pdcool.utils.dataframe import *
from pdcool.utils.datetime import current_time
from pdcool.utils.param import get_param


def _get_fund_weighting_dataframe(fund_code):
    user_agent = get_param("pdcool", "web", "user_agent")
    url = f"https://danjuanapp.com/djapi/fund/detail/{fund_code[0:6]}"
    headers = {"User-Agent": user_agent}
    cookies = {}  # 获取不需要cookie
    html = requests.get(url, headers=headers, cookies=cookies)
    json_text = html.text
    json_data = json.loads(json_text)

    fund_weighting = []
    end_date = json_data.get("data").get("fund_position").get("enddate")
    stock_list = json_data.get("data").get("fund_position").get("stock_list")
    for stock in stock_list:
        stock_code = f'{stock.get("xq_symbol")[2:8]}.{stock.get("xq_symbol")[0:2]}'
        stock_name = stock.get("name")
        stock_price = stock.get("current_price")
        percent = stock.get("percent")
        change_percent = stock.get("change_percentage")
        fund_weighting.append(
            {
                "date": end_date,
                "fund_code": fund_code,
                "stock_code": stock_code,
                "stock_name": stock_name,
                "stock_price": stock_price,
                "percent": percent,
                "change_percent": change_percent,
                "source": "danjuan",
                "create_time": current_time(),
                "update_time": current_time(),
            }
        )
    df = dataframe_from_json(fund_weighting)
    return df


def _put_fund_weighting_dataframe(df):
    # 插入预处理
    delete_args_df = df[["date", "fund_code"]]
    delete_args_df = delete_args_df.drop_duplicates()  # 删除重复值
    delete_args_json = dataframe_to_json(delete_args_df)
    db = DBUtil()
    for item in delete_args_json:
        date = item.get("date")
        fund_code = item.get("fund_code")
        db.delete(
            f"delete from tfund_weighting where c_date='{date}' and c_fund_code='{fund_code}'"
        )

    # 插入数据
    df.set_axis(
        [
            "c_date",
            "c_fund_code",
            "c_stock_code",
            "c_stock_name",
            "n_stock_price",
            "n_percent",
            "n_change_percent",
            "c_source",
            "c_create_time",
            "c_update_time",
        ],
        axis="columns",
        inplace=True,
    )
    dataframe_to_table(df, "tfund_weighting", if_exists="append")


def sync_fund_weighting(fund):
    """
    获取基金权重股 fund_code 可以是单个基金代码, 也可以是列表
    """
    if isinstance(fund, str) or isinstance(fund, list):
        df_list = []
        fund_list = [fund] if isinstance(fund, str) else fund
        for fund_code in fund_list:
            df_list.append(_get_fund_weighting_dataframe(fund_code))
        df = dataframe_concat(df_list)
        _put_fund_weighting_dataframe(df)
        return

    raise ValueError(f"invalid datatype: fund={type(fund)}")


def get_dataframe_for_fund_realtime_quotes_from_fund_code(fund_code):
    user_agent = get_param("pdcool", "web", "user_agent")
    url = f"https://danjuanapp.com/djapi/fund/estimate-nav/{fund_code[0:6]}"
    headers = {"User-Agent": user_agent}
    html = requests.get(url, headers=headers)
    json_text = html.text
    json_data = json.loads(json_text)
    item_list = json_data.get("data").get("items")
    df = dataframe_from_json(item_list)
    return df
