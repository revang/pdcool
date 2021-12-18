
import unittest
import logging
from pdcool.system.param import *
from pdcool.utils.dataframe import *

logging.basicConfig(level=logging.DEBUG)


class DataframeTest(unittest.TestCase):
    def test_dataframe_from_sql(self):
        df = dataframe_from_sql("select * from tstock limit 3")
        logging.debug(df)
        self.assertIsNotNone(df)

    def test_dataframe_concat(self):
        df1 = dataframe_from_sql("select * from tstock limit 3")
        df2 = dataframe_from_sql("select * from tstock limit 5")
        df = dataframe_concat([df1, df2])
        logging.debug(df)
        self.assertIsNotNone(df)


if __name__ == '__main__':
    unittest.main()
