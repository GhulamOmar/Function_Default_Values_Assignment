import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_valid(self):
        self.assertTrue(validate_input_in_functions.score_input("python", 33))

    def test_above_range_input(self):
        self.assertTrue(validate_input_in_functions.score_input("Invalid value, above the range"), 223)

    def test_score_below_range_input(self):
        self.assertTrue(validate_input_in_functions.score_input("Invalid value, below the range"), -1)

    def test_test_score_non_numeric(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input(("Non numeric"), 'd'))


if __name__ == '__main__':
    unittest.main()
