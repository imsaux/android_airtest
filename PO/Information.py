# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import *
import time


# 资讯首页
def information_home(poco):
    poco('com.sgcc.grsg.app:id/navigation_news').click()
    sleep(3)
    clicked_obj = poco('com.sgcc.grsg.app:id/tv_index_title')
    clicked_obj_text = clicked_obj.get_text()
    assert_equal(clicked_obj_text, '资讯', 'app首页跳转资讯首页异常')


# 资讯搜索
def information_search(poco, keyword='能源'):
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
    # todo 待开发
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


# 资讯详情
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
def information_contribute_edit(poco, title='投稿标题测试', content='投稿内容测试'):
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

