import unittest
import logging
from pdcool.finance.danjuan import *

logging.basicConfig(level=logging.DEBUG)


class FinanceDanjuanTest(unittest.TestCase):
    def test_sync_fund_weighting(self):
        # sync_fund_weighting("320007.OF")
        # sync_fund_weighting("519674.OF")

        sync_fund_weighting(["320007.OF", "519674.OF"])


if __name__ == '__main__':
    unittest.main()
