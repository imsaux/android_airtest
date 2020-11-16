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


class SmokeTesting_3175(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_3175(self):
        # 3175用例
        util._app_home_page(self.poco)
        sleep(3)
        util._innovation_home_page(self.poco)
        sleep(3)
        util._innovation_result_list(self.poco)

        # # 生成报告
        # from airtest.report import report
        # from airtest.utils.compat import decode_path, script_dir_name
        # path, name = script_dir_name(__file__)
        # logpath = os.path.join(path, "log.txt")
        # rpt = report.LogToHtml(__file__, logpath, logfile="log.txt", script_name=name)
        # rpt.report(
        #     "c:\\code\\SGCC_ANDROID\\doc\\log_template.html",
        #     output_file="c:\\code\\SGCC_ANDROID\\Innovation\\log.html"
        # )
        #

if __name__ == '__main__':
    unittest.main()
