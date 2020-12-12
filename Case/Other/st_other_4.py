# -*- encoding=utf8 -*-
import unittest
from airtest.core.api import *
from PO.Other import other_login_by_username, other_home
from Base import Utility


class ChangeLoginMode(unittest.TestCase):
    def setUp(self):
        self.p_login_by_username = other_login_by_username.LoginByUsername()
        self.p_home = home.Home()
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

    def test_change_login_mode(self):
        self.p_home.click_login_button()
        assert_equal(self.p_login_by_username.get_current_title(), "登录", "登录页面跳转异常！")
        self.p_login_by_username.click_login_change_to_phone()
        assert_equal(self.p_login_by_username.get_current_mode(), "手机号快捷登录", "登录模式切换异常！")
        self.p_login_by_username.click_login_change_to_username()
        assert_equal(self.p_login_by_username.get_current_mode(), "帐号登录", "登录模式切换异常！")