
import unittest
from pdcool.utils.dbutil import *
import logging

logging.basicConfig(level=logging.DEBUG)


class UtilsDbutilTest(unittest.TestCase):
    def test_get_param(self):
        # value = get_param("dutool", "web", "user_agent")
        # logging.debug(f"{value}")
        # self.assertIsNotNone(value)

        db = DBUtil()
        value = db.queryone("select c_value from tparameter where c_system='pdcool' and c_module='web' and c_item='user_agent'")[0]
        return value


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
