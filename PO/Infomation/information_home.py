# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_index_title'),
            "查询框tb": self.poco('com.sgcc.grsg.app:id/et_consult_search'),
            "投稿btn": self.poco('com.sgcc.grsg.app:id/tv_index_contribution'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'),
            "个人信息btn": self.poco('com.sgcc.grsg.app:id/civ_index_head'),
            "资讯分类lbl": self.poco('com.sgcc.grsg.app:id/tl_consult_title'),
            "资讯list": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout'),
            "资讯标题list": self.poco('com.sgcc.grsg.app:id/tv_info_title'),
            "推荐tab": self.poco('推荐'),
            "新闻资讯tab": self.poco('新闻资讯'),
            "政策法规tab": self.poco('政策法规'),
            "技术标准tab": self.poco('技术标准'),
            "官方通告tab": self.poco('官方通告'),
            "科技前沿tab": self.poco('科技前沿'),
            "经验交流tab": self.poco('经验交流')
        }
        self.top_obj = self.objs["资讯分类lbl"]
        self.bottom_obj = self.objs["资讯list"]

    # 点击登录
    def click_login_button(self):
        self.objs["登录btn"].click()
        sleep(3)

    # 点击个人信息
    def click_personal_information_button(self):
        self.objs["个人信息btn"].click()
        sleep(3)

    # 点击投稿
    def click_contribute_button(self):
        self.objs["投稿btn"].click()
        sleep(3)

    # 点击推荐标签tab
    def click_recommend_tab(self):
        self.objs["推荐tab"].click()
        sleep(3)

    # 点击新闻资讯tab
    def click_news_tab(self):
        self.objs["新闻资讯tab"].click()
        sleep(3)

    # 点击政策法规tab
    def click_law_tab(self):
        self.objs["政策法规tab"].click()
        sleep(3)

    # 点击技术标准tab
    def click_standards_tab(self):
        self.objs["技术标准tab"].click()
        sleep(3)

    # 点击官方通告tab
    def click_official_tab(self):
        self.objs["官方通告tab"].click()
        sleep(3)

    # 点击科技前沿tab
    def click_science_and_technology_tab(self):
        self.objs["科技前沿tab"].click()
        sleep(3)

    # 点击经验交流tab
    def click_experience_tab(self):
        self.objs["经验交流tab"].click()
        sleep(3)

    # 加载新的资讯
    def load_new_information(self, times=1):
        self.locate(self.bottom_obj)
        for i in range(times):
            self.swipe_down()
            sleep(2)

    def get_information_title(self, index=1):
        _information_titles = self.objs["资讯标题list"]
        if self.get_information_count() > 0:
            return self.get_obj_by_index(_information_titles, index).get_text()
        else:
            raise PocoException(message="资讯标题列表无数据")

    def get_information_count(self):
        return self.get_obj_count(self.objs["资讯list"])

    # 点击查看资讯详情
    def click_information_details(self, index=1):
        _information_list = self.objs["资讯list"]
        if self.get_information_count() > 0:
            self.get_obj_by_index(_information_list, index).click()
            sleep(5)
        else:
            raise PocoException(message="资讯列表无数据")