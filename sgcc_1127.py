import unittest
import os

case_path = os.getcwd()

def GetSuite():
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().discover(case_path, pattern="ST*.py", top_level_dir=None))
    return suites


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=0)
    _suite = GetSuite()
    runner.run(_suite)