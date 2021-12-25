import unittest
import logging
from pdcool.finance import *
from pdcool.utils.dataframe import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTest(unittest.TestCase):
    # 2021.12.19 测试通过
    def test_get_stock_name(self):
        name = get_stock_name("600570.SH")
        logging.debug(name)
        assert name == "恒生电子"

    # 2021.12.19 测试通过
    def test_get_fund_name(self):
        name = get_fund_name("320007.OF")
        logging.debug(name)
        assert name == "诺安成长"

    # 2021.12.25 测试通过
    def test_income(self):
        """
        1. today_income = 1000*(62.3-62.68) = -380, total_income = 2409
        2. today_income = 1000*(62.3-62.68)+62.3*200-12600 = -520, total_income = 2269
        3. today_income = 800*(62.3-62.68)+12600-62.68*200 = -240, total_income = 2549
        4. today_income = 700*(62.3-62.68)+62.3*200-12600+18900-62.68*300 = -310, total_income = 2479
        """
        json_data = [
            {'date': '2021-12-25', 'channel': 'test1', 'user_code': 'default', 'fina_code': '600570.SH', 'fina_type': 'stock', 'cost': 59891.0, 'sell': 0.0,
                'share': 1000.0, 'price': 62.3, 'pre_price': 62.68, 'today_cost': 0.0, 'today_sell': 0.0, 'today_inc_share': 0.0, 'today_dec_share': 0.0},
            {'date': '2021-12-25', 'channel': 'test2', 'user_code': 'default', 'fina_code': '600570.SH', 'fina_type': 'stock', 'cost': 72491.0, 'sell': 0.0,
                'share': 1200.0, 'price': 62.3, 'pre_price': 62.68, 'today_cost': 12600.0, 'today_sell': 0.0, 'today_inc_share': 200.0, 'today_dec_share': 0.0},
            {'date': '2021-12-25', 'channel': 'test3', 'user_code': 'default', 'fina_code': '600570.SH', 'fina_type': 'stock', 'cost': 59891.0, 'sell': 12600.0,
                'share': 800.0, 'price': 62.3, 'pre_price': 62.68, 'today_cost': 0.0, 'today_sell': 12600.0, 'today_inc_share': 0.0, 'today_dec_share': 200.0},
            {'date': '2021-12-25', 'channel': 'test4', 'user_code': 'default', 'fina_code': '600570.SH', 'fina_type': 'stock', 'cost': 72491.0, 'sell': 18900.0,
                'share': 900.0, 'price': 62.3, 'pre_price': 62.68, 'today_cost': 12600.0, 'today_sell': 18900.0, 'today_inc_share': 200.0, 'today_dec_share': 300.0}
        ]
        df = dataframe_from_json(json_data)
        df["today_income"] = df.apply(calc_today_income, axis=1)
        df["total_income"] = df.apply(calc_total_income, axis=1)

        assert -380-0.1 <= df["today_income"][0] <= -380+0.1
        assert -520-0.1 <= df["today_income"][1] <= -520+0.1
        assert -240-0.1 <= df["today_income"][2] <= -240+0.1
        assert -310-0.1 <= df["today_income"][3] <= -310+0.1

        assert 2409-0.1 <= df["total_income"][0] <= 2409+0.1
        assert 2269-0.1 <= df["total_income"][1] <= 2269+0.1
        assert 2549-0.1 <= df["total_income"][2] <= 2549+0.1
        assert 2479-0.1 <= df["total_income"][3] <= 2479+0.1


if __name__ == '__main__':
    unittest.main()
