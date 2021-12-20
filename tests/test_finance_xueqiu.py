import unittest
import logging
from pdcool.finance.xueqiu import *
from pdcool.utils.dataframe import show_dataframe

logging.basicConfig(level=logging.DEBUG)


class FinanceXueqiuTest(unittest.TestCase):
    def test_get_stock_quotes_by_current_date(self):
        df = get_stock_quotes_by_current_date("600570.SH")
        show_dataframe(df)


if __name__ == '__main__':
    unittest.main()
