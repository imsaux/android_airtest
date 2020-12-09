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
            "密码可视btn": self.poco('com.sgcc.grsg.app:id/cb_login2_eye'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/bt_login2_submit'),
            "登录方式转换btn": self.poco('com.sgcc.grsg.app:id/tv_phone_login'),
            "注册btn": self.poco('com.sgcc.grsg.app:id/tv_login2_register'),
            "忘记密码btn": self.poco('com.sgcc.grsg.app:id/tv_login2_forget')
        }

    def input_username(self, username='18502268862'):
        _obj = self.objs["用户名textbox"]
        if _obj.exists():
            _obj.click()
            text(username)
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


