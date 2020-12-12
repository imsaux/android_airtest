# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class LiveList(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/iv_common_title_text'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/iv_common_title_back'),
            "直播列表list": self.poco('com.sgcc.grsg.app:id/view_item_live'),
            "直播标题列表list": self.poco('com.sgcc.grsg.app:id/tv_item_live_title'),
            "直播讲师列表list": self.poco('com.sgcc.grsg.app:id/iv_item_live_bottom_left')
        }
        self.top_obj = self.objs["视频view"]
        self.bottom_obj = self.objs["直播简介text"]

    def click_back(self):
        self.objs["回退btn"].click()
        sleep(3)
