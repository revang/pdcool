from pdcool.utils.config import dbconfig
from sqlalchemy import create_engine
import pandas as pd


# def dataframe_from_json(json_data):
#     None


def dataframe_to_json(df):
    """
    加载dataframe到json
    """
    json_text = df.to_json(orient="records")
    json_data = df.loads(json_text)
    return json_data


# def dataframe_from_csv(csv):
#     None


# def dataframe_to_csv(df, csv):
#     None


def dataframe_to_table(dataframe, table, if_exists="append"):
    """
    if_exists: fail 引发ValueError; replace 在插入新值前删除表; append 向现有表插入新值
    加载dataframe到数据表
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


# def show_dataframe(df, type="json"):
#     None


def dataframe_concat(df_list, type="row"):
    """
    dataframe合并
    """
    if type == "row":
        return pd.concat(df_list)
    if type == "column":
        return pd.concat(df_list, axis=1)
    raise ValueError("")
