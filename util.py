from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import *
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
    _innovation_homepage_title_obj_text = ''
    try:
        _innovation_btn = poco("com.sgcc.grsg.app:id/tv_index_innovate")
        _innovation_btn.wait_for_appearance(timeout=180)
        _innovation_btn.click()
    except PocoNoSuchNodeException as ex:
        print(repr(ex))
        # assert_equal('0', '1', '未发现培育创新图标')
        assert_equal('0', '1', '培育创新图标发生异常')
    time.sleep(3)
    try:
        _innovation_homepage_title_obj = poco("com.sgcc.grsg.app:id/tv_navigatio_title")
        _innovation_homepage_title_obj.wait_for_appearance(timeout=180)
        _innovation_homepage_title_obj_text = _innovation_homepage_title_obj.get_text()
    except PocoNoSuchNodeException as ex:
        assert_equal('0', '1', '未发现培育创新标题')
    assert_equal(_innovation_homepage_title_obj_text, "培育创新", "培育创新首页显示正常")


# 成果概览详情（点击图片）
def _innovation_result_detail_from_pic(poco):
    _obj_text, _click_obj_text = '',''
    try:
        _obj = poco("com.sgcc.grsg.app:id/title")
        _obj.wait_for_appearance(timeout=180)
        _obj_text = _obj.get_text()
    except PocoNoSuchNodeException as ex:
        print(repr(ex))
        assert_equal('0', '1', '未发现成果文字')
    # 获取成果名称
    try:
        _img_obj = poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/innovation_results").child("android.widget.LinearLayout")[0].child("com.sgcc.grsg.app:id/image")
        _img_obj.wait_for_appearance(timeout=180)
        _img_obj.click()
    except PocoNoSuchNodeException as ex:
        assert_equal('0', '1', '未发现图片')
    # 点击一个图片
    time.sleep(5)
    try:
        _detail_obj = poco(text=_obj_text)
        # _detail_obj.wait_for_appearance(timeout=180)
        _click_obj_text = _detail_obj.get_text()
    except PocoNoSuchNodeException as ex:
        assert_equal('0', '1', '未发现详情标题')
    # 获取详情标题
    assert_equal(_obj_text, _click_obj_text, '成果概览详情正确显示')


def _innovation_result_list(poco):
    # 成果概览列表
    _obj = poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring(
        "android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/rl_index_result").child(
        "android.widget.TextView")[1]
    _obj.click()
    _result_list_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.sgcc.grsg.app:id/innovation_overview_result_bar").offspring("com.sgcc.grsg.app:id/tv_navigatio_title")
    # _result_list_obj.wait_for_appearance()
    _result_list_obj_text = _result_list_obj.get_text()
    assert_equal(_result_list_obj_text, '成果概览', '成果概览列表页显示验证')
    # pass


def _innovation_result_list_search(poco):
    # 成果概览列表搜索
    pass


if __name__ == '__main__':
    import config

    if not cli_setup():
        auto_setup(
            __file__,
            logdir=True,
            devices=[config.to_device["android"], ],
            # project_root="Z:/Downloads/AirTest_python_script"
        )
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    start_app("com.sgcc.grsg.app")
    time.sleep(10)
    print('_innovation_home_page >>')
    _innovation_home_page(poco)
    time.sleep(5)
    print('_innovation_result_detail_from_pic >>')
    _innovation_result_detail_from_pic(poco)