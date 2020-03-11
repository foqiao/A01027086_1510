from unittest import TestCase

from lab_06.maze import current_character


class Test(TestCase):
    def test_current_character(self):
        x_location = 5
        y_location = 5
        location = "(%d,%d)" % (x_location, y_location)
        self.assertTrue(location, current_character())
