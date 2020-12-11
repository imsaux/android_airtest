# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_home
from PO.EnergyAcademy import energy_academy_home, energy_academy_course_details


class JumpCourseDetails(unittest.TestCase):
    def setUp(self):
        self.p_energy_academy_home = energy_academy_home.Home()
        self.p_energy_academy_details = energy_academy_course_details.CourseDetails()
        self.p_other_home = other_home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_jump_hot_course_details(self):
        self.p_other_home.click_academy_tab()
        assert_equal(self.p_energy_academy_home.get_current_title(), "学院", "首页跳转学院首页异常！")
        after_course_title = self.p_energy_academy_home.get_hot_course_title()
        self.p_energy_academy_home.click_hot_course_details()
        assert_equal(self.p_energy_academy_details.get_course_title(), after_course_title, "跳转课程详情不一致！")