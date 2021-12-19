
import unittest
from pdcool.utils.param import *
import logging

logging.basicConfig(level=logging.DEBUG)


class CommonTest(unittest.TestCase):
    # 2021.12.19 测试通过
    # def test_get_param(self):
    #     value = get_param("pdcool", "web", "user_agent")
    #     logging.debug(f"{value}")

    # 2021.12.19 测试通过
    # def test_put_param(self):
    #     value = put_param("test", "test", "test", "test", "test")
    #     logging.debug(f"{value}")

    # 2021.12.19 测试通过
    # def test_post_param(self):
    #     value = post_param("test", "test", "test", "hello")
    #     logging.debug(f"{value}")

    # 2021.12.19 测试通过
    # def test_delete_param(self):
    #     value = delete_param("test", "test", "test")
    #     logging.debug(f"{value}")

    # 2021.12.19 测试通过
    def test_show_param(self):
        show_param()


if __name__ == '__main__':
    """
    python -m unittest tests/test_param.py 
    """
    unittest.main()
