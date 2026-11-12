
import unittest
from main import check_position

class TestCheckPosition(unittest.TestCase):

    def test_position_one(self):
        self.assertEqual(check_position(1), "Steve")

    def test_position_five(self):
        self.assertEqual(check_position(5), "Michael")

    def test_position_nine(self):
        self.assertEqual(check_position(9), "George")

    def test_invalid_position(self):
        self.assertIsNone(check_position(10))

if __name__ == "__main__":
    unittest.main()
    
