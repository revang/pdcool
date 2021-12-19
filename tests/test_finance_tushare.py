import unittest
import logging
from pdcool.finance.tushare import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTushareTest(unittest.TestCase):
    # 2021.12.19 测试通过
    def test_sync_stock(self):
        sync_stock()


if __name__ == '__main__':
    unittest.main()
