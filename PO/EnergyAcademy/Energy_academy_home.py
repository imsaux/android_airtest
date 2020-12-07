# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题": self.poco('com.sgcc.grsg.app:id/tv_index_title'),
            "查询框": self.poco('com.sgcc.grsg.app:id/et_consult_search'),
            "投稿btn": self.poco('com.sgcc.grsg.app:id/tv_index_contribution'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'),
            "个人信息btn": self.poco('com.sgcc.grsg.app:id/civ_index_head'),
            "消息通知btn": self.poco('com.sgcc.grsg.app:id/iv_index_news'),
            "资讯分类": self.poco('com.sgcc.grsg.app:id/tl_consult_title'),
            "资讯列表": self.poco('com.sgcc.grsg.app:id/recycler_base_page_list')
                .offspring('android.widget.RelativeLayout')
        }

    # 是否当前页面为首页
    def is_right(self):
        pass

    # 点击登录
    def click_login_button(self):
        pass

    # 点击个人信息
    def click_personal_information_button(self):
        pass

    # 点击投稿
    def click_contribute_button(self):
        pass

    # 获取当前页面资讯列表
    def get_current_informations_list(self):
        pass

    # 点击推荐标签tab
    def click_recommend_tab(self):
        pass

    # 点击新闻资讯tab
    def click_news_tab(self):
        pass

    # 点击政策法规tab
    def click_law_tab(self):
        pass

    # 点击技术标准tab
    def click_standards_tab(self):
        pass

    # 点击官方通告tab
    def click_official_tab(self):
        pass

    # 点击科技前沿tab
    def click_science_and_technology_tab(self):
        pass

    # 点击经验交流tab
    def click_experience_tab(self):
        pass

    # 下拉加载新的资讯
    def swipe_down_to_load(self):
        pass

    # 点击查看资讯详情
    def click_to_details(self):
        pass