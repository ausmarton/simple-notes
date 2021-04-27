"""
Test cases
"""

#!coding: utf-8

from unittest import TestCase
import http_app

class SimpleTestCase(TestCase):
    """ Tests"""
    def test_sample(self):
        """ should convert input_list into a string"""
        input_list = [1,2,3]
        expected_output = "1,2,3"
        self.assertEqual(expected_output,http_app.print_list(input_list) )