# -*- encoding=utf8 -*-
__author__ = "suny"

import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import util
import config

if not cli_setup():
    auto_setup(
        __file__,
        logdir=True,
        devices=[config.to_device["android"],],
        # project_root="Z:/Downloads/AirTest_python_script"
    )


class SmokeTesting_3172(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)
    
    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_3172(self):
        util._app_home_page(self.poco)
        time.sleep(3)
        util._innovation_home_page(self.poco)


if __name__ == '__main__':
    unittest.main(verbosity=2)