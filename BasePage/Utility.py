from airtest.core.api import *
import json


with open("settings.json", 'r') as f:
    setting = json.load(f)


def debug(fn):
    def _in(*args, **kwargs):
        start_app("com.sgcc.grsg.app")
        sleep(5)
        fn(*args, **kwargs)
        stop_app("com.sgcc.grsg.app")
    return _in

