from hs_udata import set_token, fund_list
import tushare as ts
from pdcool.utils.dataframe import *
from pdcool.utils.param import *
from pdcool.utils.database.mongo import *


def sync_stock_by_hsudata():
    token = get_param("pdcool", "finance", "hsudata_token")
    set_token(token=token)


def sync_fund_by_tushare():
    token = get_param("pdcool", "finance", "tushare_token")
    pro = ts.pro_api(token)
    df = pro.stock_basic(
        exchange="",
        list_status="L",
        fields="ts_code,name",
    )
    df = dataframe_rename(df, {"ts_code": "stock_code", "name": "stock_name"})
    dictlist = dataframe_to_dictlist(df)

    db = MongoDBUtil()
    insert_count = db.insert("stock", dictlist)
    print(f"sync stock complete, update=0, insert={insert_count}")

    # print(dictlist)
    # show_dataframe(df)
