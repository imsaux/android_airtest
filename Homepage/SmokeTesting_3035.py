# -*- encoding=utf8 -*-
__author__ = "suny"

import unittest
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


class SmokeTesting_3035(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)
    
    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def _app_home_page(self):
        # app首页
        _home_page_title_obj = self.poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.sgcc.grsg.app:id/tv_index_title")
        _home_page_title_obj.wait_for_appearance()
        _home_page_title_obj_text = _home_page_title_obj.get_text()
        assert_equal(_home_page_title_obj_text, '首页', '首页显示正常')
        time.sleep(3)

    def test_3035(self):
        self._app_home_page()


if __name__ == '__main__':
    unittest.main(verbosity=2)