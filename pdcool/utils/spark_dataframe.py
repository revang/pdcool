#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author            : revang
Date              : 2022-01-01 18:47:35
Last Modified by  : revang
Last Modified time: 2022-01-01 18:47:35
"""

from pyspark.sql import SparkSession
from pdcool.utils.database.config import dbconfig as config

jdbc_url = (
    f'jdbc:mysql://{config.get("host")}:{config.get("port")}/{config.get("database")}'
)
jdbc_prop = {
    "user": config.get("username"),
    "password": config.get("password"),
    "driver": "com.mysql.jdbc.Driver",
}
spark = (
    SparkSession.builder.appName("PySpark Application")
    .enableHiveSupport()
    .getOrCreate()
)


def spark_dataframe_from_sql(sql):
    """
    加载sql到spark_dataframe
    """
    spark_sql = f"({sql}) t"
    sparkdf = spark.read.jdbc(table=spark_sql, url=jdbc_url, properties=jdbc_prop)
    return sparkdf


def spark_dataframe_from_dataframe(df):
    """
    加载dataframe到spark_dataframe
    """
    sparkdf = spark.createDataFrame(df)
    return sparkdf


def spark_dataframe_to_dataframe(sparkdf):
    """
    加载spark_dataframe到dataframe
    """
    df = sparkdf.toPandas()
    return df


def spark_execute(sql):
    """
    执行sql
    """
    spark.sql(sql)


def spark_query(sql):
    """
    执行查询sql. 如果是select语句，会返回spark_dataframe
    """
    sparkdf = spark.sql(sql)
    return sparkdf
