#!/usr/bin/env python2

import sys
import unittest
from tests.example_test import LoginLogoutTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginLogoutTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
