#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""
    def test_empty_list(self):
        """Test that None is returned for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_ordered_list(self):
        """Test a list already in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list not in order"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the largest element is at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_floats(self):
        """Test list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Test mixed ints and floats"""
        self.assertEqual(max_integer([1, 2.2, 3, 2.9]), 3)

    def test_negatives(self):
        """Test list containing negative numbers"""
        self.assertEqual(max_integer([-10, -5, -2, -3]), -2)

    def test_strings(self):
        """Test list of strings returns max string by comparison"""
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_list_of_lists(self):
        """Test list of lists compares by first element"""
        self.assertEqual(max_integer([[1], [3], [2]]), [3])


if __name__ == '__main__':
    unittest.main()
