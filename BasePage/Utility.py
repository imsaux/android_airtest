from airtest.core.api import *
import json


with open("settings.json", 'r') as s:
    setting = json.load(s)

with open("devices.json", 'r') as d:
    devices = json.load(d)


def debug(fn):
    def _in(*args, **kwargs):
        start_app("com.sgcc.grsg.app")
        sleep(5)
        fn(*args, **kwargs)
        stop_app("com.sgcc.grsg.app")
    return _in


# 获取sms验证码
def get_sms():
    # todo 待开发
    v = 'adb shell dumpsys activity broadcasts | grep sender'


# 获取滑动操作所需的坐标
def get_pos(displayInfo, direction):
    x_max, y_max = \
        displayInfo['width'], \
        displayInfo['height']
    swipe_up_pos = (0.5 * x_max, 0.3 * y_max)
    swipe_down_pos = (0.5 * x_max, 0.7 * y_max)
    swipe_left_pos = (0.3 * x_max, 0.5 * y_max)
    swipe_right_pos = (0.7 * x_max, 0.5 * y_max)
    if direction == 'up':
        start_pos = swipe_up_pos
        end_pos = swipe_down_pos
    elif direction == 'down':
        start_pos = swipe_down_pos
        end_pos = swipe_up_pos
    elif direction == 'left':
        start_pos = swipe_left_pos
        end_pos = swipe_right_pos
    else:
        start_pos = swipe_right_pos
        end_pos = swipe_left_pos
    return start_pos, end_pos