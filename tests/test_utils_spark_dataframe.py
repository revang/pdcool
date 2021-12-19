
import unittest
from pdcool.utils.spark_dataframe import *
from pdcool.utils.dataframe import show_dataframe, dataframe_from_sql


class UtilsDbutilTest(unittest.TestCase):

    # # 2021.12.19 测试通过
    # def test_spark_dataframe_from_sql(self):
    #     stock_sparkdf = spark_dataframe_from_sql("select c_fina_code,c_name from tstock t")
    #     stock_sparkdf.createOrReplaceTempView("tstock")

    #     stock_quotes_sparkdf = spark_dataframe_from_sql("select * from tstock_quote_daily t where t.c_trade_date='2021-12-17'")
    #     stock_quotes_sparkdf.createOrReplaceTempView("tstock_quote_daily")

    #     sparkdf = spark_query("""select t.c_fina_code,t.c_name,s.c_trade_date,s.n_prev_close_price,s.n_open_price,s.n_high_price,s.n_low_price,s.n_close_price
    #     from tstock t, tstock_quote_daily s where t.c_fina_code=s.c_fina_code
    #     order by s.c_trade_date desc,t.c_fina_code asc""")
    #     sparkdf.show()

    # # 2021.12.19 测试通过
    # def test_spark_dataframe_from_dataframe(self):
    #     df = dataframe_from_sql("select c_fina_code,c_name from tstock t")
    #     sparkdf = spark_dataframe_from_dataframe(df)
    #     sparkdf.show()

    # 2021.12.19 测试通过
    def test_spark_dataframe_to_dataframe(self):
        # 数据准备
        # df = dataframe_from_sql("select c_fina_code,c_name from tstock limit 10")
        # dataframe_to_csv(df, "stock.csv") # 注意: 这一步生成的csv还是带head的, 需要手动去掉, 才能执行后续操作

        spark_execute("drop table if exists stock")
        spark_execute("create table if not exists stock(stock_code string, stock_name string) row format delimited fields terminated by ','")  # Hive-SQL
        spark_execute(r"load data local inpath 'D:\\temp\\stock.csv' into table stock")
        sparkdf = spark_query("select * from stock")
        df = spark_dataframe_to_dataframe(sparkdf)
        show_dataframe(df)


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
