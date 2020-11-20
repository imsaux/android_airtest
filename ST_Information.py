# -*- encoding=utf8 -*-
__author__ = "suny"

import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import BusinessLogic
import Utility

if not cli_setup():
    auto_setup(
        __file__,
        logdir=False,
        devices=[Utility.to_device["android"], ],
    )


class 资讯(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    # 资讯，搜索栏功能验证
    def test_资讯查询验证_3038(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_home(self.poco)
        sleep(3)
        BusinessLogic.information_search(self.poco)

    # 查看资讯详情
    def test_资讯详情内容验证_3039(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_home(self.poco)
        sleep(3)
        BusinessLogic.information_details(self.poco)

    # 资讯tab页切换
    def test_资讯TAB切换验证_3040(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_home(self.poco)
        sleep(3)
        BusinessLogic.information_tab_change(self.poco)

    # 资讯，进入资讯首页
    def test_资讯首页跳转验证_3041(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_home(self.poco)

    # 资讯，进入投稿页面
    def test_投稿页面跳转验证_3042(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_contribute_home(self.poco)

    # 资讯，投稿发布
    def test_投稿发布验证_3043(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.information_contribute_home(self.poco)
        sleep(3)
        BusinessLogic.information_contribute_edit(self.poco)
        BusinessLogic.information_contribute_commit(self.poco)

