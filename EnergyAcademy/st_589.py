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


class st_589(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        time.sleep(5)
    
    def tearDown(self):
        pass
    
    def _read_tab1_topic(self):
        self.poco(text="推荐").click()
        self.poco(text="国网信通产业集团创新研发能源大数据中心助力“新基建”").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].get_text()
        assert_equal(_v, "国网信通产业集团创新研发能源大数据中心助力“新基建”", "资讯加载正常")
        self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("firstAnchor").offspring("android.widget.Image").click()
    
    def _read_tab2_topic(self):
        self.poco(text="新闻资讯").click()
        self.poco(text="奇点能源：以电为中心的综合能源服务典型业态——区域能源发展研究（一）").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].get_text()
        assert_equal(_v, "奇点能源：以电为中心的综合能源服务典型业态——区域能源发展研究（一）", "资讯加载正常")
        self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("firstAnchor").offspring("android.widget.Image").click()

    def _read_tab3_topic(self):
        self.poco(text="政策法规").click()
        self.poco(text="住建部发布工程建设强制性国家规范《太阳能发电工程项目规范（征求意见稿）》").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].get_text()
        assert_equal(_v, "住建部发布工程建设强制性国家规范《太阳能发电工程项目规范（征求意见稿）》", "资讯加载正常")
        self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("firstAnchor").offspring("android.widget.Image").click()

    def _read_tab3_topic_failed(self):
        self.poco(text="政策法规").click()
        self.poco(text="住建部发布工程建设强制性国家规范《太阳能发电工程项目规范（征求意见稿）》").click()
        time.sleep(3)
        _v = self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].get_text()
        assert_equal(_v, "hh", "资讯加载正常")
        self.poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("firstAnchor").offspring("android.widget.Image").click()


    def test_scene_read_information(self):
        _topic_btn = self.poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/navigation").offspring("com.sgcc.grsg.app:id/navigation_news").child("android.view.ViewGroup")
        _topic_btn.wait_for_appearance()
        _topic_btn.click()
        time.sleep(3)
        self._read_tab2_topic()
        time.sleep(3)
        self._read_tab3_topic()
        time.sleep(3)
        self._read_tab1_topic()
        time.sleep(3)
        self._read_tab3_topic_failed()


if __name__ == '__main__':
    unittest.main(verbosity=2)