import unittest
import logging
from pdcool.finance import *

logging.basicConfig(level=logging.DEBUG)


class FinanceTest(unittest.TestCase):
    def test_get_stock_name(self):
        name = get_stock_name("600570.SH")
        print(name)


if __name__ == '__main__':
    unittest.main()
