#!/usr/bin/env python2

import sys
import unittest
from tests.buy_page_test import BuyPageTest
from tests.example_test import LoginLogoutTest


if __name__ == '__main__':
    test_classes_to_run = [BuyPageTest]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    result = runner.run(big_suite)
    sys.exit(not result.wasSuccessful())
