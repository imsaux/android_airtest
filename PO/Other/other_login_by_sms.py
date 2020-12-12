# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class LoginBySMS(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "手机号textbox": self.poco('com.sgcc.grsg.app:id/et_login2_phone'),
            "密码textbox": self.poco('com.sgcc.grsg.app:id/et_login2_password'),
            "获取验证码btn": self.poco('com.sgcc.grsg.app:id/tv_login2_smscode'),
            "登录btn": self.poco('com.sgcc.grsg.app:id/bt_login2_submit'),
            "登录方式转换btn": self.poco('com.sgcc.grsg.app:id/tv_phone_login'),
            "注册btn": self.poco('com.sgcc.grsg.app:id/tv_login2_register'),
            "忘记密码btn": self.poco('com.sgcc.grsg.app:id/tv_login2_forget')
        }

    def input_phone_number(self, phone_number='18502268862'):
        _obj = self.objs["手机号textbox"]
        if _obj.exists():
            _obj.click()
            text(phone_number)
        else:
            raise PocoNoSuchNodeException

    def click_get_sms(self):
        _obj = self.objs["获取验证码btn"]
        if _obj.exists():
            _obj.click()

    def get_sms_code(self):
        self._find_smscode()

    def _find_smscode(self):
        start_app('com.android.mms')
        sleep(1)
        sms_list = self.poco('com.android.mms:id/subject')
        for sms in sms_list:
            if "【绿色国网】" in sms.get_text():
                pass # todo 待开发
        stop_app('com.android.mms')
