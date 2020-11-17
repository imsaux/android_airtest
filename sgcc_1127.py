import unittest
import os
from pytestreport import TestRunner

case_path = os.getcwd()

def GetSuite():
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().discover(case_path, pattern="ST_*.py", top_level_dir=None))
    return suites


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=0)
    _suite = GetSuite()
    with open(__name__ + r'_report.html', 'wb') as fp:
        runner = TestRunner(fp, title='1127发版', description='冒烟测试验证', verbosity=1)
        runner.run(_suite)