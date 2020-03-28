from unittest import TestCase

from lab_08.Tree import Tree

def broken_function():
    tree = Tree(None, 20, 20)

class TestTree(TestCase):
    def test_class(self):
        with self.assertRaises(ValueError):
            broken_function()
