# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class CourseDetails(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_back'),
            "标签页列表list": self.poco('com.sgcc.grsg.app:id/tl_good_course_title')
                .offspring('android.widget.LinearLayout'),
            "课程列表list": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout'),
            "课程标题列表list": self.poco('com.sgcc.grsg.app:id/tv_indexhot_mainTitle'),
            "课程观看量列表list": self.poco('com.sgcc.grsg.app:id/tv_indexhot_browseNum'),
        }
        self.top_obj = self.objs["标签页列表list"]
        self.bottom_obj = self.objs["课程列表list"]
