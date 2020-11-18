# -*- encoding=utf8 -*-
__author__ = "suny"


import unittest
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import BusinessLogic
import Config

if not cli_setup():
    auto_setup(
        __file__,
        logdir=False,
        devices=[Config.to_device["android"], ],
    )


class ST_Information(unittest.TestCase):
    def setUp(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        start_app("com.sgcc.grsg.app")
        sleep(5)

    def tearDown(self):
        stop_app("com.sgcc.grsg.app")

