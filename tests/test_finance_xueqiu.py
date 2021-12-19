import unittest
import logging
from pdcool.finance.xueqiu import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTushareTest(unittest.TestCase):
    def test_get_stock_quotes_by_current_date(self):
        df = get_stock_quotes_by_current_date()
        print(df)


if __name__ == '__main__':
    unittest.main()
