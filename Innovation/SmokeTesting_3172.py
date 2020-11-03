# -*- encoding=utf8 -*-
__author__ = "suny"

import unittest
import time
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

if not cli_setup():
    auto_setup(
        __file__, 
        logdir=True, 
        devices=[
            "android://127.0.0.1:5037/1f4ac875?cap_method=MINICAP_STREAM&&ori_method=ADBORI&&touch_method=ADBTOUCH",], 
        project_root="Z:/Downloads/AirTest_python_script"
    )


class SmokeTesting_3172(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)
    
    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    
    def _first_page(self):
        # 首页
        self.poco("com.sgcc.grsg.app:id/tv_index_innovate").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("com.sgcc.grsg.app:id/navigation").offspring("com.sgcc.grsg.app:id/tv_navigatio_title").get_text()
        assert_equal(_v, "培育创新", "培育创新首页加载正常")

    def test_3172(self):
        self._first_page()


if __name__ == '__main__':
    unittest.main(verbosity=2)