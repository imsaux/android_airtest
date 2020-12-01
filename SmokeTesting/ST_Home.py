# -*- encoding=utf8 -*-
__author__ = "suny"


import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from PO import Public, Utility


if not cli_setup():
    auto_setup(__file__)
    connect_device(Utility.setting["android"])


class 首页(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_首页跳转验证_3035(self):
        Public.app_home(self.poco)

