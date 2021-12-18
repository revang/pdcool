import time
from pdcool.utils.db_utils import DBUtil


def get_param(system, module, item):
    db = DBUtil()
    statement = "select c_value from tparameter where c_system=%s and c_module=%s and c_item=%s"
    args = [system, module, item]
    value = db.queryone(statement, args)[0]
    return value


def put_param(system, module, item, describe, value):
    db = DBUtil()
    statement = "insert into tparameter(c_system,c_module,c_item,c_describe,c_value,c_createtime,c_updatetime) values(%s,%s,%s,%s,%s,%s,%s)"
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    args = [system, module, item, describe, value, current_time, current_time]
    count = db.insert(statement, args)
    return count


def post_param(system, module, item, value):
    db = DBUtil()
    statement = "update tparameter set c_value=%s,c_updatetime=%s where c_system=%s and c_module=%s and c_item=%s"
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    args = [value, current_time, system, module, item]
    count = db.update(statement, args)
    return count


def delete_param(system, module, item):
    db = DBUtil()
    statement = "delete from tparameter where c_system=%s and c_module=%s and c_item=%s"
    args = [system, module, item]
    count = db.insert(statement, args)
    return count


def show_param():
    db = DBUtil()
    statement = "select c_system,c_module,c_item,c_describe,c_value,c_createtime,c_updatetime from tparameter"
    rows = db.query(statement)
    for row in rows:
        print(row)
