
import unittest
from main import check_position

class TestCheckPosition(unittest.TestCase):

    def test_position_one(self):
        self.assertEqual(check_position(1), "Steve")

    def test_position_five(self):
        self.assertEqual(check_position(5), "Michael")

if __name__ == "__main__":
    unittest.main()
    
