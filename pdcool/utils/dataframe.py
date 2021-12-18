import json
from pdcool.utils.config import dbconfig
from sqlalchemy import create_engine
import pandas as pd
from pandas.core.series import Series


def generate_simple_dataframe():
    dict_list = [
        {"name": "alice", "age": 18, "gender": "female"},
        {"name": "bob", "age": 8, "gender": "male"},
        {"name": "jack", "age": 13, "gender": "male"}
    ]
    df = pd.DataFrame(dict_list)
    return df


def dataframe_from_json(json_data):
    """
    加载json到dataframe. 注意: 这里json准确说应该是dict的list
    """
    df = pd.DataFrame(json_data)
    return df


def dataframe_to_json(df):
    """
    加载dataframe到json. 注意: 这里json准确说应该是dict的list
    """
    json_text = df.to_json(orient="records")
    json_data = json.loads(json_text)
    return json_data


def dataframe_to_csv(df, path):
    """
    加载dataframe到csv文件
    """
    df.to_csv(path, index=False)


def dataframe_from_csv(path):
    """
    加载csv文件到dataframe
    """
    return pd.read_csv(path)


def dataframe_to_excel(df, path):
    """
    加载dataframe到excel文件. 注意: 只支持xlsx格式
    """
    # df.to_csv(path, index=False)
    df.to_excel(path, index=False)


def dataframe_from_excel(path, sheet_name="Sheet1"):
    """
    加载excel文件到dataframe. 注意: 只支持xlsx格式
    """
    return pd.read_excel(path, sheet_name=sheet_name)


def dataframe_to_table(dataframe, table, if_exists="append"):
    """
    加载dataframe到数据表. if_exists: fail 引发ValueError; replace 在插入新值前删除表; append 向现有表插入新值
    """
    database_url = "mysql+pymysql://%s:%s@%s:%s/%s" % (dbconfig.get("username"), dbconfig.get("password"), dbconfig.get("host"), dbconfig.get("port"), dbconfig.get("database"))
    engine = create_engine(database_url)
    dataframe.to_sql(table, engine, if_exists=if_exists, index=False)


def dataframe_from_sql(sql, type=None):
    """
    加载sql到dataframe
    """
    db = "mysql+pymysql://%s:%s@%s:%s/%s" % (dbconfig.get("username"), dbconfig.get("password"), dbconfig.get("host"), dbconfig.get("port"), dbconfig.get("database"))
    df = pd.read_sql(sql, db)

    if type == "rename":
        df.rename(columns=lambda x: x[2:], inplace=True)

    return df


def show_dataframe(df, type="normal"):
    if type == "normal":
        print(df)
    if type == "json":
        json_data = dataframe_to_json(df)
        for i in json_data:
            print(i)
    raise ValueError(f"invalid type: {type}")


def dataframe_concat(df_list, type="row"):
    """
    dataframe合并
    """
    if type == "row":
        return pd.concat(df_list)
    if type == "column":
        return pd.concat(df_list, axis=1)
    raise ValueError(f"invalid type: {type}")


def generate_simple_series():
    user_dict = {"name": "alice", "age": 18, "gender": "female"}
    return pd.Series(user_dict)


def series_to_list(s):
    return Series.tolist(s)


def series_to_dict(s):
    return Series.to_dict(s)


def series_to_dataframe(s):
    df = pd.DataFrame(s)
    df = df.T  # 转置: 交换行列
    return df
