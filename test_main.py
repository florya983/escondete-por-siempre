
import unittest
from funciones import check_position

matrix = [
    ["Steve", "Tom", "Max"],
    ["John", "Michael", "Brad"],
    ["Frank", "Robbie", "George"],
]


class TestCheckPosition(unittest.TestCase):

    def test_position_one(self):
        self.assertEqual(check_position(1,matrix), "Steve")

    def test_position_five(self):
        self.assertEqual(check_position(5,matrix), "Michael")

    def test_position_nine(self):
        self.assertEqual(check_position(9,matrix), "George")

    def test_invalid_position(self):
        self.assertIsNone(check_position(10,matrix))

if __name__ == "__main__":
    unittest.main()
    


    
