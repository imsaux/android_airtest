# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class LecturerDetails(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('app')
                .child('android.view.View')[0]
                .offspring('android.view.View'),
            "回退btn": self.poco('app')
                .child('android.view.View')[0]
                .offspring('android.widget.Image'),
            "大咖姓名text": self.poco('app')
                .child('android.view.View')[1]
                .child('android.view.View')
                .offspring('android.view.View')[0],
            "大咖关注数text": self.poco('app')
                .child('android.view.View')[1]
                .child('android.view.View')
                .offspring('android.view.View')[2],
            "大咖主讲数text": self.poco('app')
                .child('android.view.View')[1]
                .child('android.view.View')
                .offspring('android.view.View')[4],
            "关注讲师btn": self.poco('app')
                .child('android.view.View')[3]
                .offspring('android.widget.Button'),
            "讲师介绍btn": self.poco('app')
                .child('android.view.View')[2]
                .offspring('android.widget.TabWidget')
                .offspring('android.view.View')[0],
            "主讲课程btn": self.poco('app')
                .child('android.view.View')[2]
                .offspring('android.widget.TabWidget')
                .offspring('android.view.View')[1]

        }
        self.top_obj = self.objs["大咖姓名text"]
        self.bottom_obj = self.objs["关注讲师btn"]

    def click_back(self):
        self.objs["回退btn"].click()
        sleep(3)
