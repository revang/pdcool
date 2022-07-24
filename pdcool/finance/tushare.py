import tushare as ts
import numpy as np
from pdcool.utils.database.mysql import DBUtil
from pdcool.utils.dataframe import *
from pdcool.utils.param import get_param


token = get_param("pdcool", "finance", "tushare_token")
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
    df = pro.stock_basic(
        exchange="",
        list_status="L",
        fields="ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_status,list_date,delist_date,is_hs",
    )

    # 补充缺失列
    df["code"] = df["ts_code"].map(lambda x: x.split(".")[0])
    df["exchange"] = df["ts_code"].map(lambda x: x.split(".")[1])
    df["source"] = "tushare"

    # 处理异常值和字典转换
    df.replace(
        to_replace=r"^\s*$", value=np.nan, regex=True, inplace=True
    )  # 将空字符串变更为空值
    df["is_hs"].replace({"N": "否", "H": "沪港通", "S": "深港通"}, inplace=True)
    df["list_status"].replace({"L": "上市", "D": "退市", "P": "暂停上市"}, inplace=True)

    # 重命名列
    df.rename(
        columns={"ts_code": "fina_code", "is_hs": "shsc", "market": "list_board"},
        inplace=True,
    )

    # 列筛选排序
    df = df[
        [
            "fina_code",
            "code",
            "exchange",
            "name",
            "fullname",
            "enname",
            "cnspell",
            "area",
            "industry",
            "list_status",
            "list_board",
            "list_date",
            "delist_date",
            "curr_type",
            "shsc",
            "source",
        ]
    ]

    # 重命名列(和数据库列名一致)
    df.set_axis(
        [
            "c_fina_code",
            "c_code",
            "c_exchange",
            "c_name",
            "c_fullname",
            "c_enname",
            "c_cnspell",
            "c_area",
            "c_industry",
            "c_list_status",
            "c_list_board",
            "c_list_date",
            "c_delist_date",
            "c_curr_type",
            "c_shsc",
            "c_source",
        ],
        axis="columns",
        inplace=True,
    )

    dataframe_to_table(df, "ttmp_stock", if_exists="replace")

    db = DBUtil()

    update_count = db.update(
        """update tstock t,ttmp_stock s
    set t.c_fina_code   = ifnull(s.c_fina_code  ,t.c_fina_code  ),
        t.c_code        = ifnull(s.c_code       ,t.c_code       ),
        t.c_exchange    = ifnull(s.c_exchange   ,t.c_exchange   ),
        t.c_name        = ifnull(s.c_name       ,t.c_name       ),
        t.c_fullname    = ifnull(s.c_fullname   ,t.c_fullname   ),
        t.c_enname      = ifnull(s.c_enname     ,t.c_enname     ),
        t.c_cnspell     = ifnull(s.c_cnspell    ,t.c_cnspell    ),
        t.c_area        = ifnull(s.c_area       ,t.c_area       ),
        t.c_industry    = ifnull(s.c_industry   ,t.c_industry   ),
        t.c_list_status = ifnull(s.c_list_status,t.c_list_status),
        t.c_list_board  = ifnull(s.c_list_board ,t.c_list_board ),
        t.c_list_date   = ifnull(s.c_list_date  ,t.c_list_date  ),
        t.c_delist_date = ifnull(s.c_delist_date,t.c_delist_date),
        t.c_curr_type   = ifnull(s.c_curr_type  ,t.c_curr_type  ),
        t.c_shsc        = ifnull(s.c_shsc       ,t.c_shsc       ),
        t.c_source      = ifnull(s.c_source     ,t.c_source     ),
        t.c_update_time = now()
    where t.c_fina_code = s.c_fina_code"""
    )

    insert_count = db.insert(
        """insert ignore into tstock(c_fina_code,c_code,c_exchange,c_name,c_fullname,c_enname,c_cnspell,c_area,c_industry,c_list_status,c_list_board,c_list_date,c_delist_date,c_curr_type,c_shsc,c_source,c_create_time,c_update_time)
    select c_fina_code,
        c_code        ,
        c_exchange    ,
        c_name        ,
        c_fullname    ,
        c_enname      ,
        c_cnspell     ,
        c_area        ,
        c_industry    ,
        c_list_status ,
        c_list_board  ,
        c_list_date   ,
        c_delist_date ,
        c_curr_type   ,
        c_shsc        ,
        c_source      ,
        now(),
        now()
    from ttmp_stock"""
    )

    db.execute("drop table ttmp_stock")
    print(f"sync stock complete, update={update_count}, insert={insert_count}")


def get_dataframe_for_index(index_code=None, market=None):
    """
    获取指数信息
    index_code 指数代码
    market     市场代码: MSCI 指数, CSI 中证指数, SSE 上交所指数, SZSE 深交所指数, CICC 中金指数, SW 申万指数, OTH 其他指数
    """
    df = pro.index_basic(ts_code=index_code, market=market)
    return df


sync_stock()
