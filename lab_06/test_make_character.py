from unittest import TestCase

from lab_06.maze import make_character


class Test(TestCase):
    def test_make_character(self):
        result = {'x': -1, 'y': -1}
        result1 = {'x': 5, 'y': 5}
        self.assertTrue(result1, make_character(5, 5))
        self.assertTrue(result, make_character(-1, -1))
