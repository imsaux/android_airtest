import unittest
from pytestreport import TestRunner
from BasePage import Utility


if __name__ == '__main__':
    case_dir = Utility.setting['discover_path']
    _pattern = Utility.setting['discover_pattern']
    _discover = unittest.defaultTestLoader.discover(case_dir, _pattern)
    suites = unittest.TestSuite()
    suites.addTests(_discover)
    if suites.countTestCases() > 0:
        with open(Utility.setting['report_title'] + r'_report.html', 'wb') as fp:
            runner = TestRunner(
                fp,
                title=Utility.setting['report_title'],
                description=Utility.setting['report_description'],
                verbosity=1
            )
            runner.run(suites)