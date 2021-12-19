
import unittest
from pdcool.utils.database import *
import logging

logging.basicConfig(level=logging.DEBUG)


class UtilsDatabaseTest(unittest.TestCase):
    # 2021.12.19 测试通过
    def test_queryone(self):
        db = DBUtil()
        value = db.queryone("select c_value from tparameter where c_system='pdcool' and c_module='web' and c_item='user_agent'")[0]
        logging.debug(value)


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
