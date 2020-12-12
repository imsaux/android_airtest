# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class Details(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('firstAnchor').child('android.view.View').offspring('android.view.View'),
            "资讯标题text": self.poco('app')
        }
    # 点击回退
    def click_back(self):
        pass

    # 点击底部点赞
    def click_bottom_thumbs_up_button(self):
        pass

    # 点击底部收藏
    def click_bottom_collection_button(self):
        pass

    # 点击底部分享
    def click_bottom_share_button(self):
        pass

    # 点击文章底部点赞
    def click_text_bottom_thumbs_up_button(self):
        pass

    # 点击文章底部点赞
    def click_text_bottom_collection_button(self):
        pass

    # 获取相关推荐列表
    def get_recommend_list(self):
        pass

    # 点击推荐资讯
    def click_recommand_obj(self):
        pass

