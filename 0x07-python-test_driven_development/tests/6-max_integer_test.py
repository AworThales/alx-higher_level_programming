#!/usr/bin/python3
"""For Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""

    def test_ordered_list(self):
        """For the Test an arrange list of integers."""
        arrange = [1, 2, 3, 4]
        self.assertEqual(max_integer(arrange), 4)

    def test_unordered_list(self):
        """For the Test an unarrage list of integers."""
        unarrage = [1, 2, 4, 3]
        self.assertEqual(max_integer(unarrage), 4)

    def test_max_at_begginning(self):
        """For the Test a list with a beginning max value."""
        maximum_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(maximum_at_beginning), 4)

    def test_empty_list(self):
        """For the Test an nothing list."""
        nothing = []
        self.assertEqual(max_integer(nothing), None)

    def test_one_element_list(self):
        """For the Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """For the Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """For the Test a list of ints and floats."""
        intes_and_float = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(intes_and_float), 15.5)

    def test_string(self):
        """For the Test a strings."""
        strings = "Brennan"
        self.assertEqual(max_integer(strings), 'r')

    def test_list_of_strings(self):
        """For the Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """For the Test an nothing strings."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

