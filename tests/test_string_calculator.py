
import unittest
from calculator.string_calculator import add

class TestStringCalci (unittest.TestCase):
    def test_empty_string_return_zero (self):
        self.assertEqual(add("",0))