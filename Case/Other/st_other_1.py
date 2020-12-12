# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_login_by_username, other_home
from Base import Utility


class RedirectLogin(unittest.TestCase):
    def setUp(self):
        self.p_login_by_username = other_login_by_username.LoginByUsername()
        self.p_home = home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_jump_login(self):
        self.p_home.click_login_button()
        assert_equal(self.p_login_by_username.get_current_title(), "登录", "登录页面跳转异常！")