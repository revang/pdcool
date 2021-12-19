import time
from pdcool.utils.dbutil import DBUtil
from pdcool.utils.datetime import current_time


def get_param(system, module, item):
    db = DBUtil()
    return db.queryone(f"select c_value from tparameter where c_system='{system}' and c_module='{module}' and c_item='{item}'")[0]


def put_param(system, module, item, describe, value):
    db = DBUtil()
    return db.insert(f"""insert into tparameter(c_system,c_module,c_item,c_describe,c_value,c_createtime,c_updatetime) 
    values('{system}','{module}','{item}','{describe}','{value}','{current_time()}','{current_time()}')""")


def post_param(system, module, item, value):
    db = DBUtil()
    return db.insert(f"""update tparameter set c_value='{value}',c_updatetime='{current_time()}'
    where c_system='{system}' and c_module='{module}' and c_item='{item}'""")


def delete_param(system, module, item):
    db = DBUtil()
    return db.insert(f"""delete from tparameter where c_system='{system}' and c_module='{module}' and c_item='{item}'""")


def show_param():
    db = DBUtil()
    statement = "select c_system,c_module,c_item,c_describe,c_value,c_createtime,c_updatetime from tparameter"
    rows = db.query(statement)
    for row in rows:
        print(row)
