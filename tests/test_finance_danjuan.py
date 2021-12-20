import unittest
import logging
from pdcool.finance.danjuan import *

logging.basicConfig(level=logging.DEBUG)


class FinanceDanjuanTest(unittest.TestCase):
    # 2021.12.19 测试通过
    # def test_sync_fund_weighting(self):
    #     sync_fund_weighting("320007.OF")  # 单个获取

    # 2021.12.19 测试通过
    # def test_sync_fund_weighting_1(self):
    #     sync_fund_weighting(["320007.OF", "519674.OF"])  # 多个获取

    # [缺陷] (ID=10002) 获取成分股信息添加异常处理: 债券基金没有成分股信息(000092 信诚新双盈分级债券A)
    # def test_sync_fund_weighting_2(self):
    #     sync_fund_weighting("000092.OF")

    def test_get_dataframe_for_fund_realtime_quotes_from_fund_code(self):
        df = get_dataframe_for_fund_realtime_quotes_from_fund_code("000404.OF")
        show_dataframe(df)


if __name__ == '__main__':
    unittest.main()
