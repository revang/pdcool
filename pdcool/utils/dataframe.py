import json
import re
from pdcool.utils.config import dbconfig as config
from sqlalchemy import create_engine
import pandas as pd
from pandas.core.series import Series

""" 基于pandas, 参考文档: http://www.pypandas.cn/docs/reference.html """


def generate_simple_dataframe():
    """ 生成一个dataframe """
    simple_dictlist = [
        {"name": "alice", "age": 18, "gender": "female"},
        {"name": "bob", "age": 8, "gender": "male"},
        {"name": "jack", "age": 13, "gender": "male"}
    ]
    return pd.DataFrame(simple_dictlist)


def dataframe_from_dictlist(dictlist):
    """ 加载dictlist到dataframe """
    return pd.DataFrame(dictlist)


def dataframe_to_dictlist(df):
    """ 加载dataframe到dictlist """
    json_text = df.to_json(orient="records")
    json_data = json.loads(json_text)
    return json_data


def dataframe_from_csv(path, column_name=None, column_type=None, encoding="utf-8"):
    """ 获取dataframe(读取csv文件) """
    if not isinstance(path, str) and not isinstance(path, list):
        raise ValueError(f"invalid path: {path}")

    if isinstance(path, str):
        return pd.read_csv(path, names=column_name, dtype=column_type, encoding=encoding)

    if isinstance(path, list):
        df_list = []
        for item in path:
            item_df = pd.read_csv(item, names=column_name, dtype=column_type, encoding=encoding)
            df_list.append(item_df)
        df = pd.concat(df_list)
        return df


def dataframe_to_csv(df, path):
    """ 保存dataframe(写入csv文件) """
    df.to_csv(path, index=False)


def dataframe_from_excel(path, sheet=0, column_name=None, column_type=None, encoding="utf-8"):
    """ 获取dataframe(读取excel文件) """
    return pd.read_excel(path, sheet_name=sheet, names=column_name, dtype=column_type, encoding=encoding)


def dataframe_to_excel(df, path):
    """ 
    加载dataframe到excel文件. 注意: 只支持xlsx格式
    """
    df.to_excel(path, index=False)


def dataframe_to_table(dataframe, table, insert_mode="append"):
    """
    加载dataframe到数据表. if_exists: fail 引发ValueError; replace 在插入新值前删除表; append 向现有表插入新值
    """
    if insert_mode not in ("append", "replace"):
        raise ValueError(f"invalid insert_mode: {insert_mode}")

    username = config.get("username")
    password = config.get("password")
    host = config.get("host")
    port = config.get("port")
    database = config.get("database")
    database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(database_url)
    dataframe.to_sql(table, engine, if_exists=insert_mode, index=False)


def dataframe_from_sql(sql):
    """
    加载sql到dataframe
    """
    username = config.get("username")
    password = config.get("password")
    host = config.get("host")
    port = config.get("port")
    database = config.get("database")
    database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    df = pd.read_sql(sql, database_url)
    return df


def show_dataframe(df, show_type="normal"):
    """ 显示dataframe """
    if show_type not in ("normal", "dictlist"):
        raise ValueError(f"invalid show_type: {show_type}")

    if show_type == "normal":
        pd.set_option('display.unicode.east_asian_width', True)  # 设置命令行输出右对齐
        print(df)
        return

    if show_type == "dictlist":
        distlist = dataframe_to_dictlist(df)
        for i in distlist:
            print(i)
        return


def dataframe_concat(df_list, type="row"):
    """
    合并dataframe
    """
    if type == "row":
        return pd.concat(df_list)
    if type == "column":
        return pd.concat(df_list, axis=1)
    raise ValueError(f"invalid type: {type}")


def dataframe_union(df_list):
    """ dataframe纵向拼接 """
    return pd.concat(df_list)


def dataframe_join(df1, df2):
    """ dataframe横向拼接 """
    return pd.merge(df1, df2)


def dataframe_count(df, count_type="row"):
    """ dataframe行数/列数/单元格数 """
    if count_type not in ("row", "column", "cell"):
        raise ValueError(f"invaild count_type: {count_type}")

    if count_type == "row":
        return len(df)

    if count_type == "column":
        return len(df.columns)

    if count_type == "cell":
        return df.size


def dataframe_first_value(df):
    """ dataframe第一个值 """
    return df.iloc[[0], [0]].values[0][0]


def generate_simple_series():
    """ 生成一个Series """
    simple_dict = {"name": "alice", "age": 18, "gender": "female"}
    return pd.Series(simple_dict)


def series_to_list(s):
    """
    加载series到list
    """
    return Series.tolist(s)


def series_to_dict(s):
    """
    加载series到dict
    """
    return Series.to_dict(s)


def series_to_dataframe(s):
    """
    加载series到dataframe
    """
    df = pd.DataFrame(s)
    df = df.T  # 转置: 交换行列
    return df
