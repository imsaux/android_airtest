# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from BasePage import Utility


class PageObject(object):
    def __init__(self):
        if not cli_setup():
            auto_setup(__file__)
            self.device = connect_device(Utility.devices["huaweip8"])
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.objs = {}
        self.top_obj = None
        self.bottom_obj = None
        self.is_top = False
        self.is_bottom = False
        self.current_directon = ""

    def _get_coordinate(self):
        if self.top_obj.exists():
            self.is_top = True
        else:
            self.is_top = False

        if self.bottom_obj.exists():
            self.is_bottom = True
        else:
            self.is_bottom = False

        if self.current_directon == "":
            start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "down")
            self.current_directon = "down"

        if not self.is_bottom and self.current_directon == "down":
            start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "down")
        if not self.is_top and self.current_directon == "up":
            start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "up")

        if self.is_top and self.current_directon == "up":
            start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "down")
            self.current_directon = "down"
        if self.is_bottom and self.current_directon == "down":
            start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "up")
            self.current_directon = "up"
        return start_pos, end_pos

    def swipe_down(self):
        start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "down")
        swipe(start_pos, end_pos)

    def swipe_up(self):
        start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "up")
        swipe(start_pos, end_pos)

    # 定位元素
    def locate(self, obj, timeout=180.0):
        _start = time.time()
        while True:
            if obj.exists():
                break
            start_pos, end_pos = self._get_coordinate()
            if self.is_top and self.is_bottom and not obj.exists():
                raise PocoNoSuchNodeException
            swipe(start_pos, end_pos)
            _end = time.time()
            if _end - _start > timeout:
                print(_end - _start)
                raise PocoNoSuchNodeException

    # 刷新
    def refresh(self):
        self.locate(self.top_obj)
        start_pos, end_pos = Utility.get_pos(self.device.get_display_info(), "up")
        swipe(start_pos, end_pos)

    def __del__(self):
        self.poco.stop_running()
