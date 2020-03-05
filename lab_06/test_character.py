from unittest import TestCase

from lab_06.maze import character

class Test(TestCase):
    def test_character(self):
        self.assertNotEqual(1, character())