
import unittest
from pdcool.utils.param import *
import logging

logging.basicConfig(level=logging.DEBUG)


class CommonTest(unittest.TestCase):
    def test_param(self):
        # get_param ---> OK
        # value = get_param("pdcool", "web", "user_agent")
        # logging.debug(f"{value}")

        # put_param ---> OK
        # value = put_param("test", "test", "test", "test", "test")
        # logging.debug(f"{value}")

        # post_param ---> OK
        # value = post_param("test", "test", "test", "hello")
        # logging.debug(f"{value}")

        # delete_param ---> OK
        # value = delete_param("test", "test", "test")
        # logging.debug(f"{value}")

        # show_param ---> OK
        show_param()


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
