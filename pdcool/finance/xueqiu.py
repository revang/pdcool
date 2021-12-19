from pdcool.utils.dataframe import dataframe_from_json
from pdcool.utils.param import get_param
import requests
import json
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"


def get_stock_quotes_by_current_date(stock_code):
    stock_symbol = stock_code[0:6]+stock_code[7:9]
    user_agent = get_param("pdcool", "web", "user_agent")
    token = get_param("pdcool", "finance", "xueqiu_token")
    url = f"https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol={stock_symbol}&period=1d"
    headers = {"user-agent": user_agent}
    cookies = {"xq_a_token": token}
    html = requests.get(url, headers=headers, cookies=cookies)
    json_text = html.text
    json_data = json.loads(json_text)
    if json_data.get("error_code") == "400016":
        raise ValueError(f"invalid token: {token}")

    quotes_json = []
    item_list = json_data.get("data").get("items")
    for item in item_list:
        quotes_json.append({
            "stock_code": stock_code,
            "current_price": item.get("current"),
            "percent": item.get("current"),
            "update_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item.get("timestamp")/1000))
        })
    df = dataframe_from_json(quotes_json)
    return df
