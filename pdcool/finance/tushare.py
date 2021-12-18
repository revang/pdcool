
import tushare as ts
from pdcool.utils.db_utils import DBUtil
from pdcool.utils.dataframe import *
from pdcool.utils.param import get_param


token = get_param("dutool", "finance", "tushare_token")
pro = ts.pro_api(token)

"""
数据同步流程:
1. 获取dataframe
2. 处理dataframe: 补充缺失列, 处理异常值和字典转换, 重命名列, 列筛选排序, 重命名列(和数据库列名一致)
3. 加载dataframe到临时表
4. 处理临时表到目的表
5. 删除临时表
6. 显示结果
"""


def sync_stock():
    df = pro.stock_basic(exchange="", list_status="L", fields="ts_code,name")

    # 补充缺失列
    df["code"] = df["ts_code"].map(lambda x: x.split(".")[0])
    df["exchange"] = df["ts_code"].map(lambda x: x.split(".")[1])
    df["source"] = "tushare"

    # 处理异常值和字典转换

    # 重命名列
    df.rename(columns={"ts_code": "fina_code"}, inplace=True)

    # 列筛选排序
    df = df[["fina_code", "code", "exchange_market", "name", "source"]]

    # 重命名列(和数据库列名一致)
    df.set_axis(["c_fina_code", "c_code", "c_exchange", "c_name", "c_source"], axis="columns", inplace=True)

    dataframe_to_table(df, "ttmp_stock", if_exists="replace")
    # db = DBUtil()
    # db.execute("replace into tstock(c_code, c_exchange_market, c_name, c_source, c_create_time, c_update_time) select c_code, c_exchange_market, c_name, c_source, now(), now() from ttmp_stock")
    # db.execute("drop table ttmp_stock")
    # count = db.queryone("select count(*) from tstock")[0]
    # print("sync stock complete, count=%s" % (count))
