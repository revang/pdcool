import unittest
import logging
from pdcool.finance.danjuan import *

logging.basicConfig(level=logging.DEBUG)


class FinanceDanjuanTest(unittest.TestCase):
    def test_sync_fund_weighting(self):
        # 单个获取
        # sync_fund_weighting("320007.OF")

        # 多个获取
        # sync_fund_weighting(["320007.OF", "519674.OF"])

        # [缺陷] (ID=10002) 获取成分股信息添加异常处理: 债券基金没有成分股信息(000092 信诚新双盈分级债券A)
        sync_fund_weighting("000092.OF")


if __name__ == '__main__':
    unittest.main()
