import unittest
import logging
from pdcool.finance.hsudata import *

logging.basicConfig(level=logging.DEBUG)


class FinanceHsudataTest(unittest.TestCase):
    # def test_sync_stock(self):
    #     sync_stock()

    # def test_sync_fund(self):
    #     sync_fund()

    # def test_sync_fund_by_code(self):
    #     sync_fund_by_code("000008.OF")

    def test_sync_stock_quote_daily_by_date(self):
        sync_stock_quote_daily_by_date("20211217")


if __name__ == '__main__':
    unittest.main()
