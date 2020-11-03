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


class SmokeTesting_3174(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)
    
    def tearDown(self):
        stop_app("com.sgcc.grsg.app")


    def _app_home_page(self):
        _home_page_title_obj = self.poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/tv_index_title")
        _home_page_title_obj.wait_for_appearance()
        _home_page_title_obj_text = _home_page_title_obj.get_text()
        assert_equal(_home_page_title_obj_text, '首页', '首页显示正常')
        
    def _first_page(self):
        # 首页
        self.poco("com.sgcc.grsg.app:id/tv_index_innovate").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("com.sgcc.grsg.app:id/navigation").offspring("com.sgcc.grsg.app:id/tv_navigatio_title").get_text()
        assert_equal(_v, "培育创新", "培育创新首页加载正常")

    def _innovation_result_detail_pic(self):
        # 成果概览详情
        _obj = self.poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/innovation_results").child("android.widget.LinearLayout")[0].child("com.sgcc.grsg.app:id/title")
        _obj_text = _obj.get_text()
        _obj.click()
        _obj.wait_for_disappearance()
        _clicked_obj = self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[2]
        _clicked_obj.wait_for_appearance()
        _clicked_obj_text = _clicked_obj.get_text()
        assert_equal(_obj_text, _clicked_obj_text, '成果概览详情正确显示')
        
        
    def test_3174(self):
        self._app_home_page()
        self._first_page()
        self._innovation_result_detail_pic()


if __name__ == '__main__':
    unittest.main(verbosity=2)