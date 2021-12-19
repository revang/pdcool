import unittest
import logging
from pdcool.utils.string import *

logging.basicConfig(level=logging.DEBUG)


class UtilsStringTest(unittest.TestCase):
    def test_string_replace(self):
        text = "ac*bb*ac*xx*ac*bb"
        replace_dict = {"ac": "yz", "bb": "pp", "xx": ""}
        text = string_replace(text, replace_dict)
        logging.debug(text)
        assert text == "yz*pp*yz**yz*pp"


if __name__ == '__main__':
    unittest.main()
