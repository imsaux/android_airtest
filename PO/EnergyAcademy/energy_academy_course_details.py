# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class CourseDetails(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "课程标题text": self.poco('com.sgcc.grsg.app:id/tv_course_details_mainTitle'),
            "回退btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_back'),
            "收藏btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_right'),
            "图片image": self.poco('com.sgcc.grsg.app:id/iv_course_details_cover'),
            "讲师姓名text": self.poco('com.sgcc.grsg.app:id/tv_course_details_lectureName'),
            "观看量text": self.poco('com.sgcc.grsg.app:id/tv_course_details_browseNum'),
            "总课时text": self.poco('com.sgcc.grsg.app:id/tv_course_details_collectNum'),
            "学习进度text": self.poco('com.sgcc.grsg.app:id/tv_course_details_totalProcess'),
            "课程介绍btn": self.poco(text='课程介绍'),
            "课程目录btn": self.poco(text='课程目录'),
            "开始学习btn": self.poco('com.sgcc.grsg.app:id/btn_haveBuy')
        }
        self.top_obj = self.objs["图片image"]
        self.bottom_obj = self.objs["开始学习btn"]

    def get_course_title(self):
        return self.objs["课程标题text"].get_text()
