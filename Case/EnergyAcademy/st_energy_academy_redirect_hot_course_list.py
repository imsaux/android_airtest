# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_home
from PO.EnergyAcademy import energy_academy_home, energy_academy_hot_course_list


class RedirectHotCourseList(unittest.TestCase):
    def setUp(self):
        self.p_energy_academy_hot_course_list = energy_academy_hot_course_list.HotCourseDetails()
        self.p_energy_academy_home = energy_academy_home.Home()
        self.p_other_home = other_home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_redirect_hot_course_list(self):
        self.p_other_home.click_academy_tab()
        assert_equal(self.p_energy_academy_home.get_current_title(), '学院', '首页跳转学院异常！')
        self.p_energy_academy_home.click_hot_course_more()
        assert_equal(self.p_energy_academy_hot_course_list.get_current_title(), "精品课程", "学院首页跳转精品课程列表异常！")