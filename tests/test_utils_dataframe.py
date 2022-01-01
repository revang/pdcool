
import enum
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
    # def test_dataframe_concat(self):
    #     df1 = dataframe_from_sql("select * from tstock limit 3")
    #     df2 = dataframe_from_sql("select * from tstock limit 5")
    #     df = dataframe_concat([df1, df2])
    #     logging.debug(df)
    #     self.assertIsNotNone(df)

    # 2022.01.01 测试通过
    def test_generate_simple_dataframe(self):
        df = generate_simple_dataframe()
        assert dataframe_count(df, count_type="row") == 3
        assert dataframe_count(df, count_type="column") == 3

    # 2022.01.01 测试通过
    def test_dataframe_from_dictlist(self):
        simple_dictlist = [
            {"name": "alice", "age": 18, "gender": "female"},
            {"name": "bob", "age": 8, "gender": "male"},
            {"name": "jack", "age": 13, "gender": "male"}
        ]
        df = dataframe_from_dictlist(simple_dictlist)
        assert dataframe_count(df, count_type="row") == 3
        assert dataframe_count(df, count_type="column") == 3

    # 2022.01.01 测试通过
    def test_dataframe_to_dictlist(self):
        df = generate_simple_dataframe()
        dictlist = dataframe_to_dictlist(df)
        assert len(dictlist) == 3
        for idx, val in enumerate(dictlist):
            assert len(val) == 3

    # 2022.01.01 测试通过
    def test_dataframe_from_listdict(self):
        listdict1 = {
            "name": ["alice", "bob", "jack"],
            "age": [18, 8, 13],
            "gender": ["female", "male", "male"]
        }
        df1 = dataframe_from_listdict(listdict1)
        assert dataframe_count(df1, count_type="row") == 3
        assert dataframe_count(df1, count_type="column") == 3

        listdict2 = {
            "宁德时代": ["易方达新兴成长", "国天惠成长混合", "xxx"],
            "三花智控": ["易方达新兴成长", "xxx"],
            "古井贡酒": ["招商中证白酒指数"]
        }
        df2 = dataframe_from_listdict(listdict2, dict_type="index", column_name=["stock_name", "fund_name_1", "fund_name_2", "fund_name_3"])
        assert dataframe_count(df2, count_type="row") == 3
        assert dataframe_count(df2, count_type="column") == 4

    # 2022.01.01 测试通过
    def test_dataframe_from_csv(self):
        df1 = dataframe_from_csv(r"resources\input\fund.csv")
        # show_dataframe(df1)
        assert dataframe_count(df1, count_type="row") == 7
        assert dataframe_count(df1, count_type="column") == 4

        df2 = dataframe_from_csv(r"resources\input\fund.csv", column_name=["fund_code", "fund_name", "fund_manager", "fund_company"])
        # show_dataframe(df2)
        assert dataframe_count(df2, count_type="row") == 7
        assert dataframe_count(df2, count_type="column") == 4

    # 2022.01.01 测试通过
    def test_dataframe_to_csv(self):
        df1_1 = generate_simple_dataframe()
        # show_dataframe(df1_1)
        dataframe_to_csv(df1_1, r"resources\output\test.csv")
        df1_2 = dataframe_from_csv(r"resources\output\test.csv")
        # show_dataframe(df1_2)
        assert dataframe_count(df1_2, count_type="row") == 3
        assert dataframe_count(df1_2, count_type="column") == 3

    def test_dataframe_from_excel(self):
        df1 = dataframe_from_excel(r"resources\input\fund.xlsx")
        # show_dataframe(df1)
        assert dataframe_count(df1, count_type="row") == 7
        assert dataframe_count(df1, count_type="column") == 4

        df2 = dataframe_from_excel(r"resources\input\fund.xlsx", column_name=["fund_code", "fund_name", "fund_manager", "fund_company"])
        # show_dataframe(df2)
        assert dataframe_count(df2, count_type="row") == 7
        assert dataframe_count(df2, count_type="column") == 4

    def test_dataframe_to_excel(self):
        df1_1 = generate_simple_dataframe()
        # show_dataframe(df1_1)
        dataframe_to_excel(df1_1, r"resources\output\test.xlsx")
        df1_2 = dataframe_from_excel(r"resources\output\test.xlsx")
        # show_dataframe(df1_2)
        assert dataframe_count(df1_2, count_type="row") == 3
        assert dataframe_count(df1_2, count_type="column") == 3


if __name__ == '__main__':
    unittest.main()
    """
    python -m unittest tests/test_utils_dataframe.py
    """
