from dutool import DBUtil
from common import get_param
import requests
import json
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"


class Stock:
    def __init__(self, stock_code, exchange_market):
        self.code = stock_code
        self.exchange_market = exchange_market
        self.name = ""
        self.source = "xueqiu"

    def save(self):
        pass

    @staticmethod
    def get_daily_from_web(code, exchange_market):
        xieqiu_token = get_param("dutool", "stock", "xq_token_1")
        url = "https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=SH600570&period=1d"
        headers = {"user-agent": user_agent}
        cookies = {"xq_a_token": xieqiu_token}
        html = requests.get(url, headers=headers, cookies=cookies)
        json_text = html.text
        json_data = json.loads(json_text)
        if json_data.get("error_code") == "400016":
            raise ValueError("token error {%s}" % xieqiu_token)
        json_item = json_data.get("data").get("items")[-1]
        stock_daily = {}
        stock_daily["code"] = code
        stock_daily["name"] = "XXXX"
        stock_daily["current_price"] = json_item.get("current")
        stock_daily["percent"] = json_item.get("percent")
        stock_daily["update_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(json_item["timestamp"]/1000))
        print(stock_daily)


Stock.get_daily_from_web("", "")
