# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.exceptions import *
from Base import BasePage


class Home(BasePage.PageObject):
    def __init__(self):
        super().__init__()
