#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""
    
    def test_max_integer(self):
        """Test with a list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 6]), 6)
    
    def test_max_integer_unsorted(self):
        """Test with an unsorted list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_max_integer_negative(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-10, -2, -3, -4]), -2)
    
    def test_max_integer_single_element(self):
        """Test with a list containing a single integer."""
        self.assertEqual(max_integer([27]), 27)
    
    def test_max_integer_empty(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))
    
    def test_max_integer_duplicates(self):
        """Test with a list containing duplicate maximum values."""
        self.assertEqual(max_integer([1, 2, 3, 5, 5, 4]), 5)
    
    def test_max_integer_type_error(self):
        """Test with a list of mixed types (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer([2, 'c', 4])

if __name__ == "__main__":
    unittest.main()
