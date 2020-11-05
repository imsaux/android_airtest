# -*- encoding=utf8 -*-
__author__ = "suny"

import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Homepage.SmokeTesting_3035 import SmokeTesting_3035
from Innovation.SmokeTesting_3172 import SmokeTesting_3172

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

    def _innovation_result_detail_from_pic(self):
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
        SmokeTesting_3035._app_home_page()
        SmokeTesting_3172._innovation_home_page()
        self._innovation_result_detail_from_pic()


if __name__ == '__main__':
    unittest.main(verbosity=2)