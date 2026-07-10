#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python, Unit Testing
"""

import unittest


class TestMain(unittest.TestCase):
    """Test cases for the main module."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.example_data = "test"

    def tearDown(self) -> None:
        """Clean up after tests."""
        self.example_data = None

    def test_example(self):
        """An example test case."""
        self.assertTrue(True)

    @unittest.skip("Skipping this test case for demonstration purposes")
    def test_skip(self):
        """An example test case that is skipped."""
        self.assertTrue(True)

    def test_example_raises(self):
        """An example test case that raises an exception."""
        with self.assertRaises(ValueError):
            raise ValueError("This is a test exception")
