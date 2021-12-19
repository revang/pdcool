
import unittest
import logging
from pdcool.utils.datetime import *

logging.basicConfig(level=logging.DEBUG)


class UtilsDatetimeTest(unittest.TestCase):
    def test_current_time(self):
        now = current_time()
        logging.debug(now)

    def test_current_date(self):
        date = current_date()
        logging.debug(date)


if __name__ == '__main__':
    unittest.main()
