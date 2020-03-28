from unittest import TestCase

from lab_08.Tree import Tree


class TestTree(TestCase):
    def test_Str(self):
        tree = Tree("Maple", 20, 20)
        result = "The tree is called %s. It is %dmm. It is %s wide" % (tree.species, tree.age, tree.trunk_circumference)
        self.assertTrue(result, tree.__str__())
