# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_home
from PO.EnergyAcademy import energy_academy_home


class CheckUI(unittest.TestCase):
    def setUp(self):
        self.p_energy_academy_home = energy_academy_home.Home()
        self.p_other_home = other_home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_check_banner(self):
        self.p_other_home.click_academy_tab()
        assert_equal(
            self.p_energy_academy_home.banner_is_visibled(),
            True,
            "轮播图显示异常！"
        )

    def test_check_hot_course(self):
        self.p_other_home.click_academy_tab()
        assert_equal(
            self.p_energy_academy_home.hot_course_is_visibled(),
            True,
            "热门课程显示异常！"
        )

    def test_check_series(self):
        self.p_other_home.click_academy_tab()
        assert_equal(
            self.p_energy_academy_home.series_is_visibled(),
            True,
            "系列课程显示异常！"
        )

    def test_check_lecturer(self):
        self.p_other_home.click_academy_tab()
        assert_equal(
            self.p_energy_academy_home.lecturer_is_visibled(),
            True,
            "大咖讲师显示异常！"
        )
