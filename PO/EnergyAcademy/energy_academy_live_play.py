# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class LivePlay(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/superplayer_iv_back'),
            "分享btn": self.poco('com.sgcc.grsg.app:id/superplayer_iv_share'),
            "刷新btn": self.poco('com.sgcc.grsg.app:id/superplayer_iv_refresh'),
            "原画质btn": self.poco('com.sgcc.grsg.app:id/superplayer_custom_quality'),
            "全屏btn": self.poco('com.sgcc.grsg.app:id/superplayer_iv_fullscreen'),
            "讲师头像image": self.poco('com.sgcc.grsg.app:id/speaker_photo'),
            "讲师姓名text": self.poco('com.sgcc.grsg.app:id/speaker_name'),
            "直播简介text": self.poco('com.sgcc.grsg.app:id/live_detail_indroduce_text'),
            "视频view": self.poco('com.sgcc.grsg.app:id/live_video_view')
        }
        self.top_obj = self.objs["视频view"]
        self.bottom_obj = self.objs["直播简介text"]

    def click_back(self):
        self.objs["回退btn"].click()
        sleep(3)
