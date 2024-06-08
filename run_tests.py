"""
This script is a convenience script and just runs all 
the tests in the tests package.

Alternatively, you can run the tests by running the following command:
    python -m unittest discover tests
    OR
    python3 -m unittest discover tests

Depending on how python is installed on your system.
"""
import unittest

def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
