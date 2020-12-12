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
            "推荐btn": self.poco(text="推荐"),
            "最新btn": self.poco(text="最新"),
            "热门btn": self.poco(text="热门"),
            "标签页list": self.poco('com.sgcc.grsg.app:id/tl_series_course_title'),
            "系列课程列表list": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout'),
            "系列名称列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_albumName'),
            "系列课程数量列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_courseCount'),
            "系列课程观看量列表list": self.poco('com.sgcc.grsg.app:id/tv_collect_series_browseNum')
        }
        self.top_obj = self.objs["标签页list"]
        self.bottom_obj = self.objs["系列课程列表list"]