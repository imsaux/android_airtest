# -*- encoding=utf8 -*-
__author__ = "suny"


import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from PO import Public, Innovation, Utility

if not cli_setup():
    auto_setup(__file__)
    connect_device(Utility.setting["android"])


class 培育创新(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_成果概览列表跳转验证_3175(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_result_list(self.poco)

    def test_成果概览详情内容验证_3174_轮播图(self):
        # todo 设计有点问题
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_result_detail_from_pic(self.poco)

    def test_培育创新首页跳转验证_3172(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)

    #  成果概览列表查询验证
    def test_成果概览列表查询验证_3176(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_result_list(self.poco)
        sleep(3)
        Innovation.innovation_result_list_search(self.poco)

    # 成果概览详情验证（成果概览列表）
    def test_成果概览详情内容验证_3177(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_result_list(self.poco)
        sleep(3)
        Innovation.innovation_result_details(self.poco)

    # 研究单位详情验证
    def test_研究单位详情内容验证_3178(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_result_list(self.poco)
        sleep(3)
        Innovation.innovation_result_details(self.poco)
        sleep(3)
        Innovation.innovation_corporation_description(self.poco)

    # 创新动态详情验证
    def test_创新动态详情内容验证_3179(self):
        Public.app_home(self.poco)
        sleep(5)
        Innovation.innovation_home(self.poco)
        sleep(5)
        Innovation.innovation_developments_details(self.poco)

    #创新动态详情页面
    def test_进入动态详情页面_3181(self):
        # todo 待开发
        pass

    # 培育共同体首页验证
    def test_培育共同体首页跳转验证_3182(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home(self.poco)

    # 培育共同体实验室首页验证
    def test_培育共同体实验室首页跳转验证_3183(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home_more(self.poco)

    # 培育共同体专家列表验证
    def test_培育共同体专家列表跳转验证_3184(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home(self.poco)
        sleep(3)
        Innovation.innovation_experts_list(self.poco)

    # 培育共同体专家详情验证 —— 共同体首页
    def test_培育共同体专家详情内容验证_3185_共同体首页(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(5)
        Innovation.innovation_community_home(self.poco)
        sleep(3)
        Innovation.innovation_experts_details_from_homepage(self.poco)

    # 培育共同体专家详情验证 —— 专家列表
    def test_培育共同体专家详情内容验证_3185_专家列表(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home(self.poco)
        sleep(3)
        Innovation.innovation_experts_list(self.poco)
        sleep(3)
        Innovation.innovation_experts_details_from_experts_list(self.poco)

    #  培育共同体专家列表查询验证
    def test_培育共同体专家列表查询验证_3186(self):
        Public.app_home(self.poco)
        sleep(3)
        Innovation.innovation_home(self.poco)
        sleep(3)
        Innovation.innovation_community_home(self.poco)
        sleep(3)
        Innovation.innovation_experts_list(self.poco)
        sleep(3)
        Innovation.innovation_experts_details_from_experts_list(self.poco)

