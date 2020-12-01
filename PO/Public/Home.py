# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage,Utility


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.__page_name__ = '首页'
        self.objs = {
            "页面标题": self.poco("android.widget.LinearLayout")\
                .offspring("android:id/content")\
                .offspring("com.sgcc.grsg.app:id/tv_index_title"),
            "轮播图列表": self.poco('com.sgcc.grsg.app:id/xbanner')
                .offspring('android.widget.ImageView'),
            "首页tab": self.poco('com.sgcc.grsg.app:id/navigation_index'),
            "资讯tab": self.poco('com.sgcc.grsg.app:id/navigation_news'),
            "学院tab": self.poco('com.sgcc.grsg.app:id/navigation_school'),
            "我的tab": self.poco('com.sgcc.grsg.app:id/navigation_mycenter'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'),
            "个人信息btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'), # todo 待修改
            "消息通知btn": self.poco('com.sgcc.grsg.app:id/tv_index_login'), # todo 待修改
            "解决方案btn": self.poco('com.sgcc.grsg.app:id/tv_index_solution'),
            "供需服务btn": self.poco('com.sgcc.grsg.app:id/tv_index_service'),
            "培育创新btn": self.poco('com.sgcc.grsg.app:id/tv_index_innovate'),
            "服务云市场btn": self.poco('com.sgcc.grsg.app:id/tv_index_market'),
            "产业联盟btn": self.poco('com.sgcc.grsg.app:id/tv_index_coalition'),
            "方案详情列表": self.poco('com.sgcc.grsg.app:id/rv_index_solution')
                .offspring('android.widget.RelativeLayout'),
            "解决方案更多btn": self.poco('com.sgcc.grsg.app:id/tv_index_solution_more'),
            "热门资讯列表更多btn": self.poco('com.sgcc.grsg.app:id/rv_index_hotinfo')
                .offspring('android.widget.RelativeLayout'),
            "解决方案lbl": self.poco("com.sgcc.grsg.app:id/layout_index_solution_title"),
            "热门资讯lbl": self.poco("com.sgcc.grsg.app:id/rl_index_hotinfo"),
            "热门课程lbl": self.poco("com.sgcc.grsg.app:id/rl_index_hotcouse")

        }

    # 是否当前页面为首页
    def is_right(self):
        try:
            _home_page_title_obj= self.objs["页面标题"]
            _home_page_title_obj.wait_for_appearance(timeout=180)
            _home_page_title_obj_text = _home_page_title_obj.get_text()
            if _home_page_title_obj_text == '首页':
                return True
            else:
                return False
        except PocoNoSuchNodeException as ex:
            return False

    # 点击当前轮播图
    def click_current_carousel_figure_image(self):
        figures_list = self.objs["轮播图列表"]
        if len(figures_list) > 0:
            figures_list[0].click()

    # 点击首页tab
    def click_homepage_tab(self):
        self.objs["首页tab"].click()
        sleep(3)

    # 点击资讯tab
    def click_information_tab(self):
        self.objs["资讯tab"].click()
        sleep(3)

    # 点击学院tab
    def click_academy_tab(self):
        self.objs["学院tab"].click()
        sleep(3)

    # 点击我的tab
    def click_my_tab(self):
        self.objs["我的tab"].click()
        sleep(3)

    # 点击登录
    def click_login_button(self):
        self.objs["登录btn"].click()
        sleep(3)

    # 个人信息
    def click_personal_information_button(self):
        self.objs["个人信息btn"].click()
        sleep(3)

    # 点击消息通知
    def click_message_button(self):
        self.objs["消息通知btn"].click()
        sleep(3)

    # 点击解决方案
    def click_products_and_solutions_button(self):
        self.objs["解决方案btn"].click()
        sleep(3)

    # 点击供需服务
    def click_supply_and_demand_services_button(self):
        self.objs["供需服务btn"].click()
        sleep(3)

    # 点击培育创新
    def click_innovation_button(self):
        self.objs["培育创新btn"].click()
        sleep(3)

    # 点击服务云市场
    def click_service_cloud_market_button(self):
        self.objs["服务云市场btn"].click()
        sleep(3)

    # 点击产业联盟
    def click_industry_alliance_button(self):
        self.objs["产业联盟btn"].click()
        sleep(3)

    # 点击解决方案详情
    def click_solution_details_obj(self):
        solutions_list = self.objs["方案详情列表"]
        if len(solutions_list) > 0:
            solutions_list[0].click()
            sleep(7)

    # 点击解决方案列表更多
    def click_solutions_more_button(self):
        self.objs["解决方案更多btn"].click()
        sleep(3)

    # 点击热门资讯列表更多
    def click_informations_more_button(self):
        informations_list = self.objs["热门资讯列表更多btn"]
        if len(informations_list) > 0:
            informations_list[0].click()
            sleep(5)

    # 点击热门课程详情
    def click_lesson_details_obj(self):
        pass # todo 待开发

    # 点击热门课程列表更多
    def click_lessons_more_button(self):
        pass # todo 待开发

    # 刷新
    def refresh_page(self):
        pass # todo 待开发