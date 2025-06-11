
import unittest
from calculator.string_calculator import add

class TestStringCalci (unittest.TestCase):
    def test_empty_string_return_zero (self):
        self.assertEqual(add("",0))

    def test_single_number_return_value (self):
        self.assertEqual (add('1',1))
        self.assertEqual (add("42",42))