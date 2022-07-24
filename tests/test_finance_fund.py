import unittest
import logging
from pdcool.finance.fund import *

logging.basicConfig(level=logging.DEBUG)


class FinanceDanjuanTest(unittest.TestCase):
    def test_sync_fund_tushare(self):
        sync_fund_by_tushare()


if __name__ == "__main__":
    """
    python -m unittest tests/test_finance_fund.py
    """
    unittest.main()
