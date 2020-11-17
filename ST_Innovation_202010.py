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
        logdir=False,
        devices=[config.to_device["android"],],
    )


class ST_Innovation(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_3175(self):
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)
        sleep(3)
        util.innovation_result_list(self.poco)

    def test_3174(self):
        # todo 设计有点问题
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)
        sleep(3)
        util.innovation_result_detail_from_pic(self.poco)

    def test_3172(self):
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)

    #  成果概览列表查询验证
    def test_3176(self):
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)
        sleep(3)
        util.innovation_result_list(self.poco)
        sleep(3)
        util.innovation_result_list_search(self.poco)

    # 成果概览详情验证（成果概览列表）
    def test_3177(self):
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)
        sleep(3)
        util.innovation_result_list(self.poco)
        sleep(3)
        util.innovation_result_details(self.poco)

    # 研究单位详情验证
    def test_3178(self):
        util.app_home_page(self.poco)
        sleep(3)
        util.innovation_home_page(self.poco)
        sleep(3)
        util.innovation_result_list(self.poco)
        sleep(3)
        util.innovation_result_details(self.poco)
        sleep(3)
        util.innovation_corporation_description(self.poco)



if __name__ == '__main__':
    unittest.main()
