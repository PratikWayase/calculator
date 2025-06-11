
import unittest
from calculator.string_calculator import add

class TestStringCalci (unittest.TestCase):
    def test_empty_string_return_zero (self):
        self.assertEqual(add("",0))

    def test_single_number_return_value (self):
        self.assertEqual (add('1',1))
        self.assertEqual (add("42",42))

    def test_two_numbers_comma_delimited_returns_sum(self):
        self.assertEqual(add("1,5"), 6)
        self.assertEqual(add("10,20"), 30)
    
    def test_any_amount_of_numbers(self):
        self.assertEqual(add("1,2,3,4,5"), 15)
        self.assertEqual(add("10,20,30,40"), 100)

    def test_newlines_as_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("4\n5\n6"), 15)

    def test_custom_delimiters(self):
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//|\n1|2|3"), 6)
        self.assertEqual(add("//sep\n2sep5"), 7)
        self.assertEqual(add("//*\n1*2*3"), 6)

    def test_negative_numbers_throw_exception(self):
       with self.assertRaises(ValueError) as context:
            add("-1,2")
       self.assertEqual(str(context.exception), "negative numbers not allowed -1")
        
       with self.assertRaises(ValueError) as context:
            add("2,-4,3,-5")
       self.assertEqual(str(context.exception), "negative numbers not allowed -4, -5")
    
