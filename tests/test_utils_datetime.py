
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

    def test_date_range(self):
        begin_date = "2021-01-28"
        end_date = "2021-02-01"
        date_list = date_range(begin_date, end_date)
        logging.debug(date_list)
        assert date_list == ['2021-01-28', '2021-01-29', '2021-01-30', '2021-01-31', '2021-02-01']

    def test_date_format(self):
        curr_date = "2021-01-01"
        target = date_format(curr_date, origin_type="YYYY-MM-DD", target_type="YYYYMMDD")
        logging.debug(target)
        assert target == "20210101"

        curr_date = "20210101"
        target = date_format(curr_date, origin_type="YYYYMMDD", target_type="YYYY-MM-DD")
        logging.debug(target)
        assert target == "2021-01-01"


if __name__ == '__main__':
    unittest.main()
