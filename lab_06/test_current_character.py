from unittest import TestCase

from lab_06.maze import current_character


class Test(TestCase):
    def test_current_character(self):
        self.assertFalse(f"{5},{5}", current_character())
