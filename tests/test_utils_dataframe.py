
import unittest
import logging
from pdcool.utils.param import *
from pdcool.utils.dataframe import *

logging.basicConfig(level=logging.DEBUG)


class DataframeTest(unittest.TestCase):
    # 2021.12.19 测试通过
    # def test_dataframe_from_sql(self):
    #     df = dataframe_from_sql("select * from tstock limit 3")
    #     logging.debug(df)
    #     self.assertIsNotNone(df)

    # 2021.12.19 测试通过
    # [缺陷] (ID=10001) 修复rename参数无效问题: dataframe_from_sql使用rename无效
    # def test_dataframe_from_sql_1(self):
    #     df = dataframe_from_sql("select * from tstock limit 3", type="rename")
    #     logging.debug(df)

    # 2021.12.19 测试通过
    def test_dataframe_concat(self):
        df1 = dataframe_from_sql("select * from tstock limit 3")
        df2 = dataframe_from_sql("select * from tstock limit 5")
        df = dataframe_concat([df1, df2])
        logging.debug(df)
        self.assertIsNotNone(df)


if __name__ == '__main__':
    unittest.main()
