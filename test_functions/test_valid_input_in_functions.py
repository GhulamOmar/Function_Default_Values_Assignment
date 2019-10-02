import unittest
from more_functions import validate_input_in_functions


class MyTestCase(unittest.TestCase):
    def test_score_valid(self):
        self.assertTrue(validate_input_in_functions.score_input("python", 3))

    def test_above_range_input(self):
        self.assertFalse(validate_input_in_functions.score_input("Invalid value, above the range"), 55)


if __name__ == '__main__':
    unittest.main()
