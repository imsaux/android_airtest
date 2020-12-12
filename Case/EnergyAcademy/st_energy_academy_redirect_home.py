# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_home
from PO.EnergyAcademy import energy_academy_home


class RedirectHome(unittest.TestCase):
    def setUp(self):
        self.p_energy_academy_home = energy_academy_home.Home()
        self.p_other_home = other_home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_access_energy_academy_home(self):
        self.p_other_home.click_academy_tab()
        assert_equal(self.p_energy_academy_home.get_current_title(), "学院", "首页跳转学院首页异常！")