import unittest
import os
from pytestreport import TestRunner
from BasePage import Utility


def get_suites():
    _suites = unittest.TestSuite()
    _suites.addTests(
        unittest.TestLoader().discover(
            os.getcwd(),
            pattern="FT_*.py",
            top_level_dir=None
            )
        )
    return _suites


if __name__ == '__main__':
    suites = get_suites()
    if suites.countTestCases() > 0:
        with open(Utility.setting['report_title'] + r'_report.html', 'wb') as fp:
            runner = TestRunner(
                fp,
                title=Utility.setting['report_title'],
                description=Utility.setting['report_description'],
                verbosity=2
            )
            runner.run(suites)