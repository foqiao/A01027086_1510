from unittest import TestCase

from lab_06.maze import user_choice

class Test(TestCase):
    def test_user_choice(self):
        self.assertTrue(3, user_choice())
