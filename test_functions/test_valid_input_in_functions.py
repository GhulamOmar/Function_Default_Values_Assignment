import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_valid(self):
        self.assertTrue(validate_input_in_functions.score_input("python", 3))

    def test_above_range_input(self):
        self.assertFalse(validate_input_in_functions.score_input("Invalid value, above the range"), 101)

    def test_score_below_range_input(self):
        self.assertFalse(validate_input_in_functions.score_input("Invalid value, below the range"), -44)

    def test_test_score_non_numeric(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input("Non numeric value"), )


if __name__ == '__main__':
    unittest.main()
