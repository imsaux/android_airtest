import unittest
import os
from pytestreport import TestRunner

case_path = os.getcwd()


def GetSuites():
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().discover(case_path, pattern="ST_*.py", top_level_dir=None))
    return suites


if __name__ == '__main__':
    suites = GetSuites()
    report_title = '1127发版'
    report_description = ''
    with open(report_title + r'_report.html', 'wb') as fp:
        runner = TestRunner(fp, title=report_title, description=report_description, verbosity=2)
        runner.run(suites)