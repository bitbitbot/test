"""
Test helper functions
"""

import unittest
from sample import increment_by_two

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test_incremement_by_two(self):
        """
        Test incremements
        """
        self.assertEqual(increment_by_two(-2),0)
        self.assertEqual(increment_by_two(0),2)
        self.assertEqual(increment_by_two(3),5)
        
    def test_incremement_by_three(self):
        """
        Test incremements
        """
        self.assertEqual(increment_by_two(-2),1)
        self.assertEqual(increment_by_two(0),3)
        self.assertEqual(increment_by_two(3),6)
if __name__ == '__main__':
    unittest.main()
