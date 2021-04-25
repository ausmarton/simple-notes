"""
Test cases
"""

#!coding: utf-8

from unittest import TestCase

class SimpleTestCase(TestCase):
    """ Tests"""
    def test_sample(self):
        """ simple Test """
        self.assertEqual("hello", "hello")