
import unittest
from kdcool.system.param import *
import logging

logging.basicConfig(level=logging.DEBUG)


class CommonTest(unittest.TestCase):
    def test_get_param(self):
        value = get_param("dutool", "web", "user_agent")
        logging.debug(f"{value}")
        self.assertIsNotNone(value)


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
