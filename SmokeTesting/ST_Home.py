# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Public.home import Home


class 首页(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.page_home = Home()

    def setUp(self):
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_首页跳转_3035(self):
        from PO.Innovation import home
        self.page_home.click_innovation_button()

    def test_首页跳转_(self):
        from PO.Innovation import home