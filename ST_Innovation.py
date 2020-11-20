# -*- encoding=utf8 -*-
__author__ = "suny"


import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import BusinessLogic
import Config

if not cli_setup():
    auto_setup(
        __file__,
        logdir=False,
        devices=[Config.to_device["android"], ],
    )


class ST_Innovation(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_3175(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_list(self.poco)

    def test_3174(self):
        # todo 设计有点问题
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_detail_from_pic(self.poco)

    def test_3172(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)

    #  成果概览列表查询验证
    def test_3176(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_list(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_list_search(self.poco)

    # 成果概览详情验证（成果概览列表）
    def test_3177(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_list(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_details(self.poco)

    # 研究单位详情验证
    def test_3178(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_list(self.poco)
        sleep(3)
        BusinessLogic.innovation_result_details(self.poco)
        sleep(3)
        BusinessLogic.innovation_corporation_description(self.poco)

    # 创新动态详情验证
    def test_3179(self):
        BusinessLogic.app_home(self.poco)
        sleep(5)
        BusinessLogic.innovation_home(self.poco)
        sleep(5)
        BusinessLogic.innovation_developments_details(self.poco)

    #创新政策列表查询验证
    def test_3180(self):
        # todo 待定
        pass


    #创新政策详情页面验证
    def test_3181(self):
        # todo 待定
        pass


    # 培育共同体首页验证
    def test_3182(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home(self.poco)

    # 培育共同体实验室首页验证
    def test_3183(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home_more(self.poco)

    # 培育共同体专家列表验证
    def test_3184(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_list(self.poco)

    # 培育共同体专家详情验证 —— 共同体首页
    def test_3185_1(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(5)
        BusinessLogic.innovation_community_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_details_from_homepage(self.poco)

    # 培育共同体专家详情验证 —— 专家列表
    def test_3185_2(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_list(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_details_from_experts_list(self.poco)

    #  培育共同体专家列表查询验证
    def test_3186(self):
        BusinessLogic.app_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_community_home(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_list(self.poco)
        sleep(3)
        BusinessLogic.innovation_experts_details_from_experts_list(self.poco)

