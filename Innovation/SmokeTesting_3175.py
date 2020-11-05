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
            "android://127.0.0.1:5037/1f4ac875?cap_method=MINICAP_STREAM&&ori_method=ADBORI&&touch_method=ADBTOUCH", ],
        project_root="Z:/Downloads/AirTest_python_script"
    )


class SmokeTesting_3175(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def _innovation_result_list(self):
        # 成果概览列表
        _obj = self.poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring(
            "android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/rl_index_result").child(
            "android.widget.TextView")[1]
        _obj.click()
        _result_list_obj = self.poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "com.sgcc.grsg.app:id/innovation_overview_result_bar").offspring("com.sgcc.grsg.app:id/tv_navigatio_title")
        _result_list_obj.wait_for_appearance()
        _result_list_obj_text = _result_list_obj.get_text()
        assert_equal(_result_list_obj_text, '成果概览', '成果概览列表页显示验证')

    def test_3175(self):
        # 3175用例
        SmokeTesting_3035._app_home_page()
        SmokeTesting_3172._innovation_home_page()
        self._innovation_result_list()

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
