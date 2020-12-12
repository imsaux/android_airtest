# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class LecturerList(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_back'),
            "推荐btn": self.poco(text="推荐"),
            "最新btn": self.poco(text="最新"),
            "热门btn": self.poco(text="热门"),
            "标签页list": self.poco('com.sgcc.grsg.app:id/tl_bigshot_lecturer_title'),
            "分类筛选btn": self.poco('com.sgcc.grsg.app:id/tv_choose_all'),
            "分类列表list": self.poco('com.sgcc.grsg.app:id/tv_name'),
            "大咖列表list": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout'),
            "大咖名称列表list": self.poco('com.sgcc.grsg.app:id/tv_lecturer_name'),
            "大咖课程数量列表list": self.poco('com.sgcc.grsg.app:id/tv_lecturer_courseNum'),
            "大咖分类列表list": self.poco('com.sgcc.grsg.app:id/tv_lecturer_type'),
            "大咖照片列表list": self.poco('com.sgcc.grsg.app:id/iv_lecturer_picture')
        }
        self.top_obj = self.objs["标签页list"]
        self.bottom_obj = self.objs["大咖列表list"]