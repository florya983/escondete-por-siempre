
import unittest
from funciones import check_position
from funciones import find_frank
from funciones import find_max
from unittest.mock import patch

matrix = [
    ["Steve", "Tom", "Max"],
    ["John", "Michael", "Brad"],
    ["Frank", "Robbie", "George"],
]


class TestGameFunctions(unittest.TestCase):

    def test_position_one(self):
        self.assertEqual(check_position(1,matrix), "Steve")

    def test_position_five(self):
        self.assertEqual(check_position(5,matrix), "Michael")

    def test_position_nine(self):
        self.assertEqual(check_position(9,matrix), "George")

    def test_invalid_position(self):
        self.assertIsNone(check_position(10,matrix))

    def test_negative_position(self):
        self.assertIsNone(check_position(-2,matrix))

    def test_frank_wrong_position(self):
        with patch("builtins.input", return_value="1"):
             result = find_frank(2, matrix, "Frank")
        expect=(False,3)
        self.assertEqual(result,expect)

    def test_max_wrong_position(self):
        with patch("builtins.input", return_value="8"):
             result = find_max(4, matrix, "Max")
        expect=(False,5)
        self.assertEqual(result,expect)

    def test_max_correct_position(self):
        with patch("builtins.input", return_value="3"):
             result = find_max(2, matrix, "Max")
        expect=(True,2)
        self.assertEqual(result,expect)
    
    def test_frank_correct_position(self):
        with patch("builtins.input", return_value="7"):
             result = find_frank(1, matrix, "Frank")
        expect=(True,1)
        self.assertEqual(result,expect)
    
if __name__ == "__main__":
    unittest.main()

    


    
