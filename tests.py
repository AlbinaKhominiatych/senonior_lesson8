import unittest
from main import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder("2", 2, 1), 5)

if __name__ == "__main__":
    unittest.main()