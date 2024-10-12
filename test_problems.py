import unittest
from problems import *  # Ensure that problems.py is in the same directory or adjust the path accordingly.

class ProblemTests(unittest.TestCase):
    def test_add_numbers(self):
        # Test cases for addition
        self.assertEqual(add_numbers(3, 4), 7)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-5, -6), -11)
        self.assertEqual(add_numbers(100, 200), 300)
    
    def test_subtract_numbers(self):
        # Test cases for subtraction
        self.assertEqual(subtract_numbers(7, 4), 3)
        self.assertEqual(subtract_numbers(10, 0), 10)
        self.assertEqual(subtract_numbers(-5, -5), 0)
        self.assertEqual(subtract_numbers(0, 0), 0)
        self.assertEqual(subtract_numbers(100, 50), 50)
    
    def test_convertCtoF(self):    
        # self.assertIsInstance(convertCtoF(0), int, "Your function should return an integer")
        self.assertEqual(convertCtoF(-30),  -22)
        self.assertEqual(convertCtoF(-10),  14)
        self.assertEqual(convertCtoF(0),  32)
        self.assertEqual(convertCtoF(20),  68)
        self.assertEqual(convertCtoF(30),  86)

    def test_reverseString(self):
        self.assertIsInstance(reverseString("hello"), str)
        self.assertEquals(reverseString("hello"), "olleh")
        self.assertEquals(reverseString("Howdy"), "ydwoH")
        self.assertEquals(reverseString("Greetings from Earth"), "htraE morf sgniteerG")


if __name__ == "__main__":
    unittest.main()
