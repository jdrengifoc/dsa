import unittest
# Make avaible packages inside src.
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import my packages.
from linkedlist import LinkedList
ll = LinkedList()
print(ll)

def add(a, b):
    return a + b


# Add the src directory to sys.path


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()