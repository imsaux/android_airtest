# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class ContributeDetails(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.__page_name__ = '投稿'

    # 点击取消
    def click_cancel_button(self):
        pass

    # 点击发布
    def click_release_button(self):
        pass