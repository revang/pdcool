#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 18:49:09
Last Modified by  : revang
Last Modified time: 2022-01-01 18:49:09
"""


import logging
import unittest
from pdcool.utils.dataframe import *
from pdcool.utils.param import *

logging.basicConfig(level=logging.DEBUG)


class DataframeTest(unittest.TestCase):

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
        df1 = dataframe_from_listdict(listdict1, column_name=["test1", "test2", "test3"])
        # show_dataframe(df1)
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

    # 2022.01.01 测试通过
    def test_dataframe_from_excel(self):
        df1 = dataframe_from_excel(r"resources\input\fund.xlsx")
        # show_dataframe(df1)
        assert dataframe_count(df1, count_type="row") == 7
        assert dataframe_count(df1, count_type="column") == 4

        df2 = dataframe_from_excel(r"resources\input\fund.xlsx", column_name=["fund_code", "fund_name", "fund_manager", "fund_company"])
        # show_dataframe(df2)
        assert dataframe_count(df2, count_type="row") == 7
        assert dataframe_count(df2, count_type="column") == 4

    # 2022.01.01 测试通过
    def test_dataframe_to_excel(self):
        df1_1 = generate_simple_dataframe()
        # show_dataframe(df1_1)
        dataframe_to_excel(df1_1, r"resources\output\test.xlsx")
        df1_2 = dataframe_from_excel(r"resources\output\test.xlsx")
        # show_dataframe(df1_2)
        assert dataframe_count(df1_2, count_type="row") == 3
        assert dataframe_count(df1_2, count_type="column") == 3

    # 2021.12.19 测试通过
    # def test_dataframe_from_sql(self):
    #     df = dataframe_from_sql("select * from tstock limit 3")
    #     assert dataframe_count(df, count_type="row") == 3

    # 2022.01.01 测试通过
    # def test_dataframe_to_table(self):
    #     df = generate_simple_dataframe()
    #     dataframe_to_table(df, "ttmp_simple", insert_mode="replace")
    #     db = DBUtil()
    #     count = db.queryone("select count(*) from ttmp_simple")[0]
    #     db.execute("drop table ttmp_simple")
    #     assert count == 3

    # 2022.01.01 测试通过
    def test_show_dataframe(self):
        df = generate_simple_dataframe()
        # show_dataframe(df)
        # show_dataframe(df, show_type="dictlist")

    # 2022.01.01 测试通过
    def test_dataframe_rename(self):
        df1 = generate_simple_dataframe()
        column_dict = {"name": "test1", "age": "test2", "gender": "test3"}
        df1 = dataframe_rename(df1, column_dict)
        assert list(df1) == ["test1", "test2", "test3"]

        df2 = generate_simple_dataframe()
        column_list = ["test1", "test2", "test3"]
        df2 = dataframe_rename(df1, column_list)
        assert list(df2) == ["test1", "test2", "test3"]

    # 2022.01.01 测试通过
    def test_dataframe_empty_none(self):
        df = generate_simple_dataframe()
        df["test1"] = ""
        df["test2"] = None
        df = dataframe_empty_none(df)
        # show_dataframe(df)
        count = df.isna().sum().sum()
        assert count == 6

    # 2022.01.01 测试通过
    def test_dataframe_fill_none(self):
        df = generate_simple_dataframe()
        df["test1"] = ""
        df["test2"] = None
        df = dataframe_empty_none(df)
        df = dataframe_fill_none(df, "0")
        # show_dataframe(df)
        val1 = df.iloc[[0], [3]].values[0][0]
        val2 = df.iloc[[0], [4]].values[0][0]
        assert val1 == "0"
        assert val2 == "0"

    # 2022.01.01 测试通过
    def test_dataframe_transform_dict(self):
        df = generate_simple_dataframe()
        df = dataframe_transform_dict(df, "gender", {"female": "女", "male": "男"})
        # show_dataframe(df)
        val1 = df.iloc[[0], [2]].values[0][0]
        val2 = df.iloc[[1], [2]].values[0][0]
        assert val1 == "女"
        assert val2 == "男"

    def test_dataframe_concat(self):
        None

    # 2022.01.01 测试通过
    def test_dataframe_union(self):
        df1 = generate_simple_dataframe()
        df2 = generate_simple_dataframe()
        df = dataframe_union([df1, df2])
        # show_dataframe(df)
        row_count = dataframe_count(df, count_type="row")
        column_count = dataframe_count(df, count_type="column")
        assert row_count == 6
        assert column_count == 3

    def test_dataframe_join(self):
        None

    # 2022.01.01 测试通过
    def test_dataframe_count(self):
        df = generate_simple_dataframe()
        row_count = dataframe_count(df, count_type="row")
        column_count = dataframe_count(df, count_type="column")
        cell_count = dataframe_count(df, count_type="cell")
        assert row_count == 3
        assert column_count == 3
        assert cell_count == 9

    # 2022.01.01 测试通过
    def test_dataframe_first_value(self):
        df = generate_simple_dataframe()
        val = dataframe_first_value(df)
        assert val == "alice"

    # 2022.01.01 测试通过
    def test_dataframe_groupby_count(self):
        df1 = generate_simple_dataframe()
        df2 = generate_simple_dataframe()
        df = dataframe_union([df1, df2])
        df = dataframe_groupby_count(df, "name", count_name="name_count")
        # show_dataframe(df)
        count1 = df.iloc[[0], [1]].values[0][0]
        assert count1 == 2

    def test_generate_simple_series(self):
        None

    def test_series_from_dict(self):
        None

    def test_series_to_dict(self):
        None

    def test_series_to_list(self):
        None

    def test_series_to_dataframe(self):
        None


if __name__ == '__main__':
    unittest.main()
    """
    python -m unittest tests/test_utils_dataframe.py
    """
