# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class LoginByUsername(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "用户名textbox": self.poco('com.sgcc.grsg.app:id/et_login2_account'),
            "密码textbox": self.poco('com.sgcc.grsg.app:id/et_login2_password'),
            "密码可见btn": self.poco('com.sgcc.grsg.app:id/cb_login2_eye'),
            "密码输入text": self.poco('com.sgcc.grsg.app:id/et_login2_password'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/bt_login2_submit'),
            "注册btn": self.poco('com.sgcc.grsg.app:id/tv_login2_register'),
            "忘记密码btn": self.poco('com.sgcc.grsg.app:id/tv_login2_forget'),
            "手机号登录btn": self.poco('com.sgcc.grsg.app:id/tv_phone_login'),
            "帐号登录btn": self.poco('com.sgcc.grsg.app:id/bt_login2_account'),
            "退出btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_right')
        }

    def input_username(self, username='18502268862'):
        _obj = self.objs["用户名textbox"]
        if _obj.exists():
            _obj.click()
            text(username)
        else:
            raise PocoNoSuchNodeException


    def input_phone(self, phone='18502268862'):
        _obj = self.objs["用户名textbox"]
        if _obj.exists():
            _obj.click()
            text(phone)
        else:
            raise PocoNoSuchNodeException

    def input_password(self, password='dr0wssaP'):
        _obj = self.objs["密码textbox"]
        if _obj.exists():
            _obj.click()
            text(password)
        else:
            raise PocoNoSuchNodeException

    def click_login(self):
        _obj = self.objs["登录btn"]
        if _obj.exists():
            _obj.click()
            sleep(10)

    def click_login_change_to_phone(self):
        _obj = self.objs["手机号登录btn"]
        if _obj.exists():
            _obj.click()
            sleep(1)

    def click_quit(self):
        _obj = self.objs["退出btn"]
        _obj.click()
        sleep(5)

    def get_current_mode(self):
        if self.objs["手机号登录btn"].exists():
            return self.objs["手机号登录btn"].get_text()
        if self.objs["帐号登录btn"].exists():
            return self.objs["帐号登录btn"].get_text()

    def click_login_change_to_username(self):
        _obj = self.objs["帐号登录btn"]
        if _obj.exists():
            _obj.click()
            sleep(1)

    def click_password_visible(self):
        pass

