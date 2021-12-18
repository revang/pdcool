
from common import *
import tushare as ts

token = get_param("dutool", "finance", "tushare_token")
pro = ts.pro_api(token)


def sync_stock():
    """
    同步股票信息
        1. 获取dataframe
        2. 处理dataframe
        3. 加载dataframe到临时表
        4. 处理临时表到目的表
        5. 删除临时表
        6. 显示结果
    """
    df = pro.stock_basic(exchange="", list_status="L", fields="ts_code,name")
    df["code"] = df["ts_code"].map(lambda x: x.split(".")[0])
    df["exchange_market"] = df["ts_code"].map(lambda x: x.split(".")[1])
    df["source"] = "tushare"
    df = df[["code", "exchange_market", "name", "source"]]
    df.columns = ["c_code", "c_exchange_market", "c_name", "c_source"]

    dataframe_to_table(df, "ttmp_stock", if_exists="replace")
    db = DBUtil()
    db.execute("replace into tstock(c_code, c_exchange_market, c_name, c_source, c_create_time, c_update_time) select c_code, c_exchange_market, c_name, c_source, now(), now() from ttmp_stock")
    db.execute("drop table ttmp_stock")
    count = db.queryone("select count(*) from tstock")[0]
    print("sync stock complete, count=%s" % (count))


sync_stock()
