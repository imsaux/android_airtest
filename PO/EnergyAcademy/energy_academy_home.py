# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_index_title'),
            "查询框textbox": self.poco('com.sgcc.grsg.app:id/et_consult_search'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'),
            "个人信息btn": self.poco('com.sgcc.grsg.app:id/civ_index_head'),
            "消息通知btn": self.poco('com.sgcc.grsg.app:id/iv_index_news'),
            "轮播图list": self.poco('com.sgcc.grsg.app:id/xbanner')
                .offspring('android.widget.ImageView'),
            "热门课程更多btn": self.poco('com.sgcc.grsg.app:id/tv_hot_course_more'),
            "热门课程列表list": self.poco('com.sgcc.grsg.app:id/rv_collect_hotCourse')
                .child('android.widget.RelativeLayout'),
            "热门课程标题列表list": self.poco('com.sgcc.grsg.app:id/tv_indexhot_mainTitle'),
            "直播更多btn": self.poco('com.sgcc.grsg.app:id/tv_live_course_more'),
            "系列课程更多btn": self.poco('com.sgcc.grsg.app:id/tv_series_course_more'),
            "系列课程列表list": self.poco('com.sgcc.grsg.app:id/rv_collect_seriesCourse')
                .offspring('android.widget.RelativeLayout'),
            "系列课程标题列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_albumName'),
            "大咖讲师更多btn": self.poco('com.sgcc.grsg.app:id/tv_lecturer_more'),
            "大咖讲师列表list": self.poco('com.sgcc.grsg.app:id/rv_collect_lecturer')
                .offspring('android.widget.RelativeLayout'),
            "大咖讲师姓名列表list": self.poco('com.sgcc.grsg.app:id/iv_collect_lecture_name')
        }
        self.top_obj = self.objs["轮播图list"]
        self.bottom_obj = self.objs["大咖讲师姓名列表list"]

    # 点击登录
    def click_login_button(self):
        self.objs["登录btn"].click()
        sleep(3)

    # 点击个人信息
    def click_personal_information_button(self):
        self.objs["个人信息btn"].click()
        sleep(3)

    # 点击消息通知
    def click_news_button(self):
        self.objs["消息通知btn"].click()
        sleep(3)

    # 点击当前轮播图
    def click_current_carousel_figure_image(self):
        figures_list = self.objs["轮播图list"]
        if len(figures_list) > 0:
            figures_list[0].click()

    def click_hot_course_more(self):
        self.objs["热门课程更多btn"].click()
        sleep(3)

    def click_hot_course_details(self):
        _course_list = self.objs["热门课程列表list"]
        if len(_course_list) > 0:
            _course_list[0].click()
            sleep(5)

    def click_live_more(self):
        self.objs["直播更多btn"].click()
        sleep(3)

    def click_series_more(self):
        self.objs["系列课程更多btn"].click()
        sleep(3)

    def click_series_details(self):
        _series_list = self.objs["系列课程列表list"]
        if len(_series_list) > 0:
            _series_list[0].click()
            sleep(5)

    def click_lecturer_more(self):
        self.objs["大咖讲师更多btn"].click()
        sleep(3)

    def click_lecturer_details(self):
        _lecturer_list = self.objs["大咖讲师列表list"]
        if len(_lecturer_list) > 0:
            _lecturer_list[0].click()
            sleep(5)

    def get_lecturer_name(self):
        _lecturer_names = self.objs["大咖讲师姓名列表list"]
        if len(_lecturer_names) > 0:
            return _lecturer_names[0].get_text()
        else:
            raise PocoException(message="大咖列表为空！")

    def get_series_title(self):
        _series_titles = self.objs["系列课程标题列表list"]
        if len(_series_titles) > 0:
            return _series_titles[0].get_text()
        else:
            raise PocoException(message="系列课程列表为空！")

    def get_hot_course_title(self):
        _hot_course_titles = self.objs["热门课程标题列表list"]
        if len(_hot_course_titles) > 0:
            return _hot_course_titles[0].get_text()
        else:
            raise PocoException(message="热门课程列表为空！")

    def banner_is_visibled(self):
        _obj = self.objs["轮播图list"]
        try:
            self.locate(_obj)
            return _obj.exists()
        except PocoNoSuchNodeException as ex:
            return False

    def live_is_visibled(self):
        # _obj = self.objs["轮播图list"]
        # try:
        #     self.locate(_obj)
        #     return _obj.exists()
        # except PocoNoSuchNodeException as ex:
        #     return False
        pass # todo 待开发

    def hot_course_is_visibled(self):
        _obj = self.objs["热门课程列表list"]
        try:
            self.locate(_obj)
            return _obj.exists()
        except PocoNoSuchNodeException as ex:
            return False

    def series_is_visibled(self):
        _obj = self.objs["系列课程列表list"]
        try:
            self.locate(_obj)
            return _obj.exists()
        except PocoNoSuchNodeException as ex:
            return False

    def lecturer_is_visibled(self):
        _obj = self.objs["大咖讲师列表list"]
        try:
            self.locate(_obj)
            return _obj.exists()
        except PocoNoSuchNodeException as ex:
            return False

