from unittest import TestCase

from lab_08.Tree import Tree


class TestTree(TestCase):
    def test_repr(self):
        tree = Tree("Pine", 109, 109)
        result = "Tree(%s, %d, %d)" % (tree.species, tree.age, tree.trunk_circumference)
        self.assertTrue(result, tree.__repr__())
