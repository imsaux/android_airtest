from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

def _app_home_page(poco):
    # app首页
    _home_page_title_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.sgcc.grsg.app:id/tv_index_title")
    _home_page_title_obj.wait_for_appearance()
    _home_page_title_obj_text = _home_page_title_obj.get_text()
    assert_equal(_home_page_title_obj_text, '首页', '首页显示正常')

def _innovation_home_page(poco):
    # 培育创新首页
    _innovation_btn = poco("com.sgcc.grsg.app:id/tv_index_innovate")
    _innovation_btn.click()
    _innovation_first_page_title_obj = poco("android.widget.LinearLayout").offspring(
        "com.sgcc.grsg.app:id/root_view").offspring("com.sgcc.grsg.app:id/navigation").offspring(
        "com.sgcc.grsg.app:id/tv_navigatio_title")
    _innovation_first_page_title_obj.wait_for_appearance()
    _innovation_first_page_title_obj_text = _innovation_first_page_title_obj.get_text()
    assert_equal(_innovation_first_page_title_obj_text, "培育创新", "培育创新首页显示正常")

def _innovation_result_detail_from_pic(poco):
    # 成果概览详情（点击图片）
    _obj = poco("com.sgcc.grsg.app:id/title")
    _obj_text = _obj.get_text()
    _obj.click()
    # _clicked_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[2]
    _click_obj = poco("com.sgcc.grsg.app:id/image")
    _click_obj.wait_for_appearance()
    time.sleep(3)
    _clicked_obj_text = _clicked_obj.get_text()
    assert_equal(_obj_text, _clicked_obj_text, '成果概览详情正确显示')

def _innovation_result_list(poco):
    # 成果概览列表
    _obj = poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring(
        "android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/rl_index_result").child(
        "android.widget.TextView")[1]
    _obj.click()
    _result_list_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.sgcc.grsg.app:id/innovation_overview_result_bar").offspring("com.sgcc.grsg.app:id/tv_navigatio_title")
    _result_list_obj.wait_for_appearance()
    _result_list_obj_text = _result_list_obj.get_text()
    assert_equal(_result_list_obj_text, '成果概览', '成果概览列表页显示验证')

def _innovation_result_list_search(poco):
    # 成果概览列表搜索
    pass