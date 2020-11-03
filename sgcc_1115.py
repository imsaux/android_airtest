import unittest
import os

def GetSuite():
    suites = unittest.TestSuite()
    # suites.addTests(unittest.TestLoader().loadTestsFromModule())
    # suites.addTests(unittest.TestLoader().loadTestsFromModule(fs_589))
    return suites


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    _suite = GetSuite()
    runner.run(_suite)