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


class ft_589(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.nearme.note")
        time.sleep(5)
    
    def tearDown(self):
        pass
    
    def _create_note(self):
        self.poco("com.nearme.note:id/create_note").click()
        self.poco("com.nearme.note:id/text").click()
        text("测试文本")
        self.poco("转到上一层级").click()

    def _delete_note(self):
        self.poco("com.nearme.note:id/edit_note").click()
        self.poco("android.widget.LinearLayout").offspring("com.nearme.note:id/note_list").child("com.nearme.note:id/item")[0].child("oppo:id/oppo_listview_scrollchoice_checkbox").click()
        self.poco("android.widget.LinearLayout").offspring("com.nearme.note:id/note_delete").offspring("com.nearme.note:id/icon").click()
        self.poco("android:id/button3").click()
        
    def test_scene_2(self):
        self._create_note()
        time.sleep(3)
        self._delete_note()

if __name__ == '__main__':
    unittest.main()