#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 17:48:36
Last Modified by  : revang
Last Modified time: 2022-01-01 17:48:36
"""

import json
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from pandas.core.series import Series
from pdcool.utils.database.config import db1 as dbconfig


def generate_simple_dataframe():
    """生成一个dataframe"""
    simple_dictlist = [
        {"name": "alice", "age": 18, "gender": "female"},
        {"name": "bob", "age": 8, "gender": "male"},
        {"name": "jack", "age": 13, "gender": "male"},
    ]
    return pd.DataFrame(simple_dictlist)


def dataframe_from_dictlist(dictlist):
    """获取dataframe(读取dictlist)"""
    return pd.DataFrame(dictlist)


def dataframe_to_dictlist(df):
    """保存dataframe(写入dictlist)"""
    json_text = df.to_json(orient="records")
    json_data = json.loads(json_text)
    return json_data


def dataframe_from_listdict(listdict, dict_type="columns", column_name=None):
    """获取dataframe(读取listdict)"""
    if dict_type not in ("columns", "index"):
        raise ValueError(f"invalid dict_type: {dict_type}")

    if dict_type in ("columns"):
        df = pd.DataFrame.from_dict(
            listdict, orient=dict_type
        )  # 如果dict_type="columns", 则不使用column_name
        return df

    if dict_type in ("index"):
        df = pd.DataFrame.from_dict(listdict, orient=dict_type)
        df.reset_index(level=0, inplace=True)
        if column_name:
            df = dataframe_rename(df, column_name)
        return df


def dataframe_from_csv(path, column_name=None, column_type=None, encoding="utf-8"):
    """获取dataframe(读取csv文件)"""
    if not isinstance(path, str) and not isinstance(path, list):
        raise ValueError(f"invalid path: {path}")

    if isinstance(path, str):
        if not column_name:
            return pd.read_csv(path, dtype=column_type, encoding=encoding)
        else:
            return pd.read_csv(
                path,
                names=column_name,
                dtype=column_type,
                encoding=encoding,
                skiprows=1,
            )

    if isinstance(path, list):
        df_list = []
        for item in path:
            item_df = dataframe_from_csv(
                item,
                column_name=column_name,
                column_type=column_type,
                encoding=encoding,
            )
            df_list.append(item_df)
        df = pd.concat(df_list)
        return df


def dataframe_to_csv(df, path):
    """保存dataframe(写入csv文件)"""
    df.to_csv(path, index=False)


def dataframe_from_excel(path, sheet=0, column_name=None, column_type=None):
    """获取dataframe(读取excel文件)"""
    return pd.read_excel(path, sheet_name=sheet, names=column_name, dtype=column_type)


def dataframe_to_excel(df, path):
    """保存dataframe(写入excel文件)"""
    df.to_excel(path, index=False)


def dataframe_from_sql(sql):
    """获取dataframe(读取sql)"""
    username = dbconfig.get("username")
    password = dbconfig.get("password")
    host = dbconfig.get("host")
    port = dbconfig.get("port")
    database = dbconfig.get("database")
    database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    df = pd.read_sql(sql, database_url)
    return df


def dataframe_to_table(dataframe, table, insert_mode="append"):
    """保存dataframe(写入数据库table)"""
    if insert_mode not in ("append", "replace"):
        raise ValueError(f"invalid insert_mode: {insert_mode}")

    username = dbconfig.get("username")
    password = dbconfig.get("password")
    host = dbconfig.get("host")
    port = dbconfig.get("port")
    database = dbconfig.get("database")
    database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(database_url)
    dataframe.to_sql(table, engine, if_exists=insert_mode, index=False)


def show_dataframe(df, show_type="normal"):
    """显示dataframe"""
    if show_type not in ("normal", "dictlist"):
        raise ValueError(f"invalid show_type: {show_type}")

    if show_type == "normal":
        pd.set_option("display.unicode.east_asian_width", True)  # 设置命令行输出右对齐
        print(df)
        return

    if show_type == "dictlist":
        distlist = dataframe_to_dictlist(df)
        for item in distlist:
            print(item)
        return


def dataframe_rename(df, column):
    """dataframe重命名列名"""
    if not isinstance(column, list) and not isinstance(column, dict):
        raise ValueError(f"invalid column: {column}")

    if isinstance(column, list):
        return df.set_axis(column, axis="columns")

    if isinstance(column, dict):
        return df.rename(columns=column)


def dataframe_empty_none(df):
    """dataframe清空空字符串"""
    df = df.replace("", np.nan)  # 替换空字符串
    df = df.replace(to_replace=r"^\s*?$", value=np.nan)  # 替换空白符
    df = df.fillna(value=np.nan)  # 替换None值
    return df


def dataframe_fill_none(df, val=""):
    """dataframe填充空值的值"""
    return df.fillna(val)


def dataframe_transform_dict(df, column_name, dict):
    """dataframe翻译字典值"""
    df[column_name].replace(dict, inplace=True)
    return df


def dataframe_concat(df_list, type="row"):
    """合并dataframe(已停止维护, 后续版本将会删除)"""
    if type == "row":
        return pd.concat(df_list)
    if type == "column":
        return pd.concat(df_list, axis=1)
    raise ValueError(f"invalid type: {type}")


def dataframe_union(df_list):
    """dataframe纵向拼接"""
    return pd.concat(df_list)


def dataframe_join(df1, df2):
    """dataframe横向拼接"""
    return pd.merge(df1, df2)


def dataframe_count(df, count_type="row"):
    """dataframe行数/列数/单元格数"""
    if count_type not in ("row", "column", "cell"):
        raise ValueError(f"invaild count_type: {count_type}")

    if count_type == "row":
        return len(df)

    if count_type == "column":
        return len(df.columns)

    if count_type == "cell":
        return df.size


def dataframe_first_value(df):
    """dataframe第一个值"""
    return df.iloc[[0], [0]].values[0][0]


def dataframe_groupby_count(df, column, count_name="count"):
    """dataframe分组计数"""
    if not isinstance(column, str) and not isinstance(column, list):
        raise ValueError(f"invaild column: {column}")

    return df.groupby(column).size().to_frame(count_name).reset_index()


def generate_simple_series():
    """生成一个Series"""
    simple_dict = {"name": "alice", "age": 18, "gender": "female"}
    return pd.Series(simple_dict)


def series_from_dict(d):
    """获取series(读取dict)"""
    return pd.Series(d)


def series_to_dict(s):
    """保存series(写入dict)"""
    return Series.to_dict(s)


def series_to_list(s):
    """保存series(写入list)"""
    return Series.tolist(s)


def series_to_dataframe(s, is_transposition=True):
    """保存series(写入dataframe)"""
    df = pd.DataFrame(s)
    if is_transposition:
        df = df.T  # 转置行列
    return df
