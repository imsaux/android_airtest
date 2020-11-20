from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import *
import time


def app_home(poco):
    # app首页
    _home_page_title_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.sgcc.grsg.app:id/tv_index_title")
    _home_page_title_obj.wait_for_appearance()
    _home_page_title_obj_text = _home_page_title_obj.get_text()
    assert_equal(_home_page_title_obj_text, '首页', '首页显示正常')


def innovation_home(poco):
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
def innovation_result_detail_from_pic(poco):
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


def innovation_result_list(poco):
    # 成果概览列表
    poco(text="更多").click()
    time.sleep(3)
    _result_list_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.sgcc.grsg.app:id/innovation_overview_result_bar").offspring("com.sgcc.grsg.app:id/tv_navigatio_title")
    # _result_list_obj.wait_for_appearance()
    _result_list_obj_text = _result_list_obj.get_text()
    assert_equal(_result_list_obj_text, '成果概览', '成果概览列表页显示验证')


# 成果概览列表搜索
def innovation_result_list_search(poco):
    poco("com.sgcc.grsg.app:id/iv_topnvigationbar_right").click()
    obj = poco("com.sgcc.grsg.app:id/et_search")
    obj.click()
    text('能源')
    poco("com.sgcc.grsg.app:id/search_ok").click()

    result_list = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/search_ry").child("android.widget.LinearLayout")
    if len(result_list) > 0:
        for obj in result_list:
            _title_obj = obj.child("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/item_title")
            assert_equal('能源' in _title_obj.get_text(), True, '成果列表查询结果不准确')
    else:
        assert_equal(True, False, '成果列表查询无结果')


# 查看成果详情
def innovation_result_details(poco):
    result_list = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_list").child("android.widget.LinearLayout")
    if len(result_list) > 0:
        _result_obj = result_list[0].child("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/item_title")
        _result_obj_text = _result_obj.get_text()
        _result_obj.click()
        time.sleep(5)
        _clicked_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[2]
        assert_equal(_result_obj_text, _clicked_obj.get_text(), '成果列表查询结果不准确')
    else:
        assert_equal(True, False, '成果列表查询无结果')


# 研究单位详情
def innovation_corporation_description(poco):
    poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[4].child("android.view.View")[1].click()
    sleep(3)
    _title_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[7].child("android.view.View")[0].child("android.view.View")[0]
    assert_equal(_title_obj.get_text(), '研究单位', '研究单位介绍页面异常')


# 大咖
def innovation_magnate_list(poco):
    pass


# 创新动态详情
def innovation_developments_details(poco):
    poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/innovation_results").child("android.widget.LinearLayout").swipe([-0.0882, -0.3852])
    developments_list = poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/innovation_doing").child("android.widget.RelativeLayout")
    if len(developments_list) > 0:
        title_obj = developments_list[0].child("com.sgcc.grsg.app:id/title")
        developments_title = title_obj.get_text()
        title_obj.click()
        sleep(3)
        clicked_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0]
        assert_equal(developments_title, clicked_obj.get_text(), '创新首页跳转动态详情错误')
        poco("android.widget.Image").click()
        sleep(3)

        img_obj = developments_list[0].child("com.sgcc.grsg.app:id/image")
        img_obj.click()
        sleep(3)
        clicked_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0]
        assert_equal(developments_title, clicked_obj.get_text(), '创新首页跳转动态详情错误')
        poco("android.widget.Image").click()
        sleep(3)

        subtitle_obj = developments_list[0].child("com.sgcc.grsg.app:id/subtitle")
        subtitle_obj.click()
        sleep(3)
        clicked_obj = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0]
        assert_equal(developments_title, clicked_obj.get_text(), '创新首页跳转动态详情错误')
        poco("android.widget.Image").click()
    else:
        assert_equal(True, False, '无创新动态')


# 共同体首页
def innovation_community_home(poco):
    poco(text="培育动态").swipe([-0.0588, -0.7776])
    sleep(2)
    poco(text="创新共同体").swipe([0.0, -0.6027])
    sleep(2)
    community_list = poco("android.widget.LinearLayout").offspring("com.sgcc.grsg.app:id/root_view").offspring("android.widget.ScrollView").offspring("com.sgcc.grsg.app:id/innovation_gongtongti").child("android.widget.LinearLayout")
    if len(community_list) > 0:
        community_des = community_list[0].child("com.sgcc.grsg.app:id/subtitle")
        community_des_text = community_des.get_text()

        img_click_obj = community_list[0].child("com.sgcc.grsg.app:id/image")
        img_click_obj.click()
        sleep(3)
        clicked_community_des = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").offspring("com.sgcc.grsg.app:id/tv_community_laboratory_desc")[0]
        clicked_community_des_text = clicked_community_des.get_text()
        assert_equal(community_des_text, clicked_community_des_text, '共同体首页跳转共同体详情错误')
        poco("com.sgcc.grsg.app:id/iv_topnvigationbar_back").click()

        title_click_obj = community_list[0].child("com.sgcc.grsg.app:id/title")
        title_click_obj.click()
        sleep(3)
        clicked_community_des = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").offspring("com.sgcc.grsg.app:id/tv_community_laboratory_desc")[0]
        clicked_community_des_text = clicked_community_des.get_text()
        assert_equal(community_des_text, clicked_community_des_text, '共同体首页跳转共同体详情错误')
        poco("com.sgcc.grsg.app:id/iv_topnvigationbar_back").click()

        subtitle_click_obj = community_list[0].child("com.sgcc.grsg.app:id/subtitle")
        subtitle_click_obj.click()
        sleep(3)
        clicked_community_des = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").offspring("com.sgcc.grsg.app:id/tv_community_laboratory_desc")[0]
        clicked_community_des_text = clicked_community_des.get_text()
        assert_equal(community_des_text, clicked_community_des_text, '共同体首页跳转共同体详情错误')
    else:
        assert_equal(True, False, '无共同体记录')


# 实验室介绍
def innovation_community_home_more(poco):
    community_des = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").offspring("com.sgcc.grsg.app:id/tv_community_laboratory_desc")[0]
    community_des_text = community_des.get_text()
    poco(text="查看详细介绍").click()
    sleep(5)
    clicked_community_des = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[2]
    assert_equal(community_des_text, clicked_community_des.get_text(), '共同体首页跳转实验室介绍错误')


# 专家列表
def innovation_experts_list(poco):
    try:
        poco(text="更多").click()
        sleep(3)
    except PocoNoSuchNodeException as ex:
        assert_equal(True, False, '专家元素未找到')
    title_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("android.widget.TextView")
    assert_equal(title_obj.get_text(), '专家列表', '共同体首页跳转专家列表错误')
    experts_list_obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_expert_list")
    if len(experts_list_obj) == 0:
        assert_equal(False, True, '专家列表为空')


# 专家详情1 共同体首页
def innovation_experts_details_from_homepage(poco):
    # sleep(5)
    obj = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").child("android.widget.RelativeLayout")
    if len(obj) > 0:
        expert_name_text = obj[2].child("com.sgcc.grsg.app:id/tv_item_community_expert_name").get_text()

        obj[2].child("com.sgcc.grsg.app:id/iv_item_community_expert").click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        obj[2].child("com.sgcc.grsg.app:id/tv_item_community_expert_name").click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_community_home_list").offspring("com.sgcc.grsg.app:id/tv_item_community_expert_desc")[0].click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
    else:
        assert_equal(False, True, '无专家记录')


# 专家详情1 专家列表
def innovation_experts_details_from_experts_list(poco):
    experts_list = poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sgcc.grsg.app:id/recycler_expert_list").child("android.widget.RelativeLayout")
    if len(experts_list) > 0:
        expert_name = experts_list[0].child("com.sgcc.grsg.app:id/name")
        expert_name_text = expert_name.get_text()
        expert_name.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/image")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/company")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/office")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/field")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)

        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/num")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
        sleep(3)


        expert_img = experts_list[0].child("com.sgcc.grsg.app:id/time")
        expert_img.click()
        sleep(5)
        clicked_expert_name_text = poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[1].get_text()
        assert_equal(expert_name_text, clicked_expert_name_text, '共同体首页跳转专家详情错误')
        poco("android.widget.LinearLayout").offspring("android.webkit.WebView").offspring("app").child("android.view.View")[0].child("android.widget.Image").click()
    else:
        assert_equal(False, True, '专家列表记录为空')

# 资讯首页
def information_home(poco):
    poco('com.sgcc.grsg.app:id/navigation_news').click()
    sleep(3)
    clicked_obj = poco('com.sgcc.grsg.app:id/tv_index_title')
    clicked_obj_text = clicked_obj.get_text()
    assert_equal(clicked_obj_text, '资讯', 'app首页跳转资讯首页异常')


# 资讯搜索
def information_search(poco, keyword='能源', auto_back=False):
    if keyword is not str:
        keyword = '能源'
    search_obj = poco('com.sgcc.grsg.app:id/et_consult_search')
    search_obj.click() # 进入关键字输入页面
    sleep(3)
    consult_search_obj = poco('com.sgcc.grsg.app:id/et_consult_search')
    consult_search_obj.click() # 获得输入焦点
    text(keyword) # 输入关键字
    poco('com.sgcc.grsg.app:id/search_ok').click()
    sleep(3)

    search_result_list_obj = poco('com.sgcc.grsg.app:id/public_search_ry') # 获得查询结果页面元素
    if len(search_result_list_obj) > 0:
        search_result_obj_text = search_result_list_obj[0].child('android.widget.LinearLayout').child('android.widget.LinearLayout')[0].child('com.sgcc.grsg.app:id/item_public_search_title').get_text()
        if keyword in search_result_obj_text:
            assert_equal(True, True, '资讯列表查询功能验证通过')
        else:
            assert_equal(False, True, '资讯列表查询结果错误')
    else:
        assert_equal(False, True, '资讯查询无结果')
    
# 资讯首页tab切换
def information_tab_change(poco):
    total_list = list()
    mod_list = [
        '推荐',
        '新闻资讯',
        '政策法规',
        '技术标准',
        '官方通告',
        '科技前沿',
        '经验交流'
    ]
    for mod in mod_list:
        tab_obj = poco(name=mod)
        tab_obj.click()
        sleep(3)
        current_contents = _information_get_current_contents(poco)
        if total_list.count(current_contents) == 0:
            total_list.append(current_contents)
        else:
            assert_equal(False, True, mod_list[len(total_list)+1] + '与其他tab页存在相同内容')


# 获取资讯列表内容列表
def _information_get_current_contents(poco):
    items = poco('com.sgcc.grsg.app:id/tv_info_title')
    tmp = []
    for item in items:
        tmp.append(item.get_text())
    return tmp

# 资讯列表排序
def information_list_sort(poco):
    pass


# 资讯列表日期排序验证
def _information_sort_datetime(items):
    import datetime
    tmp = datetime.datetime.min
    if len(items) > 1:
        for item in items:
            _current = datetime.datetime.strptime(item.get_text(), "%Y-%m-%d")
            if _current > tmp:
                return (False, items.index(item))
            tmp = _current
        return (True, 0)
    else:
        return (False, 0)


def information_details(poco):
    information_list = poco('com.sgcc.grsg.app:id/recycler_base_page_list').child('android.widget.RelativeLayout')
    if len(information_list) > 0:
        before_obj = poco('com.sgcc.grsg.app:id/tv_info_title')
        before_obj_text = before_obj.get_text()
        information_list[0].click()
        sleep(7)
        after_obj = poco('app')
        assert_equal(
            after_obj.child('android.view.View')[0].get_text(),
            before_obj_text,
            '资讯首页跳转详情异常'
        )
    else:
        assert_equal(False, True, '资讯列表无记录')


# 投稿入口
def information_contribute_home(poco):
    poco('com.sgcc.grsg.app:id/tv_index_contribution').click()
    sleep(2)
    try:
        poco('com.sgcc.grsg.app:id/cb_isAgree').click()
        poco('com.sgcc.grsg.app:id/button_confirm').click()
        sleep(3)
    except PocoNoSuchNodeException as ex:
        pass
    try:
        after_obj = poco('com.sgcc.grsg.app:id/tv_navigatio_title')
        assert_equal(after_obj.get_text(), '投稿', '资讯首页未正确跳转投稿页面')
    except PocoNoSuchNodeException as ex:
        assert_equal(False, True, '资讯首页未正确跳转投稿页面')


# 投稿编辑
def information_contribute_edit(poco, title, content):
    contribute_title_obj = poco('com.sgcc.grsg.app:id/et_contribute_title')
    contribute_title_obj.click()
    if title is not str:
        title = repr(title)
    text(title)
    contribute_content_obj = poco('com.sgcc.grsg.app:id/et_contribute_content')
    contribute_content_obj.click()
    if content is not str:
        content = repr(content)
    text(content)

# 资讯，投稿，保存草稿
def information_contribute_draft_save(poco):
    poco('com.sgcc.grsg.app:id/tv_navigation_left').click()
    sleep(2)
    poco('com.sgcc.grsg.app:id/button1').click()
    after_title_obj = poco('com.sgcc.grsg.app:id/title')
    assert_equal(after_title_obj.get_text(), '保存成功', '投稿草稿未成功保存')


# 资讯，投稿，不保存草稿
def information_contribute_draft_dontsave(poco):
    poco('com.sgcc.grsg.app:id/tv_navigation_left').click()
    sleep(2)
    poco('com.sgcc.grsg.app:id/button2').click()
    after_title_obj = poco('com.sgcc.grsg.app:id/tv_index_contribution')
    assert_equal(after_title_obj.get_text(), '投稿', '投稿不保存草稿跳转失败')


# 投稿发布
def information_contribute_commit(poco):
    poco('com.sgcc.grsg.app:id/tv_navigation_right').click()
    sleep(2)
    after_obj = poco('com.sgcc.grsg.app:id/title')
    assert_equal(after_obj.get_text(), '发布成功', '投稿发布失败')
    poco('com.sgcc.grsg.app:id/button1').click()


# 查看投稿列表（我的-信息通知）
def information_contribute_list(poco):
    poco(name='投稿').click()
    sleep(2)
    contribute_list_obj = poco('com.sgcc.grsg.app:id/tv_publish_solution_add_view_title')
    if len(contribute_list_obj) == 0:
        assert_equal(False, True, '投稿列表为空')

# 查看投稿详情
def information_contribute_details(poco):
    pass

# 登录
# 18502268862
# a1s2d3F4
def app_login(poco):
    # todo 找可用版本更新
    pass


if __name__ == '__main__':
    import Config

    if not cli_setup():
        auto_setup(
            __file__,
            logdir=False,
            devices=[Config.to_device["android"], ],
        )
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # start_app("com.sgcc.grsg.app")
    # time.sleep(10)

    ## 测试代码写在下面 ##
    title = '测试一下吧'
    content = '测试一下吧'
    information_contribute_edit(poco, title, content)




    ## 退出
    # poco.stop_running()
    # stop_app("com.sgcc.grsg.app")
