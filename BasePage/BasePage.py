# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from BasePage import Utility


class PageObject(object):
    def __init__(self):
        if not cli_setup():
            auto_setup(__file__)
            connect_device(Utility.setting["device"])
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.objs = {}

    # 定位
    def locate(self, obj, swipe_direction='up', swipe_times=1, swipe_duration=0.1):
        for i in range(swipe_times):
            obj.swipe(swipe_direction, duration=swipe_duration)
            sleep(1)
        x, y = self.poco.get_screen_size()
        print(x, y)
