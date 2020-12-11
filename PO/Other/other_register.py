# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from BasePage import BasePage


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
        self.objs = {
            "返回btn": self.poco('com.sgcc.grsg.app:id/iv_topnvigationbar_back'),
            "标题text": self.poco('com.sgcc.grsg.app:id/tv_navigatio_title'),
            "用户名textbox": self.poco('com.sgcc.grsg.app:id/et_register_account'),
            "密码1textbox": self.poco('com.sgcc.grsg.app:id/et_register_password'),
            "密码2textbox": self.poco('com.sgcc.grsg.app:id/et_register_password_affire'),
            "手机号textbox": self.poco('com.sgcc.grsg.app:id/et_register_phone'),
            "验证码textbox": self.poco('com.sgcc.grsg.app:id/et_register_smscode'),
            "已读checkbox": self.poco('com.sgcc.grsg.app:id/cb_register_argee'),
            "注册协议btn": self.poco('com.sgcc.grsg.app:id/user_service_agreement'),
            "隐私协议btn": self.poco('com.sgcc.grsg.app:id/user_privacy_agreement'),
            "提交btn": self.poco('com.sgcc.grsg.app:id/bt_register_submit'),
            "登录页btn": self.poco('com.sgcc.grsg.app:id/tv_resister_login')
        }