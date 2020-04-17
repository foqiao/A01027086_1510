from unittest import TestCase

from a4.assignment_four import remove_tree

class TestTreeFarm(TestCase):
    def test_remove_tree(self):
        with self.assertRaises(ValueError):
            remove_tree("h")
            remove_tree(-1)
