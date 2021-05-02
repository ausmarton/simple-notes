"""
Test cases
"""

# !coding: utf-8

from unittest import TestCase
from Calculator import add

from Calculator import multiply



class CalculatorTestCase(TestCase):
    """ Calculator Test"""

    def test_add_two_numbers(self):
        """ add two numbers"""
        first_input = 1
        second_input = 4
        expected_output = 5
        self.assertEqual(expected_output, add(first_input, second_input))


    def test_multiply_two_numbers(self):
        """ multiply two numbers"""
        first_input = 2
        second_input = 4
        expected_output = 8
        self.assertEqual(expected_output, multiply(first_input, second_input))

    def test_multiply_with_zero(self):
        """ multiply with zero"""
        first_input = 2
        second_input = 0
        expected_output = 0
        self.assertEqual(expected_output, multiply(first_input, second_input))
        self.assertEqual(expected_output, multiply(second_input, first_input))

    def test_multiply_with_negative_one(self):
        """ multiply with negative """
        first_input = 2
        second_input = -1
        expected_output = -2
        self.assertEqual(expected_output, multiply(first_input, second_input))
        self.assertEqual(expected_output, multiply(second_input, first_input))
