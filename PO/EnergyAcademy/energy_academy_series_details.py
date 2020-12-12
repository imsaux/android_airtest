# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class SeriesList(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_back'),
            "系列课程列表list": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout'),
            "系列名称列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_albumName'),
            "系列课程数量列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_courseCount'),
            "系列课程观看量列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_browseNum')
        }
        self.top_obj = self.objs["标签页list"]
        self.bottom_obj = self.objs["系列课程列表list"]

    def click_back(self):
        self.objs["回退btn"].click()
        sleep(3)

    def get_series_count(self):
        return self.get_obj_count(self.objs["系列课程列表list"])

    def get_series_title(self, index=1):
        _series_titles = self.objs["课程标题列表list"]
        if self.get_series_count() > 0:
            return self.get_obj_by_index(_series_titles, index).get_text()
        else:
            raise PocoException(message="课程标题列表无数据")

    def click_series_details(self, index=1):
        _series_list = self.objs["课程列表list"]
        if self.get_series_count() > 0:
            self.get_obj_by_index(_series_list, index).click()
            sleep(5)
        else:
            raise PocoException(message="课程列表无数据")

    def get_recommand_tab_state(self):
        return self.objs["推荐tab"].attr('clickable')

    def get_latest_tab_state(self):
        return self.objs["最新tab"].attr('clickable')

    def get_hot_tab_state(self):
        return self.objs["热门tab"].attr('clickable')

    def click_recommand_tab(self):
        self.objs["推荐tab"].click()
        sleep(1)

    def click_latest_tab(self):
        self.objs["最新tab"].click()
        sleep(1)

    def click_hot_tab(self):
        self.objs["热门tab"].click()
        sleep(1)
