#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to run unit tests.
"""

import sys
import unittest

if __name__ == '__main__':
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    sys.exit(not runner.run(suite).wasSuccessful())
