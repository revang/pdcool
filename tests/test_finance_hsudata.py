import unittest
import logging
from pdcool.finance.hsudata import *
from pdcool.finance.tushare import get_dataframe_for_index

logging.basicConfig(level=logging.DEBUG)


class FinanceHsudataTest(unittest.TestCase):
    # 2021.12.19 测试通过
    # def test_sync_stock(self):
    #     sync_stock()

    # 2021.12.19 测试通过
    # def test_sync_fund(self):
    #     sync_fund()

    # 2021.12.19 测试通过
    # def test_sync_fund_by_code(self):
    #     sync_fund_by_code("000008.OF")

    # 2021.12.19 测试通过
    def test_sync_stock_quote_daily_by_date(self):
        sync_stock_quote_daily_by_date("20211217")


if __name__ == '__main__':
    unittest.main()
