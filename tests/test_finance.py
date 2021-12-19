import unittest
import logging
from pdcool.finance import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTest(unittest.TestCase):
    def test_get_stock_name(self):
        name = get_stock_name("600570.SH")
        logging.debug(name)
        assert name == "恒生电子"

    def test_get_fund_name(self):
        name = get_fund_name("320007.OF")
        logging.debug(name)
        assert name == "诺安成长"


if __name__ == '__main__':
    unittest.main()
