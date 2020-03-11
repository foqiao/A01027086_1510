from unittest import TestCase

from lab_06.maze import character


class Test(TestCase):
    def test_character(self):
        self.assertTrue("(%d,%d)" % (3, 3), character())
