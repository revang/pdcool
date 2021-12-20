from os import makedev
import unittest
import logging
from pdcool.finance.tushare import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTushareTest(unittest.TestCase):
    # 2021.12.19 测试通过
    # def test_sync_stock(self):
    #     sync_stock()

    # 2021.12.20 测试通过
    def test_get_dataframe_for_index(self):
        df = get_dataframe_for_index(market="CSI")
        show_dataframe(df)

        df = get_dataframe_for_index(index_code="000188.CSI")
        show_dataframe(df)


if __name__ == '__main__':
    unittest.main()
